"""
user_schema.py

This module defines the sqlalchemy class for user schema.
"""
from typing import Optional
from pydantic import Field
from api.src.model.entity.user_entity import User
from api.src.model.schema.base import BaseSchema

class UserResponse(BaseSchema):
    """class for user schema."""

    id: Optional[int] = None

    name: str = Field(...,
        title='Nome do Usuário', 
    )
    description: str = Field(...,
        title='Descrição do Usuário'
    )
    identification_document: str = Field(...,
        title='CPF ou CNPJ do usuário'
    )
    email: str = Field(...,
        title='Email do usuário'
    )
    fone: str = Field(...,
        title='Telefone do usuário'
    )
    profile_type: str = Field(...,
        title='Tipo de Perfil do usuário'
    )

class UserRequest(BaseSchema):
    """class for user schema."""

    name: str = Field(...,
        title='Nome do Usuário', 
    )
    description: str = Field(...,
        title='Descrição do Usuário'
    )
    identification_document: str = Field(...,
        title='CPF ou CNPJ do usuário'
    )
    email: str = Field(...,
        title='Email do usuário'
    )
    fone: str = Field(...,
        title='Telefone do usuário'
    )
    profile_type: str = Field(...,
        title='Tipo de Perfil do usuário'
    )

    def __get_entity__(self) -> User:
        return User(name=self.name,
                    description=self.description,
                    identification_document=self.identification_document,
                    email=self.email,
                    fone=self.fone,
                    profile_type=self.profile_type)
