"""
event_repository.py

This module defines the sqlalchemy class for event repository.
"""
from typing import Sequence, Type
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from api.src.model.entity.event_entity import Event
from .base import BaseRepository

class EventRepository(BaseRepository[Event]):
    """class for event repository."""

    def __init__(self, entity: Type[Event]):
        super().__init__(entity)
    
    async def get(self, entity_id: int, session: AsyncSession) -> Event | None:
        """
        Retrieves an object based on the provided ID.

        Args:
        - entity_id (int): The ID of the object to retrieve.

        Returns:
        - The object with the provided ID.
        """
        try:
            query = select(self.entity)\
            .options(selectinload(self.entity.space), selectinload(self.entity.host))\
            .filter(getattr(self.entity, self.primary_key_name) == entity_id)
            
            result = await session.execute(query)
            return result.scalars().first()
        except Exception as e:
            raise HTTPException(500, f'Erro ao buscar o registro: {str(e)}')

    async def get_all(self, session: AsyncSession) -> Sequence[Event]:
        """
        Retrieves all objects.

        Returns:
        - List of objects.
        """
        try:
            query = select(self.entity)\
            .options(selectinload(self.entity.space), selectinload(self.entity.host))\
            .where(self.entity.active == True)
            
            result = await session.execute(query)
            return result.scalars().all()
        except Exception as e:
            raise HTTPException(500, f'Erro ao buscar o registros: {str(e)}')