import os
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from app.auth.auth_handler import verify_api_key

def create_app():
    app = FastAPI()
    @app.get("/secure", dependencies=[Depends(verify_api_key)])
    async def secure():
        return {"ok": True}
    return app

def test_rejeita_sem_token(monkeypatch):
    monkeypatch.delenv("API_KEY", raising=False)  # força ausência -> 500
    app = create_app()
    client = TestClient(app)
    resp = client.get("/secure")
    assert resp.status_code in (401, 403, 500)

def test_aceita_com_token(monkeypatch):
    monkeypatch.setenv("API_KEY", "abc123")
    app = create_app()
    client = TestClient(app)
    resp = client.get("/secure", headers={"Token": "abc123"})
    assert resp.status_code == 200
    assert resp.json()["ok"] is True