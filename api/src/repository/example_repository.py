"""
example_repository.py

This module defines the sqlalchemy class for example repository.
"""
from typing import Type

from api.src.model.entity.example_entity import Example
from .base import BaseRepository


class ExampleRepository(BaseRepository[Example]):
    """class for example repository."""

    def __init__(self, entity: Type[Example]):
        super().__init__(entity)
