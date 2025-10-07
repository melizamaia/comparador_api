import pytest
from app.providers.amazon_api import buscar_produtos_amazon

@pytest.mark.asyncio
async def test_buscar_amazon_formato_basico():
    itens = await buscar_produtos_amazon("celular")
    assert len(itens) >= 1
    p = itens[0]
    assert hasattr(p, "id")
    assert hasattr(p, "nome")
    assert hasattr(p, "preco")
    assert hasattr(p, "marketplace")
    assert hasattr(p, "link")
    assert p.marketplace == "amazon"