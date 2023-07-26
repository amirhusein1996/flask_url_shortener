from mongoengine.fields import Document, URLField, StringField, DateTimeField
from datetime import datetime
from zoneinfo import ZoneInfo
from config import time_zone


class URL(Document):
    origin_url = URLField(max_length=255)
    short_url = StringField(max_length=20)
    created_at = DateTimeField(default=datetime.now(ZoneInfo(time_zone)))
