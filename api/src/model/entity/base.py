"""
Base Entity Module

This module defines the base class for all entities.
"""
from sqlalchemy import TIMESTAMP, Boolean, Column, Integer, text
from sqlalchemy.orm import DeclarativeBase

class BaseEntity(DeclarativeBase):
    """Base class for all entities."""

    id = Column(Integer, primary_key=True, autoincrement=True)
    active = Column(Boolean, nullable=False, server_default='TRUE')
    created_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    updated_at = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'), onupdate=text('CURRENT_TIMESTAMP'))

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: The dictionary representation of the instance.
        """
        # Obtém todos os atributos do objeto, incluindo os campos da tabela
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def __repr__(self):
        return f"<Entity(id={self.id}>"
