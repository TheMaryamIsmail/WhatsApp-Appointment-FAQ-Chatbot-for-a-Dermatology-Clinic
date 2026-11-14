# DermaCare Skin Clinic — WhatsApp Business Automation Engine
**Client:** DermaCare Skin Clinic, Clifton, Karachi  
**Director:** Dr. Samiya Irfan (MBBS, FCPS Dermatology)  
**Clinic Manager:** Faraz  
**Project ID:** FF-026 | Freelancing Fest 2026 (IU Spectrum 2.0, Iqra University)  

---

## 🌟 Executive Overview
This production engine solves message burnout for DermaCare Skin Clinic, eliminating the 40+ minute delay across 120–150 daily patient interactions and saving an estimated 15–20 bookings per week. Built strictly on the **Official WhatsApp Business Cloud API**, it respects Dr. Samiya Irfan's non-negotiable medical safety rules, delivers natural Urdu script localization, and implements a resilient desktop bridge for clinic systems without APIs.

---

## 🛡️ Core Architectural Pillars

### 1. Three Non-Negotiable Lines in the Sand
1. **Official WhatsApp Business API Only:** Zero unofficial tooling. Direct Meta billing with WATI ($49/mo) and transparent per-conversation rates ($0.0195 service, $0.015 utility in Pakistan).
2. **Zero Medical Advice Guarantee:** Strict regex/fuzzy keyword interceptor flags symptoms, skin photos, voice notes, and pregnancy contraindications, immediately deflecting to human medical staff. Emergency red flags (bleeding, anaphylaxis, severe burns) fire instant hotlines.
3. **Trilingual Pakistani Localization:** Natural English, proper Nastaliq Urdu script, and colloquial Roman Urdu — chosen at first touch and remembered across sessions.

### 2. Desktop Software Bridge ("No API" Realism)
- DermaCare's local desktop appointment software has no API.
- The bot logs a structured `PENDING` request into Faraz's queue (`DeskBridge`).
- Reception enters the booking into the software and clicks **Confirm** in the desk dashboard.
- The bot dispatches an official **Appointment Confirmed** WhatsApp message with a Google Maps pin, plus automated 24-hour and 3-hour reminders with reply-to-cancel buttons.

### 3. Fault-Tolerant Sheet Resilience ("Design for Validation, Not Crashes")
- Staff typos in availability or price sheets (`Teusday`, `4pm`, `wed`, irregular casing, extra spaces) are safely parsed and normalized.
- Malformed rows log warnings without crashing the bot or dropping other slots.

---

## 📁 Repository Structure
```
dermacare-whatsapp-bot/
├── data/
│   ├── services_pricing.csv         # Faraz's single source of truth for 14 services & 8 procedure PDFs
│   ├── doctor_availability.csv      # Doctor schedules with typo resilience
│   ├── emergency_keywords.json      # Emergency, symptom, and handover keyword patterns
│   ├── appointments.db              # SQLite queue for desk bridge
│   └── analytics.db                 # Monthly operational telemetry database
├── docs/
│   ├── PROVIDER_COMPARISON_AND_COST_SHEET.md  # Official WATI vs 360dialog cost comparison
│   ├── MIGRATION_TRADEOFFS_IN_WRITING.md       # Written migration trade-off analysis
│   ├── TRILINGUAL_SCRIPT_BOOK.md               # Complete dialogue script book
│   └── ACCEPTANCE_TEST_MATRIX.md               # 40-scenario acceptance testing matrix
├── src/
│   ├── config.py                    # Environment & clinic settings
│   ├── localization.py              # EN, Nastaliq UR, and Roman RU messages & doctor bios
│   ├── sheet_validator.py           # Typo-tolerant CSV parser & validator
│   ├── triage_engine.py             # Emergency, medical query & media interceptors
│   ├── faq_engine.py                # Single-source pricing & PDF care guides
│   ├── desk_bridge.py               # Local desktop bridge & appointment state
│   ├── analytics.py                 # Monthly report & funnel telemetry
│   ├── bot_controller.py            # Central orchestrator & dialog state machine
│   └── server.py                    # FastAPI Meta webhook & desk API server
└── tests/
    ├── test_acceptance_40_scenarios.py       # Full 40-scenario test suite (100% pass)
    └── test_safety_and_validation.py         # 20 live test bookings end-to-end
```

---

## 🚀 Quickstart & Verification

### 0. Configure WhatsApp credentials
Install dependencies with `pip install -r requirements.txt`, then replace the placeholder values in the root `.env` with your WhatsApp provider credentials. `BSP_PROVIDER` accepts `wati` or `360dialog`. The application loads `.env` automatically; the file is excluded from Git so credentials are not committed.

### 1. Run the 40-Scenario Acceptance Test Suite
```powershell
python -m unittest tests/test_acceptance_40_scenarios.py
```

### 2. Run the 20 Live Test Bookings Verification
```powershell
python -m unittest tests/test_safety_and_validation.py
```

### 3. Launch the API & Webhook Server
```powershell
uvicorn src.server:app --reload --port 8000
```
- Interactive Docs: `http://localhost:8000/docs`
- Desk Pending Queue: `http://localhost:8000/desk/pending`
- Monthly Analytics: `http://localhost:8000/analytics/report`
