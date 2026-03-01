area_codes = [
  # Mobile Networks
  {"code": "010", "region": "ڤودافون", "regionEn": "Vodafone"},
  {"code": "011", "region": "اتصالات", "regionEn": "Etisalat"},
  {"code": "012", "region": "أورنج", "regionEn": "Orange"},
  {"code": "015", "region": "وي / العاشر من رمضان", "regionEn": "WE / 10th of Ramadan"},
  # Landlines
  {"code": "02", "region": "القاهرة والجيزة", "regionEn": "Cairo & Giza"},
  {"code": "03", "region": "الإسكندرية", "regionEn": "Alexandria"},
  {"code": "013", "region": "القليوبية (بنها)", "regionEn": "Qalyubia (Benha)"},
  {"code": "040", "region": "الغربية (طنطا)", "regionEn": "Gharbia (Tanta)"},
  {"code": "045", "region": "البحيرة (دمنهور)", "regionEn": "Beheira (Damanhour)"},
  {"code": "046", "region": "مطروح", "regionEn": "Matruh"},
  {"code": "047", "region": "كفر الشيخ", "regionEn": "Kafr El Sheikh"},
  {"code": "048", "region": "المنوفية (شبين الكوم)", "regionEn": "Monufia (Shebin El Kom)"},
  {"code": "050", "region": "الدقهلية (المنصورة)", "regionEn": "Dakahlia (Mansoura)"},
  {"code": "055", "region": "الشرقية (الزقازيق)", "regionEn": "Sharqia (Zagazig)"},
  {"code": "057", "region": "دمياط", "regionEn": "Damietta"},
  {"code": "062", "region": "السويس", "regionEn": "Suez"},
  {"code": "064", "region": "الإسماعيلية", "regionEn": "Ismailia"},
  {"code": "065", "region": "البحر الأحمر (الغردقة)", "regionEn": "Red Sea (Hurghada)"},
  {"code": "066", "region": "بورسعيد", "regionEn": "Port Said"},
  {"code": "068", "region": "شمال سيناء (العريش)", "regionEn": "North Sinai (Arish)"},
  {"code": "069", "region": "جنوب سيناء", "regionEn": "South Sinai"},
  {"code": "082", "region": "بني سويف", "regionEn": "Beni Suef"},
  {"code": "084", "region": "الفيوم", "regionEn": "Faiyum"},
  {"code": "086", "region": "المنيا", "regionEn": "Minya"},
  {"code": "088", "region": "أسيوط", "regionEn": "Asyut"},
  {"code": "092", "region": "الوادي الجديد", "regionEn": "New Valley"},
  {"code": "093", "region": "سوهاج", "regionEn": "Sohag"},
  {"code": "095", "region": "الأقصر", "regionEn": "Luxor"},
  {"code": "096", "region": "قنا", "regionEn": "Qena"},
  {"code": "097", "region": "أسوان", "regionEn": "Aswan"},
]

_code_map = {item["code"]: item for item in area_codes}

def get_all(): return area_codes.copy()

def get_region(code):
  if not isinstance(code, str): return None
  normalized = "0" + code.lstrip("0")
  return _code_map.get(code) or _code_map.get(normalized)

def get_code(region_name):
  if not isinstance(region_name, str) or not region_name.strip(): return None
  q = region_name.strip().lower()
  for item in area_codes:
    if q in item["region"] or q in item["regionEn"].lower(): return item
  return None
