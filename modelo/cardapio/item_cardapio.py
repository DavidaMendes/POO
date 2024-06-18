from abc import ABC, abstractmethod # Cria uma classe abstrata

class ItemCardapio(ABC):
    def __init__(self, ItemName, preco ):
       self._nome = ItemName
       self._preco = preco

    @abstractmethod # O Metodo abstrato tem que estar aplicado em todas as instancias dessa classe
    def aplicar_desconto(self):
        pass