"""
space_entity.py

This module defines the sqlalchemy class for space entity.
"""
from sqlalchemy import DECIMAL, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseEntity

class Space(BaseEntity):
    """sqlalchemy class for space entity."""

    __tablename__ = 'spaces'

    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
    latitude = Column(DECIMAL, nullable=False)
    longitude = Column(DECIMAL, nullable=False)
    host_id = Column(Integer(), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    owner = relationship("User", back_populates="spaces")
    events = relationship("Event", back_populates="space")

    def __init__(self, 
                name = None,
                description = None,
                image = None,
                latitude = None,
                longitude = None,
                host_id = None):
        self.name = name
        self.description = description
        self.image = image
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id

    def __repr__(self):
        return f"<EntitySpace: id=({self.id}), \
                name=({self.name}), \
                description=({self.description}), \
                image=({self.image}), \
                latitude=({self.latitude}), \
                longitude=({self.longitude}), \
                host_id=({self.host_id})>"
