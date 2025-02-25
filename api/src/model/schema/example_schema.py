"""
example_schema.py

This module defines the sqlalchemy class for example schema.
"""
from pydantic import Field
from api.src.model.entity.example_entity import Example
from api.src.model.schema.base import BaseSchema

class ExampleSchema(BaseSchema):
    """class for example schema."""

    example_field: str = Field(...,
        title='Campo de Exemplo',
        description='Campo de Exemplo para fins didáticos'
    )

    def __get_entity__(self) -> Example:
        return Example(example_field=self.example_field)
