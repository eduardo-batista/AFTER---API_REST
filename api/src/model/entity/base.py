"""
Base Entity Module

This module defines the base class for all entities.
"""
from sqlalchemy import Column, Integer
from sqlalchemy.orm import DeclarativeBase

class BaseEntity(DeclarativeBase):
    """Base class for all entities."""

    id = Column(Integer, primary_key=True, autoincrement=True)

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
