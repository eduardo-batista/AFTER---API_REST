"""
user_service.py

This module defines the sqlalchemy class for user service.
"""
from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.entity.user_auth_entity import UserAuth
from api.src.model.entity.user_entity import User
from api.src.model.schema.user_schema import UserLoginRequest, UserResponse
from api.src.repository.user_repository import UserRepository
from api.utils.auth import Auth
from .base import BaseService

class UserService(BaseService[UserRepository, User, UserResponse]):
    """class for user service."""

    def __init__(self):
        super().__init__(UserRepository, User, UserResponse)

    async def login(self, user_login_request: UserLoginRequest, session: AsyncSession):
        try:
            user = await self.repository.get_by_email(user_login_request.email, session)

            if not await Auth.verify_password(user_login_request.password, user.user_auth[0].password):
                raise HTTPException(403, f'Senha incorreta.')
            
            login_parameters = {
                'auth_token': Auth.create_access_token(user.user_auth[0].id),
                'refresh_token': Auth.create_access_token(user.user_auth[0].id),
                'last_access': datetime.now()
            }

            return await self.repository.login(user.user_auth[0], login_parameters, session)
        except HTTPException as e:
            if e.status_code in {403, 404}:  
                raise HTTPException(403, "Email ou senha incorretos.")
            raise e
    
    async def register(self, user_auth: UserAuth, session: AsyncSession):
        return await self.repository.create(user_auth.user, session)
