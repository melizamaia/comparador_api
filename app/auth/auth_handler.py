import os
from fastapi import HTTPException, Security
from fastapi.security.api_key import APIKeyHeader
from dotenv import load_dotenv

load_dotenv()

_api_key_header = APIKeyHeader(name="Token", auto_error=False)

async def verify_api_key(api_key: str = Security(_api_key_header)) -> bool:
    expected = os.getenv("API_KEY")
    if not expected:
        # Falha segura: não liberar se não configurado
        raise HTTPException(status_code=500, detail="API_KEY não configurada no servidor")
    if not api_key or api_key != expected:
        raise HTTPException(status_code=403, detail="Token inválido ou ausente")
    return True
