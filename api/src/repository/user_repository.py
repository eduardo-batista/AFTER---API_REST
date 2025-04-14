"""
user_repository.py

This module defines the sqlalchemy class for user repository.
"""
from typing import Type
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from api.src.model.entity.user_entity import User
from .base import BaseRepository


class UserRepository(BaseRepository[User]):
    """class for user repository."""

    def __init__(self, entity: Type[User]):
        super().__init__(entity)

    async def get_by_email(self, email: str, session: AsyncSession) -> User:
        """
        Retrieves an user based on the provided email.

        Args:
        - email (str): The email of the user to retrieve.

        Returns:
        - The user with the provided email.
        """
        query = select(self.entity).filter(self.entity.email == email)
        result = await session.execute(query)
        user = result.scalars().first()
        if not user:
            raise HTTPException(404, f'Não foi encontrado um usuário com este email.')
        return user

    async def login(self, login_parameters: dict,  session: AsyncSession):
        pass
