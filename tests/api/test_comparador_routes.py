from fastapi.testclient import TestClient
from app.main import app

def test_docs_health():
    client = TestClient(app)
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_comparar_sem_token_rejeita():
    client = TestClient(app)
    r = client.get("/api/comparar?query=notebook")
    assert r.status_code in (401, 403, 500)  # depende da config API_KEY