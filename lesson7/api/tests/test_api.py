from fastapi.testclient import TestClient

from api.app import app

client = TestClient(app)


def test_create_note():
    response = client.post(
        "/notes/",
        json={"title": "Test", "content": "Hello"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test"
    assert "id" in data


def test_get_note():
    # Сначала создадим заметку
    create_resp = client.post(
        "/notes/",
        json={"title": "Get me", "content": "Content"}
    )
    note_id = create_resp.json()["id"]

    get_resp = client.get(f"/notes/{note_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Get me"


def test_list_notes():
    resp = client.get("/notes/")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)


def test_delete_note():
    create_resp = client.post(
        "/notes/",
        json={"title": "To delete", "content": "xxx"}
    )
    note_id = create_resp.json()["id"]
    del_resp = client.delete(f"/notes/{note_id}")
    assert del_resp.status_code == 200
    # Проверяем, что заметки больше нет
    get_resp = client.get(f"/notes/{note_id}")
    assert get_resp.status_code == 404
