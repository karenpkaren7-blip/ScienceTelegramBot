TOKEN = "8781262210:AAHGz57GzbSxBhxjB0Sr1iIeeNMTqOHOnN4"
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)


# =========================================================
# 🔑8781262210:AAGbJHzBF1J8eFHM3vI6HHZZQuMJZr3_zKc
# =========================================================


# =========================================================
# 📝 بانک سؤالات فصل‌ها
# =========================================================

QUESTIONS = {

    # =====================================================
    # 📘 پایه هفتم - فصل اول: تجربه و تفکر
    # =====================================================

    "g7c1": [
        {
            "question": "کدام مورد یکی از مراحل فعالیت علمی است؟",
            "options": [
                "مشاهده و طرح پرسش",
                "حدس بدون بررسی",
                "نادیده گرفتن نتایج",
                "تغییر دادن نتایج"
            ],
            "answer": 0
        },
        {
            "question": "پس از طرح یک پرسش علمی، چه کاری انجام می‌دهیم؟",
            "options": [
                "جمع‌آوری اطلاعات و بررسی",
                "نادیده گرفتن اطلاعات",
                "اعلام نتیجه بدون بررسی",
                "تغییر دادن شواهد"
            ],
            "answer": 0
        },
        {
            "question": "کدام ویژگی برای یک پژوهشگر مهم است؟",
            "options": [
                "کنجکاوی و دقت",
                "عجله",
                "بی‌توجهی",
                "پذیرش هر پاسخ بدون بررسی"
            ],
            "answer": 0
        },
        {
            "question": "هدف از انجام آزمایش چیست؟",
            "options": [
                "بررسی یک پرسش یا فرضیه",
                "تغییر نتایج",
                "حذف شواهد",
                "حدس زدن پاسخ"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد به انجام یک فعالیت علمی درست کمک می‌کند؟",
            "options": [
                "دقت در مشاهده",
                "بی‌توجهی به شواهد",
                "عجله در نتیجه‌گیری",
                "نادیده گرفتن خطاها"
            ],
            "answer": 0
        }
    ],


    # =====================================================
    # 📘 پایه هفتم - فصل دوم: اندازه‌گیری در علوم و ابزارهای آن
    # =====================================================

    "g7c2": [
        {
            "question": "برای اندازه‌گیری طول معمولاً از چه ابزاری استفاده می‌شود؟",
            "options": [
                "خط‌کش",
                "ترازو",
                "دماسنج",
                "زمان‌سنج"
            ],
            "answer": 0
        },
        {
            "question": "واحد اصلی اندازه‌گیری طول در دستگاه SI چیست؟",
            "options": [
                "متر",
                "گرم",
                "لیتر",
                "ثانیه"
            ],
            "answer": 0
        },
        {
            "question": "برای اندازه‌گیری جرم یک جسم از چه وسیله‌ای استفاده می‌کنیم؟",
            "options": [
                "ترازو",
                "خط‌کش",
                "دماسنج",
                "استوانه مدرج"
            ],
            "answer": 0
        },
        {
            "question": "برای اندازه‌گیری دمای یک جسم از چه وسیله‌ای استفاده می‌شود؟",
            "options": [
                "دماسنج",
                "ترازو",
                "خط‌کش",
                "زمان‌سنج"
            ],
            "answer": 0
        },
        {
            "question": "کدام مورد یکای اندازه‌گیری زمان است؟",
            "options": [
                "ثانیه",
                "متر",
                "کیلوگرم",
                "درجه سلسیوس"
            ],
            "answer": 0
        },
        {
            "question": "برای اندازه‌گیری حجم مایعات معمولاً از چه وسیله‌ای استفاده می‌شود؟",
            "options": [
                "استوانه مدرج",
                "ترازو",
                "خط‌کش",
                "دماسنج"
            ],
            "answer": 0
        },
        {
            "question": "کدام کمیت با ترازو اندازه‌گیری می‌شود؟",
            "options": [
                "جرم",
                "طول",
                "دما",
                "زمان"
            ],
            "answer": 0
        },
        {
            "question": "هرچه دقت وسیله اندازه‌گیری بیشتر باشد، چه اتفاقی می‌افتد؟",
            "options": [
                "اندازه‌گیری دقیق‌تر انجام می‌شود",
                "اندازه‌گیری غیرممکن می‌شود",
                "واحد اندازه‌گیری تغییر می‌کند",
                "جرم جسم تغییر می‌کند"
            ],
            "answer": 0
        }
      ],
    
    "g7c3": [
        {
            "question": "کوچک‌ترین ذره سازنده یک عنصر که ویژگی‌های آن عنصر را حفظ می‌کند چیست؟",
            "options": ["اتم", "مولکول", "سلول", "بلور"],
            "answer": 0
        },
        {
            "question": "کدام ذره در هسته اتم قرار دارد؟",
            "options": ["الکترون", "پروتون", "الکترون و یون", "فقط مولکول"],
            "answer": 1
        },
        {
            "question": "بار الکتریکی پروتون چیست؟",
            "options": ["مثبت", "منفی", "خنثی", "بدون بار"],
            "answer": 0
        },
        {
            "question": "بار الکتریکی الکترون چیست؟",
            "options": ["مثبت", "منفی", "خنثی", "دوگانه"],
            "answer": 1
        },
        {
            "question": "کدام ذره اتم بار الکتریکی ندارد؟",
            "options": ["پروتون", "الکترون", "نوترون", "یون"],
            "answer": 2
        },
        {
            "question": "به ماده‌ای که فقط از یک نوع اتم ساخته شده باشد چه می‌گویند؟",
            "options": ["عنصر", "مخلوط", "محلول", "ترکیب"],
            "answer": 0
        },
        {
            "question": "کدام گزینه یک عنصر است؟",
            "options": ["آب", "اکسیژن", "نمک خوراکی", "دی‌اکسید کربن"],
            "answer": 1
        },
        {
            "question": "مولکول از چه چیزی تشکیل می‌شود؟",
            "options": ["از یک یا چند اتم", "فقط از پروتون‌ها", "فقط از الکترون‌ها", "فقط از نوترون‌ها"],
            "answer": 0
        },
        {
            "question": "آب از ترکیب چه عناصری تشکیل شده است؟",
            "options": ["هیدروژن و اکسیژن", "اکسیژن و کربن", "هیدروژن و نیتروژن", "کربن و نیتروژن"],
            "answer": 0
        },
        {
            "question": "کدام گزینه درباره اتم درست است؟",
            "options": ["اتم فقط از الکترون ساخته شده است", "اتم دارای هسته و الکترون است", "اتم همیشه بار منفی دارد", "اتم فقط از نوترون ساخته شده است"],
            "answer": 1
        }
    ],
    "g7c4": [
        {
            "question": "کدام گزینه یکی از ویژگی‌های فلزهاست؟",
            "options": ["رسانایی گرما و برق", "نارسانایی", "شفافیت کامل", "حل شدن در آب"],
            "answer": 0
        },
        {
            "question": "کدام ماده رسانای خوب برق است؟",
            "options": ["مس", "چوب", "پلاستیک", "شیشه"],
            "answer": 0
        },
        {
            "question": "کدام گزینه یک نارسانای الکتریکی است؟",
            "options": ["مس", "آلومینیوم", "پلاستیک", "آهن"],
            "answer": 2
        },
        {
            "question": "چرا در ساخت سیم‌های برق از مس استفاده می‌شود؟",
            "options": ["رسانایی الکتریکی خوب", "شکنندگی زیاد", "نارسانایی", "شفافیت"],
            "answer": 0
        },
        {
            "question": "کدام ویژگی برای انتخاب یک ماده مهم است؟",
            "options": ["فقط رنگ", "خواص ماده و کاربرد آن", "فقط بو", "فقط شکل"],
            "answer": 1
        },
        {
            "question": "کدام ماده معمولاً انعطاف‌پذیرتر است؟",
            "options": ["لاستیک", "شیشه", "سنگ", "گچ"],
            "answer": 0
        },
        {
            "question": "کدام گزینه نمونه‌ای از ماده طبیعی است؟",
            "options": ["چوب", "پلاستیک", "نایلون", "شیشه"],
            "answer": 0
        },
        {
            "question": "کدام مورد به حفظ محیط زیست کمک می‌کند؟",
            "options": ["بازیافت مواد", "افزایش مصرف پلاستیک", "دور ریختن مواد قابل بازیافت", "سوزاندن همه زباله‌ها"],
            "answer": 0
        },
        {
            "question": "کدام ماده معمولاً شفاف است؟",
            "options": ["شیشه", "آهن", "چوب", "سنگ"],
            "answer": 0
        },
        {
            "question": "برای ساخت قابلمه، ماده‌ای لازم است که گرما را...",
            "options": ["خوب منتقل کند", "اصلاً منتقل نکند", "فقط نور را عبور دهد", "در آب حل شود"],
            "answer": 0
        }
    ],
"g7c5": [
    {
        "question": "ماده اولیه بسیاری از وسایل مورد استفاده ما از کجا به دست می‌آید؟",
        "options": ["معادن", "ابرها", "گیاهان", "هوا"],
        "answer": 0
    },
    {
        "question": "کدام ماده از سنگ معدن آهن به دست می‌آید؟",
        "options": ["آهن", "شیشه", "پلاستیک", "چوب"],
        "answer": 0
    },
    {
        "question": "کدام فلز از سنگ معدن به دست می‌آید؟",
        "options": ["مس", "چوب", "شیشه", "لاستیک"],
        "answer": 0
    },
    {
        "question": "برای به دست آوردن فلزها از سنگ معدن چه کاری انجام می‌شود؟",
        "options": ["فرآوری و جداسازی", "منجمد کردن", "تبخیر آب دریا", "سوزاندن چوب"],
        "answer": 0
    },
    {
        "question": "کدام گزینه یک ماده معدنی است؟",
        "options": ["سنگ آهن", "چوب", "پنبه", "پشم"],
        "answer": 0
    },
    {
        "question": "آهن در کدام وسیله کاربرد زیادی دارد؟",
        "options": ["ساختمان و خودرو", "دفتر کاغذی", "لباس پشمی", "مداد چوبی"],
        "answer": 0
    },
    {
        "question": "چرا منابع معدنی باید درست مصرف شوند؟",
        "options": ["زیرا منابع معدنی محدود هستند", "زیرا همیشه بی‌نهایت هستند", "زیرا به سرعت تولید می‌شوند", "زیرا در هوا وجود دارند"],
        "answer": 0
    },
    {
        "question": "کدام کار به کاهش مصرف مواد معدنی کمک می‌کند؟",
        "options": ["بازیافت فلزها", "دور ریختن وسایل فلزی", "افزایش مصرف بی‌رویه", "سوزاندن فلزها"],
        "answer": 0
    },
    {
        "question": "مس بیشتر به دلیل کدام ویژگی در سیم‌های برق استفاده می‌شود؟",
        "options": ["رسانایی الکتریکی خوب", "شفاف بودن", "حل شدن در آب", "نرم بودن زیاد"],
        "answer": 0
    },
    {
        "question": "هدف از فرآوری مواد معدنی چیست؟",
        "options": ["جدا کردن و آماده‌سازی ماده مورد نیاز", "تبدیل همه مواد به آب", "از بین بردن همه مواد", "تبدیل سنگ به چوب"],
        "answer": 0
    }
]
}


# =========================================================
# 🚀 شروع ربات
# =========================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📘 پایه هفتم", callback_data="grade7")],
        [InlineKeyboardButton("📗 پایه هشتم", callback_data="grade8")],
        [InlineKeyboardButton("📕 پایه نهم", callback_data="grade9")]
    ]

    await update.message.reply_text(
        "سلام 👋\n\n"
        "به ربات آزمون علوم خوش آمدید. 🧪🔬\n\n"
        "لطفاً پایه تحصیلی خود را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# 📚 انتخاب پایه
# =========================================================

async def grade_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    grade = query.data

    # -----------------------------------------------------
    # پایه هفتم
    # -----------------------------------------------------

    if grade == "grade7":

        keyboard = [
            [InlineKeyboardButton(
                "فصل ۱: تجربه و تفکر",
                callback_data="g7c1"
            )],

            [InlineKeyboardButton(
                "فصل ۲: اندازه‌گیری در علوم و ابزارهای آن",
                callback_data="g7c2"
            )],

            [InlineKeyboardButton(
                "فصل ۳: اتم‌ها؛ الفبای مواد",
                callback_data="g7c3"
            )],

            [InlineKeyboardButton(
                "فصل ۴: مواد پیرامون ما",
                callback_data="g7c4"
            )],
            [InlineKeyboardButton(
                "فصل ۵: از معدن تا خانه",
                            callback_data="g7c5"
            )],    

            [InlineKeyboardButton(
                "فصل ۶: سفر آب روی زمین",
                callback_data="g7c6"
            )],

            [InlineKeyboardButton(
                "فصل ۷: سفر آب درون زمین",
                callback_data="g7c7"
            )],

            [InlineKeyboardButton(
                "فصل ۸: انرژی و تبدیل‌های آن",
                callback_data="g7c8"
            )],

            [InlineKeyboardButton(
                "فصل ۹: منابع انرژی",
                callback_data="g7c9"
            )],

            [InlineKeyboardButton(
                "فصل ۱۰: گرما و بهینه‌سازی مصرف انرژی",
                callback_data="g7c10"
            )],

            [InlineKeyboardButton(
                "فصل ۱۱: یاخته و سازمان‌بندی آن",
                callback_data="g7c11"
            )],

            [InlineKeyboardButton(
                "فصل ۱۲: سفره سلامت",
                callback_data="g7c12"
            )],

            [InlineKeyboardButton(
                "فصل ۱۳: سفر غذا",
                callback_data="g7c13"
            )],

            [InlineKeyboardButton(
                "فصل ۱۴: گردش مواد",
                callback_data="g7c14"
            )],

            [InlineKeyboardButton(
                "فصل ۱۵: تبادل با محیط",
                callback_data="g7c15"
            )],

            [InlineKeyboardButton(
                "فصل ۱۶: تنظیم عصبی",
                callback_data="g7c16"
            )],

            [InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="main_menu"
            )]
        ]

    # -----------------------------------------------------
    # پایه هشتم
    # -----------------------------------------------------

    elif grade == "grade8":

        keyboard = [
            [InlineKeyboardButton(
                "فصل ۱: مخلوط و جداسازی مواد",
                callback_data="g8c1"
            )],

            [InlineKeyboardButton(
                "فصل ۲: تغییرهای شیمیایی در خدمت زندگی",
                callback_data="g8c2"
            )],

            [InlineKeyboardButton(
                "فصل ۳: از درون اتم چه خبر",
                callback_data="g8c3"
            )],

            [InlineKeyboardButton(
                "فصل ۴: تنظیم عصبی",
                callback_data="g8c4"
            )],

            [InlineKeyboardButton(
                "فصل ۵: حس و حرکت",
                callback_data="g8c5"
            )],

            [InlineKeyboardButton(
                "فصل ۶: تنظیم هورمونی",
                callback_data="g8c6"
            )],

            [InlineKeyboardButton(
                "فصل ۷: الفبای زیست‌فناوری",
                callback_data="g8c7"
            )],

            [InlineKeyboardButton(
                "فصل ۸: تولید مثل در جانداران",
                callback_data="g8c8"
            )],

            [InlineKeyboardButton(
                "فصل ۹: الکتریسیته",
                callback_data="g8c9"
            )],

            [InlineKeyboardButton(
                "فصل ۱۰: مغناطیس",
                callback_data="g8c10"
            )],

            [InlineKeyboardButton(
                "فصل ۱۱: کانی‌ها",
                callback_data="g8c11"
            )],

            [InlineKeyboardButton(
                "فصل ۱۲: سنگ‌ها",
                callback_data="g8c12"
            )],

            [InlineKeyboardButton(
                "فصل ۱۳: هوازدگی",
                callback_data="g8c13"
            )],

            [InlineKeyboardButton(
                "فصل ۱۴: نور",
                callback_data="g8c14"
            )],

            [InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="main_menu"
            )]
        ]

    # -----------------------------------------------------
    # پایه نهم
    # -----------------------------------------------------

    elif grade == "grade9":

        keyboard = [
            [InlineKeyboardButton(
                "فصل ۱: مواد و نقش آنها در زندگی",
                callback_data="g9c1"
            )],

            [InlineKeyboardButton(
                "فصل ۲: رفتار اتم‌ها با یکدیگر",
                callback_data="g9c2"
            )],

            [InlineKeyboardButton(
                "فصل ۳: به دنبال محیطی بهتر برای زندگی",
                callback_data="g9c3"
            )],

            [InlineKeyboardButton(
                "فصل ۴: حرکت چیست؟",
                callback_data="g9c4"
            )],

            [InlineKeyboardButton(
                "فصل ۵: نیرو",
                callback_data="g9c5"
            )],

            [InlineKeyboardButton(
                "فصل ۶: زمین‌ساخت ورقه‌ای",
                callback_data="g9c6"
            )],

            [InlineKeyboardButton(
                "فصل ۷: آثاری از گذشته زمین",
                callback_data="g9c7"
            )],

            [InlineKeyboardButton(
                "فصل ۸: فشار و آثار آن",
                callback_data="g9c8"
            )],

            [InlineKeyboardButton(
                "فصل ۹: ماشین‌ها",
                callback_data="g9c9"
            )],

            [InlineKeyboardButton(
                "فصل ۱۰: نگاهی به فضا",
                callback_data="g9c10"
            )],

            [InlineKeyboardButton(
                "فصل ۱۱: گوناگونی جانداران",
                callback_data="g9c11"
            )],

            [InlineKeyboardButton(
                "فصل ۱۲: دنیای گیاهان",
                callback_data="g9c12"
            )],

            [InlineKeyboardButton(
                "فصل ۱۳: جانوران",
                callback_data="g9c13"
            )],

            [InlineKeyboardButton(
                "فصل ۱۴: جانداران و محیط",
                callback_data="g9c14"
            )],

            [InlineKeyboardButton(
                "🏠 منوی اصلی",
                callback_data="main_menu"
            )]
        ]

    await query.edit_message_text(
        "📚 لطفاً فصل مورد نظر را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# 📖 انتخاب فصل
# =========================================================

async def chapter_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    chapter = query.data

    # ذخیره فصل انتخاب‌شده
    context.user_data["chapter"] = chapter

    # اگر برای فصل سؤال نداریم
    if chapter not in QUESTIONS:

        await query.edit_message_text(
            "📚 این فصل هنوز سؤال ندارد.\n\n"
            "به‌زودی سؤال‌های این فصل اضافه خواهد شد.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="main_menu"
                    )
                ]
            ])
        )

        return

    # اگر سؤال برای فصل وجود دارد
    await query.edit_message_text(
        "📖 فصل انتخاب شد.\n\n"
        "آماده‌ای؟ 👇",
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "📝 شروع آزمون",
                    callback_data="start_exam"
                )
            ],
            [
                InlineKeyboardButton(
                    "🏠 منوی اصلی",
                    callback_data="main_menu"
                )
            ]
        ])
    )


# =========================================================
# 📝 شروع آزمون
# =========================================================

async def exam_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    chapter = context.user_data.get("chapter")

    if chapter not in QUESTIONS:

        await query.edit_message_text(
            "❌ برای این فصل هنوز سؤالی ثبت نشده است.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="main_menu"
                    )
                ]
            ])
        )

        return

    context.user_data["question_number"] = 0
    context.user_data["score"] = 0

    await send_question(query, context)


# =========================================================
# ❓ ارسال سؤال
# =========================================================

async def send_question(query, context):

    chapter = context.user_data.get("chapter")
    question_number = context.user_data["question_number"]

    chapter_questions = QUESTIONS.get(chapter, [])

    if not chapter_questions:

        await query.edit_message_text(
            "❌ برای این فصل هنوز سؤالی ثبت نشده است.",
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="main_menu"
                    )
                ]
            ])
        )

        return

    question = chapter_questions[question_number]

    keyboard = []

    for i, option in enumerate(question["options"]):

        keyboard.append([
            InlineKeyboardButton(
                option,
                callback_data=f"answer_{i}"
            )
        ])

    text = (
        f"📝 سؤال {question_number + 1} "
        f"از {len(chapter_questions)}\n\n"
        f"{question['question']}"
    )

    await query.edit_message_text(
        text,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# ✅ پاسخ به سؤال
# =========================================================

async def answer_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    selected_answer = int(query.data.split("_")[1])

    chapter = context.user_data.get("chapter")
    question_number = context.user_data["question_number"]

    chapter_questions = QUESTIONS.get(chapter, [])

    if not chapter_questions:
        return

    question = chapter_questions[question_number]

    correct_answer = question["answer"]

    if selected_answer == correct_answer:

        context.user_data["score"] += 1

        result_text = "✅ پاسخ شما صحیح است."

    else:

        correct_text = question["options"][correct_answer]

        result_text = (
            "❌ پاسخ شما نادرست است.\n\n"
            f"✅ پاسخ صحیح: {correct_text}"
        )

    # رفتن به سؤال بعدی
    context.user_data["question_number"] += 1

    # -----------------------------------------------------
    # پایان آزمون
    # -----------------------------------------------------

    if context.user_data["question_number"] >= len(chapter_questions):

        score = context.user_data["score"]

        await query.edit_message_text(
            f"{result_text}\n\n"
            "🎉 آزمون به پایان رسید.\n\n"
            f"🏆 نمره شما: {score} از "
            f"{len(chapter_questions)}",

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔄 آزمون مجدد",
                        callback_data="start_exam"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏠 منوی اصلی",
                        callback_data="main_menu"
                    )
                ]
            ])
        )

    # -----------------------------------------------------
    # ادامه آزمون
    # -----------------------------------------------------

    else:

        await query.edit_message_text(
            result_text,

            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "➡️ سؤال بعدی",
                        callback_data="next_question"
                    )
                ]
            ])
        )


# =========================================================
# ➡️ سؤال بعدی
# =========================================================

async def next_question(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    await send_question(query, context)


# =========================================================
# 🏠 منوی اصلی
# =========================================================

async def menu_selected(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    keyboard = [
        [
            InlineKeyboardButton(
                "📘 پایه هفتم",
                callback_data="grade7"
            )
        ],
        [
            InlineKeyboardButton(
                "📗 پایه هشتم",
                callback_data="grade8"
            )
        ],
        [
            InlineKeyboardButton(
                "📕 پایه نهم",
                callback_data="grade9"
            )
        ]
    ]

    await query.edit_message_text(
        "🏠 منوی اصلی\n\n"
        "لطفاً پایه تحصیلی را انتخاب کنید:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================================================
# ⚙️ اجرای ربات
# =========================================================

def main():

    app = Application.builder().token(TOKEN).build()

    # دستور /start
    app.add_handler(
        CommandHandler("start", start)
    )

    # انتخاب پایه
    app.add_handler(
        CallbackQueryHandler(
            grade_selected,
            pattern=r"^grade[789]$"
        )
    )

    # انتخاب فصل
    app.add_handler(
        CallbackQueryHandler(
            chapter_selected,
            pattern=r"^g[789]c([1-9]|1[0-6])$"
        )
    )

    # شروع آزمون
    app.add_handler(
        CallbackQueryHandler(
            exam_selected,
            pattern=r"^start_exam$"
        )
    )

    # پاسخ به سؤال
    app.add_handler(
        CallbackQueryHandler(
            answer_selected,
            pattern=r"^answer_[0-3]$"
        )
    )

    # سؤال بعدی
    app.add_handler(
        CallbackQueryHandler(
            next_question,
            pattern=r"^next_question$"
        )
    )

    # منوی اصلی
    app.add_handler(
        CallbackQueryHandler(
            menu_selected,
            pattern=r"^main_menu$"
        )
    )

    print("ربات فعال شد...")

    app.run_polling()


# =========================================================
# ▶️ اجرای برنامه
# =========================================================

if __name__ == "__main__":
    main()
