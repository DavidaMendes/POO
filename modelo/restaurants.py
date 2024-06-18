from .avaliacao import Evaluation
from modelo.cardapio.item_cardapio import ItemCardapio

 
class Restaurants:
    restaurants = []

    # Metodo da classe # Construtor
    def __init__(self, name, category): 
        self._name = name.title() # O underline protege o parametro da instancia
        self._category = category.title()
        self._condition = False  
        self._evaluation = []
        self._cardapio = []
        Restaurants.restaurants.append(self)

    #Print
    def __str__(self):
        return f'{self._name} | {self.category}'

    @classmethod # Metodos que tem a ver com a classe
    def list_restaurants(cls): #Metodo proprio
        header =  f'{"Nome do restaurante".ljust(20)} | {"Categoria".ljust(20)} | {"Avaliação".ljust(20)} | {"Status"}'
        print(header)
        print('-' * len(header))
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(20)} | {restaurant._category.ljust(20)} | {str(restaurant.media_evalution).ljust(20)}| {restaurant.condition} ')

    @property # Usa pra quando for necessário mudar algo que mais dificil de mudar
    def condition(self):
        return '⌧' if self._condition else '☐'
    
    def altern_condition(self):
        self._condition = not self._condition

    def receive_evaluation(self, client, note):
        if 0 < note <= 5:
            evaluation = Evaluation(client,note)
            self._evaluation.append(evaluation) 

    @property
    def media_evalution(self):
        if not self._evaluation:
            return '-'
        somaDasNotas = sum(avaliacao._note for avaliacao in self._evaluation)
        quantidadeDeNotas = len(self._evaluation)
        media = round(somaDasNotas / quantidadeDeNotas, 1)
        return media
    
    def add_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
    
    @property
    def exibir_cardapio(self):
        print(f'\nCardapio do Restaurante {self._name}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item,'descricao'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | {item.descricao}'
                print(mensagem_prato)
            else:
                mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | {item.tamanho}'
                print(mensagem_bebida)
                


        

