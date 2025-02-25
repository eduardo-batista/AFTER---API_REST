"""
example_entity.py

This module defines the sqlalchemy class for example entity.
"""
from sqlalchemy import Column, String
from .base import BaseEntity

class Example(BaseEntity):
    """sqlalchemy class for example entity."""

    __tablename__ = 'entity_example'

    example_field = Column(String(45))

    def __init__(self, example_field):
        self.example_field = example_field

    def __repr__(self):
        return f"<EntityExample(id={self.id}, example_field=({self.example_field})>"
