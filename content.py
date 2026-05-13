# content.py — весь текстовый контент бота
# Диалоги, опросы, интерфейсные строки на UZ / TJ / KG / RU

# ─────────────────────────────────────────────
# ДИАЛОГОВЫЕ ДЕРЕВЬЯ
# Структура каждого узла:
#   text      : str | list[str]  — сообщения бота (список = по одному)
#   question  : str              — вопрос после сообщений
#   buttons   : list[(label, next_node_id)]
#   is_end    : bool             — конец диалога, запускает опрос
# ─────────────────────────────────────────────

DIALOGUES = {

    # ══════════════════════════════════════════
    # O'ZBEKCHA
    # ══════════════════════════════════════════
    "uz": {
        "imei": {
            "start": {
                "text": [
                    "Salom! Raqamingiz boshqa qurilmaga SIM-kartani o'tkazganingiz uchun bloklangan.",
                    "Bu hal qilinadi — hozir birga ko'ramiz. 👍",
                ],
                "question": "Aytingchi: SIM-kartani oldin bo'lgan telefoningizga qayta qo'ya olasizmi?",
                "buttons": [
                    ("✅ Ha, qo'ya olaman", "a_can_return"),
                    ("❌ Yo'q — buzilgan / yo'qolgan / xohlamayman", "b_cannot_return"),
                ],
            },
            "a_can_return": {
                "text": "Zo'r! SIM-kartani qaytarib qo'ying — aloqa darhol tiklanadi. ✅",
                "question": "Chiqdi?",
                "buttons": [
                    ("🎉 Ha, hamma narsa ishlayapti!", "a_success"),
                    ("❌ Yo'q, biror narsa noto'g'ri ketdi", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Yordamlasha olganimizdan xursandmiz! Biror narsa kerak bo'lsa — yozing. Omad! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Nima bo'layotganini yozing — birga aniqlaymiz.\nYoki qo'ng'iroq qiling: 0611 (Beeline dan bepul).",
                "is_end": True,
            },
            "b_cannot_return": {
                "text": "Tushundim. Unda ikkita yo'l bor: Beeline ilovasi orqali (tezroq) yoki ofisga borish.",
                "question": "Yangi telefoningizda Beeline ilovasi o'rnatilganmi?",
                "buttons": [
                    ("✅ Ha, ilova bor", "b_has_app"),
                    ("❌ Yo'q, ilova yo'q", "b_no_app"),
                ],
            },
            "b_has_app": {
                "text": [
                    "Zo'r! Qadamma-qadam ko'rsatma:",
                    "1️⃣  Beeline ilovasini oching.\n2️⃣  Asosiy ekranda bloklash haqida xabar bo'ladi — unga bosing.\n3️⃣  Ilovadagi qadamlarni bajaring — yangi telefon IMEI-sini ko'rsating.",
                    "📱 IMEI-ni bilmaysizmi?\n*060*3# tering — u ekranda paydo bo'ladi.\nYoki: Sozlamalar → «Qurilma haqida».",
                ],
                "question": "Qildingizmi?",
                "buttons": [
                    ("✅ Ha, IMEI ni yangiladim", "b_app_done"),
                    ("❌ Yo'q, chiqmadi", "b_app_fail"),
                ],
            },
            "b_app_done": {
                "text": "IMEI yangilandi! ✅\nYana bir qadam qoldi — Gosuslugi orqali ma'lumotlarni tasdiqlash.",
                "is_end": True,
            },
            "b_app_fail": {
                "text": [
                    "Xavotir olmang! Ofisda hal qilish mumkin.",
                    "Istalgan Beeline ofisiga pasport bilan keling — u yerda IMEI yangilanadi.",
                    "👉 Eng yaqin ofis: moskva.beeline.ru/customers/beeline-map/",
                ],
                "is_end": True,
            },
            "b_no_app": {
                "question": "Ilovani o'rnatmoqchimisiz? Bu 2 daqiqa vaqt oladi.",
                "buttons": [
                    ("✅ Ha, o'rnataman", "b_will_install"),
                    ("❌ Yo'q, boshqa yo'l kerak", "b_no_install"),
                ],
            },
            "b_will_install": {
                "text": [
                    "Ajoyib! Beeline ilovasini yuklab oling:",
                    "▶ Android:\nplay.google.com/store/apps/details?id=ru.beeline.services\n▶ Huawei:\nappgallery.huawei.com/app/C100716739\n▶ iPhone:\napps.apple.com/ru/app/moj-bilajn/id569251594",
                ],
                "question": "O'rnatib bo'ldingizmi?",
                "buttons": [
                    ("✅ O'rnatdim, davom etaylik", "b_has_app"),
                ],
            },
            "b_no_install": {
                "text": [
                    "Xop! Unda ikkita yo'l:",
                    "🏢 Variant 1 — Beeline ofisi:\nPasport bilan keling, yangi telefon IMEI-sini ayting.\nIMEI: *060*3# tering yoki Sozlamalar → «Qurilma haqida»\n👉 moskva.beeline.ru/customers/beeline-map/",
                    "📞 Variant 2 — Qo'ng'iroq markazi:\n0611 (Beeline dan bepul)\n8 800 700-06-11 (istalgan operatordan)",
                ],
                "is_end": True,
            },
        },

        "ebs": {
            "start": {
                "text": [
                    "Raqamingiz bloklangan, chunki Rossiyada barcha xorijiy fuqarolar uchun biometriya orqali shaxsni tasdiqlash talab qilinadi.",
                    "Men sizga qadamma-qadam yordam beraman. 👍",
                ],
                "question": "Sizda SNILS bormi?",
                "buttons": [
                    ("✅ Ha, bor", "a_has_snils"),
                    ("❌ Yo'q / bu nima ekanini bilmayman", "b_no_snils"),
                ],
            },
            "a_has_snils": {
                "text": [
                    "Yaxshi! Biometriya qabul qiladigan bankka borish kerak.",
                    "O'zingiz bilan oling:\n✅ Pasport (asl nusxa)\n✅ Pasportning notarial tarjimasi (Belarus fuqarolariga kerak emas)\n✅ SNILS\n✅ Email yoki telefon raqami",
                    "Bankda Gosuslugi hisobi ochishga yordam berishadi va ovoz + yuzingizni qayd etishadi.",
                    "👉 Eng yaqin bank: map.gosuslugi.ru/?layer=co",
                ],
                "question": "Bankda biometriyani qayd etib bo'ldingizmi?",
                "buttons": [
                    ("✅ Bajarildi, davom etaylik", "a_bank_done"),
                ],
            },
            "a_bank_done": {
                "text": [
                    "Ajoyib! Oxirgi qadam — Gosuslugi da ma'lumotlarni tasdiqlash.",
                    "Gosuslugi ilovasini oching → «Mening profilim» → «Hujjatlar» → «Mobil aloqa» → raqamingizni bosing va tasdiqlang.",
                    "📄 PDF ko'rsatma:\nstatic.beeline.ru/upload/images/landings/dobro/28295_manual_UZ.pdf",
                    "Yoki Beeline ofisiga keling — bepul yordam:\nmoskva.beeline.ru/customers/beeline-map/",
                ],
                "question": "Chiqdi?",
                "buttons": [
                    ("✅ Ha, hamma narsani qildim!", "a_success"),
                    ("❌ Yo'q, qiyinchiliklar bor", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Zo'r! Aloqa bir necha daqiqa ichida tiklanishi kerak.\nAgar tiklanmasa — qo'ng'iroq qiling: 0611. Omad! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Nima chiqmayotganini yozing — aniqlaymiz.\nYoki Beeline ofisiga keling: moskva.beeline.ru/customers/beeline-map/",
                "is_end": True,
            },
            "b_no_snils": {
                "text": [
                    "Unda avval SNILS olish kerak. Ikkita yo'l bor:",
                    "👔 1-usul — Ish beruvchi orqali (5 ish kuni):\nIsh beruvchingizdan ma'lumotlarni Rossiya Ijtimoiy fondiga yuborishini so'rang.",
                    "🏛 2-usul — Mustaqil ravishda:\nMFC yoki Ijtimoiy fond bo'limiga pasport va notarial tarjima bilan keling (Belarus fuqarolariga kerak emas).\n👉 MFC: map.gosuslugi.ru/?layer=co\n👉 Ijtimoiy fond: sfr.gov.ru/grazhdanam/social_fond/~8333",
                ],
                "question": "SNILS olgach — quyidagi tugmani bosing.",
                "buttons": [
                    ("✅ SNILS oldim, davom etaylik", "a_has_snils"),
                ],
            },
        },
    },

    # ══════════════════════════════════════════
    # ТОҶИКӢ
    # ══════════════════════════════════════════
    "tj": {
        "imei": {
            "start": {
                "text": [
                    "Салом! Рақами шумо баста шудааст, зеро SIM-корт ба дастгоҳи дигар гузошта шудааст.",
                    "Ин ҳал мешавад — ҳоло якҷоя мефаҳмем. 👍",
                ],
                "question": "Гӯед: оё шумо метавонед SIM-кортро ба телефони қаблиатон баргардонед?",
                "buttons": [
                    ("✅ Бале, метавонам", "a_can_return"),
                    ("❌ Не — шикаст / гум шуд / намехоҳам", "b_cannot_return"),
                ],
            },
            "a_can_return": {
                "text": "Аъло! Танҳо SIM-кортро баргардонед — алоқа фавран барқарор мешавад. ✅",
                "question": "Барқарор шуд?",
                "buttons": [
                    ("🎉 Бале, ҳама чиз кор мекунад!", "a_success"),
                    ("❌ Не, чизе нодуруст шуд", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Хурсандем, ки кӯмак карда тавонистем! Агар чизе лозим шавад — нависед. Муваффақ бошед! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Нависед чӣ гап — якҷоя мефаҳмем.\nЁ занг занед: 0611 (аз Beeline ройгон).",
                "is_end": True,
            },
            "b_cannot_return": {
                "text": "Фаҳмидам. Ду роҳ ҳаст: тавассути барномаи Beeline (тезтар) ё омадан ба офис.",
                "question": "Оё барномаи Beeline дар телефони навтон насб аст?",
                "buttons": [
                    ("✅ Бале, барнома ҳаст", "b_has_app"),
                    ("❌ Не, барнома нест", "b_no_app"),
                ],
            },
            "b_has_app": {
                "text": [
                    "Аъло! Дастури қадам ба қадам:",
                    "1️⃣  Барномаи Beeline-ро кушоед.\n2️⃣  Дар экрани асосӣ паёми бастаро мебинед — онро пахш кунед.\n3️⃣  Қадамҳои барномаро иҷро кунед — IMEI-и телефони навро нишон диҳед.",
                    "📱 IMEI-ро намедонед?\n*060*3# шумора гиред — он дар экран пайдо мешавад.\nЁ: Танзимот → «Дар бораи дастгоҳ».",
                ],
                "question": "Кардед?",
                "buttons": [
                    ("✅ Бале, IMEI-ро навсозӣ кардам", "b_app_done"),
                    ("❌ Не, нашуд", "b_app_fail"),
                ],
            },
            "b_app_done": {
                "text": "IMEI навсозӣ шуд! ✅\nЯк қадам боқӣ мондааст — тасдиқи маълумот тавассути Госуслуги.",
                "is_end": True,
            },
            "b_app_fail": {
                "text": [
                    "Ташвиш надоред! Дар офис ҳал кардан мумкин аст.",
                    "Ба ягон офиси Beeline бо шиносномаатон биёед — дар он ҷо IMEI навсозӣ мешавад.",
                    "👉 Наздиктарин офис: moskva.beeline.ru/customers/beeline-map/",
                ],
                "is_end": True,
            },
            "b_no_app": {
                "question": "Мехоҳед барномаро насб кунед? Ин 2 дақиқа вақт мегирад.",
                "buttons": [
                    ("✅ Бале, насб мекунам", "b_will_install"),
                    ("❌ Не, роҳи дигар лозим аст", "b_no_install"),
                ],
            },
            "b_will_install": {
                "text": [
                    "Аъло! Барномаи Beeline-ро зеркашӣ кунед:",
                    "▶ Android:\nplay.google.com/store/apps/details?id=ru.beeline.services\n▶ Huawei:\nappgallery.huawei.com/app/C100716739\n▶ iPhone:\napps.apple.com/ru/app/moj-bilajn/id569251594",
                ],
                "question": "Насб кардед?",
                "buttons": [
                    ("✅ Насб кардам, давом медиҳем", "b_has_app"),
                ],
            },
            "b_no_install": {
                "text": [
                    "Хоп! Ду вариант:",
                    "🏢 Варианти 1 — Офиси Beeline:\nБо шиносномаатон биёед, IMEI-и телефони навро гӯед.\nIMEI: *060*3# ё Танзимот → «Дар бораи дастгоҳ»\n👉 moskva.beeline.ru/customers/beeline-map/",
                    "📞 Варианти 2 — Маркази занг:\n0611 (аз Beeline ройгон)\n8 800 700-06-11 (аз ҳар оператор)",
                ],
                "is_end": True,
            },
        },

        "ebs": {
            "start": {
                "text": [
                    "Рақами шумо баста шудааст, зеро тибқи қонун ҳамаи шаҳрвандони хориҷӣ дар Россия бояд шахсияти худро тавассути биометрия тасдиқ намоянд.",
                    "Ман ба шумо қадам ба қадам кӯмак мекунам. 👍",
                ],
                "question": "Оё шумо СНИЛС доред?",
                "buttons": [
                    ("✅ Бале, дорам", "a_has_snils"),
                    ("❌ Не / намедонам ин чист", "b_no_snils"),
                ],
            },
            "a_has_snils": {
                "text": [
                    "Хуб! Ба бонке, ки биометрия мегирад, равед.",
                    "Бо худ гиред:\n✅ Шиносномаи аслӣ (паспорт)\n✅ Тарҷумаи нотариалии паспорт (барои шаҳрвандони Беларус лозим нест)\n✅ СНИЛС\n✅ Суроғаи почтаи электронӣ ё рақами телефон",
                    "Дар бонк ба шумо дар сохтани ҳисоби Госуслуги кӯмак мекунанд ва овоз + рӯйтонро қайд мекунанд.",
                    "👉 Наздиктарин бонк: map.gosuslugi.ru/?layer=co",
                ],
                "question": "Биометрияро дар бонк қайд кардед?",
                "buttons": [
                    ("✅ Кардам, давом медиҳем", "a_bank_done"),
                ],
            },
            "a_bank_done": {
                "text": [
                    "Аъло! Қадами охирин — тасдиқи маълумот дар Госуслуги.",
                    "Барномаи Госуслуги-ро кушоед → «Профили ман» → «Ҳуҷҷатҳо» → «Алоқаи мобилӣ» → рақами худро пахш кунед ва тасдиқ намоед.",
                    "📄 PDF:\nstatic.beeline.ru/upload/images/landings/dobro/28295_manual_TJ.pdf",
                    "Ё ба офиси Beeline биёед:\nmoskva.beeline.ru/customers/beeline-map/",
                ],
                "question": "Шуд?",
                "buttons": [
                    ("✅ Бале, ҳама чизро кардам!", "a_success"),
                    ("❌ Не, мушкилот ҳаст", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Аъло! Алоқа дар чанд дақиқа барқарор мешавад.\nАгар нашуд — занг занед: 0611. Муваффақ бошед! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Нависед чӣ нашуд — мефаҳмем.\nЁ ба офиси Beeline биёед: moskva.beeline.ru/customers/beeline-map/",
                "is_end": True,
            },
            "b_no_snils": {
                "text": [
                    "Пас аввал бояд СНИЛС гирифт. Ду роҳ:",
                    "👔 Роҳи 1 — Тавассути корфармо (5 рӯзи корӣ):\nАз корфармоятон хоҳед, ки маълумоти шуморо ба Фонди иҷтимоии Россия фиристад.",
                    "🏛 Роҳи 2 — Мустақилона:\nБо шиноснома ва тарҷумаи нотариалӣ биёед (барои шаҳрвандони Беларус лозим нест).\n👉 МФЦ: map.gosuslugi.ru/?layer=co\n👉 Фонди иҷтимоӣ: sfr.gov.ru/grazhdanam/social_fond/~8333",
                ],
                "question": "СНИЛС гирифтед?",
                "buttons": [
                    ("✅ СНИЛС гирифтам, давом медиҳем", "a_has_snils"),
                ],
            },
        },
    },

    # ══════════════════════════════════════════
    # КЫРГЫЗЧА
    # ══════════════════════════════════════════
    "kg": {
        "imei": {
            "start": {
                "text": [
                    "Саламатсызбы! Номуруңуз башка түзмөккө SIM-карта которулгандыктан бөгөттөлдү.",
                    "Бул чечилет — азыр бирге карайбыз. 👍",
                ],
                "question": "Айтыңызчы: SIM-картаны мурунку телефонуңузга кайра сала аласызбы?",
                "buttons": [
                    ("✅ Ооба, сала алам", "a_can_return"),
                    ("❌ Жок — сынды / жоголду / каалабайм", "b_cannot_return"),
                ],
            },
            "a_can_return": {
                "text": "Жакшы! SIM-картаны кайра салыңыз — байланыш дароо калыбына келет. ✅",
                "question": "Чыктыбы?",
                "buttons": [
                    ("🎉 Ооба, баары иштеп жатат!", "a_success"),
                    ("❌ Жок, бир нерсе болбой калды", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Жардам бере алганыбызга кубанычтабыз! Бир нерсе керек болсо — жазыңыз. Ийгилик! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Эмне болуп жатканын жазыңыз — бирге чечебиз.\nЖе чалыңыз: 0611 (Beeline дан бекер).",
                "is_end": True,
            },
            "b_cannot_return": {
                "text": "Түшүндүм. Анда эки жол бар: Beeline тиркемеси аркылуу (тезирээк) же офиске баруу.",
                "question": "Жаңы телефонуңузда Beeline тиркемеси орнотулганбы?",
                "buttons": [
                    ("✅ Ооба, тиркеме бар", "b_has_app"),
                    ("❌ Жок, тиркеме жок", "b_no_app"),
                ],
            },
            "b_has_app": {
                "text": [
                    "Жакшы! Кадамма-кадам нускама:",
                    "1️⃣  Beeline тиркемесин ачыңыз.\n2️⃣  Башкы экранда бөгөттөө жөнүндө билдирүү болот — ага басыңыз.\n3️⃣  Тиркемедеги кадамдарды аткарыңыз — жаңы телефондун IMEI-ин көрсөтүңүз.",
                    "📱 IMEI-ди билбейсизби?\n*060*3# теринизи — ал экранда чыгат.\nЖе: Жөндөөлөр → «Аппарат жөнүндө».",
                ],
                "question": "Кылдыңызбы?",
                "buttons": [
                    ("✅ Ооба, IMEI-ди жаңылдадым", "b_app_done"),
                    ("❌ Жок, болбоду", "b_app_fail"),
                ],
            },
            "b_app_done": {
                "text": "IMEI жаңыланды! ✅\nДагы бир кадам калды — Госуслуги аркылуу маалыматтарды ырастоо.",
                "is_end": True,
            },
            "b_app_fail": {
                "text": [
                    "Кам эмес! Офисте чечүүгө болот.",
                    "Каалаган Beeline офисине паспортуңуз менен келиңиз — ал жерде IMEI жаңыланат.",
                    "👉 Жакынкы офис: moskva.beeline.ru/customers/beeline-map/",
                ],
                "is_end": True,
            },
            "b_no_app": {
                "question": "Тиркемени орнотко каласызбы? Бул 2 мүнөт убакыт алат.",
                "buttons": [
                    ("✅ Ооба, орнотом", "b_will_install"),
                    ("❌ Жок, башка жол керек", "b_no_install"),
                ],
            },
            "b_will_install": {
                "text": [
                    "Жакшы! Beeline тиркемесин жүктөп алыңыз:",
                    "▶ Android:\nplay.google.com/store/apps/details?id=ru.beeline.services\n▶ Huawei:\nappgallery.huawei.com/app/C100716739\n▶ iPhone:\napps.apple.com/ru/app/moj-bilajn/id569251594",
                ],
                "question": "Орноттуңузбу?",
                "buttons": [
                    ("✅ Орноттум, улантайбыз", "b_has_app"),
                ],
            },
            "b_no_install": {
                "text": [
                    "Макул! Эки вариант:",
                    "🏢 1-вариант — Beeline офиси:\nПаспортуңуз менен келиңиз, жаңы телефондун IMEI-ин айтыңыз.\nIMEI: *060*3# же Жөндөөлөр → «Аппарат жөнүндө»\n👉 moskva.beeline.ru/customers/beeline-map/",
                    "📞 2-вариант — КЦ:\n0611 (Beeline дан бекер)\n8 800 700-06-11 (каалаган оператордон)",
                ],
                "is_end": True,
            },
        },

        "ebs": {
            "start": {
                "text": [
                    "Номуруңуз бөгөттөлгөн, анткени Россиядагы мыйзам боюнча бардык чет элдик жарандар биометрия аркылуу инсандыгын ырасташы керек.",
                    "Мен сизге кадамма-кадам жардам берем. 👍",
                ],
                "question": "Сизде СНИЛС барбы?",
                "buttons": [
                    ("✅ Ооба, бар", "a_has_snils"),
                    ("❌ Жок / бул эмне экенин билбейм", "b_no_snils"),
                ],
            },
            "a_has_snils": {
                "text": [
                    "Жакшы! Биометрия кабыл алган банкка барышыңыз керек.",
                    "Өзүңүз менен алыңыз:\n✅ Паспорт (оригинал)\n✅ Нотариалдык котормо (Беларусь жарандарына керек эмес)\n✅ СНИЛС\n✅ Email же телефон",
                    "Банкта Госуслуги аккаунту ачуuga жардам беришет жана үн + жүзүңүздү каттап алышат.",
                    "👉 Жакынкы банк: map.gosuslugi.ru/?layer=co",
                ],
                "question": "Банкта биометрияны каттатып бүттүңүзбү?",
                "buttons": [
                    ("✅ Кылдым, улантайбыз", "a_bank_done"),
                ],
            },
            "a_bank_done": {
                "text": [
                    "Жакшы! Акыркы кадам — Госуслуги де маалыматтарды ырастоо.",
                    "Госуслуги тиркемесин ачыңыз → «Менин профилим» → «Документтер» → «Мобилдик байланыш» → номеруңузду басып ырастаңыз.",
                    "📄 PDF:\nstatic.beeline.ru/upload/images/landings/dobro/28295_manual_KG.pdf",
                    "Же Beeline офисине келиңиз:\nmoskva.beeline.ru/customers/beeline-map/",
                ],
                "question": "Чыктыбы?",
                "buttons": [
                    ("✅ Ооба, баарын жасадым!", "a_success"),
                    ("❌ Жок, кыйынчылыктар бар", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Жакшы! Байланыш бир нече мүнөттүн ичинде калыбына келиши керек.\nЭгер болбосо — чалыңыз: 0611. Ийгилик! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Эмне болбой жатканын жазыңыз — чечебиз.\nЖе Beeline офисине келиңиз: moskva.beeline.ru/customers/beeline-map/",
                "is_end": True,
            },
            "b_no_snils": {
                "text": [
                    "Анда адегенде СНИЛС алуу керек. Эки жол:",
                    "👔 1-жол — Иш берүүчү аркылуу (5 жумуш күн):\nИш берүүчүңүздөн маалыматтарды Россиянын Социалдык фондуна жөнөтүүсүн суранышыңыз.",
                    "🏛 2-жол — Өз алдынча:\nМФЦ же Социалдык фондго паспорт + котормо менен барыңыз (Беларусь жарандарына керек эмес).\n👉 МФЦ: map.gosuslugi.ru/?layer=co\n👉 Социалдык фонд: sfr.gov.ru/grazhdanam/social_fond/~8333",
                ],
                "question": "СНИЛС алдыңызбы?",
                "buttons": [
                    ("✅ СНИЛС алдым, улантайбыз", "a_has_snils"),
                ],
            },
        },
    },

    # ══════════════════════════════════════════
    # РУССКИЙ (для тестирования Еленой)
    # ══════════════════════════════════════════
    "ru": {
        "imei": {
            "start": {
                "text": [
                    "Привет! Твой номер заблокирован, потому что SIM-карту переставили в другое устройство.",
                    "Это решается — сейчас разберёмся вместе. 👍",
                ],
                "question": "Ты можешь вернуть SIM-карту обратно в тот телефон, где она была раньше?",
                "buttons": [
                    ("✅ Да, могу", "a_can_return"),
                    ("❌ Нет — сломан / потерян / не хочу", "b_cannot_return"),
                ],
            },
            "a_can_return": {
                "text": "Отлично! Переставь SIM обратно — связь восстановится сразу. ✅",
                "question": "Получилось?",
                "buttons": [
                    ("🎉 Да, всё работает!", "a_success"),
                    ("❌ Нет, что-то пошло не так", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Рады помочь! Если что-то понадобится — пиши. Удачи! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Напиши, что происходит — разберёмся.\nИли звони: 0611 (бесплатно с билайн).",
                "is_end": True,
            },
            "b_cannot_return": {
                "text": "Понял. Два варианта: через приложение билайн (быстрее) или через офис.",
                "question": "Приложение билайн установлено на новом телефоне?",
                "buttons": [
                    ("✅ Да, приложение есть", "b_has_app"),
                    ("❌ Нет, нет приложения", "b_no_app"),
                ],
            },
            "b_has_app": {
                "text": [
                    "Отлично! Пошаговая инструкция:",
                    "1️⃣  Открой приложение билайн.\n2️⃣  На главном экране будет сообщение о блокировке — нажми на него.\n3️⃣  Следуй шагам в приложении — укажи IMEI нового телефона.",
                    "📱 Не знаешь IMEI?\nНабери *060*3# — появится на экране.\nИли: Настройки → «Об устройстве».",
                ],
                "question": "Сделал?",
                "buttons": [
                    ("✅ Да, обновил IMEI", "b_app_done"),
                    ("❌ Нет, не получается", "b_app_fail"),
                ],
            },
            "b_app_done": {
                "text": "IMEI обновлён! ✅\nОстался один шаг — подтвердить данные через Госуслуги.",
                "is_end": True,
            },
            "b_app_fail": {
                "text": [
                    "Не страшно! Можно решить в офисе.",
                    "Приходи в любой офис билайна с паспортом — там обновят IMEI.",
                    "👉 Найти офис: moskva.beeline.ru/customers/beeline-map/",
                ],
                "is_end": True,
            },
            "b_no_app": {
                "question": "Хочешь установить приложение? Займёт 2 минуты.",
                "buttons": [
                    ("✅ Да, установлю", "b_will_install"),
                    ("❌ Нет, лучше другой способ", "b_no_install"),
                ],
            },
            "b_will_install": {
                "text": [
                    "Отлично! Скачай приложение билайн:",
                    "▶ Android:\nplay.google.com/store/apps/details?id=ru.beeline.services\n▶ Huawei:\nappgallery.huawei.com/app/C100716739\n▶ iPhone:\napps.apple.com/ru/app/moj-bilajn/id569251594",
                ],
                "question": "Установил?",
                "buttons": [
                    ("✅ Установил, продолжаем", "b_has_app"),
                ],
            },
            "b_no_install": {
                "text": [
                    "Окей! Два варианта:",
                    "🏢 Вариант 1 — Офис билайна:\nПриходи с паспортом, скажи IMEI нового телефона.\nIMEI: *060*3# или Настройки → «Об устройстве»\n👉 moskva.beeline.ru/customers/beeline-map/",
                    "📞 Вариант 2 — Колл-центр:\n0611 (бесплатно с билайн)\n8 800 700-06-11 (с любого оператора)",
                ],
                "is_end": True,
            },
        },

        "ebs": {
            "start": {
                "text": [
                    "Твой номер заблокирован, потому что нужно подтвердить личность через биометрию — это требование закона для всех иностранных граждан в России.",
                    "Я помогу сделать это шаг за шагом. 👍",
                ],
                "question": "У тебя есть СНИЛС?",
                "buttons": [
                    ("✅ Да, есть", "a_has_snils"),
                    ("❌ Нет / не знаю что это", "b_no_snils"),
                ],
            },
            "a_has_snils": {
                "text": [
                    "Хорошо! Тебе нужно прийти в банк, где принимают биометрию.",
                    "Возьми с собой:\n✅ Паспорт (оригинал)\n✅ Нотариально заверенный перевод паспорта (не нужен гражданам Беларуси)\n✅ СНИЛС\n✅ Email или номер телефона",
                    "В банке создадут аккаунт на Госуслугах (если нет) и запишут голос + лицо в ЕБС.",
                    "👉 Найти ближайший банк: map.gosuslugi.ru/?layer=co",
                ],
                "question": "Записал биометрию в банке?",
                "buttons": [
                    ("✅ Сделал, продолжаем", "a_bank_done"),
                ],
            },
            "a_bank_done": {
                "text": [
                    "Отлично! Последний шаг — подтвердить данные на Госуслугах.",
                    "Открой приложение Госуслуги → «Мой профиль» → «Документы» → «Мобильная связь» → нажми на свой номер и подтверди.",
                    "📄 PDF-инструкция:\nstatic.beeline.ru/upload/images/landings/dobro/29788_aktivacija_sim.pdf",
                    "Или приходи в офис билайна:\nmoskva.beeline.ru/customers/beeline-map/",
                ],
                "question": "Получилось?",
                "buttons": [
                    ("✅ Да, всё сделал!", "a_success"),
                    ("❌ Нет, возникли трудности", "a_fail"),
                ],
            },
            "a_success": {
                "text": "Отлично! Связь должна восстановиться в течение нескольких минут.\nЕсли нет — позвони: 0611. Удачи! 😊",
                "is_end": True,
            },
            "a_fail": {
                "text": "Напиши, что именно не получается — разберёмся.\nИли приходи в офис: moskva.beeline.ru/customers/beeline-map/",
                "is_end": True,
            },
            "b_no_snils": {
                "text": [
                    "Тогда сначала нужно получить СНИЛС. Два способа:",
                    "👔 Способ 1 — Через работодателя (5 рабочих дней):\nПопроси работодателя отправить данные в Социальный фонд России.",
                    "🏛 Способ 2 — Самостоятельно:\nПриди в МФЦ или Соцфонд с паспортом и нотариальным переводом (не нужен гражданам Беларуси).\n👉 МФЦ: map.gosuslugi.ru/?layer=co\n👉 Соцфонд: sfr.gov.ru/grazhdanam/social_fond/~8333",
                ],
                "question": "Получил СНИЛС?",
                "buttons": [
                    ("✅ Есть СНИЛС, продолжаем", "a_has_snils"),
                ],
            },
        },
    },
}


# ─────────────────────────────────────────────
# ОПРОС (после завершения диалога)
# ─────────────────────────────────────────────

SURVEY = {
    "uz": {
        "intro":  "📊 Qisqa so'rovnoma — 5 ta savol.\nJavoblaringiz skriptni yaxshilashga yordam beradi. Rahmat! 🙏",
        "q1":     "1️⃣  Tushuntirish qanchalik *tushunarlii* edi?",
        "q1_btn": [("1 ⭐", "1"), ("2 ⭐", "2"), ("3 ⭐", "3"), ("4 ⭐", "4"), ("5 ⭐", "5")],
        "q2":     "2️⃣  Bot tili *tabiiy* eshildimi? Siz kundalik hayotda shu tarzda gaplashasizmi?",
        "q2_btn": [("✅ Ha, tabiiy", "yes"), ("🔸 Qisman", "partial"), ("❌ Yo'q, g'alati", "no")],
        "q3":     "3️⃣  Nima qilish kerakligini *tushundingizmi*?",
        "q3_btn": [("✅ To'liq tushundim", "full"), ("🔸 Qisman", "partial"), ("❌ Tushunmadim", "no")],
        "q4":     "4️⃣  *Nima noqulay yoki tushunarsiz* bo'ldi?\n(Erkin yozing. Hech nima bo'lmasa — «yo'q» deb yozing.)",
        "q5":     "5️⃣  Bunday chat-botni *tanishingizga tavsiya qilarmidingiz*?",
        "q5_btn": [("✅ Ha", "yes"), ("🔸 Balki", "maybe"), ("❌ Yo'q", "no")],
        "thanks": "Rahmat! Javoblaringiz saqlandi. 🙏\nSiz ushbu muammoni hal qilishga hissa qo'shyapsiz!",
    },
    "tj": {
        "intro":  "📊 Пурсишномаи кӯтоҳ — 5 савол.\nҶавобҳои шумо ба беҳтар кардани скрипт кӯмак мекунад. Рахмат! 🙏",
        "q1":     "1️⃣  Шарҳ чӣ қадар *фаҳмо* буд?",
        "q1_btn": [("1 ⭐", "1"), ("2 ⭐", "2"), ("3 ⭐", "3"), ("4 ⭐", "4"), ("5 ⭐", "5")],
        "q2":     "2️⃣  Забони бот *табиӣ* ба назар расид? Оё дар ҳаёти ҳаррӯза чунин гап мезанед?",
        "q2_btn": [("✅ Бале, табиӣ", "yes"), ("🔸 Қисман", "partial"), ("❌ Не, ғайриодатӣ", "no")],
        "q3":     "3️⃣  Оё *фаҳмидед* ки чӣ кор кардан лозим аст?",
        "q3_btn": [("✅ Пурра фаҳмидам", "full"), ("🔸 Қисман", "partial"), ("❌ Нафаҳмидам", "no")],
        "q4":     "4️⃣  *Чӣ нофаҳмо ё нороҳаткунанда* буд?\n(Озодона нависед. Агар чизе набошад — «не» нависед.)",
        "q5":     "5️⃣  Оё шумо ин чат-ботро ба *шиносонатон тавсия* медиҳед?",
        "q5_btn": [("✅ Бале", "yes"), ("🔸 Шояд", "maybe"), ("❌ Не", "no")],
        "thanks": "Раҳмат! Ҷавобҳоятон сабт шуд. 🙏\nШумо ба ҳалли ин мушкилот кӯмак мекунед!",
    },
    "kg": {
        "intro":  "📊 Кыска суроо — 5 суроо.\nЖоопторуңуз скриптти жакшыртууга жардам берет. Рахмат! 🙏",
        "q1":     "1️⃣  Түшүндүрмө канчалык *тушунуктуу* болду?",
        "q1_btn": [("1 ⭐", "1"), ("2 ⭐", "2"), ("3 ⭐", "3"), ("4 ⭐", "4"), ("5 ⭐", "5")],
        "q2":     "2️⃣  Боттун тили *жаратылыштуу* угулдубу? Күнүмдүк жашоодо ушундай сүйлөйсүзбү?",
        "q2_btn": [("✅ Ооба, жаратылыштуу", "yes"), ("🔸 Жарым-жартылай", "partial"), ("❌ Жок, жасалма", "no")],
        "q3":     "3️⃣  Эмне кылуу керектигин *түшүндүңүзбү*?",
        "q3_btn": [("✅ Толук түшүндүм", "full"), ("🔸 Жарым-жартылай", "partial"), ("❌ Түшүнбөдүм", "no")],
        "q4":     "4️⃣  *Эмне тушунуксуз же ыңгайсыз* болду?\n(Эркин жазыңыз. Эч нерсе болбосо — «жок» деп жазыңыз.)",
        "q5":     "5️⃣  Бул чат-ботту *тааныштарыңызга сунуштайсызбы*?",
        "q5_btn": [("✅ Ооба", "yes"), ("🔸 Балким", "maybe"), ("❌ Жок", "no")],
        "thanks": "Рахмат! Жоопторуңуз сакталды. 🙏\nСиз бул маселени чечүүгө салым кошуп жатасыз!",
    },
    "ru": {
        "intro":  "📊 Короткий опрос — 5 вопросов.\nТвои ответы помогут улучшить скрипты. Спасибо! 🙏",
        "q1":     "1️⃣  Насколько *понятным* было объяснение?",
        "q1_btn": [("1 ⭐", "1"), ("2 ⭐", "2"), ("3 ⭐", "3"), ("4 ⭐", "4"), ("5 ⭐", "5")],
        "q2":     "2️⃣  Язык бота звучал *естественно*? Так говорят в жизни?",
        "q2_btn": [("✅ Да, естественно", "yes"), ("🔸 Частично", "partial"), ("❌ Нет, странно", "no")],
        "q3":     "3️⃣  Ты *понял*, что нужно сделать?",
        "q3_btn": [("✅ Полностью понял", "full"), ("🔸 Частично", "partial"), ("❌ Не понял", "no")],
        "q4":     "4️⃣  Что было *непонятно или неудобно*?\n(Пиши свободно. Если всё ок — напиши «нет».)",
        "q5":     "5️⃣  Ты бы *порекомендовал* такой чат-бот знакомому?",
        "q5_btn": [("✅ Да", "yes"), ("🔸 Может быть", "maybe"), ("❌ Нет", "no")],
        "thanks": "Спасибо! Ответы сохранены. 🙏\nТы помогаешь сделать сервис лучше!",
    },
}


# ─────────────────────────────────────────────
# ИНТЕРФЕЙС
# ─────────────────────────────────────────────

LANG_INTRO = (
    "Привет! / Salom! / Салом! / Саламатсызбы!\n\n"
    "Выберите язык / Tilni tanlang / Забонро интихоб кунед / Тилди тандаңыз:"
)

LANG_BUTTONS = [
    ("🇺🇿 O'zbekcha", "uz"),
    ("🇹🇯 Тоҷикӣ", "tj"),
    ("🇰🇬 Кыргызча", "kg"),
    ("🇷🇺 Русский (тест)", "ru"),
]

SCENARIO_BUTTONS = {
    "uz": [
        ("📱 SIM boshqa telefonda — bloklangan (IMEI)", "imei"),
        ("🔐 Biometriya / Gosuslugi tasdiqlash (EBS)", "ebs"),
    ],
    "tj": [
        ("📱 SIM дар телефони дигар — баста шудааст (IMEI)", "imei"),
        ("🔐 Биометрия / тасдиқи Госуслуги (ЕБС)", "ebs"),
    ],
    "kg": [
        ("📱 SIM башка телефондо — бөгөттөлгөн (IMEI)", "imei"),
        ("🔐 Биометрия / Госуслуги ырастоо (ЕБС)", "ebs"),
    ],
    "ru": [
        ("📱 SIM в другом телефоне — заблокирована (IMEI)", "imei"),
        ("🔐 Биометрия / подтверждение Госуслуг (ЕБС)", "ebs"),
    ],
}

SCENARIO_QUESTION = {
    "uz": "Qaysi muammoni hal qilmoqchisiz?",
    "tj": "Кадом мушкилотро ҳал мекунед?",
    "kg": "Кандай маселени чечкиңиз келет?",
    "ru": "Какую проблему решаете?",
}
