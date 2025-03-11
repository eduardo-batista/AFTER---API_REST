"""
user_entity.py

This module defines the sqlalchemy class for user entity.
"""
from sqlalchemy import Column, String
from .base import BaseEntity

class User(BaseEntity):
    """sqlalchemy class for user entity."""

    __tablename__ = 'entity_user'

    user_field = Column(String(45))

    def __init__(self, user_field):
        self.user_field = user_field

    def __repr__(self):
        return f"<EntityUser(id={self.id}, user_field=({self.user_field})>"
