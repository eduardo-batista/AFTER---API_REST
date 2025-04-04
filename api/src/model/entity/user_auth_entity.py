"""
user_entity.py

This module defines the sqlalchemy class for user entity.
"""
from sqlalchemy import TIMESTAMP, Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseEntity


class UserAuth(BaseEntity):
    """sqlalchemy class for user entity."""

    __tablename__ = 'user_auth'

    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    auth_type = Column(Enum('password', 'google', 'apple', name='auth_type_enum'), nullable=False)
    password = Column(String(20), nullable=True)
    auth_token = Column(String(20), nullable=True)
    refresh_token = Column(String(20), nullable=True)
    user = relationship("User", back_populates="user_auth")

    def __init__(self,
                    user,
                    auth_type,
                    password=None,
                    auth_token=None,
                    refresh_token=None):
        self.user = user
        self.auth_type = auth_type
        self.password = password
        self.auth_token = auth_token
        self.refresh_token = refresh_token

    def __repr__(self):
        return f"<EntityUserAuth: user_id={self.user_id},\
                auth_type={self.auth_type},\
                password={self.password},\
                auth_token={self.auth_token},\
                refresh_token={self.refresh_token}>"
