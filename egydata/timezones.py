from datetime import datetime
from zoneinfo import ZoneInfo

name = "Africa/Cairo"
offset = "+02:00"

def now(): return datetime.now(ZoneInfo(name))

def isDST(date=None):
  if date is None: date = datetime.now()
  if date.tzinfo is None: date = date.replace(tzinfo=ZoneInfo(name))
  else: date = date.astimezone(ZoneInfo(name))
  offset_minutes = date.utcoffset().total_seconds() / 60
  return offset_minutes == 180
