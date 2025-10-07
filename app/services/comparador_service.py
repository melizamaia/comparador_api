from typing import List
import asyncio
from app.models.produto_models import Produto
from app.providers.amazon_api import buscar_produtos_amazon
from app.providers.mercadolivre_api import buscar_produtos_ml

async def comparar_produtos(query: str) -> List[Produto]:
    """
    Orquestra a busca em múltiplos providers e retorna os itens ordenados por preço.
    """
    # Executa concorrente (providers assíncronos)
    amazon_task = buscar_produtos_amazon(query)
    ml_task = buscar_produtos_ml(query)

    resultados = await asyncio.gather(amazon_task, ml_task, return_exceptions=False)
    # "achatando" listas de resultados
    produtos: List[Produto] = [p for sub in resultados for p in sub]

    # Deduplicação opcional por (marketplace, id)
    seen = set()
    dedup: List[Produto] = []
    for p in produtos:
        key = (p.marketplace, p.id)
        if key not in seen:
            seen.add(key)
            dedup.append(p)

    # Ordena por preço crescente
    dedup.sort(key=lambda p: p.preco)
    return dedup
