"""
Base Repository Module

This Repository defines the base class for all repositories.
"""
from typing import Sequence, Type, TypeVar, Generic
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy import select

from api.src.model.entity.base import BaseEntity

T = TypeVar('T', bound=BaseEntity)

class BaseRepository(Generic[T]):
    """Base class for all repositories."""

    def __init__(self, entity: Type[T]):
        self.entity = entity
        self.primary_key_name = self._get_primary_key_name()

    def _get_primary_key_name(self):
        """
        Retrieves the name of the primary key of the entity.

        This method uses SQLAlchemy's ORM to inspect the entity and 
        retrieve the name of its primary key.

        Returns:
            str: The name of the primary key for the entity.

        Example:
            primary_key_name = self._get_primary_key_name()
        """
        mapper = self.entity.__mapper__
        primary_key = mapper.primary_key[0]
        return primary_key.name

    async def get(self, entity_id: int, session: AsyncSession) -> T | None:
        """
        Retrieves an object based on the provided ID.

        Args:
        - entity_id (int): The ID of the object to retrieve.

        Returns:
        - The object with the provided ID.
        """
        query = select(self.entity).filter(getattr(self.entity, self.primary_key_name) == entity_id)
        
        result = await session.execute(query)
        return result.scalars().first()

    async def get_all(self, session: AsyncSession) -> Sequence[T]:
        """
        Retrieves all objects.

        Returns:
        - List of objects.
        """
        query = select(self.entity).where(self.entity.active == True)
        
        result = await session.execute(query)
        return result.scalars().all()

    async def create(self, obj_in: T, session: AsyncSession) -> T:
        """
        Creates a new object with the provided data.

        Args:
        - obj_in: Data to create the new object.

        Returns:
        - The newly created object.
        """
        
        session.add(obj_in)
        await session.commit()
        await session.refresh(obj_in)
        return obj_in

    async def update(self, obj_in: T, entity_id: int, session: AsyncSession) -> T:
        """
        Updates an existing object with the provided data.

        Args:
        - obj_in: Data to update the object.
        - entity_id (int): The ID of the object to update.

        Returns:
        - The updated object.
        """
        
        query = select(self.entity).filter(
            getattr(self.entity, self.primary_key_name) == entity_id
        )
        result = await session.execute(query)
        obj = result.scalars().first()

        if not obj:
            raise HTTPException(404, f'Não foi encontrado um registro com ID: {entity_id}.')

        for key, value in obj_in.to_dict().items():
            if key != self.primary_key_name and value:
                setattr(obj, key, value)
        await session.commit()
        await session.refresh(obj)
        return obj

    async def soft_delete(self, entity_id: int, session: AsyncSession) -> None:
        """
        Deactivate an object based on the provided ID.

        Args:
        - entity_id (int): The ID of the object to delete.

        Returns:
        - No content.
        """
        
        query = select(self.entity).filter(
            getattr(self.entity, self.primary_key_name) == entity_id
        )
        result = await session.execute(query)
        obj = result.scalars().first()

        if not obj:
            raise HTTPException(404, f'Não foi encontrado um registro com ID: {entity_id}.')

        if obj:
            obj.active = False
            await session.commit()

    async def delete(self, entity_id: int, session: AsyncSession) -> None:
        """
        Destroy an object based on the provided ID.

        Args:
        - entity_id (int): The ID of the object to delete.

        Returns:
        - No content.
        """
        
        query = select(self.entity).filter(
            getattr(self.entity, self.primary_key_name) == entity_id
        )
        result = await session.execute(query)
        obj = result.scalars().first()

        if not obj:
            raise HTTPException(404, f'Não foi encontrado um registro com ID: {entity_id}.')

        if obj:
            await session.delete(obj)
            await session.commit()
