from pydantic import BaseModel, Field

class ProdutoOut(BaseModel):
    id: str
    nome: str
    preco: float = Field(ge=0, description="Preço em moeda local")
    marketplace: str
    link: str