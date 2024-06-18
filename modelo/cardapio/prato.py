from .item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco) # Toda vez que usa o super, ele vai permitir que você acessa todos os metodos e parametros da classe mãe.
        self.descricao = descricao
    
    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self): # Polimorfismo: a mesma classe se adapta de formas diferentes entre classes
        self._preco -= (self._preco * 0.05)