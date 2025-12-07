def _avg_rgb(colors):
    if not colors:
        return (200, 200, 200)

    n = len(colors)
    r = sum(c[0] for c in colors.values()) / n
    g = sum(c[1] for c in colors.values()) / n
    b = sum(c[2] for c in colors.values()) / n
    return int(r), int(g), int(b)

def detect_mood(colors):
    r, g, b = _avg_rgb(colors)

    if r > g and r > b:
        return "🔥 Energetik"
    if g > r and g > b:
        return "🍃 Tinch"
    if b > r and b > g:
        return "❄️ Sovuqqon"

    return "🙂 Neytral"

def detect_mood_advanced(colors):
    """
    Foydalanuvchi tanlagan ranglardan chuqur psixologik tahlil chiqaradi.
    colors: {"tanasi": (r,g,b), "quyosh": (r,g,b), ...}
    """

    if not colors:
        return "🙂 Siz hali rang tanlamadingiz."

    # === O'rtacha rangni hisoblaymiz
    n = len(colors)
    avg_r = sum(c[0] for c in colors.values()) / n
    avg_g = sum(c[1] for c in colors.values()) / n
    avg_b = sum(c[2] for c in colors.values()) / n

    # Dominant komponentni aniqlaymiz
    if avg_r > avg_g and avg_r > avg_b:
        dominant = "red"
    elif avg_g > avg_r and avg_g > avg_b:
        dominant = "green"
    elif avg_b > avg_r and avg_b > avg_g:
        dominant = "blue"
    else:
        dominant = "mixed"

    # === PSIXOLOGIK SHARHLAR ===
    analyses = {
        "red": """🔥 <b>Energiya va irodaviylik</b>
Tanlagan ranglaringizdagi qizil ohang kuchli energiya, qat’iyat va harakatga tayyorlikni anglatadi.
Siz qarorlarni tez qabul qilasiz va boshqalarga ilhom beruvchi tipdasiz.
O'zingizga talabchan bo‘lsangiz-da, aynan shu xarakter sizni oldinga boshlaydi.""",

        "green": """🍃 <b>Tinchlik va barqarorlik</b>
Ranglaringizda yashilning ko‘pligi sizning muvozanatli, sabrli va sokin xarakterga egaligingizni ko‘rsatadi.
Siz hayotga mulohaza bilan yondashasiz va qarorlariz ishonchli.
Atrofdagilar siz bilan o‘zini qulay his qiladi.""",

        "blue": """❄️ <b>Xotirjamlik va chuqur fikrlash</b>
Ko‘k ranglar sizning hissiy barqaror, mulohazali va vazmin inson ekanligingizdan darak beradi.
Siz shovqinli muammolardan emas, tinch va chuqur tahlildan yo‘l topasiz.
Odamlar sizga ko‘proq ishonishadi.""",

        "purple": """🟣 <b>Ijodkorlik va noan’anaviy fikr</b>
Ranglaringizda to‘q yoki binafsha ohanglar bo‘lsa, sizning ijodiy va o‘ziga xos tafakkurga egaligingiz ayon.
Siz noodatiy g‘oyalarni ko‘ra olasiz va boshqalar ko‘rmaydigan ma’nolarni sezadigan odamsiz.""",

        "yellow": """🟡 <b>Quvonch va ijtimoiylik</b>
Sariq va to‘q sariq ranglar sizning optimist, ochiqko‘ngil va quvnoq inson ekanligingizni bildiradi.
Siz atrofdagilarga iliqlik ulashayapsiz, boshqalarga tetiklik berasiz.
Ijtimoiy muhit sizga mos keladi.""",

        "white": """🤍 <b>Poklik va soddalik</b>
Oq ranglar sizning minimalizmga, aniqlikka, ruhiy tozalik va soddalikka intilishdan dalolat beradi.
Siz ortiqcha shovqinlardan uzoq yurishni afzal ko‘rasiz.""",

        "dark": """⚫ <b>Jiddiylik va mustaqil xarakter</b>
To'q yoki qoramtir ranglar sizning mustaqil qarorlar qabul qiluvchi, chuqur fikrlovchi va mas’uliyatli inson ekanligingizni ko‘rsatadi.
Siz ichki dunyoga katta e’tibor berasiz.""",

        "mixed": """🌈 <b>Moslashuvchanlik va uyg‘unlik</b>
Sizning rang tanlovlaringiz bir xil emas, xilma-xil — bu sizning keng fikrlovchi,
moslasha oladigan, ijodiy va amaliy tomonlaringizni birlashtira oladigan kuchli xarakteringizni ko‘rsatadi.
Sizda ichki uyg‘unlik mavjud va bu juda noyob fazilatdir."""
    }

    # === Rangni aniqlash (dominant R/G/B orqali) ===
    # Purple aniqlash
    if avg_r > 150 and avg_b > 150:
        dominant = "purple"

    # Yellow aniqlash
    if avg_r > 200 and avg_g > 200:
        dominant = "yellow"

    # White
    if avg_r > 220 and avg_g > 220 and avg_b > 220:
        dominant = "white"

    # Dark
    if avg_r < 50 and avg_g < 50 and avg_b < 50:
        dominant = "dark"

    return analyses.get(dominant, analyses["mixed"])

