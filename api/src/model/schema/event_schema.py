"""
event_schema.py

This module defines the sqlalchemy class for event schema.
"""
from datetime import datetime
from typing import Optional
from pydantic import Field

from api.src.model.entity.event_entity import Event
from api.src.model.schema.base import BaseSchema
from api.src.model.schema.space_schema import SpaceResponse
from api.src.model.schema.user_schema import UserResponse

class EventResponse(BaseSchema):
    """class for event schema."""

    id: Optional[int] = None

    name: str = Field(...,
        title='Nome do Evento', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Evento'
    )
    image: Optional[str] = Field(None,
        title='URL da imagem principal do Evento'
    )
    start: datetime = Field(...,
        title='Data e Hora de início do Evento'
    )
    end: datetime = Field(...,
        title='Data e Hora de fim do Evento'
    )
    ticket_price: Optional[float] = Field(None,
        title='Preço do ingresso do Evento'
    )
    host_id: int = Field(...,
        title='Usuário anfitrião do Evento'
    )
    space_id: int = Field(...,
        title='Espaço onde ocorrerá o Evento'
    )
    active: bool = Field(...,
        title='Evento ativo?'
    )
    created_at: datetime = Field(...,
        title='Data e Hora de criação do Evento'
    )
    updated_at: datetime = Field(...,
        title='Data e Hora da última edição do Evento'
    )
    host: UserResponse = Field(...,
        title='Usuário organizador do evento'
    )
    space: SpaceResponse = Field(...,
        title='Espaço sede do evento'
    )

class CreateEventRequest(BaseSchema):
    """class for user schema."""

    name: str = Field(...,
        title='Nome do Evento', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Evento'
    )
    image: Optional[str] = Field(None,
        title='URL da imagem principal do Evento'
    )
    start: datetime = Field(...,
        title='Data e Hora de início do Evento'
    )
    end: datetime = Field(...,
        title='Data e Hora de fim do Evento'
    )
    ticket_price: Optional[float] = Field(None,
        title='Preço do ingresso do Evento'
    )
    host_id: int = Field(...,
        title='Usuário anfitrião do Evento'
    )
    space_id: int = Field(...,
        title='Espaço onde ocorrerá o Evento'
    )

    def __get_entity__(self) -> Event:
        return Event(name=self.name,
                    description=self.description,
                    image=self.image,
                    start=self.start,
                    end=self.end,
                    ticket_price=self.ticket_price,
                    host_id=self.host_id,
                    space_id=self.space_id)

class UpdateEventRequest(BaseSchema):
    """class for user schema."""

    name: Optional[str] = Field(None,
        title='Nome do Evento', 
    )
    description: Optional[str] = Field(None,
        title='Descrição do Evento'
    )
    image: Optional[str] = Field(None,
        title='URL da imagem principal do Evento'
    )
    start: Optional[datetime] = Field(None,
        title='Data e Hora de início do Evento'
    )
    end: Optional[datetime] = Field(None,
        title='Data e Hora de fim do Evento'
    )
    ticket_price: Optional[float] = Field(None,
        title='Preço do ingresso do Evento'
    )
    host_id: Optional[int] = Field(None,
        title='Usuário anfitrião do Evento'
    )
    space_id: Optional[int] = Field(None,
        title='Espaço onde ocorrerá o Evento'
    )

    def __get_entity__(self) -> Event:
        return Event(name=self.name,
                    description=self.description,
                    image=self.image,
                    start=self.start,
                    end=self.end,
                    ticket_price=self.ticket_price,
                    host_id=self.host_id,
                    space_id=self.space_id)
