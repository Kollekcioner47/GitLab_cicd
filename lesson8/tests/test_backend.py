from fastapi.testclient import TestClient
from backend.app import app

client = TestClient(app)


def test_create_deal():
    response = client.post(
        "/api/deals",
        json={"client_name": "Test Corp", "amount": 5000.0}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["client_name"] == "Test Corp"
    assert "id" in data


def test_list_deals():
    response = client.get("/api/deals")
    assert response.status_code == 200
    assert isinstance(response.json(), list)