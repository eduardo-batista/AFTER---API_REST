"""
tag_entity.py

This module defines the sqlalchemy class for tag entity.
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .base import BaseEntity
from .associations import event_tags

class Tag(BaseEntity):
    """sqlalchemy class for tag entity."""

    __tablename__ = 'tags'

    label = Column(String(50), nullable=False)
    events = relationship("Event", secondary=event_tags, back_populates="tags")

    def __init__(self, 
                label = None):
        self.label = label

    def __repr__(self):
        return f"<EntityTag: id=({self.id}), \
                label=({self.label})>"
