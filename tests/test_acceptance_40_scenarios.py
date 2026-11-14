"""
Acceptance Test Suite: 40-Scenario Validation Matrix
Directly tests every requirement stipulated by Dr. Samiya Irfan in FF-026.
Mandate: 100% Pass Rate (40/40) before soft launch sign-off.
"""
import pathlib
import unittest
import time
from src.bot_controller import BotController
from src.sheet_validator import normalize_day, normalize_time


class Test40AcceptanceScenarios(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bot = BotController()

    # -----------------------------------------------------------
    # CATEGORY 1: MEDICAL SAFETY & ZERO-ADVICE GUARDRAILS (01 - 10)
    # -----------------------------------------------------------

    def test_scenario_01_rash_query_deflection(self):
        """01: Rash treatment query must NOT give medical advice."""
        res = self.bot.process_incoming_message(
            phone="+923001110001",
            text="I have a red itchy rash on my neck, what cream should I apply?"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("prohibits providing medical diagnoses", res["text"])
        self.assertNotIn("hydrocortisone", res["text"].lower())
        self.assertNotIn("apply this", res["text"].lower())

    def test_scenario_02_acne_antibiotics_query(self):
        """02: Acne medication query must refuse prescriptions."""
        res = self.bot.process_incoming_message(
            phone="+923001110002",
            text="Suggest some antibiotics or gel for severe cystic acne"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("Patient Safety Notice", res["text"])
        self.assertNotIn("doxycycline", res["text"].lower())

    def test_scenario_03_urdu_eczema_query(self):
        """03: Urdu eczema query must deflect in authentic Urdu script."""
        res = self.bot.process_incoming_message(
            phone="+923001110003",
            text="میرے بچے کے چہرے پر ایگزیما ہو گیا ہے، کیا لوشن لگاؤں؟"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("طبی مشورہ", res["text"])

    def test_scenario_04_roman_urdu_bumps(self):
        """04: Roman Urdu query for painful bumps deflected safely."""
        res = self.bot.process_incoming_message(
            phone="+923001110004",
            text="Face pe achanak daane nikal aye hain bohot dard hai koi dawai bata dein"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("dawai tajweez nahi ki ja sakti", res["text"])

    def test_scenario_05_mole_cancer_biopsy(self):
        """05: Dark mole cancer query deflected; requires in-person dermatoscope."""
        res = self.bot.process_incoming_message(
            phone="+923001110005",
            text="Can you tell me if this dark mole looks like skin cancer or melanoma?"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("prohibits providing medical diagnoses", res["text"])

    def test_scenario_06_photo_of_skin_disease(self):
        """06: Photo of skin plaque uploaded; bot must NEVER diagnose image."""
        res = self.bot.process_incoming_message(
            phone="+923001110006",
            media_type="photo"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("Photo Received", res["text"])
        self.assertIn("automated systems do not inspect or evaluate skin photos", res["text"])

    def test_scenario_07_photo_of_infected_wound(self):
        """07: Pus-filled lesion photo; escalated to desk portal securely."""
        res = self.bot.process_incoming_message(
            phone="+923001110007",
            media_type="photo"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("uploaded securely to our confidential desk portal", res["text"])

    def test_scenario_08_voice_note_received(self):
        """08: Audio voice note forwarded directly to human front desk."""
        res = self.bot.process_incoming_message(
            phone="+923001110008",
            media_type="voice"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("Voice Note Received", res["text"])
        self.assertIn("listening to your audio message", res["text"])

    def test_scenario_09_pregnancy_contraindication(self):
        """09: Asking if Botox is safe during pregnancy."""
        res = self.bot.process_incoming_message(
            phone="+923001110009",
            text="Can I get Botox while 4 months pregnant?"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("Patient Safety Notice", res["text"])

    def test_scenario_10_medication_dosage(self):
        """10: Patient asking whether to take 10mg or 20mg isotretinoin."""
        res = self.bot.process_incoming_message(
            phone="+923001110010",
            text="Should I take 10mg or 20mg of the isotretinoin medicine?"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("Patient Safety Notice", res["text"])

    # -----------------------------------------------------------
    # CATEGORY 2: EMERGENCY RED FLAG KEYWORDS (11 - 15)
    # -----------------------------------------------------------

    def test_scenario_11_active_bleeding(self):
        """11: Bleeding post-laser triggers Level 1 Urgent Alert."""
        res = self.bot.process_incoming_message(
            phone="+923001110011",
            text="Bleeding heavily from my face after laser treatment!"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("URGENT MEDICAL ALERT", res["text"])
        self.assertIn("+92 300 1234567", res["text"])
        self.assertIn("021 3587XXXX", res["text"])
        self.assertIn("South City Hospital ER", res["text"])

    def test_scenario_12_anaphylaxis_allergy(self):
        """12: Acute allergic reaction with breathing issue."""
        res = self.bot.process_incoming_message(
            phone="+923001110012",
            text="Chehra sooj gaya hai anaphylaxis reaction cannot breathe"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("EMERGENCY", res["text"])
        self.assertIn("0300-1234567", res["text"])

    def test_scenario_13_severe_chemical_burn(self):
        """13: Severe chemical burn post peel."""
        res = self.bot.process_incoming_message(
            phone="+923001110013",
            text="Severe chemical burn and skin peeling off raw"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("EMERGENCY", res["text"])

    def test_scenario_14_severe_swelling(self):
        """14: Facial lips and eyes swollen shut."""
        res = self.bot.process_incoming_message(
            phone="+923001110014",
            text="My eyes and lips are swollen shut after filler"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("EMERGENCY", res["text"])

    def test_scenario_15_mixed_urdu_english_emergency(self):
        """15: 'Khoon nikal raha hai emergency' triggers immediate contact reply."""
        res = self.bot.process_incoming_message(
            phone="+923001110015",
            text="Khoon nikal raha hai emergency please help"
        )
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("EMERGENCY", res["text"])
        self.assertIn("0300-1234567", res["text"])

    # -----------------------------------------------------------
    # CATEGORY 3: LOCALIZATION & URDU SCRIPT ACCURACY (16 - 20)
    # -----------------------------------------------------------

    def test_scenario_16_language_selector_first_touch(self):
        """16: New user receives trilingual language selection prompt."""
        res = self.bot.process_incoming_message(phone="+923001110016", text="Hi")
        self.assertIn("Please select your preferred language", res["text"])
        self.assertIn("اردو رسم الخط", res["text"])
        self.assertIn("Roman Urdu", res["text"])

    def test_scenario_17_proper_urdu_script_navigation(self):
        """17: Selecting 2 sets language to authentic Nastaliq Urdu."""
        p = "+923001110017"
        self.bot.process_incoming_message(phone=p, text="Hi")
        res = self.bot.process_incoming_message(phone=p, text="2")
        self.assertIn("مرکزی مینیو", res["text"])
        self.assertIn("نیا اپائنٹمنٹ بُک کروائیں", res["text"])

    def test_scenario_18_roman_urdu_navigation(self):
        """18: Selecting 3 sets language to Roman Urdu."""
        p = "+923001110018"
        self.bot.process_incoming_message(phone=p, text="Hi")
        res = self.bot.process_incoming_message(phone=p, text="3")
        self.assertIn("Naya Appointment Book Karein", res["text"])

    def test_scenario_19_mid_conversation_language_switch(self):
        """19: Switching from English to Urdu mid-conversation."""
        p = "+923001110019"
        self.bot.process_incoming_message(phone=p, text="1")  # English
        res = self.bot.process_incoming_message(phone=p, text="Urdu")
        self.assertEqual(self.bot.get_session(p).language, "ur")
        self.assertIn("زبان اردو منتخب کر لی گئی ہے", res["text"])

    def test_scenario_20_persistent_patient_memory(self):
        """20: Returning patient language preference is remembered."""
        p = "+923001110020"
        self.bot.process_incoming_message(phone=p, text="3")  # Roman Urdu
        res = self.bot.process_incoming_message(phone=p, text="Menu")
        self.assertIn("DermaCare Skin Clinic", res["text"])
        self.assertIn("Hum aap ki kya madad kar saktay hain?", res["text"])

    # -----------------------------------------------------------
    # CATEGORY 4: APPOINTMENT FLOW & DESKTOP BRIDGE (21 - 27)
    # -----------------------------------------------------------

    def test_scenario_21_booking_category_selection(self):
        """21: Patient begins booking and chooses Clinical Dermatology."""
        p = "+923001110021"
        self.bot.process_incoming_message(phone=p, text="1")  # EN
        res = self.bot.process_incoming_message(phone=p, text="1")  # Book
        self.assertIn("Step 1/5: Select Service Category", res["text"])

    def test_scenario_22_doctor_bio_presentation(self):
        """22: Selecting Category 1 shows Dr. Samiya Irfan FCPS bio."""
        p = "+923001110022"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")  # Book
        res = self.bot.process_incoming_message(phone=p, text="1")  # Clinical
        self.assertIn("Dr. Samiya Irfan (Clinic Director)", res["text"])
        self.assertIn("MBBS, FCPS (Dermatology)", res["text"])

    def test_scenario_23_dynamic_slot_presentation(self):
        """23: Selecting Dr. Samiya fetches upcoming slots from sheet."""
        p = "+923001110023"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="1")  # Dr. Samiya
        self.assertIn("Step 3/5: Select Day & Time Slot", res["text"])
        self.assertIn("Option A", res["text"])

    def test_scenario_24_slot_selection(self):
        """24: Patient chooses Option A for consultation slot."""
        p = "+923001110024"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="A")
        self.assertIn("Step 4/5: Patient Information", res["text"])

    def test_scenario_25_patient_name_input(self):
        """25: Patient inputs name and request is logged."""
        p = "+923001110025"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="A")
        res = self.bot.process_incoming_message(phone=p, text="Mrs. Ayesha Siddiqui")
        self.assertIn("Booking Request Logged", res["text"])
        self.assertIn("Mrs. Ayesha Siddiqui", res["text"])

    def test_scenario_26_honest_desktop_bridge_logging(self):
        """26: Verifies request enters desk queue with PENDING status."""
        p = "+923001110026"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="A")
        res = self.bot.process_incoming_message(phone=p, text="Tariq Khan")
        
        # Check desk bridge queue
        pending = self.bot.desk.get_pending_queue()
        patient_entry = next((item for item in pending if item["patient_phone"] == p), None)
        self.assertIsNotNone(patient_entry)
        self.assertEqual(patient_entry["status"], "PENDING")

    def test_scenario_27_desk_1_click_confirmation(self):
        """27: Desk confirms slot; triggers confirmation push with Google Map."""
        p = "+923001110027"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="A")
        self.bot.process_incoming_message(phone=p, text="Zainab Abbas")
        
        booking = self.bot.desk.get_latest_active_booking(p)
        confirmed = self.bot.desk.confirm_by_desk(booking["request_id"], staff_member="Faraz")
        self.assertIsNotNone(confirmed)
        self.assertEqual(confirmed["status"], "CONFIRMED")

    # -----------------------------------------------------------
    # CATEGORY 5: RESCHEDULING, CANCELLATION & REMINDERS (28 - 32)
    # -----------------------------------------------------------

    def test_scenario_28_reschedule_flow(self):
        """28: Patient initiates reschedule of existing appointment."""
        p = "+923001110028"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="A")
        self.bot.process_incoming_message(phone=p, text="Bilal Ahmed")

        res = self.bot.process_incoming_message(phone=p, text="RESCHEDULE")
        self.assertIn("Select Day & Time Slot", res["text"])

    def test_scenario_29_cancellation_flow(self):
        """29: Patient types CANCEL to cancel existing booking."""
        p = "+923001110029"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="A")
        self.bot.process_incoming_message(phone=p, text="Hamza Malik")

        res = self.bot.process_incoming_message(phone=p, text="CANCEL")
        self.assertIn("has been cancelled", res["text"])

    def test_scenario_30_24h_reminder_format(self):
        """30: Verifies 24-hour reminder message template and reply options."""
        from src.localization import get_message
        msg = get_message("reminder_24h", "en", patient_name="Fatima Ali", doctor_name="Dr. Samiya Irfan", slot_time="Tuesday 4:00 PM")
        self.assertIn("Appointment Reminder (Tomorrow)", msg)
        self.assertIn("CONFIRM", msg)
        self.assertIn("CANCEL", msg)
        self.assertIn("RESCHEDULE", msg)

    def test_scenario_31_3h_urgent_reminder(self):
        """31: Verifies 3-hour urgent reminder message template."""
        from src.localization import get_message
        msg = get_message("reminder_3h", "en", patient_name="Fatima Ali", doctor_name="Dr. Samiya Irfan", slot_time="4:00 PM")
        self.assertIn("Appointment in 3 Hours", msg)
        self.assertIn("Valet & basement parking available", msg)

    def test_scenario_32_reply_cancel_to_reminder(self):
        """32: Replying CANCEL to reminder closes booking loop."""
        p = "+923001110032"
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="1")
        self.bot.process_incoming_message(phone=p, text="A")
        self.bot.process_incoming_message(phone=p, text="Sara Khan")
        
        res = self.bot.process_incoming_message(phone=p, text="CANCEL")
        self.assertIn("cancelled", res["text"].lower())

    # -----------------------------------------------------------
    # CATEGORY 6: FAQ ENGINE & SINGLE SOURCE OF TRUTH (33 - 36)
    # -----------------------------------------------------------

    def test_scenario_33_single_source_of_truth_pricing(self):
        """33: Price query pulls directly from Faraz's validated sheet."""
        p = "+923001110033"
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="How much is HydraFacial?")
        self.assertIn("HydraFacial MD", res["text"])
        self.assertIn("12000 - 18000", res["text"])

    def test_scenario_34_consultation_fee_query(self):
        """34: Consultation fee matches official tariff."""
        p = "+923001110034"
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="What is the consultation fee?")
        self.assertIn("Dr. Samiya Irfan (Director): PKR 4,000", res["text"])
        self.assertIn("Dr. Tariq Mansoor (Consultant): PKR 3,000", res["text"])

    def test_scenario_35_location_and_timings(self):
        """35: Location pin and Clifton landmark provided."""
        p = "+923001110035"
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="Where is the clinic located?")
        self.assertIn("Clifton Medical Enclave", res["text"])
        self.assertIn("Teen Talwar", res["text"])
        self.assertIn("maps.google.com", res["text"])

    def test_scenario_36_pre_post_care_pdf_dispatch(self):
        """36: Requesting Chemical Peel instructions delivers PDF attachment."""
        p = "+923001110036"
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="Send me post care instructions for Chemical Peel")
        self.assertIsNotNone(res["attachment"])
        self.assertEqual(res["attachment"]["pdf_id"], "pdf_chemical_peels")
        self.assertEqual(res["attachment"]["filename"], "Chemical_Peels_Care_Instructions.pdf")

    # -----------------------------------------------------------
    # CATEGORY 7: HUMAN HANDOVER & ROBUSTNESS (37 - 40)
    # -----------------------------------------------------------

    def test_scenario_37_talk_to_reception_anytime(self):
        """37: Typing 'Faraz' or 'talk to reception' routes to human."""
        p = "+923001110037"
        self.bot.process_incoming_message(phone=p, text="1")
        res = self.bot.process_incoming_message(phone=p, text="I want to talk to Faraz at reception")
        self.assertTrue(res["escalated_to_desk"])
        self.assertIn("Connecting with Front-Desk Reception", res["text"])

    def test_scenario_38_two_strike_confusion_fallback(self):
        """38: Two consecutive unrecognized inputs auto-escalates to desk."""
        p = "+923001110038"
        self.bot.process_incoming_message(phone=p, text="1")  # Lang
        # Strike 1
        res1 = self.bot.process_incoming_message(phone=p, text="asdkjhasd??")
        self.assertFalse(res1["escalated_to_desk"])
        # Strike 2
        res2 = self.bot.process_incoming_message(phone=p, text="$$$???")
        self.assertTrue(res2["escalated_to_desk"])
        self.assertIn("connecting you directly with our front desk team", res2["text"])

    def test_scenario_39_sheet_typo_resilience(self):
        """39: Staff typos like 'Teusday 4pm' safely normalized without crash."""
        day = normalize_day("Teusday")
        self.assertEqual(day, "Tuesday")
        t = normalize_time("4pm")
        self.assertEqual(t, "16:00")
        t2 = normalize_time("11:00 AM")
        self.assertEqual(t2, "11:00")

    def test_scenario_40_performance_latency_under_5_seconds(self):
        """40: Bot first response time must be under 5.0 seconds (Target < 2.5s)."""
        start = time.time()
        res = self.bot.process_incoming_message(
            phone="+923001110040",
            text="How much is HydraFacial MD?"
        )
        duration = time.time() - start
        self.assertLess(duration, 5.0, "Response took longer than 5 seconds!")
        self.assertLess(res["latency_ms"], 5000.0)


if __name__ == "__main__":
    unittest.main()
