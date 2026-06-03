class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = False # ._ torna ele privado como private em typescrit
        Restaurante.restaurantes.append(self)

    def mudar_estado(self):
        self._ativo = not self._ativo

    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.categoria.ljust(25)} | {self.ativo}'
    
    '''ou fazer por uma função convencional sem os metodos de python

        def mostrar_Restaurante(self):
            ativo = 'Ativado' if self._ativo == True else 'Desativado'
            print(f"o Restaurante {self.nome} com a categoria sendo de {self.categoria} está {ativo}") 
    
    '''
    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(restaurante)
    
    @property
    def ativo(self):
        return '☑ ativo' if self._ativo else '☒ desativo'
    

    
restaurante_praca = Restaurante('Ferrari','Italiano')
restaurante_pizza = Restaurante('Mercedes','Comida alemã')

restaurante_pizza.mudar_estado()

Restaurante.listar_restaurantes()