# This file defines the SQLAlchemy model for our Item table.
# We import necessary SQLAlchemy components and our Base class.
# We define an Item class that inherits from Base.
# We specify the table name and define columns for id, name, and description.

# app/models/item.py
from sqlalchemy import Column, Integer, String
from ..database import Base

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)