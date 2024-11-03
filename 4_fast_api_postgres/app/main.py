# This is the main entry point of our FastAPI application.
# We create the database tables (if they don't exist) using item.Base.metadata.create_all(bind=engine).
# We create a FastAPI application instance.
# We include the router for the items endpoints.

# app/main.py
from fastapi import FastAPI
from .api.endpoints import items
from .database import engine
from .models import item

item.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])