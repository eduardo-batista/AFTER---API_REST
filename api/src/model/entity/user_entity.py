"""
user_entity.py

This module defines the sqlalchemy class for user entity.
"""
from sqlalchemy import TIMESTAMP, Boolean, Column, Enum, String, text
from .base import BaseEntity

class User(BaseEntity):
    """sqlalchemy class for user entity."""

    __tablename__ = 'users'

    name = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    identification_document = Column(String(20), nullable=False, unique=True)
    email = Column(String(20), nullable=False, unique=True)
    fone = Column(String(20), nullable=True)
    profile_type = Column(Enum('user', 'admin', name='profile_type_enum'), nullable=False)
    status = Column(Boolean, nullable=False, server_default='TRUE')
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))

    def __init__(self, name, description, identification_document, email, fone, profile_type):
        self.name = name
        self.description = description
        self.identification_document = identification_document
        self.email = email
        self.fone = fone
        self.profile_type = profile_type

    def __repr__(self):
        return f"<EntityUser: id=({self.id}), \
                name=({self.name}), \
                description=({self.description}), \
                identification_document=({self.identification_document}), \
                email=({self.email}), \
                fone=({self.fone}), \
                profile_type=({self.profile_type}), \
                email=({self.status}), \
                fone=({self.created_at}), \
                profile_type=({self.updated_at})>"
