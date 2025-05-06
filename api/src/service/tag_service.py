"""
tag_service.py

This module defines the sqlalchemy class for tag service.
"""
from api.src.model.entity.tag_entity import Tag
from api.src.model.schema.tag_schema import TagResponse
from api.src.repository.tag_repository import TagRepository
from .base import BaseService

class TagService(BaseService[TagRepository, Tag, TagResponse]):
    """class for tag service."""

    def __init__(self):
        super().__init__(TagRepository, Tag, TagResponse)
