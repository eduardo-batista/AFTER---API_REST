"""
user_service.py

This module defines the sqlalchemy class for user service.
"""
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.entity.user_auth_entity import UserAuth
from api.src.model.entity.user_entity import User
from api.src.model.schema.user_schema import UserLoginRequest, UserResponse
from api.src.repository.user_repository import UserRepository
from .base import BaseService

class UserService(BaseService[UserRepository, User, UserResponse]):
    """class for user service."""

    def __init__(self):
        super().__init__(UserRepository, User, UserResponse)

    async def login(self, user_login_request: UserLoginRequest, session: AsyncSession):
        return self.repository.login(user_login_request, session)
    
    async def register(self, user_auth: UserAuth, session: AsyncSession):
        return await self.repository.create(user_auth.user, session)
