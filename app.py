from modelo.restaurants import Restaurants
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato

restaurante_praca = Restaurants('praça', 'gourmet') # Primeiro chama a instancia para depois executar os metodos
restaurante_praca.receive_evaluation('Gui', 10)
restaurante_praca.receive_evaluation('Laís', 8)
restaurante_praca.receive_evaluation('Laís', 5)


bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)

def main():
    Restaurants.list_restaurants()
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()