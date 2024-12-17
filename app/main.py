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

