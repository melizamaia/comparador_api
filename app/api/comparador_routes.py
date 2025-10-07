from typing import List
from fastapi import APIRouter, Depends, Query
from app.auth.auth_handler import verify_api_key
from app.services.comparador_service import comparar_produtos
from app.schemas.produto_schema import ProdutoOut

router = APIRouter(prefix="/api", tags=["comparador"], dependencies=[Depends(verify_api_key)])

@router.get("/comparar", response_model=List[ProdutoOut])
async def comparar(query: str = Query(..., min_length=2, description="Termo de busca (ex: 'notebook')")):
    """
    Compara preços entre marketplaces e retorna uma lista ordenada por preço.
    """
    return await comparar_produtos(query)
