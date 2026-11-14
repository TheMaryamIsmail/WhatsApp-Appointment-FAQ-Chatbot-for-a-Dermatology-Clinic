"""
Triage & Safety Engine for DermaCare Skin Clinic
Enforces Director Dr. Samiya Irfan's Non-Negotiable Directive:
"Not one syllable of medical advice from a robot. Any symptom question, any medical query,
any photo of a skin condition — scripted safe response and immediate handover to a human."
"""
import re
import json
import logging
from typing import Dict, Any, Optional, Tuple
from pathlib import Path
from src.config import EMERGENCY_KEYWORDS_PATH
from src.localization import get_message

logger = logging.getLogger("TriageEngine")


class TriageEngine:
    def __init__(self, keywords_file: Path = EMERGENCY_KEYWORDS_PATH):
        self.emergency_keywords = []
        self.medical_keywords = []
        self.handover_keywords = []
        self.load_keywords(keywords_file)

    def load_keywords(self, file_path: Path):
        """Loads and compiles regex patterns for safety triaging."""
        if file_path.exists():
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.emergency_keywords = [k.lower() for k in data.get("emergency_keywords", [])]
                    self.medical_keywords = [k.lower() for k in data.get("medical_query_keywords", [])]
                    self.handover_keywords = [k.lower() for k in data.get("handover_keywords", [])]
            except Exception as e:
                logger.error(f"Error loading emergency keywords: {e}")
        else:
            logger.warning("Emergency keywords file not found. Using internal fallback safety list.")
            self.emergency_keywords = ["bleeding", "blood", "khoon", "burn", "anaphylaxis", "soojan", "jalan", "emergency"]
            self.medical_keywords = ["rash", "acne", "daane", "eczema", "cream", "dawai", "medicine", "dosage", "pregnant", "mole", "cancer"]
            self.handover_keywords = ["human", "reception", "faraz", "agent", "call", "desk"]

    def is_emergency(self, text: str) -> bool:
        """Checks if text contains emergency / red flag keywords."""
        if not text:
            return False
        clean = text.lower()
        for kw in self.emergency_keywords:
            if re.search(rf"\b{re.escape(kw)}\b", clean) or kw in clean:
                return True
        return False

    def is_medical_query(self, text: str) -> bool:
        """Checks if text is asking for medical diagnosis, prescriptions, or symptoms."""
        if not text:
            return False
        clean = text.lower()
        for kw in self.medical_keywords:
            if re.search(rf"\b{re.escape(kw)}\b", clean) or kw in clean:
                return True
        return False

    def is_handover_requested(self, text: str) -> bool:
        """Checks if patient explicitly asked to speak with human staff / reception."""
        if not text:
            return False
        clean = text.lower()
        if clean.strip() in ("7", "reception", "human", "agent", "faraz", "call", "help"):
            return True
        for kw in self.handover_keywords:
            if re.search(rf"\b{re.escape(kw)}\b", clean) or kw in clean:
                return True
        return False

    def evaluate_message(
        self,
        text: Optional[str],
        media_type: Optional[str],
        lang: str = "en",
        confusion_count: int = 0
    ) -> Tuple[str, Optional[str], Dict[str, Any]]:
        """
        Evaluates incoming message through the safety triage hierarchy.
        Returns: (triage_result_type, bot_response_text, telemetry_metadata)
        Triage Result Types:
        - 'EMERGENCY': Urgent medical red flag detected
        - 'MEDICAL_DEFLECTION': Medical symptom/query deflected safely
        - 'MEDIA_PHOTO': Photo received and forwarded to desk
        - 'MEDIA_VOICE': Voice note received and forwarded to desk
        - 'HUMAN_HANDOVER': Desk staff requested by patient
        - 'CONFUSION_FALLBACK': 2-strike fallback handover
        - 'PASS': Clean message passed to booking/FAQ workflow
        """
        telemetry = {
            "has_media": bool(media_type),
            "media_type": media_type,
            "escalated_to_desk": False,
            "reason": None
        }

        # 1. Media Check: Photos
        if media_type in ("image", "photo"):
            telemetry["escalated_to_desk"] = True
            telemetry["reason"] = "patient_photo_received"
            return "MEDIA_PHOTO", get_message("photo_received", lang), telemetry

        # 2. Media Check: Audio / Voice Notes
        if media_type in ("audio", "voice"):
            telemetry["escalated_to_desk"] = True
            telemetry["reason"] = "patient_voice_note_received"
            return "MEDIA_VOICE", get_message("voice_received", lang), telemetry

        # 3. Emergency Interceptor (Top Priority)
        if text and self.is_emergency(text):
            telemetry["escalated_to_desk"] = True
            telemetry["reason"] = "medical_emergency_detected"
            return "EMERGENCY", get_message("emergency_alert", lang), telemetry

        # 4. Human Reception Handover Interceptor
        if text and self.is_handover_requested(text):
            telemetry["escalated_to_desk"] = True
            telemetry["reason"] = "user_requested_reception"
            return "HUMAN_HANDOVER", get_message("desk_handover", lang), telemetry

        # 5. Medical Advice / Symptom Interceptor (Strict Zero-Advice Rule)
        if text and self.is_medical_query(text):
            telemetry["escalated_to_desk"] = True
            telemetry["reason"] = "medical_advice_deflected"
            return "MEDICAL_DEFLECTION", get_message("medical_query_deflection", lang), telemetry

        # 6. 2-Strike Confusion Fallback
        if confusion_count >= 2:
            telemetry["escalated_to_desk"] = True
            telemetry["reason"] = "consecutive_confusion_handover"
            return "CONFUSION_FALLBACK", get_message("confusion_fallback", lang), telemetry

        # 7. Clean pass
        return "PASS", None, telemetry
