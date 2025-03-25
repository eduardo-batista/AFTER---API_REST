"""
user_repository.py

This module defines the sqlalchemy class for user repository.
"""
from typing import Type

from api.src.model.entity.user_entity import User
from .base import BaseRepository


class UserRepository(BaseRepository[User]):
    """class for user repository."""

    def __init__(self, entity: Type[User]):
        super().__init__(entity)
