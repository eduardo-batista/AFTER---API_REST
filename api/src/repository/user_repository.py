"""
user_repository.py

This module defines the sqlalchemy class for user repository.
"""
from typing import Type
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.entity.user_auth_entity import UserAuth
from api.src.model.entity.user_entity import User
from api.src.model.schema.user_schema import UserLoginRequest
from .base import BaseRepository


class UserRepository(BaseRepository[User]):
    """class for user repository."""

    def __init__(self, entity: Type[User]):
        super().__init__(entity)

    async def login(self, user_login_request: UserLoginRequest, session: AsyncSession):
        pass
    
    async def register(self, user_auth: UserAuth, session: AsyncSession):
        pass
