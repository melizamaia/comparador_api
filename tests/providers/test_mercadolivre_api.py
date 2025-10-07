from app.providers import mercadolivre_api
from app.models.produto_models import Produto

def test_buscar_produtos_mercadolivre_retorna_resultados():
    resultado = mercadolivre_api.buscar_mercadolivre("celular")

    assert isinstance(resultado, Produto)
    assert resultado.id == "ml-123" 
    assert resultado.nome == "Produto Mercado Livre - celular"
    assert resultado.preco == 89.90
    assert resultado.marketplace == "mercadolivre"
    assert resultado.link == "https://www.mercadolivre.com/produto"