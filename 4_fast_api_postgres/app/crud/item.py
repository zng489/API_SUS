# This file contains CRUD (Create, Read, Update, Delete) operations for the Item model.
# We define functions that interact with the database.
# create_item() creates a new item in the database.
# get_item() retrieves an item by its ID.

# app/crud/item.py
from sqlalchemy.orm import Session
from ..models.item import Item
from ..schemas.item import ItemCreate

def create_item(db: Session, item: ItemCreate):
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()