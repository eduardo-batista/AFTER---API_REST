from sqlalchemy import Column, ForeignKey, Integer, Table
from .base import BaseEntity

event_tags = Table(
    "event_tags",
    BaseEntity.metadata,
    Column("event_id", Integer, ForeignKey("events.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
)
