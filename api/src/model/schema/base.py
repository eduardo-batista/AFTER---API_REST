"""
Base Schema Module

This module defines the base class for all schemas.
"""
from pydantic import BaseModel

class BaseSchema(BaseModel):
    """Base class for all schemas."""

    def __get_entity__(self):
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement '__get_entity__' method"
        )

    def __repr__(self):
        raise NotImplementedError(
            f"{self.__class__.__name__} must implement '__repr__' method"
        )

    # pylint: disable=too-few-public-methods
    class Config:
        """Config class for integration with ORM."""
        from_attributes = True
