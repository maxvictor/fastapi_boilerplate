from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_posts():
    response = client.get("/api/v1/posts/")
    assert response.status_code == 200


def test_create_post_validation():
    response = client.post("/api/v1/posts/", json={})
    assert response.status_code == 422
