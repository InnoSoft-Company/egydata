```markdown
# Egydata

[![PyPI Version](https://img.shields.io/pypi/v/egydata.svg)](https://pypi.org/project/egydata/)
[![Python Versions](https://img.shields.io/pypi/pyversions/egydata.svg)](https://pypi.org/project/egydata/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/InnoSoft-Company/egydata/blob/main/LICENSE)

Structured Egyptian geographical and timezone data for Python.

Provides a complete, offline dataset of Egyptian governorates, cities, landline and mobile area codes, and timezone utilities — with zero dependencies (uses Python standard library only).

[View on GitHub](https://github.com/InnoSoft-Company/egydata) | [View on PyPI](https://pypi.org/project/egydata/)

---

## Installation

```bash
pip install egydata
```

Quick Start

```python
from egydata import governorates, cities, phoneArea, timezone

# Get all governorates
all_govs = governorates.get_all()

# Find a city by name
maadi = cities.search("Maadi")

# Check current time in Egypt
now = timezone.now()
```

---

Usage

Governorates

```python
from egydata import governorates

# Get all 27 governorates
all_govs = governorates.get_all()
# [{'id': 1, 'code': 'CAI', 'name': 'القاهرة', 'nameEn': 'Cairo'}, ...]

# Find by code
cairo = governorates.get_by_code("CAI")
# {'id': 1, 'code': 'CAI', 'name': 'القاهرة', 'nameEn': 'Cairo'}

# Find by id
alex = governorates.get_by_id(2)
# {'id': 2, 'code': 'ALX', 'name': 'الإسكندرية', 'nameEn': 'Alexandria'}

# Search (Arabic, English, or code, partial match)
results = governorates.search("alex")
# [{'id': 2, 'code': 'ALX', 'name': 'الإسكندرية', 'nameEn': 'Alexandria'}]

ar_results = governorates.search("القاهرة")
# [{'id': 1, 'code': 'CAI', 'name': 'القاهرة', 'nameEn': 'Cairo'}]
```

Cities

```python
from egydata import cities

# Get cities by governorate code
cairo_cities = cities.get_by_governorate("CAI")
# [{'id': 1, 'name': 'مدينة نصر', 'nameEn': 'Nasr City', 'governorateCode': 'CAI'}, ...]

# Find by id
sharm = cities.get_by_id(131)
# {'id': 131, 'name': 'شرم الشيخ', 'nameEn': 'Sharm El Sheikh', 'governorateCode': 'SIS'}

# Search cities (Arabic or English, partial match)
found = cities.search("Maadi")
# [{'id': 3, 'name': 'المعادي', 'nameEn': 'Maadi', 'governorateCode': 'CAI'}]
```

Phone Area Codes

```python
from egydata import phoneArea

# Get all area codes (landline and mobile)
all_codes = phoneArea.get_all()
# [{'code': '010', 'region': 'ڤودافون', 'regionEn': 'Vodafone'}, ...]

# Look up region by code
region = phoneArea.get_region("03")
# {'code': '03', 'region': 'الإسكندرية', 'regionEn': 'Alexandria'}

# Find area code by region name (Arabic or English)
entry = phoneArea.get_code("Mansoura")
# {'code': '050', 'region': 'الدقهلية (المنصورة)', 'regionEn': 'Dakahlia (Mansoura)'}
```

Timezone

```python
from egydata import timezone

print(timezone.name)      # 'Africa/Cairo'
print(timezone.offset)    # '+02:00' (standard time offset)

now = timezone.now()      # current date/time in Egypt (timezone-aware datetime)
print(now.isoformat())

# Check if daylight saving time is active (Egypt resumed DST in 2023)
is_dst = timezone.isDST() # returns True if current offset is +03:00

# Optionally check a specific date
from datetime import datetime
date = datetime(2024, 8, 1)
print(timezone.isDST(date))  # True (during DST period)
```

---

API Reference

governorates

Method Parameters Returns Description
get_all() – list[Governorate] Returns all 27 Egyptian governorates.
get_by_code(code) code: str Governorate \| None Find governorate by its code (e.g., 'CAI').
get_by_id(id) id: int/str Governorate \| None Find governorate by its numeric ID.
search(query) query: str list[Governorate] Search by Arabic/English name or code (case‑insensitive, partial).

Governorate shape:
{'id': int, 'code': str, 'name': str, 'nameEn': str}

---

cities

Method Parameters Returns Description
get_by_governorate(gov_code) gov_code: str list[City] Get all cities in a governorate (by its code).
get_by_id(id) id: int/str City \| None Find city by its numeric ID.
search(query) query: str list[City] Search by Arabic or English name (partial, case‑insensitive).

City shape:
{'id': int, 'name': str, 'nameEn': str, 'governorateCode': str}

---

phoneArea

Method Parameters Returns Description
get_all() – list[AreaCode] Returns all landline and mobile area codes.
get_region(code) code: str AreaCode \| None Look up region info by area code.
get_code(region_name) region_name: str AreaCode \| None Find area code entry by region name (Arabic or English).

AreaCode shape:
{'code': str, 'region': str, 'regionEn': str}

---

timezone

Property / Method Returns Description
name 'Africa/Cairo' IANA timezone identifier.
offset '+02:00' Standard UTC offset (without DST).
now() datetime Current date and time in Egypt (timezone‑aware).
isDST(date=None) bool Whether DST is active (for given date or now).

---

Data Coverage

· 27 governorates with Arabic and English names and ISO‑like codes.
· 151 cities and districts across all governorates.
· 30 landline and mobile area codes (including mobile operators).
· Full timezone support for Africa/Cairo (DST‑aware).

All data is embedded in the package – no network requests, no external dependencies.

---

Requirements

· Python 3.9 or later (uses standard library zoneinfo; for Python 3.8 you may need the backports.zoneinfo package).

---

License

MIT

```