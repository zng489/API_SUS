# This file handles the database connection and session management.
# We import necessary modules from SQLAlchemy and our config file.
# We construct the database URL using settings from our config.
# We create an SQLAlchemy engine, which is the starting point for any SQLAlchemy application.
# We create a SessionLocal class, which will be used to create database sessions.
# We define a Base class, which will be used to create database models.
# The get_db() function is a dependency that will be used in our API endpoints to get a database session.

# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()