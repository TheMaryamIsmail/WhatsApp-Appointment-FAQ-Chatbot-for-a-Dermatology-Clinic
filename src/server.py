"""
FastAPI Server & Webhook Handler for DermaCare Skin Clinic
Meta WhatsApp Cloud API / WATI Integration Server
"""
import logging
from typing import Dict, Any, Optional
from pathlib import Path
from fastapi import FastAPI, Request, Response, Query, HTTPException, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from src.config import WHATSAPP_VERIFY_TOKEN, CLINIC_NAME
from src.bot_controller import BotController
from src.localization import get_message

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DermaCareServer")

app = FastAPI(title=f"{CLINIC_NAME} WhatsApp Automation API", version="1.0.0")
controller = BotController()

# In-memory buffer for outgoing business notifications (desk confirmations, reminders)
patient_outbox: Dict[str, list] = {}

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
if STATIC_DIR.exists():
    app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")


class DeskActionRequest(BaseModel):
    request_id: str
    staff_name: str = "Faraz"


class DirectMessageRequest(BaseModel):
    phone: str
    text: Optional[str] = None
    media_type: Optional[str] = None


class FastBookRequest(BaseModel):
    phone: str
    patient_name: str
    doctor_choice: str = "1"
    slot_choice: str = "A"


@app.get("/", response_class=HTMLResponse)
def root():
    index_file = STATIC_DIR / "index.html"
    if index_file.exists():
        return FileResponse(index_file)
    return {
        "status": "online",
        "clinic": CLINIC_NAME,
        "director": "Dr. Samiya Irfan",
        "location": "Clifton, Karachi"
    }


@app.get("/webhook/whatsapp")
def verify_meta_webhook(
    hub_mode: Optional[str] = Query(None, alias="hub.mode"),
    hub_verify_token: Optional[str] = Query(None, alias="hub.verify_token"),
    hub_challenge: Optional[str] = Query(None, alias="hub.challenge")
):
    """Meta WhatsApp Cloud API verification handshake."""
    if hub_mode == "subscribe" and hub_verify_token == WHATSAPP_VERIFY_TOKEN:
        logger.info("Meta Webhook successfully verified!")
        return Response(content=hub_challenge, media_type="text/plain")
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Verification token mismatch")


@app.post("/webhook/whatsapp")
async def receive_whatsapp_webhook(request: Request):
    """
    Receives incoming webhook events from Meta Cloud API or WATI.
    Extracts sender phone, message content, media attachments, and processes via BotController.
    """
    try:
        data = await request.json()
        logger.info(f"Incoming webhook payload: {data}")

        sender_phone = None
        message_text = None
        media_type = None

        # Format A: Meta Cloud API Payload
        if "entry" in data:
            entry = data["entry"][0]
            changes = entry.get("changes", [])[0]
            value = changes.get("value", {})
            messages = value.get("messages", [])
            if messages:
                msg = messages[0]
                sender_phone = msg.get("from")
                msg_type = msg.get("type")
                if msg_type == "text":
                    message_text = msg.get("text", {}).get("body")
                elif msg_type in ("image", "photo"):
                    media_type = "photo"
                elif msg_type in ("audio", "voice"):
                    media_type = "voice"

        # Format B: WATI / Custom BSP Payload
        elif "sender" in data or "waId" in data:
            sender_phone = data.get("waId") or data.get("sender")
            message_text = data.get("text") or data.get("message")
            if data.get("type") in ("image", "photo"):
                media_type = "photo"
            elif data.get("type") in ("audio", "voice"):
                media_type = "voice"

        # Direct testing payload fallback
        elif "phone" in data:
            sender_phone = data.get("phone")
            message_text = data.get("text")
            media_type = data.get("media_type")

        if not sender_phone:
            return {"status": "ignored", "reason": "No sender phone detected"}

        bot_response = controller.process_incoming_message(
            phone=sender_phone,
            text=message_text,
            media_type=media_type
        )
        return {"status": "success", "response": bot_response}

    except Exception as e:
        logger.error(f"Error handling WhatsApp webhook: {e}", exc_info=True)
        return {"status": "error", "message": str(e)}


@app.post("/api/simulate-message")
def simulate_message(req: DirectMessageRequest):
    """Simulates incoming WhatsApp message for end-to-end testing."""
    response = controller.process_incoming_message(
        phone=req.phone,
        text=req.text,
        media_type=req.media_type
    )
    return response


@app.get("/desk/appointments")
def get_all_desk_appointments(status: str = Query("ALL")):
    """Returns all appointments with counts and optional status filter."""
    result = controller.desk.get_all_appointments(status)
    return result


@app.get("/desk/pending")
def get_pending_desk_queue():
    """Front-desk queue for Faraz and reception staff to enter into clinic software."""
    queue = controller.desk.get_pending_queue()
    return {"pending_count": len(queue), "queue": queue}


@app.get("/api/patient-notifications")
def get_patient_notifications(phone: str = Query(...)):
    """Fetches any outgoing WhatsApp messages dispatched by clinic desk to this patient."""
    msgs = patient_outbox.pop(phone, [])
    return {"phone": phone, "notifications": msgs}


@app.post("/api/fast-book")
def fast_book_appointment(req: FastBookRequest):
    """
    1-Click helper that completes a full end-to-end booking for testing
    and immediately places it into Faraz's desk queue.
    """
    p = req.phone
    controller.process_incoming_message(phone=p, text="1")  # Lang: English
    controller.process_incoming_message(phone=p, text="1")  # Book
    cat = "1" if int(req.doctor_choice) <= 3 else "2"
    controller.process_incoming_message(phone=p, text=cat)  # Category
    controller.process_incoming_message(phone=p, text=req.doctor_choice)  # Doctor
    controller.process_incoming_message(phone=p, text=req.slot_choice)  # Slot
    res = controller.process_incoming_message(phone=p, text=req.patient_name)  # Name
    return {"status": "booked", "response": res}


@app.post("/desk/confirm-appointment")
def confirm_appointment_by_desk(action: DeskActionRequest):
    """
    Fulfills honest desktop flow:
    Front desk staff marks booking confirmed in local software,
    then clicks 'Confirm' in desk view. Bot immediately dispatches
    the official confirmation WhatsApp message with Google Maps pin!
    """
    confirmed = controller.desk.confirm_by_desk(action.request_id, action.staff_name)
    if not confirmed:
        raise HTTPException(status_code=404, detail="Appointment request not found or already confirmed")

    # Send confirmation message to patient via Bot
    session = controller.get_session(confirmed["patient_phone"])
    lang = session.language or "en"
    confirm_msg = get_message(
        "booking_confirmed",
        lang,
        patient_name=confirmed["patient_name"],
        doctor_name=confirmed["doctor_name"],
        slot_time=confirmed["slot_time"],
        map_url=controller.validator.services_cache[0].get("description", "https://maps.google.com/?q=24.8215,67.0312")
    )

    # Queue notification for simulator chat
    p = confirmed["patient_phone"]
    if p not in patient_outbox:
        patient_outbox[p] = []
    patient_outbox[p].append(confirm_msg)

    return {
        "status": "confirmed_and_dispatched",
        "appointment": confirmed,
        "patient_notification": confirm_msg
    }


@app.get("/analytics/report")
def get_monthly_analytics_report():
    """Generates the monthly operational report for Dr. Samiya Irfan."""
    report = controller.analytics.generate_monthly_report()
    return report
