"""
event_service.py

This module defines the sqlalchemy class for event service.
"""
from api.src.model.entity.event_entity import Event
from api.src.model.schema.event_schema import EventResponse
from api.src.repository.event_repository import EventRepository
from .base import BaseService

class EventService(BaseService[EventRepository, Event, EventResponse]):
    """class for event service."""

    def __init__(self):
        super().__init__(EventRepository, Event, EventResponse)
