"""
Sheet Validator & Resilience Engine
Fulfills Directive: "The availability sheet and price sheet are maintained by my staff
who occasionally make typos — design for validation, not crashes."
"""
import csv
import re
import logging
from typing import List, Dict, Any, Optional
from datetime import time
from pathlib import Path
from src.config import SERVICES_PRICING_PATH, DOCTOR_AVAILABILITY_PATH

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SheetValidator")

# Day-of-week normalization dictionary (handles common staff typos)
DAY_MAPPING = {
    "mon": "Monday",
    "monday": "Monday",
    "mond": "Monday",
    "tue": "Tuesday",
    "tues": "Tuesday",
    "tuesday": "Tuesday",
    "teusday": "Tuesday",  # Common clinic typo
    "teus": "Tuesday",
    "wed": "Wednesday",
    "wednesday": "Wednesday",
    "wednessday": "Wednesday",
    "thu": "Thursday",
    "thur": "Thursday",
    "thurs": "Thursday",
    "thursday": "Thursday",
    "thurday": "Thursday",
    "fri": "Friday",
    "friday": "Friday",
    "sat": "Saturday",
    "saturday": "Saturday",
    "satur": "Saturday",
    "sun": "Sunday",
    "sunday": "Sunday"
}


def normalize_day(day_str: str) -> Optional[str]:
    """Cleans and standardizes day of the week, absorbing staff typos."""
    if not day_str:
        return None
    cleaned = re.sub(r"[^a-zA-Z]", "", day_str).strip().lower()
    return DAY_MAPPING.get(cleaned)


def normalize_time(time_str: str) -> Optional[str]:
    """
    Parses flexible human inputs like '4pm', '4:00 PM', '16:00', '11:00 am'
    into standardized 24-hour HH:MM format.
    """
    if not time_str:
        return None
    cleaned = time_str.strip().upper()
    
    # Format: HH:MM 24-hr (e.g. 16:00 or 09:30)
    match_24 = re.match(r"^(\d{1,2}):(\d{2})$", cleaned)
    if match_24:
        h, m = int(match_24.group(1)), int(match_24.group(2))
        if 0 <= h <= 23 and 0 <= m <= 59:
            return f"{h:02d}:{m:02d}"

    # Format: 4PM or 4 PM or 04:30PM
    match_12 = re.match(r"^(\d{1,2})(?::(\d{2}))?\s*(AM|PM)$", cleaned)
    if match_12:
        h = int(match_12.group(1))
        m = int(match_12.group(2) or 0)
        meridiem = match_12.group(3)
        if meridiem == "PM" and h < 12:
            h += 12
        elif meridiem == "AM" and h == 12:
            h = 0
        if 0 <= h <= 23 and 0 <= m <= 59:
            return f"{h:02d}:{m:02d}"

    # Fallback integer hour (e.g. '16' or '4')
    if cleaned.isdigit():
        h = int(cleaned)
        if 0 <= h <= 23:
            return f"{h:02d}:00"

    logger.warning(f"Unable to parse time string '{time_str}'. Dropping slot safely.")
    return None


class SheetValidator:
    """Safely loads and validates staff-maintained CSV sheets without crashing."""

    def __init__(self, services_csv: Path = SERVICES_PRICING_PATH, availability_csv: Path = DOCTOR_AVAILABILITY_PATH):
        self.services_csv = services_csv
        self.availability_csv = availability_csv
        self.services_cache: List[Dict[str, Any]] = []
        self.availability_cache: List[Dict[str, Any]] = []
        self.load_all()

    def load_services(self) -> List[Dict[str, Any]]:
        """Parses services and pricing sheet."""
        if not self.services_csv.exists():
            logger.error(f"Services file not found at {self.services_csv}")
            return []

        clean_services = []
        try:
            with open(self.services_csv, mode="r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for line_no, row in enumerate(reader, start=2):
                    name = row.get("service_name", "").strip()
                    if not name:
                        logger.warning(f"Line {line_no} in services CSV has no name. Skipping.")
                        continue
                    clean_services.append({
                        "service_id": row.get("service_id", str(line_no)).strip(),
                        "category": row.get("category", "General").strip(),
                        "service_name": name,
                        "service_name_ur": row.get("service_name_ur", name).strip(),
                        "service_name_ru": row.get("service_name_ru", name).strip(),
                        "price_range_pkr": row.get("price_range_pkr", "On Consultation").strip(),
                        "practitioner": row.get("practitioner", "Clinic Specialists").strip(),
                        "pre_post_pdf_id": row.get("pre_post_pdf_id", "").strip(),
                        "description": row.get("description", "").strip()
                    })
            self.services_cache = clean_services
            logger.info(f"Loaded {len(clean_services)} validated services.")
        except Exception as e:
            logger.error(f"Error parsing services CSV: {e}. Bot will use fallback memory.", exc_info=True)
        return self.services_cache

    def load_availability(self) -> List[Dict[str, Any]]:
        """Parses doctor availability schedule with typo tolerance."""
        if not self.availability_csv.exists():
            logger.error(f"Availability file not found at {self.availability_csv}")
            return []

        clean_slots = []
        try:
            with open(self.availability_csv, mode="r", encoding="utf-8") as f:
                # Strip out comment lines starting with #
                lines = [line for line in f if not line.strip().startswith("#")]
                reader = csv.DictReader(lines)
                for line_no, row in enumerate(reader, start=2):
                    raw_doc_id = row.get("doctor_id", "").strip()
                    raw_doc_name = row.get("doctor_name", "").strip()
                    raw_day = row.get("day_of_week", "").strip()
                    raw_start = row.get("start_time", "").strip()
                    raw_end = row.get("end_time", "").strip()

                    # Normalize day
                    norm_day = normalize_day(raw_day)
                    if not norm_day:
                        logger.warning(f"Line {line_no}: Invalid day '{raw_day}'. Safely skipped.")
                        continue

                    # Normalize times
                    norm_start = normalize_time(raw_start)
                    norm_end = normalize_time(raw_end)
                    if not norm_start or not norm_end:
                        logger.warning(f"Line {line_no}: Invalid time '{raw_start} - {raw_end}'. Safely skipped.")
                        continue

                    # Standardize doctor id
                    doc_id_clean = raw_doc_id.lower().replace(".", "").replace(" ", "_")
                    if not doc_id_clean:
                        if "samiya" in raw_doc_name.lower():
                            doc_id_clean = "doc_samiya"
                        elif "tariq" in raw_doc_name.lower():
                            doc_id_clean = "doc_tariq"
                        elif "hina" in raw_doc_name.lower():
                            doc_id_clean = "doc_hina"
                        elif "sarah" in raw_doc_name.lower():
                            doc_id_clean = "cons_sarah"
                        elif "fatima" in raw_doc_name.lower():
                            doc_id_clean = "cons_fatima"
                        else:
                            doc_id_clean = "doc_specialist"

                    clean_slots.append({
                        "doctor_id": doc_id_clean,
                        "doctor_name": raw_doc_name.title() if raw_doc_name else "Specialist",
                        "day_of_week": norm_day,
                        "start_time": norm_start,
                        "end_time": norm_end,
                        "slot_duration_mins": int(row.get("slot_duration_mins") or 30),
                        "is_active": str(row.get("is_active", "true")).lower() == "true"
                    })
            self.availability_cache = clean_slots
            logger.info(f"Loaded {len(clean_slots)} validated availability schedules.")
        except Exception as e:
            logger.error(f"Error parsing availability CSV: {e}. Non-crash fallback engaged.", exc_info=True)
        return self.availability_cache

    def load_all(self):
        self.load_services()
        self.load_availability()

    def get_slots_for_doctor(self, doctor_id: str) -> List[Dict[str, Any]]:
        """Returns validated active slots for a given doctor."""
        norm_id = doctor_id.lower().replace(".", "").replace(" ", "_")
        matches = [s for s in self.availability_cache if norm_id in s["doctor_id"] and s["is_active"]]
        return matches

    def search_service(self, query: str) -> List[Dict[str, Any]]:
        """Fuzzy search on service name or category."""
        q = query.lower().strip()
        results = []
        for s in self.services_cache:
            if (q in s["service_name"].lower() or 
                q in s["service_name_ur"] or 
                q in s["service_name_ru"].lower() or 
                q in s["category"].lower()):
                results.append(s)
        return results

    def get_pdf_for_service(self, procedure_name: str) -> Optional[str]:
        """Returns the pre/post PDF identifier for a procedure."""
        matches = self.search_service(procedure_name)
        if matches and matches[0]["pre_post_pdf_id"]:
            return matches[0]["pre_post_pdf_id"]
        return None
