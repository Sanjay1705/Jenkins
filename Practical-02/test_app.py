import pytest
from app import app 

@pytest.fixture
def client():
    return app.test_client()

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"  

def test_counter_increment(client):

    response1 = client.get("/counter")
    val1 = int(response1.data)
    response2 = client.get("/counter")
    val2 = int(response2.data)
    assert val2 == val1 + 1
