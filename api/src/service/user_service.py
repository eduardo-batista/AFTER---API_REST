"""
user_service.py

This module defines the sqlalchemy class for user service.
"""
from api.src.model.entity.user_entity import User
from api.src.model.schema.user_schema import UserResponse
from api.src.repository.user_repository import UserRepository
from .base import BaseService

class UserService(BaseService[UserRepository, User, UserResponse]):
    """class for user service."""

    def __init__(self):
        super().__init__(UserRepository, User, UserResponse)
