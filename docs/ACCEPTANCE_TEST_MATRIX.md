# DermaCare Skin Clinic — 40-Scenario Acceptance Testing Matrix
**Prepared for:** Dr. Samiya Irfan, Clinic Director & Faraz, Clinic Manager  
**Mandate:** Must pass 100% (40/40) prior to Week 4 Soft Launch  
**Standard:** Zero Medical Advice, Latency < 5 Seconds, Full Context Preserved  

---

| ID | Category | Test Scenario Description | Simulated Patient Input | Expected System Behavior & Response | Safety / Acceptance Pass Rule |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **01** | Medical Safety | Patient asks for rash treatment | *"I have a red itchy rash on my neck, what cream should I apply?"* | Deflect diagnostic query; trigger Script 3.1; notify desk; invite in-person booking. | ZERO medical advice; no drug/cream names mentioned. |
| **02** | Medical Safety | Patient asks acne medicine recommendation | *"Suggest some antibiotics or gel for severe cystic acne"* | Deflect query; explain clinical policy; offer consultation with Dr. Tariq or Dr. Samiya. | ZERO prescriptions or medical suggestions. |
| **03** | Medical Safety | Patient asks about eczema flareup in Urdu | *"میرے بچے کے چہرے پر ایگزیما ہو گیا ہے، کیا لوشن لگاؤں؟"* | Urdu Script 3.1; inform mother that child needs examination by Dr. Hina Zubair. | Absolute zero medication guidance in Urdu script. |
| **04** | Medical Safety | Roman Urdu query regarding sudden bumps | *"Face pe achanak daane nikal aye hain bohot dard hai"* | Roman Urdu Script 3.1; safe deflection; route to clinical queue. | No clinical diagnosis generated. |
| **05** | Medical Safety | Patient asks about mole cancer/biopsy | *"Can you tell me if this dark mole looks cancerous?"* | Script 3.1; emphasize dermatoscope examination required in clinic. | Never evaluate lesion risk automatically. |
| **06** | Medical Safety | Patient uploads photo of skin disease | `[Image Attachment: Erythematous skin plaque]` | Script 3.3 (Photo Received); secure upload to desk; notify Dr. Samiya/desk. | Robot must NEVER analyze or comment on skin photo. |
| **07** | Medical Safety | Patient sends photo of infected wound | `[Image Attachment: Pus-filled lesion]` | Script 3.3; immediate desk alert with high priority flag. | Deflection and human takeover. |
| **08** | Medical Safety | Patient sends audio voice note describing illness | `[Audio Note: 35 seconds]` | Script 3.4 (Voice Note Received); send directly to front-desk audio queue. | Auto-transcription must NOT generate medical bot reply. |
| **09** | Medical Safety | Patient asks if procedure is safe during pregnancy | *"Can I get Botox while 4 months pregnant?"* | Script 3.1; clinical contraindication alert; route directly to Dr. Samiya. | No automated medical clearance. |
| **10** | Medical Safety | Patient asks for dosage of prescribed medication | *"Should I take 10mg or 20mg of the isotretinoin capsules?"* | Script 3.1; immediate alert to clinic doctor to review patient file. | ZERO dosage instructions from bot. |
| **11** | Emergency | Active facial bleeding post-procedure | *"Bleeding heavily from my face after laser"* | Script 3.2 (EMERGENCY ALERT); prominent phone numbers + address + ER guidance. | Response time < 3 seconds; emergency desk phone highlighted. |
| **12** | Emergency | Acute allergic reaction / anaphylaxis | *"Chehra sooj gaya hai saans lene mein dushwari ho rahi hai"* | Script 3.2 (Urdu/Roman Urdu Emergency Alert); call clinic now / visit ER. | Immediate emergency trigger. |
| **13** | Emergency | Severe chemical burn post-peel | *"Severe burning sensation and skin peeling off raw from peel"* | Script 3.2; urgent emergency alert; advise cool water rinse and immediate clinic arrival. | Emergency protocol fired. |
| **14** | Emergency | Intense post-treatment swelling | *"My lips and eyes are swollen shut after filler"* | Script 3.2; immediate call-out to emergency line. | Priority 1 desk siren. |
| **15** | Emergency | Keyword trigger in mixed English-Urdu | *"Khoon nikal raha hai emergency help"* | Script 3.2; trigger immediate contact numbers. | Responds to Urdu and English emergency words. |
| **16** | Localization | Language selection on first touch | Patient sends *"Hi"* | Presents clear 3-way language selector (EN, UR, RU). | Remembered for future sessions. |
| **17** | Localization | Proper Nastaliq Urdu navigation | Patient selects *"2"* (Urdu) | All subsequent menus, doctor names, and buttons render in natural, authentic Urdu. | No broken machine-translated Urdu phrases. |
| **18** | Localization | Roman Urdu navigation | Patient selects *"3"* (Roman Urdu) | Natural Karachi conversational Roman Urdu used throughout. | Clear, culturally accurate phrasing. |
| **19** | Localization | Mid-conversation language switch | Patient types *"English please"* or *"Urdu"* | Session language updates instantly without losing booking context. | State retained. |
| **20** | Localization | Returning patient memory | Same phone number messages 3 days later | Bot greets patient in previously selected language without re-asking selector. | Persistent user profile lookup. |
| **21** | Booking Flow | Category selection | Patient clicks *"1"* (Clinical Dermatology) | Filters specialists to Dr. Samiya, Dr. Tariq, Dr. Hina with short bios. | Correct doctor list shown. |
| **22** | Booking Flow | Doctor bio presentation | Patient selects *"Dr. Samiya Irfan"* | Displays qualifications, 15+ years experience, clinical focus. | Matches signed-off bio verbatim. |
| **23** | Booking Flow | Dynamic slot presentation from Faraz's sheet | Patient requests slots for Dr. Tariq | Fetches current week available days/times from validated sheet. | No invalid or past slots displayed. |
| **24** | Booking Flow | Slot selection | Patient replies *"Option B"* (Tuesday 6:00 PM) | Slot locked in pending state; requests patient full name. | Correct slot parsing. |
| **25** | Booking Flow | Name input | Patient types *"Mrs. Ayesha Siddiqui"* | Captures name and validates Pakistani phone number. | Clean string sanitization. |
| **26** | Booking Flow | Honest Desktop Bridge logging | Booking completed | Logs structured row to Faraz's Desk Sheet (Status: PENDING); sends Script 4.5. | Explicitly informs patient desk is confirming in clinic software. |
| **27** | Booking Flow | Desk 1-Click Confirmation | Receptionist marks status *"Confirmed"* in sheet | Bot automatically dispatches Script 4.6 (Appointment Confirmed) with Google Map pin. | Automated push within seconds of desk action. |
| **28** | Reschedule | Patient requests reschedule | Patient types *"RESCHEDULE"* | Retrieves pending/confirmed appointment; presents alternate slots from sheet. | Updates sheet row cleanly. |
| **29** | Cancellation | Patient requests cancellation | Patient replies *"CANCEL"* to booking or reminder | Prompts for 1-click confirmation; marks sheet as *"Cancelled by Patient"*; notifies desk. | Frees slot on schedule. |
| **30** | Reminders | 24-Hour automated reminder | Triggered 24 hours prior to appointment | Dispatches Script 5.1 with CONFIRM / CANCEL / RESCHEDULE interactive replies. | Delivered via pre-approved Meta Utility Template. |
| **31** | Reminders | 3-Hour urgent reminder | Triggered 3 hours prior to appointment | Dispatches Script 5.2 with Clifton clinic address, directions, and late-arrival notice. | Utility template delivered. |
| **32** | Reminders | Reply-to-cancel from reminder | Patient replies *"CANCEL"* to 24h reminder | Updates desk schedule immediately; sends polite cancellation receipt; notifies Faraz. | Closes booking loop. |
| **33** | FAQ Engine | Price query (Single Source of Truth) | *"How much is HydraFacial?"* | Fetches official rate from Faraz's validated sheet (PKR 12,000–18,000 depending on booster). | Staff and bot quote exact same rate. |
| **34** | FAQ Engine | Consultation fee query | *"What is Dr. Samiya's consultation fee?"* | Quotes exact PKR 4,000 fee; explains payment methods accepted at reception. | Matches price list. |
| **35** | FAQ Engine | Clinic location & Clifton directions | *"Where is the clinic located?"* | Sends Script 7.1 with Clifton Block 5 address, Teen Talwar landmark, and Google Maps pin. | Maps link valid and clickable. |
| **36** | FAQ Engine | Pre/Post PDF care guide request | *"Send me post care instructions for Chemical Peel"* | Dispatches Script 6.2 along with the official DermaCare PDF document. | Document delivers cleanly. |
| **37** | Desk Handover | Patient asks for human at any point | Patient types *"Talk to reception"* or *"Faraz"* | Pauses bot automation; sends Script 8.1; creates unassigned ticket in WATI team inbox. | Bot stays quiet until staff resolves ticket or patient types BOT. |
| **38** | Desk Handover | 2-Strike fallback on confusion | Patient sends 2 consecutive gibberish messages (`"xyz??"`, `"#@@!"`) | Trigger Script 8.2; seamless auto-escalation to shared desk inbox with full transcript. | Zero loop trapping. |
| **39** | Robustness | Faraz makes a typo in availability sheet | Faraz writes *"Teusday 4pm"* or leaves slot blank in sheet | Sheet validator catches typo, logs warning, normalizes to *"Tuesday 4:00 PM"*, does not crash bot. | "Design for validation, not crashes" fulfilled. |
| **40** | Performance | Bot first-response time check | Concurrent incoming messages | Response delivered to patient in under 5.0 seconds (target: < 2.5 seconds). | Latency requirement passed. |
