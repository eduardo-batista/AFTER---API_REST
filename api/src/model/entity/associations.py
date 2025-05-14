from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey, Integer, Table, text
from .base import BaseEntity

event_tags = Table(
    "event_tags",
    BaseEntity.metadata,
    Column("event_id", Integer, ForeignKey("events.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
    Column("active", Boolean, nullable=False, server_default='TRUE'),
    Column("created_at", TIMESTAMP, server_default=text('CURRENT_TIMESTAMP')),
    Column("updated_at", TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
)

attendance_confirmations = Table(
    "attendance_confirmations",
    BaseEntity.metadata,
    Column("event_id", Integer, ForeignKey("events.id", ondelete="CASCADE"), primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("active", Boolean, nullable=False, server_default='TRUE'),
    Column("created_at", TIMESTAMP, server_default=text('CURRENT_TIMESTAMP')),
    Column("updated_at", TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))
)
