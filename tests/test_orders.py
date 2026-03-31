from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_order_requires_valid_user():
    response = client.post(
        "/orders",
        json={"total": 100.0, "user_id": 9999},
    )
    assert response.status_code == 404
