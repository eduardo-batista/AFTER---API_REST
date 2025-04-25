"""
space_schema.py

This module defines the sqlalchemy class for space schema.
"""
from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import Field
from api.src.model.entity.space_entity import Space
from api.src.model.schema.base import BaseSchema

class SpaceResponse(BaseSchema):
    """class for space schema."""

    id: Optional[int] = None

    name: str = Field(...,
        title='Nome do Espaço', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Espaço'
    )
    image: Optional[str] = Field(None,
        title='URL da imagem principal do Espaço'
    )
    latitude: Decimal = Field(...,
        title='latitude do Espaço'
    )
    longitude: Decimal = Field(...,
        title='longitude do Espaço'
    )
    host_id: int = Field(...,
        title='Usuário responsável pelo Espaço'
    )
    active: bool = Field(...,
        title='Espaço ativo?'
    )
    created_at: datetime = Field(...,
        title='Data e Hora de criação do Espaço'
    )
    updated_at: datetime = Field(...,
        title='Data e Hora da última edição do Espaço'
    )

class CreateSpaceRequest(BaseSchema):
    """class for user schema."""

    name: str = Field(...,
        title='Nome do Espaço', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Espaço'
    )
    image: Optional[str] = Field(None,
        title='URL da imagem principal do Espaço'
    )
    latitude: Decimal = Field(...,
        title='latitude do Espaço'
    )
    longitude: Decimal = Field(...,
        title='longitude do Espaço'
    )
    host_id: int = Field(...,
        title='Usuário responsável pelo Espaço'
    )

    def __get_entity__(self) -> Space:
        return Space(name=self.name,
                    description=self.description,
                    image=self.image,
                    latitude=self.latitude,
                    longitude=self.longitude,
                    host_id=self.host_id)

class UpdateSpaceRequest(BaseSchema):
    """class for user schema."""
    name: Optional[str] = Field(None,
        title='Nome do Espaço', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Espaço'
    )
    image: Optional[str] = Field(None,
        title='URL da imagem principal do Espaço'
    )
    latitude:  Optional[Decimal] = Field(None,
        title='latitude do Espaço'
    )
    longitude:  Optional[Decimal] = Field(None,
        title='longitude do Espaço'
    )
    host_id:  Optional[int] = Field(None,
        title='Usuário responsável pelo Espaço'
    )

    def __get_entity__(self) -> Space:
        return Space(name=self.name,
                    description=self.description,
                    image=self.image,
                    latitude=self.latitude,
                    longitude=self.longitude,
                    host_id=self.host_id)
