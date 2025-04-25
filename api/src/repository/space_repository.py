"""
space_repository.py

This module defines the sqlalchemy class for space repository.
"""
from typing import Type
from api.src.model.entity.space_entity import Space
from .base import BaseRepository


class SpaceRepository(BaseRepository[Space]):
    """class for space repository."""

    def __init__(self, entity: Type[Space]):
        super().__init__(entity)