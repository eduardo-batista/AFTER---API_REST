"""
user_controller.py

This module contains the default REST structure of controllers for a CRUD user object.
"""
from typing import Sequence
from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from api.database.database import DatabaseConfig
from api.src.model.schema.user_schema import CreateUserAuthRequest, UpdateUserRequest, UserLoginRequest, UserResponse, CreateUserRequest
from api.src.service.user_service import UserService

user_router = APIRouter(prefix='/user')
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

# POST /register
@user_router.post('/register', status_code=status.HTTP_201_CREATED)
async def register(
        user_auth_request: CreateUserAuthRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ):
    """Creates a new 'User Auth' and 'User' object with the provided data."""
    return await service.register(user_auth_request.__get_entity__(), session)

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
        user_request: CreateUserRequest, 
        session: AsyncSession = Depends(database_config.get_session)
    ) -> UserResponse:
    """Creates a new 'User' object with the provided data."""
    return await service.create(user_request.__get_entity__(), session)

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
