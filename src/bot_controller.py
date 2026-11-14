"""
Central Bot Controller & Dialog State Machine for DermaCare Skin Clinic
Orchestrates sessions, localization, triage, FAQs, and appointment workflows.
"""
import time
import logging
from typing import Dict, Any, Optional, Tuple
from src.localization import get_message, DOCTOR_BIOS
from src.sheet_validator import SheetValidator
from src.triage_engine import TriageEngine
from src.faq_engine import FAQEngine
from src.desk_bridge import DeskBridge
from src.analytics import AnalyticsEngine
from src.config import CLINIC_MAP_URL

logger = logging.getLogger("BotController")


class UserSession:
    def __init__(self, phone: str):
        self.phone = phone
        self.language: Optional[str] = None  # en, ur, ru
        self.state: str = "AWAITING_LANGUAGE"
        self.confusion_count: int = 0
        self.booking_data: Dict[str, Any] = {}
        self.last_interaction: float = time.time()


class BotController:
    def __init__(self):
        self.validator = SheetValidator()
        self.triage = TriageEngine()
        self.faq = FAQEngine(self.validator)
        self.desk = DeskBridge()
        self.analytics = AnalyticsEngine()
        self.sessions: Dict[str, UserSession] = {}

    def get_session(self, phone: str) -> UserSession:
        if phone not in self.sessions:
            self.sessions[phone] = UserSession(phone)
        return self.sessions[phone]

    def process_incoming_message(
        self,
        phone: str,
        text: Optional[str] = None,
        media_type: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Main entry point for incoming WhatsApp webhooks (Meta Cloud API or WATI).
        Returns response payload containing message text, attachments, and metadata.
        """
        start_time = time.time()
        session = self.get_session(phone)
        session.last_interaction = time.time()
        raw_text = (text or "").strip()
        # Auto-detect language if not already locked
        if session.language is None:
            import re
            if re.search(r"[\u0600-\u06FF]", raw_text):
                session.language = "ur"
            elif any(w in raw_text.lower() for w in ["hai", "karein", "bata", "mujhe", "daane", "dawai", "chahiye", "raabta", "nahi", "kya"]):
                session.language = "ru"

        lang = session.language or "en"

        response_payload = {
            "recipient_phone": phone,
            "text": "",
            "attachment": None,
            "escalated_to_desk": False,
            "latency_ms": 0.0
        }

        # ----------------------------------------------------
        # 1. TOP-PRIORITY SAFETY TRIAGE HIERARCHY
        # ----------------------------------------------------
        triage_type, triage_msg, telemetry = self.triage.evaluate_message(
            text=raw_text,
            media_type=media_type,
            lang=lang,
            confusion_count=session.confusion_count
        )

        if triage_type != "PASS":
            response_payload["text"] = triage_msg
            response_payload["escalated_to_desk"] = telemetry["escalated_to_desk"]
            if triage_type in ("EMERGENCY", "MEDICAL_DEFLECTION", "HUMAN_HANDOVER", "CONFUSION_FALLBACK"):
                session.state = "IDLE"
                session.confusion_count = 0

            latency = (time.time() - start_time) * 1000
            response_payload["latency_ms"] = round(latency, 2)
            self.analytics.log_interaction(
                phone=phone,
                is_bot=True,
                is_human=telemetry["escalated_to_desk"],
                reason=telemetry.get("reason"),
                latency_ms=latency
            )
            return response_payload

        # ----------------------------------------------------
        # 2. MID-CONVERSATION LANGUAGE SWITCH CHECK
        # ----------------------------------------------------
        lower_text = raw_text.lower()
        if lower_text in ("english", "en", "select english"):
            session.language = "en"
            session.state = "IDLE"
            response_payload["text"] = "Language set to English.\n\n" + get_message("main_menu", "en")
            return self._finalize_response(session, response_payload, start_time)
        elif lower_text in ("urdu", "اردو", "select urdu"):
            session.language = "ur"
            session.state = "IDLE"
            response_payload["text"] = "زبان اردو منتخب کر لی گئی ہے۔\n\n" + get_message("main_menu", "ur")
            return self._finalize_response(session, response_payload, start_time)
        elif lower_text in ("roman urdu", "roman", "select roman urdu"):
            session.language = "ru"
            session.state = "IDLE"
            response_payload["text"] = "Language Roman Urdu set kar di gayi hai.\n\n" + get_message("main_menu", "ru")
            return self._finalize_response(session, response_payload, start_time)

        # ----------------------------------------------------
        # 3. FIRST CONTACT / LANGUAGE SELECTION
        # ----------------------------------------------------
        if session.language is None or session.state == "AWAITING_LANGUAGE":
            if raw_text in ("1", "en", "English"):
                session.language = "en"
                session.state = "IDLE"
                response_payload["text"] = get_message("main_menu", "en")
            elif raw_text in ("2", "ur", "اردو", "Urdu"):
                session.language = "ur"
                session.state = "IDLE"
                response_payload["text"] = get_message("main_menu", "ur")
            elif raw_text in ("3", "ru", "Roman Urdu", "Roman"):
                session.language = "ru"
                session.state = "IDLE"
                response_payload["text"] = get_message("main_menu", "ru")
            else:
                response_payload["text"] = get_message("language_prompt", "en")
                session.state = "AWAITING_LANGUAGE"
            return self._finalize_response(session, response_payload, start_time)

        lang = session.language

        # ----------------------------------------------------
        # 4. GLOBAL NAVIGATION COMMANDS (MENU, CANCEL, RESCHEDULE)
        # ----------------------------------------------------
        if lower_text in ("menu", "start", "home", "hi", "hello", "salam", "assalam o alaikum"):
            session.state = "IDLE"
            session.confusion_count = 0
            response_payload["text"] = get_message("main_menu", lang)
            return self._finalize_response(session, response_payload, start_time)

        if lower_text in ("cancel", "cancel appointment", "منسوخ"):
            booking = self.desk.get_latest_active_booking(phone)
            if booking:
                cancelled = self.desk.cancel_appointment(booking["request_id"])
                session.state = "IDLE"
                response_payload["text"] = get_message("cancellation_done", lang, request_id=cancelled["request_id"])
            else:
                response_payload["text"] = "No active booking found under this number to cancel."
            return self._finalize_response(session, response_payload, start_time)

        if lower_text in ("reschedule", "change time", "وقت تبدیل"):
            booking = self.desk.get_latest_active_booking(phone)
            if booking:
                session.state = "BOOKING_STEP_SLOT"
                session.booking_data = {
                    "doctor_id": booking["doctor_id"],
                    "doctor_name": booking["doctor_name"],
                    "category": booking["service_category"],
                    "reschedule_ref": booking["request_id"]
                }
                slots_text = self._format_slots_for_doctor(booking["doctor_id"])
                response_payload["text"] = get_message("booking_step_slot", lang, doctor_name=booking["doctor_name"], slot_list=slots_text)
                return self._finalize_response(session, response_payload, start_time)

        # ----------------------------------------------------
        # 5. DIALOG STATE MACHINE: APPOINTMENT FLOW
        # ----------------------------------------------------
        if session.state == "BOOKING_STEP_CATEGORY":
            cat_map = {"1": "Clinical", "2": "Aesthetic", "3": "Injectable"}
            selected_cat = cat_map.get(raw_text)
            if selected_cat:
                session.booking_data["category"] = selected_cat
                session.state = "BOOKING_STEP_DOCTOR"
                self.analytics.log_funnel_step(phone, "CATEGORY_SELECTED")
                doc_list_text = self._format_doctor_list(selected_cat, lang)
                response_payload["text"] = get_message("booking_step_doctor", lang, doctor_list=doc_list_text)
                return self._finalize_response(session, response_payload, start_time)
            else:
                session.confusion_count += 1
                response_payload["text"] = "Please reply with 1, 2, or 3 to choose your service category.\n\n" + get_message("booking_step_category", lang)
                return self._finalize_response(session, response_payload, start_time)

        elif session.state == "BOOKING_STEP_DOCTOR":
            doc_map = {
                "1": ("doc_samiya", "Dr. Samiya Irfan", 4000),
                "2": ("doc_tariq", "Dr. Tariq Mansoor", 3000),
                "3": ("doc_hina", "Dr. Hina Zubair", 2500),
                "4": ("cons_sarah", "Sarah Ahmed", 1500),
                "5": ("cons_fatima", "Fatima Noor", 1500),
            }
            if raw_text in doc_map:
                doc_id, doc_name, fee = doc_map[raw_text]
                session.booking_data["doctor_id"] = doc_id
                session.booking_data["doctor_name"] = doc_name
                session.booking_data["fee"] = fee
                session.state = "BOOKING_STEP_SLOT"
                self.analytics.log_funnel_step(phone, "DOCTOR_SELECTED")
                slots_text = self._format_slots_for_doctor(doc_id)
                response_payload["text"] = get_message("booking_step_slot", lang, doctor_name=doc_name, slot_list=slots_text)
                return self._finalize_response(session, response_payload, start_time)
            else:
                session.confusion_count += 1
                response_payload["text"] = "Please select a valid doctor number (1–5).\n\n" + self._format_doctor_list(session.booking_data.get("category", "Clinical"), lang)
                return self._finalize_response(session, response_payload, start_time)

        elif session.state == "BOOKING_STEP_SLOT":
            # Map letters A, B, C or numbers
            doc_id = session.booking_data.get("doctor_id", "doc_samiya")
            slots = self.validator.get_slots_for_doctor(doc_id)
            slot_map = {"a": 0, "b": 1, "c": 2, "d": 3, "1": 0, "2": 1, "3": 2, "4": 3}
            idx = slot_map.get(raw_text.lower())
            if idx is not None and idx < len(slots):
                chosen_slot = slots[idx]
                slot_str = f"{chosen_slot['day_of_week']} ({chosen_slot['start_time']} - {chosen_slot['end_time']})"
                session.booking_data["slot_time"] = slot_str
                
                # Check if this was a reschedule
                if "reschedule_ref" in session.booking_data:
                    ref = session.booking_data["reschedule_ref"]
                    self.desk.reschedule_appointment(ref, slot_str)
                    session.state = "IDLE"
                    response_payload["text"] = f"✅ Appointment #{ref} rescheduled to {slot_str}. Desk will review and confirm."
                    return self._finalize_response(session, response_payload, start_time)

                session.state = "BOOKING_STEP_NAME"
                self.analytics.log_funnel_step(phone, "SLOT_SELECTED")
                response_payload["text"] = get_message("booking_step_name", lang)
                return self._finalize_response(session, response_payload, start_time)
            else:
                session.confusion_count += 1
                response_payload["text"] = "Please select a valid option (A, B, C, or D).\n\n" + self._format_slots_for_doctor(doc_id)
                return self._finalize_response(session, response_payload, start_time)

        elif session.state == "BOOKING_STEP_NAME":
            patient_name = raw_text.strip()
            if len(patient_name) >= 2:
                session.booking_data["patient_name"] = patient_name
                # Honest flow: Log structured request to Desk Bridge awaiting desk entry in software
                booking_record = self.desk.log_request(
                    patient_phone=phone,
                    patient_name=patient_name,
                    doctor_id=session.booking_data["doctor_id"],
                    doctor_name=session.booking_data["doctor_name"],
                    category=session.booking_data.get("category", "General"),
                    slot_time=session.booking_data["slot_time"]
                )
                session.state = "IDLE"
                session.confusion_count = 0
                self.analytics.log_funnel_step(phone, "BOOKING_COMPLETED", completed=True)

                response_payload["text"] = get_message(
                    "booking_request_logged",
                    lang,
                    request_id=booking_record["request_id"],
                    patient_name=patient_name,
                    doctor_name=session.booking_data["doctor_name"],
                    slot_time=session.booking_data["slot_time"],
                    fee=session.booking_data.get("fee", 3000)
                )
                return self._finalize_response(session, response_payload, start_time)
            else:
                response_payload["text"] = "Please provide the patient's full name:"
                return self._finalize_response(session, response_payload, start_time)

        # ----------------------------------------------------
        # 6. MAIN MENU OPTION SELECTION (STATE == IDLE)
        # ----------------------------------------------------
        if raw_text == "1" or lower_text in ("book", "booking", "appointment"):
            session.state = "BOOKING_STEP_CATEGORY"
            self.analytics.log_funnel_step(phone, "BOOKING_STARTED")
            response_payload["text"] = get_message("booking_step_category", lang)
            return self._finalize_response(session, response_payload, start_time)

        elif raw_text == "2":
            booking = self.desk.get_latest_active_booking(phone)
            if booking:
                response_payload["text"] = (
                    f"📅 *Active Appointment Found (Ref #{booking['request_id']})*\n"
                    f"• Doctor: {booking['doctor_name']}\n"
                    f"• Time: {booking['slot_time']}\n"
                    f"• Status: {booking['status']}\n\n"
                    f"Reply *RESCHEDULE* to change time, or *CANCEL* to cancel."
                )
            else:
                response_payload["text"] = "No active appointment found for your number. To book a new visit, reply *BOOK*."
            return self._finalize_response(session, response_payload, start_time)

        elif raw_text == "3":
            response_payload["text"] = self.faq.format_service_price_list("", lang)
            self.analytics.log_faq_hit("SERVICES_PRICE_LIST", raw_text)
            return self._finalize_response(session, response_payload, start_time)

        elif raw_text == "4":
            response_payload["text"] = get_message("faq_location_timings", lang)
            self.analytics.log_faq_hit("LOCATION_TIMINGS", raw_text)
            return self._finalize_response(session, response_payload, start_time)

        elif raw_text == "5":
            response_payload["text"] = (
                "📄 *Pre & Post-Procedure Care Guides*\n"
                "Please type the name of the treatment you would like care instructions for:\n\n"
                "1. HydraFacial MD\n"
                "2. Chemical Peels\n"
                "3. Laser Hair Removal\n"
                "4. Microneedling / PRP\n"
                "5. Botox & Dermal Fillers\n"
                "6. CO2 Fractional Laser\n"
                "7. Wart & Skin Tag Removal\n"
                "8. Glutathione IV Drip\n\n"
                "_(e.g., reply 'HydraFacial' or 'Chemical Peel')_"
            )
            self.analytics.log_faq_hit("PDF_PROCEDURE_GUIDES", raw_text)
            return self._finalize_response(session, response_payload, start_time)

        elif raw_text == "6":
            response_payload["text"] = get_message("faq_fees_payments", lang)
            self.analytics.log_faq_hit("FEES_AND_PAYMENTS", raw_text)
            return self._finalize_response(session, response_payload, start_time)

        elif raw_text == "7":
            response_payload["text"] = get_message("desk_handover", lang)
            response_payload["escalated_to_desk"] = True
            return self._finalize_response(session, response_payload, start_time)

        # ----------------------------------------------------
        # 7. FAQ ENGINE MATCHING
        # ----------------------------------------------------
        faq_matched, faq_text, faq_att = self.faq.match_faq(raw_text, lang)
        if faq_matched:
            response_payload["text"] = faq_text
            response_payload["attachment"] = faq_att
            self.analytics.log_faq_hit("AUTO_MATCHED_FAQ", raw_text)
            return self._finalize_response(session, response_payload, start_time)

        # ----------------------------------------------------
        # 8. UNRECOGNIZED INPUT (INCREMENT CONFUSION COUNT)
        # ----------------------------------------------------
        session.confusion_count += 1
        if session.confusion_count >= 2:
            response_payload["text"] = get_message("confusion_fallback", lang)
            response_payload["escalated_to_desk"] = True
            session.confusion_count = 0
        else:
            response_payload["text"] = (
                "I didn't quite catch that. You can reply with a number from the menu below, or type *RECEPTION* to talk to our front desk:\n\n"
                + get_message("main_menu", lang)
            )

        return self._finalize_response(session, response_payload, start_time)

    def _format_doctor_list(self, category: str, lang: str) -> str:
        """Formats doctors based on category."""
        if category == "Injectable":
            return DOCTOR_BIOS["doc_samiya"][lang]
        elif category == "Aesthetic":
            return "\n\n".join([
                DOCTOR_BIOS["cons_sarah"][lang],
                DOCTOR_BIOS["cons_fatima"][lang],
                DOCTOR_BIOS["doc_tariq"][lang]
            ])
        else:
            return "\n\n".join([
                DOCTOR_BIOS["doc_samiya"][lang],
                DOCTOR_BIOS["doc_tariq"][lang],
                DOCTOR_BIOS["doc_hina"][lang]
            ])

    def _format_slots_for_doctor(self, doctor_id: str) -> str:
        slots = self.validator.get_slots_for_doctor(doctor_id)
        if not slots:
            return "No slots currently scheduled. Please call desk at 021-3587XXXX."
        lines = []
        letters = ["A", "B", "C", "D", "E"]
        for idx, s in enumerate(slots[:4]):
            let = letters[idx] if idx < len(letters) else str(idx + 1)
            lines.append(f"📅 *Option {let}:* {s['day_of_week']} ({s['start_time']} - {s['end_time']})")
        return "\n".join(lines)

    def _finalize_response(self, session: UserSession, payload: Dict[str, Any], start_time: float) -> Dict[str, Any]:
        latency = (time.time() - start_time) * 1000
        payload["latency_ms"] = round(latency, 2)
        self.analytics.log_interaction(
            phone=session.phone,
            is_bot=True,
            is_human=payload["escalated_to_desk"],
            reason="handover_or_confusion" if payload["escalated_to_desk"] else None,
            latency_ms=latency
        )
        return payload
