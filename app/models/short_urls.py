from mongoengine.fields import Document, URLField, StringField, DateTimeField ,IntField
from datetime import datetime
from zoneinfo import ZoneInfo
from config import Config


class URL(Document):
    origin_url = URLField(max_length=255)
    short_url = StringField(max_length=20)
    total_visit = IntField(default=0 , min_value=0)
    created_at = DateTimeField(default=datetime.now(ZoneInfo(Config.TIME_ZONE)))
