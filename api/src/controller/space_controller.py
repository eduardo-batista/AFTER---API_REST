"""
space_controller.py

This module contains the default REST structure of controllers for a CRUD space object.
"""
from typing import Sequence
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.schema.space_schema import UpdateSpaceRequest, SpaceResponse, CreateSpaceRequest
from api.src.service.space_service import SpaceService
from api.infra.database.database import DatabaseConfig

space_router = APIRouter(prefix='/space',tags=["space"])
database_config = DatabaseConfig()
service = SpaceService()

# GET /space/{space_id}
@space_router.get('/{space_id}', status_code=status.HTTP_200_OK)
async def get(
        space_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> SpaceResponse | None:
    """Retrieves an 'Space' object based on the provided ID."""
    return await service.get(space_id, session)

# GET /space
@space_router.get('/', status_code=status.HTTP_200_OK)
async def get_all(
        session: AsyncSession = Depends(database_config.get_session)
    ) -> Sequence[SpaceResponse]:
    """Retrieves all 'Space' objects."""
    return await service.get_all(session)

# POST /space
@space_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
        space_request: CreateSpaceRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> SpaceResponse:
    """Creates a new 'Space' object with the provided data."""
    return await service.create(space_request.__get_entity__(), session)

# PUT /space/{space_id}
@space_router.put('/{space_id}', status_code=status.HTTP_200_OK)
async def update(
        space_request: UpdateSpaceRequest,
        space_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> SpaceResponse:
    """Updates an existing 'Space' object with the provided data."""
    return await service.update(space_request.__get_entity__(), space_id, session)

# DELETE /space/{space_id}
@space_router.delete('/{space_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        space_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> None:
    """Deletes an 'Space' object based on the provided ID."""
    return await service.delete(space_id, session)
