"""
FAQ & Knowledge Engine for DermaCare Skin Clinic
Enforces single-source-of-truth pricing and pre/post procedure PDF delivery.
"""
import logging
from typing import Optional, Tuple, Dict, Any, List
from src.sheet_validator import SheetValidator
from src.localization import get_message, PROCEDURE_PDF_CAPTIONS

logger = logging.getLogger("FAQEngine")


class FAQEngine:
    def __init__(self, validator: SheetValidator):
        self.validator = validator

    def match_faq(self, text: str, lang: str = "en") -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
        """
        Attempts to match patient input against clinic FAQs.
        Returns: (matched, response_text, attachment_info)
        """
        if not text:
            return False, None, None

        clean = text.lower().strip()

        # 1. Location & Timings Query
        if any(w in clean for w in ["location", "located", "locat", "address", "where", "directions", "map", "pin", "timing", "timings", "hours", "kahan", "pata", "kdr", "kidhar", "time", "open"]):
            return True, get_message("faq_location_timings", lang), None

        # 2. Consultation Fees & Payment Methods Query
        if any(w in clean for w in ["fee", "fees", "charges", "payment", "card", "raast", "jazzcash", "cash", "visiting fee"]):
            return True, get_message("faq_fees_payments", lang), None

        # 3. Pre/Post-Procedure Care Guides (8 Procedures)
        pdf_match = self.match_procedure_guide(clean, lang)
        if pdf_match:
            return True, pdf_match[0], pdf_match[1]

        # 4. Service Price List Queries
        if any(w in clean for w in ["price", "rates", "cost", "how much", "rate list", "menu 3"]):
            return True, self.format_service_price_list(clean, lang), None

        # 5. Direct Service Name lookup (e.g. "HydraFacial price", "botox cost")
        services = self.validator.services_cache
        for s in services:
            s_name = s["service_name"].lower()
            if s_name in clean or (s.get("category", "").lower() in clean and "treatment" in clean):
                resp = (
                    f"💰 *{s['service_name']}*\n"
                    f"• *Price Range:* PKR {s['price_range_pkr']}\n"
                    f"• *Practitioner:* {s['practitioner']}\n"
                    f"• *Details:* {s['description']}\n\n"
                    f"_(To book a consultation or treatment, reply *BOOK*)_"
                )
                return True, resp, None

        return False, None, None

    def match_procedure_guide(self, clean_text: str, lang: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Matches request for pre/post-procedure care guides."""
        procedure_mappings = [
            ("hydra", "pdf_hydrafacial", "HydraFacial_Pre_Post_Care_Guide.pdf"),
            ("peel", "pdf_chemical_peels", "Chemical_Peels_Care_Instructions.pdf"),
            ("laser", "pdf_laser_hair_removal", "Laser_Hair_Removal_Pre_Post_Protocol.pdf"),
            ("prp", "pdf_prp_microneedling", "PRP_Microneedling_Post_Care.pdf"),
            ("microneedling", "pdf_prp_microneedling", "PRP_Microneedling_Post_Care.pdf"),
            ("botox", "pdf_botox_fillers", "Botox_Fillers_Post_Injection_Advisory.pdf"),
            ("filler", "pdf_botox_fillers", "Botox_Fillers_Post_Injection_Advisory.pdf"),
            ("co2", "pdf_co2_laser", "CO2_Fractional_Laser_Wound_Care.pdf"),
            ("wart", "pdf_wart_removal", "Wart_Tag_Removal_Wound_Care.pdf"),
            ("tag", "pdf_wart_removal", "Wart_Tag_Removal_Wound_Care.pdf"),
            ("glutathione", "pdf_glutathione_iv", "Glutathione_IV_Drip_Advisory.pdf"),
            ("drip", "pdf_glutathione_iv", "Glutathione_IV_Drip_Advisory.pdf"),
        ]

        if any(w in clean_text for w in ["pdf", "guide", "care", "instructions", "post care", "pre care", "hidayat", "tariqa"]):
            for key, pdf_id, filename in procedure_mappings:
                if key in clean_text:
                    caption_dict = PROCEDURE_PDF_CAPTIONS.get(pdf_id, {})
                    caption = caption_dict.get(lang) or caption_dict.get("en", "Attached is your procedure care guide.")
                    attachment = {
                        "type": "document",
                        "pdf_id": pdf_id,
                        "filename": filename,
                        "caption": caption
                    }
                    return caption, attachment

        return None

    def format_service_price_list(self, clean_text: str, lang: str) -> str:
        """Formats the official single-source-of-truth price sheet into a readable message."""
        services = self.validator.services_cache
        if not services:
            return "Official price list is currently being updated. Please call reception at 021-3587XXXX."

        header = "✨ *DermaCare Official Treatment & Price List (Clifton)*\n\n"
        lines = []
        for s in services:
            lines.append(f"• *{s['service_name']}:* PKR {s['price_range_pkr']}")

        footer = "\n\n📌 *All prices are strictly maintained by Clinic Manager Faraz.*\nTo book an appointment, reply *BOOK*."
        return header + "\n".join(lines) + footer
