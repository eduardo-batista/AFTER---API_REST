"""
example_controller.py

This module contains the default REST structure of controllers for a CRUD example object.
"""
from typing import Sequence
from fastapi import APIRouter, status

from api.src.model.schema.example_schema import ExampleSchema
from api.src.service.example_service import ExampleService

example_router = APIRouter(prefix='/example')
service = ExampleService()

# GET /example/{example_id}
@example_router.get('/{example_id}', status_code=status.HTTP_200_OK)
async def get(example_id: int) -> ExampleSchema | None:
    """Retrieves an 'Example' object based on the provided ID."""
    return await service.get(example_id)

# GET /example
@example_router.get('/', status_code=status.HTTP_200_OK)
async def get_all() -> Sequence[ExampleSchema]:
    """Retrieves all 'Example' objects."""
    return await service.get_all()

# POST /example
@example_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(example_request: ExampleSchema) -> ExampleSchema:
    """Creates a new 'Example' object with the provided data."""
    return await service.create(example_request.__get_entity__())

# PUT /example/{example_id}
@example_router.put('/{example_id}', status_code=status.HTTP_200_OK)
async def update(example_request: ExampleSchema, example_id: int) -> ExampleSchema:
    """Updates an existing 'Example' object with the provided data."""
    return await service.update(example_request.__get_entity__(), example_id)

# DELETE /example/{example_id}
@example_router.delete('/{example_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(example_id: int) -> None:
    """Deletes an 'Example' object based on the provided ID."""
    return await service.delete(example_id)
