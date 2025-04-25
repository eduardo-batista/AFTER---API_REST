"""
user_controller.py

This module contains the default REST structure of controllers for a CRUD user object.
"""
from typing import Sequence
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.src.model.schema.user_schema import UpdateUserRequest, UserLoginRequest, UserResponse, CreateUserWithPasswordRequest
from api.src.service.user_service import UserService
from api.infra.database.database import DatabaseConfig

user_router = APIRouter(prefix='/user',tags=["user"])
database_config = DatabaseConfig()
service = UserService()

# POST /login
@user_router.post('/login', status_code=status.HTTP_201_CREATED)
async def login(
        user_login_request: UserLoginRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ):
    """Authenticate user on the plataform."""
    return await service.login(user_login_request, session)

# GET /user/{user_id}
@user_router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get(
        user_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> UserResponse | None:
    """Retrieves an 'User' object based on the provided ID."""
    return await service.get(user_id, session)

# GET /user
@user_router.get('/', status_code=status.HTTP_200_OK)
async def get_all(
        session: AsyncSession = Depends(database_config.get_session)
    ) -> Sequence[UserResponse]:
    """Retrieves all 'User' objects."""
    return await service.get_all(session)

# POST /user
@user_router.post('/', status_code=status.HTTP_201_CREATED)
async def create(
        user_request: CreateUserWithPasswordRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> UserResponse:
    """Creates a new 'User' object with the provided data."""
    return await service.create(user_request.__get_entity__(), user_request.password, session)

# PUT /user/{user_id}
@user_router.put('/{user_id}', status_code=status.HTTP_200_OK)
async def update(
        user_request: UpdateUserRequest,
        user_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> UserResponse:
    """Updates an existing 'User' object with the provided data."""
    return await service.update(user_request.__get_entity__(), user_id, session)

# DELETE /user/{user_id}
@user_router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(
        user_id: int, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> None:
    """Deletes an 'User' object based on the provided ID."""
    return await service.delete(user_id, session)
