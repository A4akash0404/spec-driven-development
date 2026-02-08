from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks", json={"title": "Write tests"})
    assert response.status_code == 200
    assert response.json()["title"] == "Write tests"

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200

def test_filter_tasks():
    client.post("/tasks", json={"title": "Task 1"})
    response = client.get("/tasks?status=pending")
    assert response.status_code == 200

def test_get_task_by_id():
    task = client.post("/tasks", json={"title": "Find me"}).json()
    response = client.get(f"/tasks/{task['id']}")
    assert response.status_code == 200

def test_invalid_task():
    response = client.get("/tasks/invalid")
    assert response.status_code == 404
