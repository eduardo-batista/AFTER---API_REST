"""
event_entity.py

This module defines the sqlalchemy class for event entity.
"""
from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseEntity

class Event(BaseEntity):
    """sqlalchemy class for event entity."""

    __tablename__ = 'events'

    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    image = Column(String(255), nullable=True)
    start = Column(Date(), nullable=False)
    end = Column(Date(), nullable=False)
    ticket_price = Column(Float(), nullable=True)
    host_id = Column(Integer(), ForeignKey("users.id", ondelete="RESTRICT"), nullable=False)
    space_id = Column(Integer(), ForeignKey("spaces.id", ondelete="RESTRICT"), nullable=False)
    host = relationship("User", back_populates="events")
    space = relationship("Space", back_populates="events")

    def __init__(self, 
                name = None, 
                description = None, 
                image = None, 
                start = None, 
                end = None, 
                ticket_price = None, 
                host_id = None, 
                host = None, 
                space_id = None, 
                space = None):
        name = name
        description = description
        image = image
        start = start
        end = end
        ticket_price = ticket_price
        host_id = host_id
        host = host
        space_id = space_id
        space = space

    def __repr__(self):
        return f"<EntityEvent: id=({self.id}), \
                name=({self.name}), \
                description=({self.description}), \
                image=({self.image}), \
                start=({self.start}), \
                end=({self.end}), \
                ticket_price=({self.ticket_price}), \
                host_id=({self.host_id}), \
                space_id=({self.space_id})>"
