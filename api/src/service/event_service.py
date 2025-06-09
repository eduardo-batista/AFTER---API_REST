"""
event_service.py

This module defines the sqlalchemy class for event service.
"""
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.entity.event_entity import Event
from api.src.model.schema.event_schema import EventResponse, EventWithRelationshipsResponse
from api.src.repository.event_repository import EventRepository
from .base import BaseService

class EventService(BaseService[EventRepository, Event, EventResponse]):
    """class for event service."""

    def __init__(self):
        super().__init__(EventRepository, Event, EventResponse)


    async def get(self, entity_id: int, session: AsyncSession) -> EventWithRelationshipsResponse | None:
        """
        Retrieves an object based on the provided ID.

        Args:
        - entity_id (int): The ID of the object to retrieve.

        Returns:
        - The object with the provided ID.
        """
        entity = await self.repository.get(entity_id, session)
        if entity is None:
            return None
        return EventWithRelationshipsResponse.model_validate(entity)

    async def get_all(self, session: AsyncSession) -> List[EventWithRelationshipsResponse]:
        """
        Retrieves all objects.

        Returns:
        - List of objects.
        """
        entities = await self.repository.get_all(session)
        return [EventWithRelationshipsResponse.model_validate(entity) for entity in entities]