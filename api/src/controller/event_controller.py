"""
event_controller.py

This module contains the default REST structure of controllers for a CRUD event object.
"""
from typing import Sequence
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.schema.event_schema import EventWithRelationshipsResponse, UpdateEventRequest, EventResponse, CreateEventRequest
from api.src.service.event_service import EventService
from api.infra.database.database import DatabaseConfig

event_router = APIRouter(prefix='/event',tags=["event"])
database_config = DatabaseConfig()
service = EventService()

# GET /event/{event_id}
@event_router.get('/{event_id}', status_code=status.HTTP_200_OK)
async def get(
        event_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> EventWithRelationshipsResponse | None:
    """Retrieves an 'Event' object based on the provided ID."""
    return await service.get(event_id, session)

# GET /event
@event_router.get('/', status_code=status.HTTP_200_OK)
async def get_all(
        session: AsyncSession = Depends(database_config.get_session)
    ) -> Sequence[EventWithRelationshipsResponse]:
    """Retrieves all 'Event' objects."""
    return await service.get_all(session)

# POST /event
@event_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
        event_request: CreateEventRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> EventResponse:
    """Creates a new 'Event' object with the provided data."""
    return await service.create(event_request, session)

# PUT /event/{event_id}
@event_router.put('/{event_id}', status_code=status.HTTP_200_OK)
async def update(
        event_request: UpdateEventRequest,
        event_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> EventResponse:
    """Updates an existing 'Event' object with the provided data."""
    return await service.update(event_request, event_id, session)

# DELETE /event/{event_id}
@event_router.delete('/{event_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        event_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> None:
    """Deletes an 'Event' object based on the provided ID."""
    return await service.delete(event_id, session)
