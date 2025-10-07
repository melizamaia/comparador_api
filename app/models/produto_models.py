from dataclasses import dataclass

@dataclass(slots=True)
class Produto:
    id: str
    nome: str
    preco: float
    marketplace: str
    link: str