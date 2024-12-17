"""
Integration tests for the FastAPI application.
Tests the root and health check endpoints.
"""
import pytest
import requests

BASE_URL = "http://localhost:8000"

def test_read_root():
    """
    Test the root endpoint (/) to ensure it returns the expected greeting message.
    
    Verifies:
    - HTTP 200 status code
    - Correct JSON response structure
    """
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_health_check():
    """
    Test the health check endpoint (/health) to verify service status.
    
    Verifies:
    - HTTP 200 status code
    - Service status is healthy
    - Service name is correct
    """
    response = requests.get(f"{BASE_URL}/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "service": "fastapi-app"
    }