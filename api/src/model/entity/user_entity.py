"""
user_entity.py

This module defines the sqlalchemy class for user entity.
"""
from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship


from .base import BaseEntity
from .associations import event_tags, attendance_confirmations
class User(BaseEntity):
    """sqlalchemy class for user entity."""

    __tablename__ = 'users'

    supabase_id = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    identification_document = Column(String(20), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    fone = Column(String(20), nullable=True)
    profile_type = Column(Enum('user', 'admin', name='profile_type_enum'), nullable=False)
    spaces = relationship("Space", back_populates="owner")
    events = relationship("Event", back_populates="host")
    reviews = relationship("EventReview", back_populates="user")
    attendance_confirmations = relationship("Tag", secondary=attendance_confirmations, back_populates="events")

    def __init__(self, name = None, description = None, identification_document = None, email = None, fone = None, profile_type = None):
        self.name = name
        self.description = description
        self.identification_document = identification_document
        self.email = email
        self.fone = fone
        self.profile_type = profile_type

    def __repr__(self):
        return f"<EntityUser: id=({self.id}), \
                supabase_id=({self.supabase_id}), \
                name=({self.name}), \
                description=({self.description}), \
                identification_document=({self.identification_document}), \
                email=({self.email}), \
                fone=({self.fone}), \
                profile_type=({self.profile_type}), \
                fone=({self.created_at}), \
                profile_type=({self.updated_at})>"
