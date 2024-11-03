# This file defines the API routes for the items resource.
# We create an APIRouter instance to define our routes.
# We define two endpoints: one for creating items and another for retrieving items by ID.
# We use dependency injection to get the database session.
# We use Pydantic models for request and response validation.

# app/api/endpoints/items.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ...database import get_db
from ...schemas.item import ItemCreate, ItemResponse
from ...crud import item as item_crud

router = APIRouter()

@router.post("/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    return item_crud.create_item(db=db, item=item)

@router.get("/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = item_crud.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item