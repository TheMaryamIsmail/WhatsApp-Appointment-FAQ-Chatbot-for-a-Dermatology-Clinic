"""
Configuration for DermaCare Skin Clinic WhatsApp Automation System
Clifton, Karachi, Pakistan
Director: Dr. Samiya Irfan
"""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"

# Clinic Profile & Contact Details
CLINIC_NAME = "DermaCare Skin Clinic"
CLINIC_DIRECTOR = "Dr. Samiya Irfan"
CLINIC_MANAGER = "Faraz"
CLINIC_LOCATION = "Suite 302, 3rd Floor, Clifton Medical Enclave, Khayaban-e-Iqbal, Block 5, Clifton, Karachi"
CLINIC_MAP_URL = "https://maps.google.com/?q=24.8215,67.0312"
CLINIC_PHONE_PRIMARY = "021-3587XXXX"
CLINIC_PHONE_EMERGENCY = "+92-300-1234567"
CLINIC_WHATSAPP_BOT_NUMBER = "+92-300-DERMACARE"

# Data file paths
SERVICES_PRICING_PATH = DATA_DIR / "services_pricing.csv"
DOCTOR_AVAILABILITY_PATH = DATA_DIR / "doctor_availability.csv"
EMERGENCY_KEYWORDS_PATH = DATA_DIR / "emergency_keywords.json"
APPOINTMENTS_DB_PATH = DATA_DIR / "appointments.db"
ANALYTICS_DB_PATH = DATA_DIR / "analytics.db"

# Meta WhatsApp Cloud API / BSP Config (can be loaded via env)
WHATSAPP_API_TOKEN = os.getenv("WHATSAPP_API_TOKEN", "mock_meta_token_dermacare")
WHATSAPP_PHONE_NUMBER_ID = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "100023456789")
WHATSAPP_VERIFY_TOKEN = os.getenv("WHATSAPP_VERIFY_TOKEN", "dermacare_clifton_verify_token_2026")
BSP_PROVIDER = os.getenv("BSP_PROVIDER", "wati")  # wati or 360dialog

# SLA and Performance Targets
MAX_BOT_LATENCY_SECONDS = 5.0
DEFAULT_LANGUAGE = "en"  # "en", "ur", "ru"
