# This file manages configuration settings, typically loaded from environment variables.
# We define a Settings class that inherits from BaseSettings.
# This class will automatically read from environment variables or a .env file.
# We create an instance of Settings that can be imported and used throughout the application.

# Additional Components

# tests/: This directory would contain your test files. You'd typically have tests for your API endpoints, database operations, and any utility functions.
# alembic/: If you decide to use Alembic for database migrations, this directory would contain migration scripts and configuration.
# requirements.txt: This file lists all the Python packages required for your project. You'd typically include:
# Copyfastapi
# uvicorn
# sqlalchemy
# psycopg2-binary
# pydantic
# pydantic-settings
# python-dotenv

# .env: This file contains your environment variables, such as database credentials. It should not be committed to version control.
# README.md: This file would contain documentation about your project, how to set it up, and how to use it.

# app/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOSTNAME: str
    DATABASE_PORT: str
    DATABASE_NAME: str

    class Config:
        env_file = ".env"

settings = Settings()