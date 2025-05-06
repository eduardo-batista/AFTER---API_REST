"""
tag_controller.py

This module contains the default REST structure of controllers for a CRUD tag object.
"""
from typing import Sequence
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.schema.tag_schema import UpdateTagRequest, TagResponse, CreateTagRequest
from api.src.service.tag_service import TagService
from api.infra.database.database import DatabaseConfig

tag_router = APIRouter(prefix='/tag',tags=["tag"])
database_config = DatabaseConfig()
service = TagService()

# GET /tag/{tag_id}
@tag_router.get('/{tag_id}', status_code=status.HTTP_200_OK)
async def get(
        tag_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> TagResponse | None:
    """Retrieves an 'Tag' object based on the provided ID."""
    return await service.get(tag_id, session)

# GET /tag
@tag_router.get('/', status_code=status.HTTP_200_OK)
async def get_all(
        session: AsyncSession = Depends(database_config.get_session)
    ) -> Sequence[TagResponse]:
    """Retrieves all 'Tag' objects."""
    return await service.get_all(session)

# POST /tag
@tag_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
        tag_request: CreateTagRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> TagResponse:
    """Creates a new 'Tag' object with the provided data."""
    return await service.create(tag_request.__get_entity__(), session)

# PUT /tag/{tag_id}
@tag_router.put('/{tag_id}', status_code=status.HTTP_200_OK)
async def update(
        tag_request: UpdateTagRequest,
        tag_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> TagResponse:
    """Updates an existing 'Tag' object with the provided data."""
    return await service.update(tag_request.__get_entity__(), tag_id, session)

# DELETE /tag/{tag_id}
@tag_router.delete('/{tag_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        tag_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> None:
    """Deletes an 'Tag' object based on the provided ID."""
    return await service.delete(tag_id, session)
