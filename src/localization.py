"""
Localization Module for DermaCare Skin Clinic
Supports:
- English ('en')
- Urdu Nastaliq Script ('ur')
- Roman Urdu ('ru')
"""

MESSAGES = {
    # 1. Language Selection
    "language_prompt": {
        "en": "Welcome to DermaCare Skin Clinic, Clifton, Karachi.\nUnder the direction of Dr. Samiya Irfan.\n\nبراہِ کرم اپنی پسندیدہ زبان کا انتخاب کریں:\nPlease select your preferred language:\n\n1️⃣ English\n2️⃣ اردو (اردو رسم الخط)\n3️⃣ Roman Urdu\n\n(Reply with 1, 2, or 3)",
        "ur": "ڈرما کیئر سکن کلینک، کلفٹن، کراچی میں خوش آمدید۔\nڈائریکٹر: ڈاکٹر سمیعہ عرفان\n\nبراہِ کرم اپنی پسندیدہ زبان کا انتخاب کریں:\n1️⃣ English\n2️⃣ اردو (اردو رسم الخط)\n3️⃣ Roman Urdu",
        "ru": "DermaCare Skin Clinic, Clifton, Karachi mein khush-aamdeed.\nDirector: Dr. Samiya Irfan\n\nBarah-e-karam language select karein:\n1️⃣ English\n2️⃣ اردو (Urdu Script)\n3️⃣ Roman Urdu"
    },

    # 2. Main Menu
    "main_menu": {
        "en": (
            "✨ *DermaCare Skin Clinic — Main Menu*\n"
            "How may we assist you today?\n\n"
            "1️⃣ 📅 *Book an Appointment*\n"
            "2️⃣ 🔄 *Reschedule or Cancel Booking*\n"
            "3️⃣ 💰 *Services & Treatment Price List*\n"
            "4️⃣ 📍 *Clinic Location & Timings*\n"
            "5️⃣ 📄 *Pre & Post-Procedure Care Guides*\n"
            "6️⃣ 💳 *Consultation Fees & Payment Methods*\n"
            "7️⃣ 👤 *Speak with Front-Desk Reception*\n\n"
            "_(Reply with a number 1–7, or type your query below)_"
        ),
        "ur": (
            "✨ *ڈرما کیئر سکن کلینک — مرکزی مینیو*\n"
            "ہم آپ کی کیا رہنمائی کر سکتے ہیں؟\n\n"
            "1️⃣ 📅 *نیا اپائنٹمنٹ بُک کروائیں*\n"
            "2️⃣ 🔄 *اپائنٹمنٹ تبدیل یا منسوخ کریں*\n"
            "3️⃣ 💰 *سروسز اور علاج کے چارجز*\n"
            "4️⃣ 📍 *کلینک کا پتہ اور اوقاتِ کار*\n"
            "5️⃣ 📄 *علاج سے قبل اور بعد کی ضروری ہدایات (PDFs)*\n"
            "6️⃣ 💳 *کنسلٹیشن فیس اور ادائیگی کے طریقے*\n"
            "7️⃣ 👤 *ہمارے فرنٹ ڈیسک اسٹاف سے بات کریں*\n\n"
            "_(براہِ کرم 1 سے 7 میں سے مطلوبہ نمبر لکھ کر بھیجیں)_"
        ),
        "ru": (
            "✨ *DermaCare Skin Clinic — Main Menu*\n"
            "Hum aap ki kya madad kar saktay hain?\n\n"
            "1️⃣ 📅 *Naya Appointment Book Karein*\n"
            "2️⃣ 🔄 *Appointment Reschedule ya Cancel Karein*\n"
            "3️⃣ 💰 *Services aur Treatment Rates*\n"
            "4️⃣ 📍 *Clinic Location aur Timings*\n"
            "5️⃣ 📄 *Pre aur Post-Procedure Care Guides (PDFs)*\n"
            "6️⃣ 💳 *Consultation Fees aur Payment Methods*\n"
            "7️⃣ 👤 *Front-Desk Receptionist se baat karein*\n\n"
            "_(Apni pasand ka number 1–7 reply karein ya type karein)_"
        )
    },

    # 3. Medical Safety & Zero-Advice Deflection (Line in the Sand #2)
    "medical_query_deflection": {
        "en": (
            "⚠️ *Patient Safety Notice:*\n"
            "At DermaCare, clinical policy strictly prohibits providing medical diagnoses, prescriptions, "
            "or treatment advice via automated messaging.\n\n"
            "Your concern has been forwarded directly to our medical coordination desk. A qualified clinical "
            "team member will review your query and reply during clinic hours.\n\n"
            "To book an in-person consultation with Dr. Samiya Irfan or our specialist team, reply *BOOK* or call *021-3587XXXX*."
        ),
        "ur": (
            "⚠️ *مریضوں کی حفاظت سے متعلق ضروری وضاحت:*\n"
            "ڈرما کیئر سکن کلینک کی پیشہ ورانہ پالیسی کے مطابق، خودکار میسجنگ (بوٹ) کے ذریعے کسی قسم کا طبی مشورہ، "
            "تشخیص یا دوائی تجویز کرنا سخت منع ہے۔\n\n"
            "آپ کا پیغام ہمارے فرنٹ ڈیسک اور میڈیکل عملے کو بھیج دیا گیا ہے جو کلینک کے اوقات میں جائزہ لے کر جلد جواب دیں گے۔\n\n"
            "اگر آپ ڈاکٹر سمیعہ عرفان یا ہماری ٹیم سے باقاعدہ معائنہ کروانا چاہتے ہیں تو *BOOK* لکھیں یا براہِ راست *021-3587XXXX* پر کال کریں۔"
        ),
        "ru": (
            "⚠️ *Patient Safety Notice:*\n"
            "DermaCare clinic ki strict policy hai ke WhatsApp bot ke zariye koi medical advice, diagnosis ya dawai tajweez nahi ki ja sakti.\n\n"
            "Aap ka message hamari medical coordination team ko forward kar diya gaya hai, aur clinic staff jald hi aapse raabta karega.\n\n"
            "Agar aap Dr. Samiya Irfan ya hamari team se clinic aakar consultation karwana chahtay hain to *BOOK* likhein ya *021-3587XXXX* par call karein."
        )
    },

    # Emergency Alert Protocol
    "emergency_alert": {
        "en": (
            "🚨 *URGENT MEDICAL ALERT* 🚨\n\n"
            "If you are experiencing severe bleeding, acute allergic reaction, sudden facial swelling, "
            "chemical burns, or breathing difficulty, *DO NOT WAIT FOR A TEXT REPLY.*\n\n"
            "📞 *CALL OUR CLINIC EMERGENCY LINE IMMEDIATELY:*\n"
            "📱 *+92 300 1234567* or ☎️ *021 3587XXXX*\n\n"
            "📍 *Clinic Address:* Suite 302, 3rd Floor, Clifton Medical Enclave, Block 5, Clifton, Karachi.\n\n"
            "_(If outside clinic hours and severe, please visit South City Hospital ER or Ziauddin Clifton ER immediately)._"
        ),
        "ur": (
            "🚨 *انتہائی ہنگامی میڈیکل الرٹ* 🚨\n\n"
            "اگر آپ کو شدید خون بہنے، چہرے پر اچانک شدید سوجن، کیمیکل سے جلنے یا شدید الرجک ری ایکشن کا سامنا ہے، تو *میسج کے جواب کا ہرگز انتظار نہ کریں۔*\n\n"
            "📞 *فوری طور پر کلینک کی ایمرجنسی لائن پر کال کریں:*\n"
            "📱 *0300-1234567* یا ☎️ *021-3587XXXX*\n\n"
            "📍 *کلینک کا پتہ:* سویٹ 302، کلفٹن میڈیکل انکلیو، بلاک 5، کلفٹن، کراچی۔\n\n"
            "_(اگر اوقاتِ کار کے بعد شدید ایمرجنسی ہو تو فوری طور پر ساؤتھ سٹی ہسپتال یا ضیاء الدین کلفٹن ایمرجنسی رجوع کریں)_"
        ),
        "ru": (
            "🚨 *URGENT EMERGENCY ALERT* 🚨\n\n"
            "Agar khoon beh raha hai, chehre par shadeed soojan hai, chemical burn hai ya shadeed allergy hui hai, to *MESSAGE KE JAWAB KA INTEZAR NA KAREIN.*\n\n"
            "📞 *FORI CALL KAREIN:*\n"
            "📱 *0300-1234567* ya ☎️ *021-3587XXXX*\n\n"
            "📍 *Clinic Address:* Suite 302, Clifton Medical Enclave, Block 5, Clifton, Karachi.\n\n"
            "_(Agar clinic band hai aur shadeed takleef hai to foran South City Hospital ya Ziauddin Clifton Emergency pohnchein)._"
        )
    },

    # Image / Photo Received
    "photo_received": {
        "en": (
            "📷 *Photo Received & Secured:*\n"
            "We have securely received your image. In accordance with clinical safety regulations, automated systems "
            "do not inspect or evaluate skin photos.\n\n"
            "Your photo has been uploaded securely to our confidential desk portal for review by Dr. Samiya and the clinical staff. "
            "Our team will follow up with you shortly.\n\n"
            "_(Note: Accurate dermatological diagnosis requires an in-person dermatoscope examination)._"
        ),
        "ur": (
            "📷 *تصویر موصول ہو گئی ہے:*\n"
            "ہمیں آپ کی تصویر موصول ہو گئی ہے۔ ڈاکٹر سمیعہ عرفان کی سخت ہدایات کے مطابق، خودکار سسٹم کے ذریعے جلد کی تصاویر کی جانچ یا تشخیص نہیں کی جاتی۔\n\n"
            "آپ کی تصویر محفوظ طریقے سے کلینک کے کانفیڈنشل پورٹل پر منتقل کر دی گئی ہے جہاں ہمارے ڈاکٹرز اور ڈیسک عملہ اس کا جائزہ لیں گے۔ عملہ جلد آپ سے رابطہ کرے گا۔"
        ),
        "ru": (
            "📷 *Photo Receive Ho Gayi Hai:*\n"
            "Aap ki photo secured portal par upload ho chuki hai. Medical regulations ke mutabiq robot skin photos ko diagnose nahi kar sakta.\n\n"
            "Ye tasweer confidential desk par Dr. Samiya aur clinical team ke samnay rakh di gayi hai. Humara staff jald raabta karega."
        )
    },

    # Voice Note Received
    "voice_received": {
        "en": "🎙️ *Voice Note Received:* Our front-desk team is listening to your audio message and will reply in writing or call you back shortly.",
        "ur": "🎙️ *وائس میسج موصول ہو گیا ہے:* ہمارے فرنٹ ڈیسک کا عملہ آپ کا آڈیو میسج سن کر جلد ہی آپ کو جواب یا کال کرے گا۔",
        "ru": "🎙️ *Voice Note Receive Ho Gaya:* Hamari reception team aap ka voice note sun kar jald text reply ya call back karegi."
    },

    # Handover to Reception
    "desk_handover": {
        "en": (
            "👤 *Connecting with Front-Desk Reception:*\n"
            "Automated replies have been paused. Faraz or an on-duty receptionist has been notified and will assist you directly.\n\n"
            "📞 Direct Desk Line: *021-3587XXXX*\n"
            "_(Type *BOT* anytime to return to the automated service)._"
        ),
        "ur": (
            "👤 *فرنٹ ڈیسک اسٹاف کو منتقل کیا جا رہا ہے:*\n"
            "خودکار بوٹ کو روک دیا گیا ہے اور فرنٹ ڈیسک کو مطلع کر دیا گیا ہے۔ فراز یا ہماری ٹیم کی رکن آپ کی رہنمائی کریں گی۔\n\n"
            "📞 فون نمبر: *021-3587XXXX*\n"
            "_(دوبارہ بوٹ مینیو پر جانے کے لیے *BOT* لکھیں)_"
        ),
        "ru": (
            "👤 *Front-Desk Reception se Raabta:*\n"
            "Automated bot pause ho chuka hai aur receptionist ko notify kar diya gaya hai. Faraz ya reception team jald message karegi.\n\n"
            "📞 Direct Phone: *021-3587XXXX*\n"
            "_(Wapas menu ke liye *BOT* type karein)_"
        )
    },

    # 2-Strike Confusion Fallback
    "confusion_fallback": {
        "en": "I want to ensure you receive the exact assistance you need without confusion. I am connecting you directly with our front desk team now.",
        "ur": "میں یقینی بنانا چاہتا ہوں کہ آپ کو درست معلومات ملیں۔ میں آپ کا رابطہ فوری طور پر ہمارے فرنٹ ڈیسک اسٹاف سے کروا رہا ہوں۔",
        "ru": "Mein aap ki baat direct humari reception team se karwa raha hoon taake aap ko behtar maloomat mil sakein. Humara staff abhi aapse raabta karega."
    },

    # 4. Booking Flow Steps
    "booking_step_category": {
        "en": (
            "📅 *Step 1/5: Select Service Category*\n"
            "Please select the nature of your visit:\n\n"
            "1️⃣ *Clinical Dermatology* (Acne, Eczema, Psoriasis, Hair Loss, Mole checks, Rashes)\n"
            "2️⃣ *Aesthetic & Cosmetic Procedures* (HydraFacial, Chemical Peels, Microneedling/PRP, Laser Hair Removal)\n"
            "3️⃣ *Advanced Injectables & Anti-Aging* (Botox, Dermal Fillers, CO2 Fractional Laser)\n\n"
            "_(Reply with 1, 2, or 3)_"
        ),
        "ur": (
            "📅 *مرحلہ 1/5: علاج یا معائنے کی قسم منتخب کریں*\n\n"
            "1️⃣ *کلینیکل ڈرمیٹولوجی* (کیل مہاسے، الرجی، ایگزیما، خارش، بال گرنا، تل یا جلدی امراض)\n"
            "2️⃣ *کاسمیٹک و فیشل ٹریٹمنٹس* (ہائیڈرا فیشل، کیمیکل پیلز، پی آر پی، لیزر ہیئر ریموول)\n"
            "3️⃣ *ایڈوانسڈ اینٹی ایجنگ اور فلرز* (بوٹوکس، فلرز، فریکشنل CO2 لیزر)\n\n"
            "_(براہِ کرم 1، 2 یا 3 لکھ کر بھیجیں)_"
        ),
        "ru": (
            "📅 *Step 1/5: Category Select Karein*\n\n"
            "1️⃣ *Clinical Dermatology* (Acne, daane, baal girna, allergy, eczema, skin infection)\n"
            "2️⃣ *Aesthetic Treatments* (HydraFacial, Chemical Peels, PRP, Laser Hair Removal)\n"
            "3️⃣ *Injectables & Laser* (Botox, Fillers, CO2 Laser)\n\n"
            "_(Reply karein 1, 2, ya 3)_"
        )
    },

    "booking_step_doctor": {
        "en": "📅 *Step 2/5: Choose Your Specialist*\n\n{doctor_list}\n_(Reply with the doctor number)_",
        "ur": "📅 *مرحلہ 2/5: اپنے ماہر ڈاکٹر کا انتخاب کریں*\n\n{doctor_list}\n_(براہِ کرم متعلقہ نمبر لکھ کر بھیجیں)_",
        "ru": "📅 *Step 2/5: Specialist Select Karein*\n\n{doctor_list}\n_(Doctor number reply karein)_"
    },

    "booking_step_slot": {
        "en": "📅 *Step 3/5: Select Day & Time Slot for {doctor_name}*\n\n{slot_list}\n_(Reply with the option letter, e.g. A, B, C)_",
        "ur": "📅 *مرحلہ 3/5: {doctor_name} کے لیے دن اور وقت منتخب کریں*\n\n{slot_list}\n_(براہِ کرم آپشن کا حرف جیسے A, B, C لکھ کر بھیجیں)_",
        "ru": "📅 *Step 3/5: {doctor_name} ke liye Slot Muntakhib Karein*\n\n{slot_list}\n_(Option letter reply karein, maslan A, B, C)_"
    },

    "booking_step_name": {
        "en": "📅 *Step 4/5: Patient Information*\nPlease reply with the *Full Name* of the patient attending the consultation:",
        "ur": "📅 *مرحلہ 4/5: مریض کی معلومات*\nبراہِ کرم مریض کا *مکمل نام* درج فرمائیں جو معائنے کے لیے تشریف لائیں گے:",
        "ru": "📅 *Step 4/5: Patient Ki Maloomat*\nBarah-e-karam checkup ke liye aane walay mareez ka *Pura Naam* type karein:"
    },

    "booking_request_logged": {
        "en": (
            "⏳ *Booking Request Logged (Ref #{request_id})*\n\n"
            "• *Patient:* {patient_name}\n"
            "• *Doctor:* {doctor_name}\n"
            "• *Slot:* {slot_time}\n"
            "• *Fee:* PKR {fee} *(payable at reception)*\n\n"
            "📌 *Next Step:* Our front-desk manager (Faraz or desk staff) is confirming this slot in our clinic software. "
            "You will receive an official *Booking Confirmation Message* within 15–20 minutes during clinic hours.\n\n"
            "_(To change details, reply *EDIT* or *MENU*)_"
        ),
        "ur": (
            "⏳ *درخواست موصول ہو گئی ہے (ریفرنس: #{request_id})*\n\n"
            "• *مریض کا نام:* {patient_name}\n"
            "• *ڈاکٹر:* {doctor_name}\n"
            "• *وقت:* {slot_time}\n"
            "• *کنسلٹیشن فیس:* {fee} روپے\n\n"
            "📌 *اگلا مرحلہ:* ہمارے فرنٹ ڈیسک منیجر (فراز یا ڈیسک اسٹاف) کلینک سافٹ ویئر میں اس وقت کا اندراج کر رہے ہیں۔ "
            "کلینک اوقات کے دوران اگلے 15 سے 20 منٹ میں آپ کو حتمی تصدیقی میسج موصول ہو جائے گا۔"
        ),
        "ru": (
            "⏳ *Booking Request Log Ho Gayi (Ref #{request_id})*\n\n"
            "• *Patient:* {patient_name}\n"
            "• *Doctor:* {doctor_name}\n"
            "• *Waqt:* {slot_time}\n"
            "• *Fee:* PKR {fee}\n\n"
            "📌 *Agla Marhala:* Humara front-desk staff is slot ko clinic system mein confirm kar raha hai. "
            "15–20 minute ke andar aap ko confirmation message mil jayega."
        )
    },

    "booking_confirmed": {
        "en": (
            "✅ *APPOINTMENT CONFIRMED!*\n\n"
            "Dear {patient_name}, your consultation with *{doctor_name}* has been confirmed by DermaCare front desk.\n\n"
            "📅 *Date & Time:* {slot_time}\n"
            "📍 *Location:* Suite 302, Clifton Medical Enclave, Block 5, Clifton, Karachi.\n"
            "🗺️ *Google Maps Pin:* {map_url}\n\n"
            "⚠️ *Please arrive 10 minutes prior* to your scheduled appointment.\n"
            "To reschedule or cancel at any time, simply reply *CANCEL* or *RESCHEDULE*."
        ),
        "ur": (
            "✅ *اپائنٹمنٹ کی حتمی تصدیق!*\n\n"
            "محترم {patient_name}، *{doctor_name}* کے ساتھ آپ کا وقت ڈرما کیئر فرنٹ ڈیسک نے کنفرم کر دیا ہے۔\n\n"
            "📅 *تاریخ اور وقت:* {slot_time}\n"
            "📍 *پتہ:* سویٹ 302، کلفٹن میڈیکل انکلیو، بلاک 5، کلفٹن، کراچی۔\n"
            "🗺️ *گوگل میپ لوکیشن:* {map_url}\n\n"
            "⚠️ گزارش ہے کہ وقت سے 10 منٹ پہلے تشریف لائیں۔ منسوخ کرنے کے لیے *CANCEL* یا *RESCHEDULE* لکھیں۔"
        ),
        "ru": (
            "✅ *APPOINTMENT CONFIRM HO GAYA HAI!*\n\n"
            "Mohtaram {patient_name}, *{doctor_name}* ke sath aap ka appointment desk se confirm ho chuka hai.\n\n"
            "📅 *Date & Time:* {slot_time}\n"
            "📍 *Location:* Suite 302, Clifton Medical Enclave, Block 5, Clifton, Karachi.\n"
            "🗺️ *Map Pin:* {map_url}\n\n"
            "Barah-e-karam 10 minute pehle tashreef layein. Cancel ya reschedule karne ke liye *CANCEL* ya *RESCHEDULE* reply karein."
        )
    },

    # Reminders
    "reminder_24h": {
        "en": (
            "🔔 *Appointment Reminder (Tomorrow)*\n\n"
            "Dear {patient_name}, this is a gentle reminder of your upcoming consultation with *{doctor_name}* tomorrow, *{slot_time}*.\n\n"
            "Please confirm your attendance by replying:\n"
            "1️⃣ *CONFIRM* (I will be there)\n"
            "2️⃣ *CANCEL* (I cannot make it)\n"
            "3️⃣ *RESCHEDULE* (Change date/time)"
        ),
        "ur": (
            "🔔 *اپائنٹمنٹ یاد دہانی (بروز کل)*\n\n"
            "محترم {patient_name}، کل *{slot_time}* آپ کا *{doctor_name}* کے ساتھ معائنہ مقرر ہے۔\n\n"
            "براہِ کرم اپنی آمد کی تصدیق فرمائیں:\n"
            "1️⃣ *CONFIRM* (جی ہاں، میں آؤں گا/گی)\n"
            "2️⃣ *CANCEL* (میں نہیں آ سکتا/سکتی)\n"
            "3️⃣ *RESCHEDULE* (وقت تبدیل کروائیں)"
        ),
        "ru": (
            "🔔 *Appointment Reminder (Kal)*\n\n"
            "Mohtaram {patient_name}, kal *{slot_time}* par aap ka *{doctor_name}* ke sath appointment hai.\n\n"
            "Barah-e-karam reply karein:\n"
            "1️⃣ *CONFIRM* (Aaon ga/gi)\n"
            "2️⃣ *CANCEL* (Nahi aa sakta/sakti)\n"
            "3️⃣ *RESCHEDULE* (Date change karein)"
        )
    },

    "reminder_3h": {
        "en": (
            "⏰ *Appointment in 3 Hours:*\n"
            "Dear {patient_name}, your consultation with *{doctor_name}* is today at *{slot_time}*.\n\n"
            "📍 Clinic Location: Suite 302, Clifton Medical Enclave, Block 5, Clifton.\n"
            "🚗 Valet & basement parking available.\n"
            "If running late, please let us know immediately by replying here!"
        ),
        "ur": (
            "⏰ *3 گھنٹے میں آپ کا اپائنٹمنٹ ہے:*\n"
            "محترم {patient_name}، آج *{slot_time}* پر آپ کا *{doctor_name}* کے ساتھ معائنہ ہے۔\n\n"
            "📍 کلفٹن میڈیکل انکلیو، بلاک 5، کلفٹن، کراچی۔\n"
            "اگر پہنچنے میں تاخیر ہو تو فوراً یہاں آگاہ فرمائیں!"
        ),
        "ru": (
            "⏰ *Aap ka Appointment 3 Ghantay Mein Hai:*\n"
            "Mohtaram {patient_name}, aaj *{slot_time}* par *{doctor_name}* ke sath appointment hai.\n\n"
            "📍 Suite 302, Clifton Medical Enclave, Block 5, Clifton.\n"
            "Agar late ho jayein to foran yahan message karein!"
        )
    },

    # Cancellation Confirmation
    "cancellation_done": {
        "en": "❌ Your appointment #{request_id} has been cancelled. If you wish to re-book at a later time, simply reply *BOOK*.",
        "ur": "❌ آپ کا اپائنٹمنٹ ریفرنس #{request_id} منسوخ کر دیا گیا ہے۔ دوبارہ بکنگ کے لیے *BOOK* لکھ کر بھیجیں۔",
        "ru": "❌ Aap ka appointment #{request_id} cancel ho gaya hai. Dobara booking ke liye *BOOK* type karein."
    },

    # FAQs
    "faq_location_timings": {
        "en": (
            "📍 *DermaCare Skin Clinic Location & Hours:*\n"
            "• Suite 302, 3rd Floor, Clifton Medical Enclave, Khayaban-e-Iqbal, Block 5, Clifton, Karachi.\n"
            "• Landmark: Near Teen Talwar & Schon Circle.\n"
            "🗺️ *Google Maps Pin:* https://maps.google.com/?q=24.8215,67.0312\n\n"
            "🕒 *Clinic Timings:*\n"
            "• Monday to Saturday: 11:00 AM – 8:30 PM\n"
            "• Sunday: Closed\n"
            "🚗 Dedicated basement valet parking available."
        ),
        "ur": (
            "📍 *ڈرما کیئر سکن کلینک کا پتہ اور اوقات:*\n"
            "• سویٹ 302، تیسری منزل، کلفٹن میڈیکل انکلیو، خیابانِ اقبال، بلاک 5، کلفٹن، کراچی (تین تلوار کے قریب)۔\n"
            "🗺️ *گوگل میپ لوکیشن:* https://maps.google.com/?q=24.8215,67.0312\n\n"
            "🕒 *اوقاتِ کار:*\n"
            "• پیر تا ہفتہ: صبح 11:00 تا رات 8:30 بجے\n"
            "• اتوار: چھٹی\n"
            "🚗 کلینک کی بیسمنٹ میں گاڑی پارکنگ کی سہولت موجود ہے۔"
        ),
        "ru": (
            "📍 *Clinic Location aur Timings:*\n"
            "• Suite 302, 3rd Floor, Clifton Medical Enclave, Block 5, Clifton, Karachi (Teen Talwar ke paas).\n"
            "🗺️ *Map Pin:* https://maps.google.com/?q=24.8215,67.0312\n\n"
            "🕒 *Timings:*\n"
            "• Monday to Saturday: 11:00 AM se 8:30 PM\n"
            "• Sunday: Off\n"
            "🚗 Basement parking available hai."
        )
    },

    "faq_fees_payments": {
        "en": (
            "💳 *Consultation Fees & Payment Methods:*\n\n"
            "• Dr. Samiya Irfan (Director): PKR 4,000\n"
            "• Dr. Tariq Mansoor (Consultant): PKR 3,000\n"
            "• Dr. Hina Zubair (Associate): PKR 2,500\n"
            "• Aesthetic Evaluation: PKR 1,500 *(Waived if procedure taken on the same day)*\n\n"
            "💵 *Payment Methods:*\n"
            "Cash at counter, Visa / Mastercard Credit & Debit cards, Raast ID, Bank Transfer (Faysal / Meezan), and JazzCash."
        ),
        "ur": (
            "💳 *کنسلٹیشن فیس اور ادائیگی کے طریقے:*\n\n"
            "• ڈاکٹر سمیعہ عرفان (ڈائریکٹر): 4,000 روپے\n"
            "• ڈاکٹر طارق منصور: 3,000 روپے\n"
            "• ڈاکٹر حنا زبیر: 2,500 روپے\n"
            "• ایستھیٹک معائنہ: 1,500 روپے *(اگر اسی دن ٹریٹمنٹ کروائیں تو فیس معاف)*\n\n"
            "💵 *ادائیگی کے ذرائع:*\n"
            "کیش، تمام ڈیبٹ اور کریڈٹ کارڈز، راست (Raast)، آن لائن بینک ٹرانسفر، اور جاز کیش۔"
        ),
        "ru": (
            "💳 *Consultation Fees aur Payment Methods:*\n\n"
            "• Dr. Samiya Irfan: PKR 4,000\n"
            "• Dr. Tariq Mansoor: PKR 3,000\n"
            "• Dr. Hina Zubair: PKR 2,500\n"
            "• Aesthetic Consultation: PKR 1,500 *(Procedure lene par waive)*\n\n"
            "💵 *Payment:*\n"
            "Cash, Visa/Mastercard Debit & Credit Cards, Raast, Bank Transfer aur JazzCash."
        )
    }
}

DOCTOR_BIOS = {
    "doc_samiya": {
        "en": "👩‍⚕️ *1. Dr. Samiya Irfan (Clinic Director)*\n• MBBS, FCPS (Dermatology)\n• 15+ years experience; Expert in complex clinical dermatology, Melasma, and advanced aesthetic injectables.",
        "ur": "👩‍⚕️ *1. ڈاکٹر سمیعہ عرفان (ڈائریکٹر کلینک)*\n• ایم بی بی ایس، ایف سی پی ایس (ڈرمیٹولوجی)\n• 15 سالہ تجربہ؛ جلدی امراض، چھائیاں، اینٹی ایجنگ اور فلرز کی ماہر۔",
        "ru": "👩‍⚕️ *1. Dr. Samiya Irfan (Clinic Director)*\n• MBBS, FCPS Dermatology, 15+ years experience, complex skin issues, melasma & injectables."
    },
    "doc_tariq": {
        "en": "👨‍⚕️ *2. Dr. Tariq Mansoor (Consultant Dermatologist)*\n• MBBS, MCPS, Dip Derm (UK)\n• Acne scar revision, Hair restoration, and general dermatology.",
        "ur": "👨‍⚕️ *2. ڈاکٹر طارق منصور (کنسلٹنٹ ڈرمیٹولوجسٹ)*\n• ایکنی کے نشانات، بالوں کا گرنا اور عمومی جلدی بیماریاں۔",
        "ru": "👨‍⚕️ *2. Dr. Tariq Mansoor*\n• Acne scars, hair loss, general skin checkup."
    },
    "doc_hina": {
        "en": "👩‍⚕️ *3. Dr. Hina Zubair (Associate Dermatologist)*\n• MBBS, MSc Dermatology\n• Pediatric dermatology, eczema, and skin glow rejuvenation.",
        "ur": "👩‍⚕️ *3. ڈاکٹر حنا زبیر (ڈرمیٹولوجسٹ)*\n• بچوں کے جلدی مسائل، ایگزیما اور رنگت کا نکھار۔",
        "ru": "👩‍⚕️ *3. Dr. Hina Zubair*\n• Pediatric dermatology, eczema, pigmentation & sensitive skin."
    },
    "cons_sarah": {
        "en": "✨ *4. Sarah Ahmed (Senior Aesthetic Consultant)*\n• Certified Laser Specialist & HydraFacial Expert.",
        "ur": "✨ *4. سارہ احمد (سینئر ایستھیٹک کنسلٹنٹ)*\n• لیزر ہیئر ریموول اور ہائیڈرا فیشل اسپیشلسٹ۔",
        "ru": "✨ *4. Sarah Ahmed*\n• Laser hair removal & HydraFacial expert."
    },
    "cons_fatima": {
        "en": "✨ *5. Fatima Noor (Aesthetic Consultant)*\n• Chemical peels, skin rejuvenation & PRP therapy.",
        "ur": "✨ *5. فاطمہ نور (ایستھیٹک کنسلٹنٹ)*\n• کیمیکل پیلز اور پی آر پی تھراپی۔",
        "ru": "✨ *5. Fatima Noor*\n• Chemical Peels, rejuvenation & PRP."
    }
}

PROCEDURE_PDF_CAPTIONS = {
    "pdf_hydrafacial": {
        "en": "📄 *Attached:* HydraFacial Pre/Post Care Guide (Avoid direct sun for 48 hours).",
        "ur": "📄 *منسلک فائل:* ہائیڈرا فیشل سے قبل اور بعد کی ضروری ہدایات (48 گھنٹے دھوپ سے پرہیز کریں)۔",
        "ru": "📄 *Attached:* HydraFacial Pre & Post Care Guide (48 hours direct dhoop se bachein)."
    },
    "pdf_chemical_peels": {
        "en": "📄 *Attached:* Chemical Peel Post-Care Guide (Do not pick peeling skin; keep moisturized).",
        "ur": "📄 *منسلک فائل:* کیمیکل پیل کی ضروری ہدایات (اترتی جلد کو ہاتھ سے مت کھینچیں)۔",
        "ru": "📄 *Attached:* Chemical Peel Post-Care (Peeling skin ko haath se mat utarein)."
    },
    "pdf_laser_hair_removal": {
        "en": "📄 *Attached:* Laser Hair Removal Protocol (Shave 24h prior; no waxing/threading).",
        "ur": "📄 *منسلک فائل:* لیزر ہیئر ریموول ہدایات (سیشن سے قبل ویکسنگ نہ کریں)۔",
        "ru": "📄 *Attached:* Laser Hair Removal Guide (Waxing/threading nahi karni)."
    },
    "pdf_prp_microneedling": {
        "en": "📄 *Attached:* Microneedling & PRP Aftercare (No makeup or sweating for 24 hours).",
        "ur": "📄 *منسلک فائل:* پی آر پی اور مائیکرو نیڈلنگ کی دیکھ بھال کی ہدایات۔",
        "ru": "📄 *Attached:* PRP / Microneedling Aftercare (24 hours makeup na lagayein)."
    },
    "pdf_botox_fillers": {
        "en": "📄 *Attached:* Botox & Fillers Instructions (Remain upright for 4h; no gym for 24h).",
        "ur": "📄 *منسلک فائل:* بوٹوکس اور فلرز ہدایات (4 گھنٹے تک سیدھے رہیں اور جھکیں نہیں)۔",
        "ru": "📄 *Attached:* Botox & Fillers Guide (4 hours seedhay rahein, 24h gym na karein)."
    },
    "pdf_co2_laser": {
        "en": "📄 *Attached:* CO2 Fractional Laser Wound Care & Sun Protection Protocol.",
        "ur": "📄 *منسلک فائل:* فریکشنل CO2 لیزر کیئر اور سن بلاک ہدایات۔",
        "ru": "📄 *Attached:* CO2 Fractional Laser Protocol (Sunblock aur healing ointment)."
    },
    "pdf_wart_removal": {
        "en": "📄 *Attached:* Wart / Skin Tag Cautery Aftercare (Keep dry for 24h; apply prescribed cream).",
        "ur": "📄 *منسلک فائل:* مسے یا سکن ٹیگ اتارنے کے بعد زخم کی دیکھ بھال کی ہدایات۔",
        "ru": "📄 *Attached:* Wart Removal Aftercare (24 hours dry rakhein)."
    },
    "pdf_glutathione_iv": {
        "en": "📄 *Attached:* Glutathione IV Drip Hydration Advisory (Drink 2.5–3L water daily).",
        "ur": "📄 *منسلک فائل:* گلوٹاتھائیون ڈرپ کے بعد کی ہدایات (روزانہ وافر مقدار میں پانی پیئیں)۔",
        "ru": "📄 *Attached:* Glutathione IV Drip Guide (Daily 2.5-3 liters pani piyein)."
    }
}


def get_message(key: str, lang: str = "en", **kwargs) -> str:
    """Retrieve localized message string with safe fallback and template substitution."""
    lang = lang.lower() if lang in ("en", "ur", "ru") else "en"
    text_dict = MESSAGES.get(key, {})
    template = text_dict.get(lang) or text_dict.get("en", f"[{key}]")
    if kwargs:
        try:
            return template.format(**kwargs)
        except Exception:
            return template
    return template
