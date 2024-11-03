# This file defines Pydantic models for request and response validation.
# We define two Pydantic models: ItemCreate for input validation and ItemResponse for output serialization.
# ItemCreate doesn't include an id field because it's used for creating new items.
# ItemResponse includes all fields and is used when returning items from the API.
# orm_mode = True allows the Pydantic model to read data from an ORM model.

# app/schemas/item.py
from pydantic import BaseModel

class ItemCreate(BaseModel):
    name: str
    description: str

class ItemResponse(BaseModel):
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
