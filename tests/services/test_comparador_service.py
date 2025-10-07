from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

API_KEY = "supersecreta123"

def test_comparar_sucesso():
    response = client.get(
        "/comparador",
        headers={"Token": API_KEY},
        params={"query": "notebook"}
    )
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict) or isinstance(data, list)
    