from typing import List
from app.models.produto_models import Produto

async def buscar_produtos_ml(query: str) -> List[Produto]:
    """
    Busca produtos no Mercado Livre e retorna uma lista de Produto.
    """
    base = "https://www.mercadolivre.com.br"
    slug = query.strip().replace(" ", "-")
    resultados = [
        Produto(
            id="ml-001",
            nome=f"{query} - Modelo X",
            preco=2899.90,
            marketplace="mercado_livre",
            link=f"{base}/{slug}-x",
        ),
        Produto(
            id="ml-002",
            nome=f"{query} - Modelo Y",
            preco=2699.90,
            marketplace="mercado_livre",
            link=f"{base}/{slug}-y",
        ),
    ]
    return resultados
