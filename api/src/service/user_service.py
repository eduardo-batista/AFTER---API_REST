"""
user_service.py

This module defines the sqlalchemy class for user service.
"""
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.entity.user_entity import User
from api.src.model.schema.user_schema import CreateUserWithPasswordRequest, UserLoginRequest, UserResponse
from api.src.repository.user_repository import UserRepository
from api.src.service.auth_service import AuthService
from .base import BaseService

class UserService(BaseService[UserRepository, User, UserResponse]):
    """class for user service."""

    def __init__(self):
        self.auth_service = AuthService()
        super().__init__(UserRepository, User, UserResponse)

    async def login(self, user_login_request: UserLoginRequest, session: AsyncSession):
        token = await self.auth_service.login_user(user_login_request.email, user_login_request.password)
        user = await self.repository.get_by_email(user_login_request.email, session)
        return {
            'user': user,
            'acess_token': token
        }

    async def create(self, user: CreateUserWithPasswordRequest, session: AsyncSession) -> UserResponse:
        """
        Creates a new object with the provided data.

        Args:
        - user: Data to create the new object.

        Returns:
        - The newly created object.
        """
        supabase_id = await self.auth_service.register_user(user.__getattribute__('email'), user.__getattribute__('password'))

        obj_in = user.__get_entity__()
        obj_in.__setattr__('supabase_id', supabase_id)

        entity = await self.repository.create(obj_in, session)
        return self.schema.model_validate(entity)
