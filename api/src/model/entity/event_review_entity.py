"""
event_review_entity.py

This module defines the sqlalchemy class for event_review entity.
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseEntity

class EventReview(BaseEntity):
    """sqlalchemy class for event_review entity."""

    __tablename__ = 'event_reviews'

    rating = Column(Integer(), nullable=False)
    comment = Column(String(255), nullable=True)
    user_id = Column(Integer(), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    event_id = Column(Integer(), ForeignKey("events.id", ondelete="CASCADE"), nullable=False)
    reviewer = relationship("User", back_populates="reviews")
    event = relationship("Event", back_populates="reviews")

    def __init__(self, 
                rating = None,
                comment = None,
                user_id = None,
                event_id = None):
        self.rating = rating
        self.comment = comment
        self.user_id = user_id
        self.event_id = event_id

    def __repr__(self):
        return f"<EntityEventReview: id=({self.id}), \
                rating=({self.rating}), \
                comment=({self.comment}), \
                user_id=({self.user_id}), \
                event_id=({self.event_id})>"
