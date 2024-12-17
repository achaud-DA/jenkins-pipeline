"""
FastAPI application providing a simple REST API with root endpoint.
This module serves as the main entry point for the API service.
"""
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


@app.get("/health")
def health_check() -> dict:
    """
    Health check endpoint to verify service status.
    
    Returns:
        dict: Service status information
    """
    return {"status": "healthy", "service": "fastapi-app"}