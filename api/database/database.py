"""
database.py

This module handles the database configuration and connection setup.
"""
import os
from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker

class DatabaseConfig:
    """
    Database configuration class responsible for loading environment variables
    and creating an async SQLAlchemy engine.
    """
    _engine = None
    def __init__(self):
        """Initialize the database configuration by loading environment variables."""
        load_dotenv()
        self.config = {
            "db_name": os.getenv("DB_NAME"),
            "db_user": os.getenv("DB_USER"),
            "db_password": os.getenv("DB_PASSWORD"),
            "db_host": os.getenv("DB_HOST"),
            "db_port": os.getenv("DB_PORT"),
            "db_type": os.getenv("DB_TYPE"),
            "db_async_driver": os.getenv("DB_ASYNC"),
        }

    def get_database_url(self) -> str:
        """Construct and return the database URL."""
        db_url = (
            f"{self.config['db_type']}+{self.config['db_async_driver']}://"
            f"{self.config['db_user']}:{self.config['db_password']}@"
            f"{self.config['db_host']}"
            f"{':' + self.config['db_port'] if self.config['db_port'] else ''}/"
            f"{self.config['db_name']}"
        )
        return db_url

    def get_async_engine(self) -> AsyncEngine:
        """Create and return an async SQLAlchemy engine."""
        if not self._engine:
            self._engine = create_async_engine(
                self.get_database_url(),
                echo=False,
                pool_pre_ping=True,
                pool_size=10,
                max_overflow=10,
                pool_timeout=30
            )
        return self._engine

    def get_async_session_local(self) -> async_sessionmaker:
        """Create and return an async session factory."""
        engine = self.get_async_engine()
        return async_sessionmaker(bind=engine, autoflush=True, expire_on_commit=False)
