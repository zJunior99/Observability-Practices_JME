from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
    assert "orders" in response.json()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_metrics_endpoint():
    response = client.get("/metrics")
    assert response.status_code == 200
    assert b"api_requests_total" in response.content