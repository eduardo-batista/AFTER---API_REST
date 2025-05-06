"""
tag_schema.py

This module defines the sqlalchemy class for tag schema.
"""
from datetime import datetime
from typing import Optional
from pydantic import Field
from api.src.model.entity.tag_entity import Tag
from api.src.model.schema.base import BaseSchema

class TagResponse(BaseSchema):
    """class for tag schema."""
    id: Optional[int] = None
    label: str = Field(...,
        title='Rótulo da Tag', 
    )
    active: bool = Field(...,
        title='Tag ativa?'
    )
    created_at: datetime = Field(...,
        title='Data e Hora de criação da Tag'
    )
    updated_at: datetime = Field(...,
        title='Data e Hora da última edição da Tag'
    )

class CreateTagRequest(BaseSchema):
    """class for user schema."""
    label: str = Field(...,
        title='Rótulo da Tag', 
    )

    def __get_entity__(self) -> Tag:
        return Tag(label=self.label)

class UpdateTagRequest(BaseSchema):
    """class for user schema."""
    label: Optional[str] = Field(None,
        title='Rótulo da Tag', 
    )

    def __get_entity__(self) -> Tag:
        return Tag(label=self.label)
