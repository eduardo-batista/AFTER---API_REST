"""
user_schema.py

This module defines the sqlalchemy class for user schema.
"""
from datetime import datetime
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
    active: bool = Field(...,
        title='Usuário ativo?'
    )
    created_at: datetime = Field(...,
        title='Data e Hora de criação do usuário'
    )
    updated_at: datetime = Field(...,
        title='Data e Hora da última edição do usuário'
    )

class CreateUserRequest(BaseSchema):
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

class UpdateUserRequest(BaseSchema):
    """class for user schema."""

    name: Optional[str] = Field(None,
        title='Nome do Usuário', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Usuário'
    )
    identification_document: Optional[str] = Field(None,
        title='CPF ou CNPJ do usuário'
    )
    email: Optional[str] = Field(None,
        title='Email do usuário'
    )
    fone: Optional[str] = Field(None,
        title='Telefone do usuário'
    )
    profile_type: Optional[str] = Field(None,
        title='Tipo de Perfil do usuário'
    )

    def __get_entity__(self) -> User:
        return User(name=self.name,
                    description=self.description,
                    identification_document=self.identification_document,
                    email=self.email,
                    fone=self.fone,
                    profile_type=self.profile_type)
