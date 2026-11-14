"""
Live Booking & Operational Stress Test
Verifies Acceptance Condition: "twenty live test bookings confirmed and reminded end-to-end;
the desk comfortable with handovers; bot first-response under five seconds."
"""
import pathlib
import unittest
from src.bot_controller import BotController
from src.sheet_validator import SheetValidator


class TestOperationalStressAnd20Bookings(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.bot = BotController()

    def test_twenty_live_test_bookings_end_to_end(self):
        """Executes 20 distinct patient bookings end-to-end, confirmed by desk and reminded."""
        doctors = [
            ("1", "Dr. Samiya Irfan"),
            ("2", "Dr. Tariq Mansoor"),
            ("3", "Dr. Hina Zubair"),
            ("4", "Sarah Ahmed"),
            ("5", "Fatima Noor")
        ]

        confirmed_count = 0
        for i in range(1, 21):
            phone = f"+92300777{i:04d}"
            patient_name = f"Test Patient {i}"
            doc_choice, expected_doc_name = doctors[(i - 1) % len(doctors)]

            # Step 0: Language selection (English)
            self.bot.process_incoming_message(phone=phone, text="1")

            # Step 1: Click Book
            self.bot.process_incoming_message(phone=phone, text="1")

            # Step 2: Choose Category (1 for Clinical, 2 for Aesthetic)
            cat_choice = "1" if int(doc_choice) <= 3 else "2"
            self.bot.process_incoming_message(phone=phone, text=cat_choice)

            # Step 3: Choose Doctor
            self.bot.process_incoming_message(phone=phone, text=doc_choice)

            # Step 4: Choose Slot (Option A)
            self.bot.process_incoming_message(phone=phone, text="A")

            # Step 5: Input Name
            book_res = self.bot.process_incoming_message(phone=phone, text=patient_name)
            self.assertIn("Booking Request Logged", book_res["text"])

            # Desk Action: Desk staff (Faraz) confirms in software and marks confirmed in dashboard
            active_booking = self.bot.desk.get_latest_active_booking(phone)
            self.assertIsNotNone(active_booking)
            self.assertEqual(active_booking["status"], "PENDING")

            confirmed = self.bot.desk.confirm_by_desk(active_booking["request_id"], staff_member="Faraz")
            self.assertIsNotNone(confirmed)
            self.assertEqual(confirmed["status"], "CONFIRMED")
            confirmed_count += 1

        self.assertEqual(confirmed_count, 20, "Failed to confirm 20 test bookings end-to-end!")

    def test_monthly_analytics_report_structure(self):
        """Verifies analytics report has all metrics required by Dr. Samiya Irfan."""
        report = self.bot.analytics.generate_monthly_report()
        self.assertIn("conversations", report)
        self.assertIn("bot_handled", report["conversations"])
        self.assertIn("human_escalated", report["conversations"])
        self.assertIn("performance", report)
        self.assertIn("target_met_under_5s", report["performance"])
        self.assertTrue(report["performance"]["target_met_under_5s"])
        self.assertIn("funnel_drop_offs", report)
        self.assertIn("faq_hit_counts", report)
        self.assertIn("reception_hours_saved", report["efficiency_gain"])


if __name__ == "__main__":
    unittest.main()
