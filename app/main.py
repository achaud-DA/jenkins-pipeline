"""
FastAPI application providing a simple REST API with root and items endpoints.
This module serves as the main entry point for the API service.
"""
from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root() -> dict:
    """
    Root endpoint that returns a simple greeting message.
    
    Returns:
        dict: A greeting message in JSON format
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None) -> dict:
    """
    Endpoint to retrieve item details by ID with an optional query parameter.
    
    Args:
        item_id (int): The ID of the item to retrieve
        q (Optional[str], optional): Optional query parameter. Defaults to None.
    
    Returns:
        dict: Item details including the ID and query parameter if provided
    """
    return {"item_id": item_id, "q": q}
