from fastapi import FastAPI
from app.api import comparador_routes

app = FastAPI(
    title="Comparador de Preços API",
    version="1.1.0",
    description="API para comparar preços entre fornecedores (Amazon, Mercado Livre, etc)",
)

@app.get("/", tags=["health"])
async def raiz():
    """
    Endpoint de healthcheck simples.
    """
    return {"status": "ok", "name": "comparador-api", "version": "1.1.0"}

# Registra o router das rotas de comparação
app.include_router(comparador_routes.router)
