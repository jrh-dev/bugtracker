from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'title': 'simple bug tracker'}


def test_get_all_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_all_users():
    response = client.get("/users/1")
    assert response.status_code == 404
    assert response.json() == {'detail': 'User not found'}


def test_user_interactions():
    data = {"first": "string", "last": "string"}
    response_create = client.post("/users/create/", json=data)
    response_update = client.patch("/users/update/1/", json=data)
    assert response_create.status_code == 200
    assert response_create.json() == {'first': 'string', 'last': 'string'}
    assert response_update.status_code == 200
    assert response_update.json() == {'first': 'string', 'last': 'string'}


def test_get_all_bugs():
    response = client.get("/bugs/")
    assert response.status_code == 200
    assert response.json() == []


def test_get_all_users():
    response = client.get("/bugs/1")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Bug not found'}


def test_bug_interactions():
    data = {
        "title": "string",
        "description": "string",
        "is_open": True,
        "owner_id": 1
    }
    response_create = client.post("/bugs/create/1/", json=data)
    response_update = client.patch("/bugs/update/1/", json=data)
    assert response_create.status_code == 200
    assert response_create.json() == {
        'title': 'string', 'description': 'string', 'is_open': True, 'owner_id': 1}
    assert response_update.status_code == 200
    assert response_update.json() == {
        'title': 'string', 'description': 'string', 'is_open': True, 'owner_id': 1}
