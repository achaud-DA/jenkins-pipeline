import pytest
import requests

BASE_URL = "http://localhost:8000"

def test_read_root():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}

def test_read_item_without_query():
    item_id = 5
    response = requests.get(f"{BASE_URL}/items/{item_id}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": None}

def test_read_item_with_query():
    item_id = 5
    query = "test-query"
    response = requests.get(f"{BASE_URL}/items/{item_id}?q={query}")
    assert response.status_code == 200
    assert response.json() == {"item_id": item_id, "q": query}

def test_read_item_invalid_id():
    # Testing with a string instead of an integer
    response = requests.get(f"{BASE_URL}/items/invalid")
    assert response.status_code == 422  # FastAPI returns 422 for validation errors 