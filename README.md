# Egydata

<!-- ==========================
     PyPI Badges
========================== -->
[![PyPI Version](https://img.shields.io/pypi/v/egydata.svg)](https://pypi.org/project/egydata/)
[![Python Versions](https://img.shields.io/pypi/pyversions/egydata.svg)](https://pypi.org/project/egydata/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/InnoSoft-Company/egydata/blob/main/LICENSE)
[![Downloads Today](https://img.shields.io/pypi/dt/egydata.svg)](https://pypi.org/project/egydata/)
[![Downloads Last Week](https://pepy.tech/badge/egydata/week)](https://pepy.tech/project/egydata)
[![Downloads Last Month](https://pepy.tech/badge/egydata/month)](https://pepy.tech/project/egydata)
[![Total Downloads](https://pepy.tech/badge/egydata)](https://pepy.tech/project/egydata)
[![PyPI Status](https://img.shields.io/pypi/status/egydata.svg)](https://pypi.org/project/egydata/)

<!-- ==========================
     GitHub Badges
========================== -->
[![GitHub stars](https://img.shields.io/github/stars/InnoSoft-Company/egydata.svg?style=social)](https://github.com/InnoSoft-Company/egydata)
[![GitHub forks](https://img.shields.io/github/forks/InnoSoft-Company/egydata.svg?style=social)](https://github.com/InnoSoft-Company/egydata)
[![GitHub issues](https://img.shields.io/github/issues/InnoSoft-Company/egydata.svg)](https://github.com/InnoSoft-Company/egydata/issues)
[![GitHub PRs](https://img.shields.io/github/issues-pr/InnoSoft-Company/egydata.svg)](https://github.com/InnoSoft-Company/egydata/pulls)
[![GitHub last commit](https://img.shields.io/github/last-commit/InnoSoft-Company/egydata.svg)](https://github.com/InnoSoft-Company/egydata/commits/main)
[![GitHub contributors](https://img.shields.io/github/contributors/InnoSoft-Company/egydata.svg)](https://github.com/InnoSoft-Company/egydata/graphs/contributors)
[![GitHub license](https://img.shields.io/github/license/InnoSoft-Company/egydata.svg)](https://github.com/InnoSoft-Company/egydata/blob/main/LICENSE)

<!-- ==========================
     CI / Testing / Coverage
========================== -->
[![Build Status](https://github.com/InnoSoft-Company/egydata/actions/workflows/python-package.yml/badge.svg)](https://github.com/InnoSoft-Company/egydata/actions)
[![Coverage](https://img.shields.io/codecov/c/github/InnoSoft-Company/egydata/main.svg)](https://codecov.io/gh/InnoSoft-Company/egydata)
[![Code Quality: Python](https://img.shields.io/lgtm/grade/python/g/InnoSoft-Company/egydata.svg)](https://lgtm.com/projects/g/InnoSoft-Company/egydata)
[![Typing](https://img.shields.io/badge/typing-strict-brightgreen.svg)](https://github.com/InnoSoft-Company/egydata)

<!-- ==========================
     Install / Social
========================== -->
[![Install via pip](https://img.shields.io/badge/pip-install-blue.svg)](https://pypi.org/project/egydata/)
[![Follow on GitHub](https://img.shields.io/badge/github-follow-blue.svg)](https://github.com/InnoSoft-Company/egydata)

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
from egydata import governorates, cities, phoneAreas, timezones

# Get all governorates
all_govs = governorates.get_all()

# Find a city by name
maadi = cities.search("Maadi")

# Check current time in Egypt
now = timezones.now()
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
from egydata import phoneAreas

# Get all area codes (landline and mobile)
all_codes = phoneAreas.get_all()
# [{'code': '010', 'region': 'ڤودافون', 'regionEn': 'Vodafone'}, ...]

# Look up region by code
region = phoneAreas.get_region("03")
# {'code': '03', 'region': 'الإسكندرية', 'regionEn': 'Alexandria'}

# Find area code by region name (Arabic or English)
entry = phoneAreas.get_code("Mansoura")
# {'code': '050', 'region': 'الدقهلية (المنصورة)', 'regionEn': 'Dakahlia (Mansoura)'}
```

Timezone

```python
from egydata import timezones

print(timezones.name)      # 'Africa/Cairo'
print(timezones.offset)    # '+02:00' (standard time offset)

now = timezones.now()      # current date/time in Egypt (timezone-aware datetime)
print(now.isoformat())

# Check if daylight saving time is active (Egypt resumed DST in 2023)
is_dst = timezones.isDST() # returns True if current offset is +03:00

# Optionally check a specific date
from datetime import datetime
date = datetime(2024, 8, 1)
print(timezones.isDST(date))  # True (during DST period)
```

---


API Reference

governorates

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Parameters</th>
      <th>Returns</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>get_all()</td>
      <td>–</td>
      <td>list&lt;Governorate&gt;</td>
      <td>Returns all 27 Egyptian governorates.</td>
    </tr>
    <tr>
      <td>get_by_code(code)</td>
      <td>code: str</td>
      <td>Governorate | None</td>
      <td>Find governorate by its code (e.g., 'CAI').</td>
    </tr>
    <tr>
      <td>get_by_id(id)</td>
      <td>id: int/str</td>
      <td>Governorate | None</td>
      <td>Find governorate by its numeric ID.</td>
    </tr>
    <tr>
      <td>search(query)</td>
      <td>query: str</td>
      <td>list&lt;Governorate&gt;</td>
      <td>Search by Arabic/English name or code (case‑insensitive, partial).</td>
    </tr>
  </tbody>
</table>

Governorate shape:
{'id': int, 'code': str, 'name': str, 'nameEn': str}

---

cities

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Parameters</th>
      <th>Returns</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>get_by_governorate(gov_code)</td>
      <td>gov_code: str</td>
      <td>list&lt;City&gt;</td>
      <td>Get all cities in a governorate (by its code).</td>
    </tr>
    <tr>
      <td>get_by_id(id)</td>
      <td>id: int/str</td>
      <td>City | None</td>
      <td>Find city by its numeric ID.</td>
    </tr>
    <tr>
      <td>search(query)</td>
      <td>query: str</td>
      <td>list&lt;City&gt;</td>
      <td>Search by Arabic or English name (partial, case‑insensitive).</td>
    </tr>
  </tbody>
</table>

City shape:
{'id': int, 'name': str, 'nameEn': str, 'governorateCode': str}

---

phoneArea

<table>
  <thead>
    <tr>
      <th>Method</th>
      <th>Parameters</th>
      <th>Returns</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>get_all()</td>
      <td>–</td>
      <td>list&lt;AreaCode&gt;</td>
      <td>Returns all landline and mobile area codes.</td>
    </tr>
    <tr>
      <td>get_region(code)</td>
      <td>code: str</td>
      <td>AreaCode | None</td>
      <td>Look up region info by area code.</td>
    </tr>
    <tr>
      <td>get_code(region_name)</td>
      <td>region_name: str</td>
      <td>AreaCode | None</td>
      <td>Find area code entry by region name (Arabic or English).</td>
    </tr>
  </tbody>
</table>

AreaCode shape:
{'code': str, 'region': str, 'regionEn': str}

---

timezone

<table>
  <thead>
    <tr>
      <th>Property / Method</th>
      <th>Returns</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>name</td>
      <td>'Africa/Cairo'</td>
      <td>IANA timezone identifier.</td>
    </tr>
    <tr>
      <td>offset</td>
      <td>'+02:00'</td>
      <td>Standard UTC offset (without DST).</td>
    </tr>
    <tr>
      <td>now()</td>
      <td>datetime</td>
      <td>Current date and time in Egypt (timezone‑aware).</td>
    </tr>
    <tr>
      <td>isDST(date=None)</td>
      <td>bool</td>
      <td>Whether DST is active (for given date or now).</td>
    </tr>
  </tbody>
</table>

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

MIT - InnoSoft Company

```