"""
event_repository.py

This module defines the sqlalchemy class for event repository.
"""
from typing import Type
from api.src.model.entity.event_entity import Event
from .base import BaseRepository


class EventRepository(BaseRepository[Event]):
    """class for event repository."""

    def __init__(self, entity: Type[Event]):
        super().__init__(entity)