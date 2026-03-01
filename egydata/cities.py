cities = [
  # Cairo (CAI)
  {"id": 1, "name": "مدينة نصر", "nameEn": "Nasr City", "governorateCode": "CAI"},
  {"id": 2, "name": "مصر الجديدة", "nameEn": "Heliopolis", "governorateCode": "CAI"},
  {"id": 3, "name": "المعادي", "nameEn": "Maadi", "governorateCode": "CAI"},
  {"id": 4, "name": "مصر القديمة", "nameEn": "Old Cairo", "governorateCode": "CAI"},
  {"id": 5, "name": "شبرا", "nameEn": "Shubra", "governorateCode": "CAI"},
  {"id": 6, "name": "عين شمس", "nameEn": "Ain Shams", "governorateCode": "CAI"},
  {"id": 7, "name": "حلوان", "nameEn": "Helwan", "governorateCode": "CAI"},
  {"id": 8, "name": "التجمع الخامس", "nameEn": "Fifth Settlement", "governorateCode": "CAI"},
  {"id": 9, "name": "القاهرة الجديدة", "nameEn": "New Cairo", "governorateCode": "CAI"},
  {"id": 10, "name": "المقطم", "nameEn": "Mokattam", "governorateCode": "CAI"},
  # Alexandria (ALX)
  {"id": 11, "name": "المنتزه", "nameEn": "Montaza", "governorateCode": "ALX"},
  {"id": 12, "name": "وسط الإسكندرية", "nameEn": "Downtown Alexandria", "governorateCode": "ALX"},
  {"id": 13, "name": "العجمي", "nameEn": "Agami", "governorateCode": "ALX"},
  {"id": 14, "name": "سيدي بشر", "nameEn": "Sidi Bishr", "governorateCode": "ALX"},
  {"id": 15, "name": "برج العرب", "nameEn": "Borg El Arab", "governorateCode": "ALX"},
  {"id": 16, "name": "العامرية", "nameEn": "Amreya", "governorateCode": "ALX"},
  # Giza (GIZ)
  {"id": 17, "name": "الدقي", "nameEn": "Dokki", "governorateCode": "GIZ"},
  {"id": 18, "name": "المهندسين", "nameEn": "Mohandessin", "governorateCode": "GIZ"},
  {"id": 19, "name": "العجوزة", "nameEn": "Agouza", "governorateCode": "GIZ"},
  {"id": 20, "name": "الهرم", "nameEn": "Haram", "governorateCode": "GIZ"},
  {"id": 21, "name": "فيصل", "nameEn": "Faisal", "governorateCode": "GIZ"},
  {"id": 22, "name": "6 أكتوبر", "nameEn": "6th of October", "governorateCode": "GIZ"},
  {"id": 23, "name": "الشيخ زايد", "nameEn": "Sheikh Zayed", "governorateCode": "GIZ"},
  {"id": 24, "name": "إمبابة", "nameEn": "Imbaba", "governorateCode": "GIZ"},
  # Port Said (PTS)
  {"id": 25, "name": "حي الشرق", "nameEn": "East District", "governorateCode": "PTS"},
  {"id": 26, "name": "حي العرب", "nameEn": "Arab District", "governorateCode": "PTS"},
  {"id": 27, "name": "حي الضواحي", "nameEn": "Suburbs District", "governorateCode": "PTS"},
  {"id": 28, "name": "بورفؤاد", "nameEn": "Port Fouad", "governorateCode": "PTS"},
  # Suez (SUZ)
  {"id": 29, "name": "حي السويس", "nameEn": "Suez District", "governorateCode": "SUZ"},
  {"id": 30, "name": "حي الأربعين", "nameEn": "Arbaeen District", "governorateCode": "SUZ"},
  {"id": 31, "name": "عتاقة", "nameEn": "Ataka", "governorateCode": "SUZ"},
  {"id": 32, "name": "حي فيصل", "nameEn": "Faisal District", "governorateCode": "SUZ"},
  # Dakahlia (DKH)
  {"id": 33, "name": "المنصورة", "nameEn": "Mansoura", "governorateCode": "DKH"},
  {"id": 34, "name": "طلخا", "nameEn": "Talkha", "governorateCode": "DKH"},
  {"id": 35, "name": "ميت غمر", "nameEn": "Mit Ghamr", "governorateCode": "DKH"},
  {"id": 36, "name": "دكرنس", "nameEn": "Dikirnis", "governorateCode": "DKH"},
  {"id": 37, "name": "أجا", "nameEn": "Aga", "governorateCode": "DKH"},
  {"id": 38, "name": "السنبلاوين", "nameEn": "Sinbellawin", "governorateCode": "DKH"},
  # Sharqia (SHR)
  {"id": 39, "name": "الزقازيق", "nameEn": "Zagazig", "governorateCode": "SHR"},
  {"id": 40, "name": "العاشر من رمضان", "nameEn": "10th of Ramadan", "governorateCode": "SHR"},
  {"id": 41, "name": "بلبيس", "nameEn": "Bilbeis", "governorateCode": "SHR"},
  {"id": 42, "name": "أبو حماد", "nameEn": "Abu Hammad", "governorateCode": "SHR"},
  {"id": 43, "name": "منيا القمح", "nameEn": "Minya Al Qamh", "governorateCode": "SHR"},
  {"id": 44, "name": "فاقوس", "nameEn": "Faqous", "governorateCode": "SHR"},
  # Qalyubia (QLB)
  {"id": 45, "name": "بنها", "nameEn": "Benha", "governorateCode": "QLB"},
  {"id": 46, "name": "شبرا الخيمة", "nameEn": "Shubra El Kheima", "governorateCode": "QLB"},
  {"id": 47, "name": "قليوب", "nameEn": "Qalyub", "governorateCode": "QLB"},
  {"id": 48, "name": "القناطر الخيرية", "nameEn": "El Qanater El Khayreya", "governorateCode": "QLB"},
  {"id": 49, "name": "طوخ", "nameEn": "Toukh", "governorateCode": "QLB"},
  # Kafr El Sheikh (KFS)
  {"id": 50, "name": "كفر الشيخ", "nameEn": "Kafr El Sheikh City", "governorateCode": "KFS"},
  {"id": 51, "name": "دسوق", "nameEn": "Desouk", "governorateCode": "KFS"},
  {"id": 52, "name": "فوه", "nameEn": "Fuwwah", "governorateCode": "KFS"},
  {"id": 53, "name": "بيلا", "nameEn": "Bella", "governorateCode": "KFS"},
  # Gharbia (GHR)
  {"id": 54, "name": "طنطا", "nameEn": "Tanta", "governorateCode": "GHR"},
  {"id": 55, "name": "المحلة الكبرى", "nameEn": "El Mahalla El Kubra", "governorateCode": "GHR"},
  {"id": 56, "name": "كفر الزيات", "nameEn": "Kafr El Zayat", "governorateCode": "GHR"},
  {"id": 57, "name": "زفتى", "nameEn": "Zefta", "governorateCode": "GHR"},
  {"id": 58, "name": "السنطة", "nameEn": "Santa", "governorateCode": "GHR"},
  # Monufia (MNF)
  {"id": 59, "name": "شبين الكوم", "nameEn": "Shebin El Kom", "governorateCode": "MNF"},
  {"id": 60, "name": "منوف", "nameEn": "Menouf", "governorateCode": "MNF"},
  {"id": 61, "name": "أشمون", "nameEn": "Ashmoun", "governorateCode": "MNF"},
  {"id": 62, "name": "السادات", "nameEn": "Sadat City", "governorateCode": "MNF"},
  {"id": 63, "name": "تلا", "nameEn": "Tala", "governorateCode": "MNF"},
  # Beheira (BHR)
  {"id": 64, "name": "دمنهور", "nameEn": "Damanhour", "governorateCode": "BHR"},
  {"id": 65, "name": "كفر الدوار", "nameEn": "Kafr El Dawar", "governorateCode": "BHR"},
  {"id": 66, "name": "رشيد", "nameEn": "Rashid", "governorateCode": "BHR"},
  {"id": 67, "name": "إدكو", "nameEn": "Edku", "governorateCode": "BHR"},
  {"id": 68, "name": "أبو المطامير", "nameEn": "Abu El Matamir", "governorateCode": "BHR"},
  # Ismailia (ISM)
  {"id": 69, "name": "الإسماعيلية", "nameEn": "Ismailia City", "governorateCode": "ISM"},
  {"id": 70, "name": "فايد", "nameEn": "Fayed", "governorateCode": "ISM"},
  {"id": 71, "name": "القنطرة شرق", "nameEn": "Qantara East", "governorateCode": "ISM"},
  {"id": 72, "name": "التل الكبير", "nameEn": "Tell El Kebir", "governorateCode": "ISM"},
  # Damietta (DMT)
  {"id": 73, "name": "دمياط", "nameEn": "Damietta City", "governorateCode": "DMT"},
  {"id": 74, "name": "دمياط الجديدة", "nameEn": "New Damietta", "governorateCode": "DMT"},
  {"id": 75, "name": "رأس البر", "nameEn": "Ras El Bar", "governorateCode": "DMT"},
  {"id": 76, "name": "فارسكور", "nameEn": "Faraskour", "governorateCode": "DMT"},
  # Faiyum (FYM)
  {"id": 77, "name": "الفيوم", "nameEn": "Faiyum City", "governorateCode": "FYM"},
  {"id": 78, "name": "إطسا", "nameEn": "Etsa", "governorateCode": "FYM"},
  {"id": 79, "name": "طامية", "nameEn": "Tamiya", "governorateCode": "FYM"},
  {"id": 80, "name": "سنورس", "nameEn": "Snouris", "governorateCode": "FYM"},
  # Beni Suef (BNS)
  {"id": 81, "name": "بني سويف", "nameEn": "Beni Suef City", "governorateCode": "BNS"},
  {"id": 82, "name": "الواسطى", "nameEn": "El Wasta", "governorateCode": "BNS"},
  {"id": 83, "name": "ناصر", "nameEn": "Nasser", "governorateCode": "BNS"},
  {"id": 84, "name": "إهناسيا", "nameEn": "Ehnasia", "governorateCode": "BNS"},
  # Minya (MNY)
  {"id": 85, "name": "المنيا", "nameEn": "Minya City", "governorateCode": "MNY"},
  {"id": 86, "name": "ملوي", "nameEn": "Mallawi", "governorateCode": "MNY"},
  {"id": 87, "name": "سمالوط", "nameEn": "Samalut", "governorateCode": "MNY"},
  {"id": 88, "name": "المنيا الجديدة", "nameEn": "New Minya", "governorateCode": "MNY"},
  {"id": 89, "name": "أبو قرقاص", "nameEn": "Abu Qurqas", "governorateCode": "MNY"},
  # Asyut (AST)
  {"id": 90, "name": "أسيوط", "nameEn": "Asyut City", "governorateCode": "AST"},
  {"id": 91, "name": "ديروط", "nameEn": "Dairut", "governorateCode": "AST"},
  {"id": 92, "name": "القوصية", "nameEn": "El Qusiya", "governorateCode": "AST"},
  {"id": 93, "name": "منفلوط", "nameEn": "Manfalut", "governorateCode": "AST"},
  {"id": 94, "name": "أبنوب", "nameEn": "Abnoub", "governorateCode": "AST"},
  # Sohag (SHG)
  {"id": 95, "name": "سوهاج", "nameEn": "Sohag City", "governorateCode": "SHG"},
  {"id": 96, "name": "أخميم", "nameEn": "Akhmim", "governorateCode": "SHG"},
  {"id": 97, "name": "جرجا", "nameEn": "Girga", "governorateCode": "SHG"},
  {"id": 98, "name": "طهطا", "nameEn": "Tahta", "governorateCode": "SHG"},
  {"id": 99, "name": "المراغة", "nameEn": "El Maragha", "governorateCode": "SHG"},
  # Qena (QNA)
  {"id": 100, "name": "قنا", "nameEn": "Qena City", "governorateCode": "QNA"},
  {"id": 101, "name": "نجع حمادي", "nameEn": "Nag Hammadi", "governorateCode": "QNA"},
  {"id": 102, "name": "دشنا", "nameEn": "Dishna", "governorateCode": "QNA"},
  {"id": 103, "name": "قوص", "nameEn": "Qus", "governorateCode": "QNA"},
  # Luxor (LXR)
  {"id": 104, "name": "الأقصر", "nameEn": "Luxor City", "governorateCode": "LXR"},
  {"id": 105, "name": "إسنا", "nameEn": "Esna", "governorateCode": "LXR"},
  {"id": 106, "name": "أرمنت", "nameEn": "Armant", "governorateCode": "LXR"},
  {"id": 107, "name": "الطود", "nameEn": "El Tod", "governorateCode": "LXR"},
    # Aswan (ASN)
    {"id": 108, "name": "أسوان", "nameEn": "Aswan City", "governorateCode": "ASN"},
    {"id": 109, "name": "كوم أمبو", "nameEn": "Kom Ombo", "governorateCode": "ASN"},
    {"id": 110, "name": "إدفو", "nameEn": "Edfu", "governorateCode": "ASN"},
    {"id": 111, "name": "دراو", "nameEn": "Daraw", "governorateCode": "ASN"},
    {"id": 112, "name": "أبو سمبل", "nameEn": "Abu Simbel", "governorateCode": "ASN"},
    # Red Sea (RED)
    {"id": 113, "name": "الغردقة", "nameEn": "Hurghada", "governorateCode": "RED"},
    {"id": 114, "name": "سفاجا", "nameEn": "Safaga", "governorateCode": "RED"},
    {"id": 115, "name": "القصير", "nameEn": "El Quseir", "governorateCode": "RED"},
    {"id": 116, "name": "مرسى علم", "nameEn": "Marsa Alam", "governorateCode": "RED"},
    {"id": 117, "name": "رأس غارب", "nameEn": "Ras Ghareb", "governorateCode": "RED"},
    # New Valley (WAD)
    {"id": 118, "name": "الخارجة", "nameEn": "El Kharga", "governorateCode": "WAD"},
    {"id": 119, "name": "الداخلة", "nameEn": "Dakhla", "governorateCode": "WAD"},
    {"id": 120, "name": "الفرافرة", "nameEn": "Farafra", "governorateCode": "WAD"},
    {"id": 121, "name": "باريس", "nameEn": "Paris", "governorateCode": "WAD"},
    # Matruh (MTR)
    {"id": 122, "name": "مرسى مطروح", "nameEn": "Marsa Matruh", "governorateCode": "MTR"},
    {"id": 123, "name": "سيوة", "nameEn": "Siwa", "governorateCode": "MTR"},
    {"id": 124, "name": "الحمام", "nameEn": "El Hamam", "governorateCode": "MTR"},
    {"id": 125, "name": "العلمين", "nameEn": "El Alamein", "governorateCode": "MTR"},
    {"id": 126, "name": "الضبعة", "nameEn": "El Dabaa", "governorateCode": "MTR"},
    # North Sinai (SIN)
    {"id": 127, "name": "العريش", "nameEn": "Arish", "governorateCode": "SIN"},
    {"id": 128, "name": "الشيخ زويد", "nameEn": "Sheikh Zuweid", "governorateCode": "SIN"},
    {"id": 129, "name": "رفح", "nameEn": "Rafah", "governorateCode": "SIN"},
    {"id": 130, "name": "بئر العبد", "nameEn": "Bir al-Abed", "governorateCode": "SIN"},
    # South Sinai (SIS)
    {"id": 131, "name": "شرم الشيخ", "nameEn": "Sharm El Sheikh", "governorateCode": "SIS"},
    {"id": 132, "name": "دهب", "nameEn": "Dahab", "governorateCode": "SIS"},
    {"id": 133, "name": "نويبع", "nameEn": "Nuweiba", "governorateCode": "SIS"},
    {"id": 134, "name": "طابا", "nameEn": "Taba", "governorateCode": "SIS"},
    {"id": 135, "name": "سانت كاترين", "nameEn": "Saint Catherine", "governorateCode": "SIS"},
    {"id": 136, "name": "الطور", "nameEn": "El Tor", "governorateCode": "SIS"},
    # New Cities (4th Generation & Others)
    {"id": 137, "name": "العاصمة الإدارية الجديدة", "nameEn": "New Administrative Capital", "governorateCode": "CAI"},
    {"id": 138, "name": "الشروق", "nameEn": "El Shorouk", "governorateCode": "CAI"},
    {"id": 139, "name": "بدر", "nameEn": "Badr City", "governorateCode": "CAI"},
    {"id": 140, "name": "مدينتي", "nameEn": "Madinaty", "governorateCode": "CAI"},
    {"id": 141, "name": "مدينة الرحاب", "nameEn": "Al Rehab", "governorateCode": "CAI"},
    {"id": 142, "name": "15 مايو", "nameEn": "15 May City", "governorateCode": "CAI"},
    {"id": 143, "name": "سفنكس الجديدة", "nameEn": "New Sphinx", "governorateCode": "GIZ"},
    {"id": 144, "name": "حدائق أكتوبر", "nameEn": "Hadayek October", "governorateCode": "GIZ"},
    {"id": 145, "name": "برج العرب الجديدة", "nameEn": "New Borg El Arab", "governorateCode": "ALX"},
    {"id": 146, "name": "العبور", "nameEn": "El Obour", "governorateCode": "QLB"},
    {"id": 147, "name": "العبور الجديدة", "nameEn": "New Obour", "governorateCode": "QLB"},
    {"id": 148, "name": "المنصورة الجديدة", "nameEn": "New Mansoura", "governorateCode": "DKH"},
    {"id": 149, "name": "العلمين الجديدة", "nameEn": "New Alamein", "governorateCode": "MTR"},
    {"id": 150, "name": "مدينة الجلالة", "nameEn": "Galala City", "governorateCode": "SUZ"},
    {"id": 151, "name": "مدينة ناصر (غرب أسيوط)", "nameEn": "Nasser City (West Asyut)", "governorateCode": "AST"},
]

_id_map = {c["id"]: c for c in cities}
_gov_map = {}
for city in cities:
    code = city["governorateCode"]
    _gov_map.setdefault(code, []).append(city)

def get_by_governorate(gov_code):
    """إرجاع قائمة المدن التابعة لمحافظة معينة (باستخدام كود المحافظة)."""
    if not isinstance(gov_code, str):
        return []
    return _gov_map.get(gov_code.upper(), []).copy()

def get_by_id(id):
    """إرجاع المدينة باستخدام الرقم التعريفي."""
    try:
        num_id = int(id)
    except (ValueError, TypeError):
        return None
    return _id_map.get(num_id)

def search(query):
    """البحث في المدن بالاسم العربي أو الإنجليزي."""
    if not isinstance(query, str) or not query.strip():
        return []
    q = query.strip().lower()
    result = []
    for city in cities:
        if q in city["name"] or q in city["nameEn"].lower():
            result.append(city)
    return result
