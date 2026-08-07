from .Avaliacao import Avaliacao
from .cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False # ._ torna ele privado como private em typescrit
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def mudar_estado(self):
        self._ativo = not self._ativo

    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.categoria.ljust(25)} | {str(self.media_avaliacao).ljust(25)} | {self.ativo}'
    
    '''ou fazer por uma função convencional sem os metodos de python

        def mostrar_Restaurante(self):
            ativo = 'Ativado' if self._ativo == True else 'Desativado'
            print(f"o Restaurante {self.nome} com a categoria sendo de {self.categoria} está {ativo}") 
    
    '''
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'} ")
        for restaurante in cls.restaurantes:
            print(restaurante)
    
    @property
    def ativo(self):
        return '☑ ativo' if self._ativo else '☒ desativo'
    
    def receber_avaliacao(self,cliente,nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self.nome}\n")
        for i,item  in enumerate(self._cardapio,start=1):
            if hasattr(item,'descricao'):
                mensagem = f"{i}. Nome: {item._nome} | Preço R$: {item._preco} | Descrição: {item.descricao}"
                print(mensagem)
            else:
                mensagem = f"{i}. Nome: {item._nome} | Preço R$: {item._preco} | Tamanho: {item.tamanho}"
                print(mensagem)

