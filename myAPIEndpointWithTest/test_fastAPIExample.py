from fastapi.testclient import TestClient
from myAPIEndpoint.fastAPIExample import app
import pytest
from unittest.mock import patch

client = TestClient(app)

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item":{"name": "Apple"}}
    
    response = client.get("/items/3")
    assert response.status_code == 404
    assert response.json() == {"detail": "out of index error"}

# using a fixture from pytest prepare test data
@pytest.fixture
def fixClient():
    with TestClient(app) as c:
        yield c

def test_read_item_ok(fixClient):
    response = fixClient.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item" : {"name": "Apple"}}


#patching or swapping out myAPIEndpoint.fastAPIExample.items
# to {1: Item(name="Apple")} 
def test_patching_item():
    with patch("myAPIEndpoint.fastAPIExample.items", {1: Item(name = "Apple")}):
        response = client.get("/items/1")
        assert response.status_code == 200