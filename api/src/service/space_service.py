"""
space_service.py

This module defines the sqlalchemy class for space service.
"""
from api.src.model.entity.space_entity import Space
from api.src.model.schema.space_schema import SpaceResponse
from api.src.repository.space_repository import SpaceRepository
from .base import BaseService

class SpaceService(BaseService[SpaceRepository, Space, SpaceResponse]):
    """class for space service."""

    def __init__(self):
        super().__init__(SpaceRepository, Space, SpaceResponse)
