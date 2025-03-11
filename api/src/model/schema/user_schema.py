"""
user_schema.py

This module defines the sqlalchemy class for user schema.
"""
from pydantic import Field
from api.src.model.entity.user_entity import User
from api.src.model.schema.base import BaseSchema

class UserSchema(BaseSchema):
    """class for user schema."""

    user_field: str = Field(...,
        title='Campo de Exemplo',
        description='Campo de Exemplo para fins didáticos'
    )

    def __get_entity__(self) -> User:
        return User(user_field=self.user_field)
