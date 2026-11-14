# DermaCare Skin Clinic — Master Trilingual Dialogue Script Book
**Author:** AI Automation Engineering Team  
**Reviewer & Final Authority:** Dr. Samiya Irfan, Clinic Director  
**Clinic Manager:** Faraz  
**Version:** 1.0 (Production Candidate for Thursday Review)  
**Supported Languages:** English (EN) | Urdu Nastaliq Script (UR) | Roman Urdu (RU)  

---

## 1. Language Selection & First Contact

### Script 1.1: First-Time User Welcome & Language Selector
*Trigger:* When a new number messages the clinic for the first time.
*System Logic:* Stores the user's language selection (`en`, `ur`, `ru`) in the patient session table. All future messages default to this language automatically unless changed.

| Language | Message Script |
| :--- | :--- |
| **Bilingual Greeting** | **Welcome to DermaCare Skin Clinic, Clifton, Karachi.**<br>Under the direction of Dr. Samiya Irfan.<br><br>براہِ کرم اپنی پسندیدہ زبان کا انتخاب کریں:<br>Please select your preferred language:<br><br>1️⃣ English<br>2️⃣ اردو (اردو رسم الخط)<br>3️⃣ Roman Urdu |

---

## 2. Main Menu

### Script 2.1: Main Menu
*Trigger:* After language selection, or when patient types "Menu" / "Home" / "Start".

| Language | Script |
| :--- | :--- |
| **English** | **DermaCare Skin Clinic**<br>How may we assist you today?<br><br>1️⃣ 📅 Book an Appointment<br>2️⃣ 🔄 Reschedule or Cancel Booking<br>3️⃣ 💰 Services & Treatment Price List<br>4️⃣ 📍 Clinic Location & Timings<br>5️⃣ 📄 Pre & Post-Procedure Care Guides<br>6️⃣ 💳 Consultation Fees & Payment Methods<br>7️⃣ 👤 Speak with Front-Desk Reception<br><br>*(Reply with the number of your choice, or type your query below)* |
| **Urdu (اردو)** | **ڈرما کیئر سکن کلینک، کلفٹن**<br>ہم آپ کی کیا رہنمائی کر سکتے ہیں؟<br><br>1️⃣ 📅 نیا اپائنٹمنٹ بُک کروائیں<br>2️⃣ 🔄 وقت تبدیل یا منسوخ کریں<br>3️⃣ 💰 سروسز اور علاج کے چارجز<br>4️⃣ 📍 کلینک کا پتہ اور اوقاتِ کار<br>5️⃣ 📄 علاج سے قبل اور بعد کی ضروری ہدایات (PDFs)<br>6️⃣ 💳 کنسلٹیشن فیس اور ادائیگی کے طریقے<br>7️⃣ 👤 ہمارے فرنٹ ڈیسک اسٹاف سے بات کریں<br><br>*(براہِ کرم متعلقہ نمبر لکھ کر بھیجیں)* |
| **Roman Urdu** | **DermaCare Skin Clinic, Clifton**<br>Hum aap ki kya madad kar saktay hain?<br><br>1️⃣ 📅 Naya Appointment Book Karein<br>2️⃣ 🔄 Appointment Reschedule ya Cancel Karein<br>3️⃣ 💰 Services aur Treatment Rates<br>4️⃣ 📍 Clinic Location aur Timings<br>5️⃣ 📄 Treatment se pehle aur baad ki hidayat (PDFs)<br>6️⃣ 💳 Consultation Fees aur Payment ke tareeqay<br>7️⃣ 👤 Front-Desk Receptionist se baat karein<br><br>*(Apni pasand ka number reply karein ya type karein)* |

---

## 3. Strict Medical Safety & Zero-Advice Guardrails (Line in the Sand #2)

### Script 3.1: Medical Query / Symptom Question Deflection
*Trigger:* Any question asking for medical diagnosis, prescriptions, creams, rashes, acne treatment, dosage, or symptoms (e.g., *"mera chehra red ho gaya hai"*, *"which cream for dark circles?"*, *"is this eczema?"*).
*System Logic:* Instantly flags the message as a clinical query. ZERO diagnostic advice is generated. Alerts the front-desk shared inbox with patient phone and transcript.

| Language | Script |
| :--- | :--- |
| **English** | **Patient Safety Notice:**<br>At DermaCare, our clinical policy strictly prohibits providing medical diagnoses or treatment recommendations via automated messaging.<br><br>Your concern has been forwarded directly to our medical coordination desk. A qualified clinical team member will review your query and reply during clinic hours.<br><br>If you would like to book an in-person consultation with Dr. Samiya Irfan or our specialist team, reply **BOOK** or call our clinic at **021-3587XXXX**. |
| **Urdu (اردو)** | **مریضوں کی حفاظت سے متعلق ضروری وضاحت:**<br>ڈرما کیئر سکن کلینک کی پیشہ ورانہ پالیسی کے مطابق، خودکار میسجنگ (بوٹ) کے ذریعے کسی قسم کا طبی مشورہ، تشخیص یا دوائی تجویز کرنا سخت منع ہے۔<br><br>آپ کا پیغام ہمارے فرنٹ ڈیسک اور میڈیکل عملے کو بھیج دیا گیا ہے۔ ہمارے ماہرین جلد از جلد کلینک کے اوقات میں آپ سے رابطہ کریں گے۔<br><br>اگر آپ ڈاکٹر سمیعہ عرفان یا ہماری ٹیم سے باقاعدہ معائنہ کروانا چاہتے ہیں تو **BOOK** لکھیں یا براہِ راست **021-3587XXXX** پر کال کریں۔ |
| **Roman Urdu** | **Patient Safety Notice:**<br>DermaCare clinic ki strict policy hai ke WhatsApp bot ke zariye koi medical advice, diagnosis ya dawai tajweez nahi ki ja sakti.<br><br>Aap ka message hamari medical coordination team ko forward kar diya gaya hai, aur clinic staff jald hi aapse raabta karega.<br><br>Agar aap Dr. Samiya Irfan ya hamari specialist team se clinic aakar muana (consultation) karwana chahtay hain to **BOOK** likhein ya **021-3587XXXX** par call karein. |

---

### Script 3.2: Immediate Emergency Protocol ("Call This Number Now")
*Trigger:* Agreed emergency keywords: `bleeding`, `blood`, `severe burn`, `chemical burn`, `anaphylaxis`, `can't breathe`, `severe allergic reaction`, `intense swelling`, `khoon`, `jalan`, `soojan`, `shadid dard`, `emergency`, `reaction`.
*System Logic:* Priority Level 1 Alert. Rings reception buzzer / flashes red banner in WATI inbox. Sends immediate emergency Karachi helpline instructions.

| Language | Script |
| :--- | :--- |
| **English** | 🚨 **URGENT MEDICAL ALERT** 🚨<br><br>If you are experiencing severe bleeding, acute allergic reaction, sudden facial swelling, chemical burns, or breathing difficulty, **DO NOT WAIT FOR A TEXT REPLY.**<br><br>📞 **CALL OUR CLINIC EMERGENCY DESK IMMEDIATELY:**<br>**+92 300 1234567** or **021 3587XXXX**<br><br>📍 **Clinic Address:** Suite 302, 3rd Floor, Clifton Medical Enclave, Block 5, Clifton, Karachi.<br><br>*(If outside clinic hours and severe, please visit South City Hospital ER or Ziauddin Clifton ER immediately).* |
| **Urdu (اردو)** | 🚨 **انتہائی ہنگامی میڈیکل الرٹ** 🚨<br><br>اگر آپ کو شدید خون بہنے، اچانک چہرے پر شدید سوجن، کیمیکل سے جلنے یا شدید الرجک ری ایکشن کا سامنا ہے، تو **میسج کے جواب کا ہرگز انتظار نہ کریں۔**<br><br>📞 **فوری طور پر کلینک کی ایمرجنسی لائن پر کال کریں:**<br>**0300-1234567** یا **021-3587XXXX**<br><br>📍 **کلینک کا پتہ:** سویٹ 302، کلفٹن میڈیکل انکلیو، بلاک 5، کلفٹن، کراچی۔<br><br>*(اگر اوقاتِ کار کے بعد شدید ایمرجنسی ہو تو فوری طور پر ساؤتھ سٹی ہسپتال یا ضیاء الدین کلفٹن ایمرجنسی رجوع کریں)* |
| **Roman Urdu** | 🚨 **URGENT EMERGENCY ALERT** 🚨<br><br>Agar khoon beh raha hai, chehre par shadeed soojan hai, chemical burn hai ya shadeed allergy hui hai, to **MESSAGE KE JAWAB KA INTEZAR NA KAREIN.**<br><br>📞 **FORI CALL KAREIN:**<br>**0300-1234567** ya **021-3587XXXX**<br><br>📍 **Clinic Address:** Suite 302, Clifton Medical Enclave, Block 5, Clifton, Karachi.<br><br>*(Agar clinic band hai aur shadeed takleef hai to foran South City Hospital ya Ziauddin Clifton Emergency pohnchein).* |

---

### Script 3.3: Photo / Skin Condition Image Received
*Trigger:* Patient uploads any image / photo.

| Language | Script |
| :--- | :--- |
| **English** | 📷 **Photo Received:**<br>We have safely received your image. In compliance with Dr. Samiya Irfan's safety directives, automated systems do not inspect or evaluate skin photos.<br><br>Your photo has been uploaded securely to our confidential desk portal for review by Dr. Samiya and the clinical staff. Our receptionist will message you shortly.<br><br>*(Note: Accurate dermatological diagnosis requires an in-person dermatoscope examination).* |
| **Urdu (اردو)** | 📷 **تصویر موصول ہو گئی ہے:**<br>ہمیں آپ کی تصویر موصول ہو گئی ہے۔ ڈاکٹر سمیعہ عرفان کی سخت ہدایات کے مطابق، کمپیوٹرائزڈ سسٹم کے ذریعے جلد کی تصاویر کا تجزیہ نہیں کیا جاتا۔<br><br>آپ کی تصویر محفوظ طریقے سے کلینک کے کانفیڈنشل پورٹل پر منتقل کر دی گئی ہے جہاں ہمارے ڈاکٹرز اور ڈیسک عملہ اس کا جائزہ لیں گے۔ ہمارا عملہ جلد آپ سے رابطہ کرے گا۔ |
| **Roman Urdu** | 📷 **Photo Receive Ho Gayi Hai:**<br>Aap ki photo hamaray secured portal par submit ho chuki hai. Dr. Samiya Irfan ki clinical safety rules ke mutabiq robot skin photos ko diagnose nahi kar sakta.<br><br>Ye tasweer confidential desk par Dr. Samiya aur clinical team ke samnay rakh di gayi hai. Humari team jald hi aap se raabta karegi. |

---

### Script 3.4: Voice Note Received
*Trigger:* Patient sends an audio note.

| Language | Script |
| :--- | :--- |
| **English** | 🎙️ **Voice Note Received:**<br>Thank you for sending your audio message. Our front-desk team is listening to your voice note and will reply in writing or call you back shortly. |
| **Urdu (اردو)** | 🎙️ **وائس میسج موصول ہو گیا ہے:**<br>آپ کے وائس نوٹ کا شکریہ۔ ہمارے فرنٹ ڈیسک کا عملہ آپ کا آڈیو میسج سن کر جلد ہی آپ کو جواب یا کال کرے گا۔ |
| **Roman Urdu** | 🎙️ **Voice Note Receive Ho Gaya Hai:**<br>Aap ka audio note hamaray front desk ko mil gaya hai. Staff aap ka message sun kar jald text reply ya call back karega. |

---

## 4. Structured Appointment Booking Flow

### Script 4.1: Step 1 — Select Service Category
*Trigger:* Option 1 from Main Menu.

| Language | Script |
| :--- | :--- |
| **English** | **Step 1/5: Select Service Category**<br>Please select the nature of your visit:<br><br>1️⃣ **Clinical Dermatology** (Acne, Eczema, Psoriasis, Hair Loss, Mole check, Skin infections)<br>2️⃣ **Aesthetic & Cosmetic Procedures** (HydraFacial, Chemical Peels, Microneedling/PRP, Laser Hair Removal)<br>3️⃣ **Advanced Injectables & Anti-Aging** (Botox, Dermal Fillers, CO2 Laser Resurfacing) |
| **Urdu (اردو)** | **مرحلہ 1/5: معائنے یا علاج کی قسم منتخب کریں**<br><br>1️⃣ **کلینیکل ڈرمیٹولوجی** (کیل مہاسے، الرجی، ایگزیما، خارش، بال گرنا، تل یا جلد کی بیماریاں)<br>2️⃣ **کاسمیٹک و فیشل ٹریٹمنٹس** (ہائیڈرا فیشل، کیمیکل پیلز، پی آر پی، لیزر ہیئر ریموول)<br>3️⃣ **ایڈوانسڈ اینٹی ایجنگ اور فلرز** (بوٹوکس، فلرز، فریکشنل CO2 لیزر) |
| **Roman Urdu** | **Step 1/5: Category Select Karein**<br><br>1️⃣ **Clinical Dermatology** (Acne, daane, baal girna, allergy, eczema, skin infection)<br>2️⃣ **Aesthetic Treatments** (HydraFacial, Chemical Peels, PRP, Laser Hair Removal)<br>3️⃣ **Injectables & Laser** (Botox, Fillers, CO2 Laser) |

---

### Script 4.2: Step 2 — Doctor Selection with Bios
*Trigger:* Category selected. System displays available doctors for that specialty.

| Language | Script |
| :--- | :--- |
| **English** | **Step 2/5: Choose Your Specialist**<br><br>👩‍⚕️ **1. Dr. Samiya Irfan (Clinic Director)**<br>• MBBS, FCPS (Dermatology)<br>• 15+ years experience; Specialist in complex clinical dermatology, Melasma, and advanced aesthetic injectables.<br><br>👨‍⚕️ **2. Dr. Tariq Mansoor (Consultant Dermatologist)**<br>• MBBS, MCPS, Dip Derm (UK)<br>• Acne scar revision, Hair restoration, and general skin diseases.<br><br>👩‍⚕️ **3. Dr. Hina Zubair (Associate Dermatologist)**<br>• MBBS, MSc Dermatology<br>• Pediatric dermatology, eczema, and hyperpigmentation.<br><br>✨ **4. Sarah Ahmed (Senior Aesthetic Consultant)**<br>• Certified Laser Specialist & HydraFacial Expert.<br><br>✨ **5. Fatima Noor (Aesthetic Consultant)**<br>• Chemical peeling, skin rejuvenation & PRP therapy.<br><br>*(Reply with 1, 2, 3, 4, or 5)* |
| **Urdu (اردو)** | **مرحلہ 2/5: اپنے ماہر ڈاکٹر کا انتخاب کریں**<br><br>👩‍⚕️ **1. ڈاکٹر سمیعہ عرفان (ڈائریکٹر کلینک)**<br>• ایم بی بی ایس، ایف سی پی ایس (ڈرمیٹولوجی)<br>• 15 سالہ تجربہ؛ جلدی امراض، چھائیاں، اینٹی ایجنگ اور فلرز کی ماہر۔<br><br>👨‍⚕️ **2. ڈاکٹر طارق منصور (کنسلٹنٹ ڈرمیٹولوجسٹ)**<br>• ایکنی کے نشانات، بالوں کا گرنا اور عمومی جلدی بیماریاں۔<br><br>👩‍⚕️ **3. ڈاکٹر حنا زبیر (ڈرمیٹولوجسٹ)**<br>• بچوں کے جلدی مسائل، ایگزیما اور رنگت کا نکھار۔<br><br>✨ **4. سارہ احمد (سینئر ایستھیٹک کنسلٹنٹ)**<br>• لیزر اور ہائیڈرا فیشل اسپیشلسٹ۔<br><br>✨ **5. فاطمہ نور (ایستھیٹک کنسلٹنٹ)**<br>• کیمیکل پیلز اور پی آر پی تھراپی۔<br><br>*(براہِ کرم 1 سے 5 میں سے انتخاب کریں)* |
| **Roman Urdu** | **Step 2/5: Specialist Select Karein**<br><br>👩‍⚕️ **1. Dr. Samiya Irfan (Clinic Director)** — FCPS Dermatology, 15+ years tajurba, complex skin issues, melasma & injectables.<br>👨‍⚕️ **2. Dr. Tariq Mansoor** — Acne scars, hair loss, general skin diseases.<br>👩‍⚕️ **3. Dr. Hina Zubair** — Eczema, pigmentation, sensitive skin.<br>✨ **4. Sarah Ahmed** — Laser Hair Removal & HydraFacial expert.<br>✨ **5. Fatima Noor** — Chemical Peels, rejuvenation & PRP.<br><br>*(Reply karein 1, 2, 3, 4, ya 5)* |

---

### Script 4.3: Step 3 — Select Day and Time Slot (Dynamic from Faraz's Sheet)
*Trigger:* Doctor chosen. Bot reads real-time schedule from Faraz's availability sheet.

| Language | Script |
| :--- | :--- |
| **English** | **Step 3/5: Select Preferred Day & Time Slot**<br>Here are the upcoming consultation slots for **{Doctor Name}**:<br><br>📅 **Option A:** Tuesday, Nov 17 — 4:00 PM to 5:00 PM<br>📅 **Option B:** Tuesday, Nov 17 — 6:00 PM to 7:00 PM<br>📅 **Option C:** Thursday, Nov 19 — 3:30 PM to 4:30 PM<br>📅 **Option D:** Friday, Nov 20 — 5:00 PM to 6:00 PM<br><br>*(Reply with A, B, C, or D, or type your preferred date)* |
| **Urdu (اردو)** | **مرحلہ 3/5: دن اور وقت کا انتخاب**<br>**{ڈاکٹر کا نام}** کے لیے دستیابی مندرجہ ذیل ہے:<br><br>📅 **آپشن A:** بروز منگل، 17 نومبر — شام 4:00 تا 5:00 بجے<br>📅 **آپشن B:** بروز منگل، 17 نومبر — شام 6:00 تا 7:00 بجے<br>📅 **آپشن C:** بروز جمعرات، 19 نومبر — دوپہر 3:30 تا 4:30 بجے<br>📅 **آپشن D:** بروز جمعہ، 20 نومبر — شام 5:00 تا 6:00 بجے<br><br>*(براہِ کرم A, B, C یا D لکھ کر بھیجیں)* |
| **Roman Urdu** | **Step 3/5: Din aur Time Slot Muntakhib Karein**<br>**{Doctor Name}** ke liye available slots:<br><br>📅 **Option A:** Tuesday, 17 Nov — 4:00 PM se 5:00 PM<br>📅 **Option B:** Tuesday, 17 Nov — 6:00 PM se 7:00 PM<br>📅 **Option C:** Thursday, 19 Nov — 3:30 PM se 4:30 PM<br>📅 **Option D:** Friday, 20 Nov — 5:00 PM se 6:00 PM<br><br>*(Reply karein A, B, C ya D)* |

---

### Script 4.4: Step 4 — Patient Name & Contact Details
*Trigger:* Slot chosen.

| Language | Script |
| :--- | :--- |
| **English** | **Step 4/5: Patient Information**<br>Please type the **Full Name** of the patient who will be attending the consultation. |
| **Urdu (اردو)** | **مرحلہ 4/5: مریض کی معلومات**<br>براہِ کرم مریض کا **مکمل نام** درج فرمائیں جو معائنے کے لیے تشریف لائیں گے۔ |
| **Roman Urdu** | **Step 4/5: Mareez Ki Maloomat**<br>Barah-e-karam check-up ke liye aane walay patient ka **Pura Naam** type karein. |

---

### Script 4.5: Step 5 — Structured Request Logged (Pending Desk Confirmation)
*Trigger:* Patient details collected. Logged to Faraz's Desk Sheet.
*Note:* Explains the honest flow without promising false instant calendar integration.

| Language | Script |
| :--- | :--- |
| **English** | ⏳ **Booking Request Logged (Ref #{RequestID})**<br><br>• **Patient:** {Patient Name}<br>• **Doctor:** {Doctor Name}<br>• **Slot:** {Date & Time}<br>• **Fee:** PKR {Consultation Fee} *(payable at desk)*<br><br>📌 **Next Step:** Our front-desk manager (Faraz or desk staff) is confirming this slot in our clinic schedule. You will receive an official **Booking Confirmation Message** within 15–20 minutes during clinic hours.<br><br>*(To change details, reply **EDIT** or **MENU**)* |
| **Urdu (اردو)** | ⏳ **درخواست موصول ہو گئی ہے (ریفرنس نمبر: #{RequestID})**<br><br>• **مریض کا نام:** {مریض کا نام}<br>• **ڈاکٹر:** {ڈاکٹر کا نام}<br>• **وقت:** {تاریخ اور وقت}<br>• **فیس:** {کنسلٹیشن فیس} روپے<br><br>📌 **اگلا مرحلہ:** ہمارے فرنٹ ڈیسک منیجر (فراز یا ڈیسک اسٹاف) کلینک سافٹ ویئر میں اس وقت کی تصدیق کر رہے ہیں۔ کلینک اوقات کے دوران اگلے 15 سے 20 منٹ میں آپ کو حتمی تصدیقی میسج موصول ہو جائے گا۔ |
| **Roman Urdu** | ⏳ **Booking Request Register Ho Gayi (Ref #{RequestID})**<br><br>• **Patient:** {Patient Name}<br>• **Doctor:** {Doctor Name}<br>• **Waqt:** {Date & Time}<br>• **Fee:** PKR {Fee}<br><br>📌 **Agla Marhala:** Humara front desk staff is slot ko clinic system mein enter kar raha hai. 15 se 20 minute ke andar aap ko confirmed status ka message mil jayega. |

---

### Script 4.6: Desk Confirmation Message (Triggered by Desk Staff 1-Click)
*Trigger:* Front desk verifies slot in local desktop software and marks status as "Confirmed".

| Language | Script |
| :--- | :--- |
| **English** | ✅ **APPOINTMENT CONFIRMED!**<br><br>Dear {Patient Name}, your consultation with **{Doctor Name}** has been confirmed by DermaCare front desk.<br><br>📅 **Date & Time:** {Confirmed Date & Time}<br>📍 **Location:** Suite 302, Clifton Medical Enclave, Block 5, Clifton, Karachi.<br>🗺️ **Google Maps:** https://maps.google.com/?q=24.8215,67.0312<br><br>⚠️ **Please arrive 10 minutes prior** to your scheduled time.<br>To reschedule or cancel at any time, simply reply **CANCEL** or **RESCHEDULE**. |
| **Urdu (اردو)** | ✅ **اپائنٹمنٹ کی حتمی تصدیق!**<br><br>محترم {مریض کا نام}، **{ڈاکٹر کا نام}** کے ساتھ آپ کا وقت ڈرما کیئر فرنٹ ڈیسک نے کنفرم کر دیا ہے۔<br><br>📅 **تاریخ اور وقت:** {تاریخ اور وقت}<br>📍 **پتہ:** سویٹ 302، کلفٹن میڈیکل انکلیو، بلاک 5، کلفٹن، کراچی۔<br>🗺️ **گوگل میپ لوکیشن:** https://maps.google.com/?q=24.8215,67.0312<br><br>⚠️ گزارش ہے کہ وقت سے 10 منٹ پہلے تشریف لائیں۔ اگر وقت تبدیل یا منسوخ کرنا ہو تو **CANCEL** یا **RESCHEDULE** لکھیں۔ |
| **Roman Urdu** | ✅ **APPOINTMENT CONFIRM HO GAYA HAI!**<br><br>Mohtaram {Patient Name}, **{Doctor Name}** ke sath aap ka appointment DermaCare desk se confirm ho chuka hai.<br><br>📅 **Date & Time:** {Confirmed Date & Time}<br>📍 **Location:** Suite 302, Clifton Medical Enclave, Block 5, Clifton, Karachi.<br>🗺️ **Map Pin:** https://maps.google.com/?q=24.8215,67.0312<br><br>Barah-e-karam time se 10 minute pehle tashreef layein. Reschedule ya cancel karne ke liye **CANCEL** ya **RESCHEDULE** reply karein. |

---

## 5. Automated Reminders (24 Hours & 3 Hours Prior)

### Script 5.1: 24-Hour Reminder with Reply-to-Cancel
*Trigger:* Automatically sent 24 hours before confirmed appointment time.

| Language | Script |
| :--- | :--- |
| **English** | 🔔 **Appointment Reminder (Tomorrow)**<br><br>Dear {Patient Name}, this is a gentle reminder of your upcoming consultation with **{Doctor Name}** tomorrow, **{Date} at {Time}**.<br><br>Please confirm your attendance by replying:<br>1️⃣ **CONFIRM** (I will be there)<br>2️⃣ **CANCEL** (I cannot make it)<br>3️⃣ **RESCHEDULE** (Change date/time) |
| **Urdu (اردو)** | 🔔 **اپائنٹمنٹ یاد دہانی (بروز کل)**<br><br>محترم {مریض کا نام}، کل **{تاریخ} بوقت {وقت}** آپ کا **{ڈاکٹر کا نام}** کے ساتھ معائنہ مقرر ہے۔<br><br>براہِ کرم اپنی آمد کی تصدیق فرمائیں:<br>1️⃣ **CONFIRM** (جی ہاں، میں آؤں گا/گی)<br>2️⃣ **CANCEL** (میں تشریف نہیں لا سکتا/سکتی)<br>3️⃣ **RESCHEDULE** (وقت تبدیل کروائیں) |
| **Roman Urdu** | 🔔 **Appointment Reminder (Kal)**<br><br>Mohtaram {Patient Name}, kal **{Date} ko {Time}** par aap ka **{Doctor Name}** ke sath appointment scheduled hai.<br><br>Barah-e-karam reply karein:<br>1️⃣ **CONFIRM** (Mein aaon ga/gi)<br>2️⃣ **CANCEL** (Nahi aa sakta/sakti)<br>3️⃣ **RESCHEDULE** (Date change karein) |

---

### Script 5.2: 3-Hour Urgent Reminder
*Trigger:* Automatically sent 3 hours before consultation.

| Language | Script |
| :--- | :--- |
| **English** | ⏰ **Appointment in 3 Hours:**<br>Dear {Patient Name}, your consultation with **{Doctor Name}** is today at **{Time}**.<br><br>📍 Clinic Location: Suite 302, Clifton Medical Enclave, Block 5, Clifton.<br>🚗 Valet & street parking available.<br><br>If running late, please let us know immediately by replying here! |
| **Urdu (اردو)** | ⏰ **3 گھنٹے میں آپ کا اپائنٹمنٹ ہے:**<br>محترم {مریض کا نام}، آج **{وقت}** پر آپ کا **{ڈاکٹر کا نام}** کے ساتھ معائنہ ہے۔<br><br>📍 کلفٹن میڈیکل انکلیو، بلاک 5، کلفٹن، کراچی۔<br>اگر پہنچنے میں تاخیر ہو تو فوراً یہاں آگاہ فرمائیں۔ |
| **Roman Urdu** | ⏰ **Aap ka Appointment 3 Ghantay Mein Hai:**<br>Mohtaram {Patient Name}, aaj **{Time}** par **{Doctor Name}** ke sath aap ka appointment hai.<br><br>📍 Suite 302, Clifton Medical Enclave, Block 5, Clifton.<br>Agar late ho jayein to foran yahan message karein! |

---

## 6. Pre- and Post-Procedure PDF Guides (8 Listed Treatments)

When patient selects Option 5 or types the procedure name, the bot instantly dispatches the official DermaCare PDF instruction sheet.

| # | Treatment Name | English PDF Caption | Urdu PDF Caption |
| :--- | :--- | :--- | :--- |
| 1 | **HydraFacial MD** | 📄 Attached: HydraFacial pre-treatment and aftercare guide. Avoid direct sun exposure for 48 hours. | 📄 منسلک فائل: ہائیڈرا فیشل کے بعد کی ہدایات۔ 48 گھنٹے دھوپ اور تیز گرمی سے پرہیز کریں۔ |
| 2 | **Chemical Peels** | 📄 Attached: Chemical Peel prep & post-peel hydration instructions. Do not pick or peel flaking skin. | 📄 منسلک فائل: کیمیکل پیل کی احتیاطی تدابیر۔ چہرے پر اترنے والی جلد کو ہاتھ سے مت کھینچیں۔ |
| 3 | **Laser Hair Removal** | 📄 Attached: Pre-laser shaving protocol & post-laser soothing instructions. No waxing/plucking for 3 weeks prior. | 📄 منسلک فائل: لیزر ہیئر ریموول ہدایات۔ سیشن سے 3 ہفتے قبل ویکسنگ یا تھریڈنگ بالکل نہ کریں۔ |
| 4 | **Microneedling & PRP** | 📄 Attached: Post-PRP healing guide. Avoid heavy makeup and sweating for 24 hours. | 📄 منسلک فائل: مائیکرو نیڈلنگ اور پی آر پی کی ہدایات۔ 24 گھنٹے میک اپ اور پسینے سے بچیں۔ |
| 5 | **Botox & Dermal Fillers** | 📄 Attached: Anti-bruising protocol. Remain upright for 4 hours; avoid strenuous exercise for 24 hours. | 📄 منسلک فائل: بوٹوکس اور فلرز ہدایات۔ انجیکشن کے بعد 4 گھنٹے تک سیدھے رہیں اور نیچے نہ جھکیں۔ |
| 6 | **CO2 Fractional Laser** | 📄 Attached: Intensive post-resurfacing wound care and barrier repair protocol. | 📄 منسلک فائل: فریکشنل CO2 لیزر کیئر۔ مسلسل موئسچرائزر اور سن بلاک کا استعمال کریں۔ |
| 7 | **Wart / Tag Removal** | 📄 Attached: Cautery/Cryo wound care instructions. Keep site dry for 24 hours; apply prescribed antibiotic cream. | 📄 منسلک فائل: مسے یا سکن ٹیگ اتارنے کے بعد زخم کی دیکھ بھال کی ہدایات۔ 24 گھنٹے خشک رکھیں۔ |
| 8 | **Glutathione IV Therapy** | 📄 Attached: IV hydration advisory. Drink at least 2.5–3 liters of water daily. | 📄 منسلک فائل: گلوٹاتھائیون ڈرپ کے بعد کی ہدایات۔ روزانہ وافر مقدار میں پانی پیئیں۔ |

---

## 7. Single Source-of-Truth FAQs (Timings, Clifton Pin, Fees, Payments)

### Script 7.1: Clinic Location Pin & Clifton Address
| Language | Script |
| :--- | :--- |
| **English** | 📍 **DermaCare Skin Clinic Location:**<br>Suite 302, 3rd Floor, Clifton Medical Enclave, Khayaban-e-Iqbal, Block 5, Clifton, Karachi.<br>*(Near Schon Circle / Teen Talwar landmark)*<br><br>🗺️ **Google Maps Pin:** https://maps.google.com/?q=24.8215,67.0312<br>🚗 Dedicated basement valet parking available for patients. |
| **Urdu (اردو)** | 📍 **ڈرما کیئر سکن کلینک کا پتہ:**<br>سویٹ 302، تیسری منزل، کلفٹن میڈیکل انکلیو، خیابانِ اقبال، بلاک 5، کلفٹن، کراچی۔ (تین تلوار اور شون سرکل کے قریب)<br><br>🗺️ **گوگل میپ لوکیشن:** https://maps.google.com/?q=24.8215,67.0312<br>🚗 کلینک کی بیسمنٹ میں گاڑی پارکنگ کی سہولت موجود ہے۔ |
| **Roman Urdu** | 📍 **Clinic Location:**<br>Suite 302, 3rd Floor, Clifton Medical Enclave, Block 5, Clifton, Karachi (Teen Talwar ke qareeb).<br><br>🗺️ **Maps Pin:** https://maps.google.com/?q=24.8215,67.0312<br>🚗 Basement parking available hai. |

---

### Script 7.2: Timings, Fees & Payment Methods
| Language | Script |
| :--- | :--- |
| **English** | 🕒 **Clinic Operating Hours:**<br>• Monday to Saturday: 11:00 AM – 8:30 PM<br>• Sunday: Closed<br><br>💳 **Consultation Fees (Per Visit):**<br>• Dr. Samiya Irfan (Director): PKR 4,000<br>• Dr. Tariq Mansoor (Consultant): PKR 3,000<br>• Dr. Hina Zubair (Associate): PKR 2,500<br>• Aesthetic Consultant Evaluation: PKR 1,500 (Waived if treatment is taken on the same day)<br><br>💵 **Payment Methods Accepted:**<br>• Cash at Reception<br>• Debit & Credit Cards (Visa / Mastercard)<br>• Raast ID / Direct Bank Transfer (Faysal Bank / Meezan Bank)<br>• JazzCash / EasyPaisa QR |
| **Urdu (اردو)** | 🕒 **کلینک کے اوقات:**<br>• پیر تا ہفتہ: صبح 11:00 تا رات 8:30 بجے<br>• اتوار: چھٹی<br><br>💳 **کنسلٹیشن فیس:**<br>• ڈاکٹر سمیعہ عرفان: 4,000 روپے<br>• ڈاکٹر طارق منصور: 3,000 روپے<br>• ڈاکٹر حنا زبیر: 2,500 روپے<br>• ایستھیٹک کنسلٹنٹ معائنہ: 1,500 روپے (اگر اسی روز ٹریٹمنٹ لیا جائے تو فیس معاف)<br><br>💵 **ادائیگی کے طریقے:**<br>• کیش<br>• تمام بینکس کے ڈیبٹ اور کریڈٹ کارڈز<br>• راست (Raast) اور بینک اکاؤنٹ ٹرانسفر<br>• جاز کیش اور ایزی پیسہ |
| **Roman Urdu** | 🕒 **Clinic Timings:**<br>• Mon to Sat: 11:00 AM se 8:30 PM<br>• Sunday: Off<br><br>💳 **Consultation Fees:**<br>• Dr. Samiya Irfan: PKR 4,000<br>• Dr. Tariq Mansoor: PKR 3,000<br>• Dr. Hina Zubair: PKR 2,500<br>• Aesthetic Consultant: PKR 1,500 (Agar same day procedure ho to fee waive)<br><br>💵 **Payment Options:**<br>• Cash, Debit/Credit Card, Raast, Online Bank Transfer, JazzCash. |

---

## 8. Front-Desk Handover & 2-Strike Fallback

### Script 8.1: "Talk to Reception" (Available Anytime)
*Trigger:* Patient types "Talk to reception", "Agent", "Faraz", "Human", "Call", or selects Option 7.

| Language | Script |
| :--- | :--- |
| **English** | 👤 **Connecting to Reception:**<br>I have paused automated replies and notified our front desk. Faraz or an on-duty receptionist is reviewing your chat history right now and will message you within a few minutes.<br><br>📞 You may also call us directly at **021-3587XXXX**.<br>*(Type **BOT** at any time to return to the automated menu).* |
| **Urdu (اردو)** | 👤 **فرنٹ ڈیسک اسٹاف کو منتقل کیا جا رہا ہے:**<br>خودکار بوٹ کو روک دیا گیا ہے اور فرنٹ ڈیسک کو مطلع کر دیا گیا ہے۔ فراز یا ہماری ٹیم کی رکن آپ کی چیٹ دیکھ کر چند منٹوں میں جواب دیں گی۔<br><br>📞 آپ فوری رابطے کے لیے **021-3587XXXX** پر کال بھی کر سکتے ہیں۔<br>*(دوبارہ مینیو پر جانے کے لیے **BOT** لکھیں)* |
| **Roman Urdu** | 👤 **Reception se Raabta:**<br>Automated bot rok diya gaya hai aur hamaray staff ko alert chala gaya hai. Faraz ya front-desk team member foran aap se raabta karenge.<br><br>📞 Aap direct call bhi kar saktay hain: **021-3587XXXX**.<br>*(Wapas menu par aane ke liye **BOT** type karein)* |

---

### Script 8.2: 2-Strike Automated Fallback Handover
*Trigger:* Patient enters 2 consecutive unrecognized, confusing, or unparsable responses.

| Language | Script |
| :--- | :--- |
| **English** | I want to make sure you get the exact help you need without confusion. I am connecting you directly with our front desk team now. A receptionist will assist you personally. |
| **Urdu (اردو)** | میں یقینی بنانا چاہتا ہوں کہ آپ کو بغیر کسی پریشانی کے درست معلومات ملیں۔ میں آپ کا رابطہ فوری طور پر ہمارے فرنٹ ڈیسک اسٹاف سے کروا رہا ہوں۔ ہمارے نمائندے آپ کی ذاتی رہنمائی کریں گے۔ |
| **Roman Urdu** | Mein aap ki baat direct humari reception team se karwa raha hoon taake aap ko behtar maloomat mil sakein. Humara staff abhi aapse raabta karega. |
