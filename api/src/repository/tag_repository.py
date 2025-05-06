"""
tag_repository.py

This module defines the sqlalchemy class for tag repository.
"""
from typing import Type
from api.src.model.entity.tag_entity import Tag
from .base import BaseRepository


class TagRepository(BaseRepository[Tag]):
    """class for tag repository."""

    def __init__(self, entity: Type[Tag]):
        super().__init__(entity)