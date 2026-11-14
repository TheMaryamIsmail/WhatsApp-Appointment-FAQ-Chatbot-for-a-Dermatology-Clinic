"""
Desk Bridge & Appointment Database
Fulfills Directive: "Our appointment software is a local desktop product with no API —
we checked — so do not promise calendar integration. The honest flow is: bot collects
a structured request, desk confirms in the software, bot sends the confirmation message."
"""
import sqlite3
import logging
from datetime import datetime
from typing import Dict, Any, List, Optional
from pathlib import Path
from src.config import APPOINTMENTS_DB_PATH

logger = logging.getLogger("DeskBridge")


class DeskBridge:
    def __init__(self, db_path: Path = APPOINTMENTS_DB_PATH):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        """Initializes appointments table schema."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    request_id TEXT UNIQUE,
                    patient_phone TEXT NOT NULL,
                    patient_name TEXT NOT NULL,
                    doctor_id TEXT NOT NULL,
                    doctor_name TEXT NOT NULL,
                    service_category TEXT,
                    slot_time TEXT NOT NULL,
                    status TEXT DEFAULT 'PENDING',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    confirmed_at TIMESTAMP,
                    reminder_24h_sent INTEGER DEFAULT 0,
                    reminder_3h_sent INTEGER DEFAULT 0,
                    notes TEXT
                )
            """)
            conn.commit()

    def log_request(
        self,
        patient_phone: str,
        patient_name: str,
        doctor_id: str,
        doctor_name: str,
        category: str,
        slot_time: str
    ) -> Dict[str, Any]:
        """Logs a newly captured structured request awaiting front-desk validation."""
        req_id = f"DC-{datetime.now().strftime('%m%d')}-{abs(hash(patient_phone + slot_time)) % 10000:04d}"
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO appointments 
                (request_id, patient_phone, patient_name, doctor_id, doctor_name, service_category, slot_time, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, 'PENDING')
            """, (req_id, patient_phone, patient_name, doctor_id, doctor_name, category, slot_time))
            conn.commit()

        logger.info(f"Logged appointment request {req_id} for {patient_name} with {doctor_name} at {slot_time}")
        return {
            "request_id": req_id,
            "patient_phone": patient_phone,
            "patient_name": patient_name,
            "doctor_id": doctor_id,
            "doctor_name": doctor_name,
            "slot_time": slot_time,
            "status": "PENDING"
        }

    def confirm_by_desk(self, request_id: str, staff_member: str = "Faraz") -> Optional[Dict[str, Any]]:
        """
        Action performed by reception staff in the shared desk dashboard.
        Triggers the WhatsApp confirmation message to the patient.
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE appointments 
                SET status = 'CONFIRMED', confirmed_at = CURRENT_TIMESTAMP, notes = ?
                WHERE request_id = ? AND status = 'PENDING'
            """, (f"Confirmed by {staff_member}", request_id))
            conn.commit()

            cursor.execute("SELECT * FROM appointments WHERE request_id = ?", (request_id,))
            row = cursor.fetchone()
            if row:
                logger.info(f"Appointment {request_id} confirmed by desk staff {staff_member}")
                return dict(row)
        return None

    def cancel_appointment(self, identifier: str) -> Optional[Dict[str, Any]]:
        """Cancels an appointment by request_id or patient_phone."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE appointments 
                SET status = 'CANCELLED'
                WHERE (request_id = ? OR patient_phone = ?) AND status IN ('PENDING', 'CONFIRMED')
            """, (identifier, identifier))
            conn.commit()

            cursor.execute("""
                SELECT * FROM appointments 
                WHERE request_id = ? OR patient_phone = ? 
                ORDER BY id DESC LIMIT 1
            """, (identifier, identifier))
            row = cursor.fetchone()
            if row:
                logger.info(f"Appointment {row['request_id']} cancelled")
                return dict(row)
        return None

    def reschedule_appointment(self, identifier: str, new_slot_time: str) -> Optional[Dict[str, Any]]:
        """Reschedules an appointment to a new slot time."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE appointments 
                SET slot_time = ?, status = 'PENDING'
                WHERE (request_id = ? OR patient_phone = ?) AND status IN ('PENDING', 'CONFIRMED')
            """, (new_slot_time, identifier, identifier))
            conn.commit()

            cursor.execute("""
                SELECT * FROM appointments 
                WHERE request_id = ? OR patient_phone = ? 
                ORDER BY id DESC LIMIT 1
            """, (identifier, identifier))
            row = cursor.fetchone()
            if row:
                logger.info(f"Appointment {row['request_id']} rescheduled to {new_slot_time}")
                return dict(row)
        return None

    def get_latest_active_booking(self, patient_phone: str) -> Optional[Dict[str, Any]]:
        """Retrieves most recent booking for a phone number."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM appointments 
                WHERE patient_phone = ? AND status IN ('PENDING', 'CONFIRMED')
                ORDER BY id DESC LIMIT 1
            """, (patient_phone,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def get_pending_queue(self) -> List[Dict[str, Any]]:
        """Returns all unconfirmed requests awaiting desk entry in clinic software."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM appointments WHERE status = 'PENDING' ORDER BY id DESC")
            return [dict(r) for r in cursor.fetchall()]

    def get_all_appointments(self, status_filter: Optional[str] = None) -> Dict[str, Any]:
        """Returns all appointments with counts across status categories."""
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute("SELECT COUNT(*) FROM appointments WHERE status = 'PENDING'")
            pending_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM appointments WHERE status = 'CONFIRMED'")
            confirmed_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM appointments WHERE status = 'CANCELLED'")
            cancelled_count = cursor.fetchone()[0]

            cursor.execute("SELECT COUNT(*) FROM appointments")
            total_count = cursor.fetchone()[0]

            if status_filter and status_filter.upper() != "ALL":
                cursor.execute(
                    "SELECT * FROM appointments WHERE status = ? ORDER BY id DESC",
                    (status_filter.upper(),)
                )
            else:
                cursor.execute("SELECT * FROM appointments ORDER BY id DESC")

            rows = [dict(r) for r in cursor.fetchall()]

            return {
                "total_count": total_count,
                "pending_count": pending_count,
                "confirmed_count": confirmed_count,
                "cancelled_count": cancelled_count,
                "appointments": rows
            }
