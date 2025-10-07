"""
Provider da Amazon (exemplo).
Substitua a lógica de scraping/SDK real aqui.
"""
from typing import List
from app.models.produto_models import Produto

# Dica: para chamadas HTTP use httpx (assíncrono) ou requests (sincrono)
# import httpx

async def buscar_produtos_amazon(query: str) -> List[Produto]:
    """
    Busca produtos na Amazon e retorna uma lista de Produto.
    Neste exemplo, usamos dados mockados; substitua pela sua implementação.
    """
    # Exemplo mockado (troque por lógica real)
    base = "https://www.amazon.com.br"
    slug = query.strip().replace(" ", "-")
    resultados = [
        Produto(
            id="amz-001",
            nome=f"{query} - Versão A",
            preco=2999.90,
            marketplace="amazon",
            link=f"{base}/{slug}-a",
        ),
        Produto(
            id="amz-002",
            nome=f"{query} - Versão B",
            preco=2799.90,
            marketplace="amazon",
            link=f"{base}/{slug}-b",
        ),
    ]
    return resultados
