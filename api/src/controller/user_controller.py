"""
user_controller.py

This module contains the default REST structure of controllers for a CRUD user object.
"""
from typing import Sequence
from fastapi import APIRouter, status

from api.src.model.schema.user_schema import UpdateUserRequest, UserResponse, CreateUserRequest
from api.src.service.user_service import UserService

user_router = APIRouter(prefix='/user')
service = UserService()

# GET /user/{user_id}
@user_router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get(user_id: int) -> UserResponse | None:
    """Retrieves an 'User' object based on the provided ID."""
    return await service.get(user_id)

# GET /user
@user_router.get('/', status_code=status.HTTP_200_OK)
async def get_all() -> Sequence[UserResponse]:
    """Retrieves all 'User' objects."""
    return await service.get_all()

# POST /user
@user_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(user_request: CreateUserRequest) -> UserResponse:
    """Creates a new 'User' object with the provided data."""
    return await service.create(user_request.__get_entity__())

# PUT /user/{user_id}
@user_router.put('/{user_id}', status_code=status.HTTP_200_OK)
async def update(user_request: UpdateUserRequest, user_id: int) -> UserResponse:
    """Updates an existing 'User' object with the provided data."""
    return await service.update(user_request.__get_entity__(), user_id)

# DELETE /user/{user_id}
@user_router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(user_id: int) -> None:
    """Deletes an 'User' object based on the provided ID."""
    return await service.delete(user_id)
