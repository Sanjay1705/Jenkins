import pytest
from unittest.mock import patch
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"

@patch("app.r")  
def test_counter_increment(mock_redis, client):

    mock_redis.set.return_value = True

    response1 = client.get("/counter")
    val1 = int(response1.data)
    response2 = client.get("/counter")
    val2 = int(response2.data)
    
    assert val2 == val1 + 1
    
    assert mock_redis.set.call_count == 2
