class Restaurante:
    Restaurantes = []

    def __init__(self,nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.Restaurantes.append(self)

    def mudar_estado(self):
        self.ativo = not self.ativo
        print("o Restaurante foi ativado") if self.ativo else print("O Restaurante foi desativado")

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {"Ativado" if self.ativo else "Desativado"}'
    
    '''ou fazer por uma função convencional sem os metodos de python

        def mostrar_Restaurante(self):
            ativo = 'Ativado' if self.ativo == True else 'Desativado'
            print(f"o Restaurante {self.nome} com a categoria sendo de {self.categoria} está {ativo}") 
    
    '''
    def listar_Restaurantes():
        for i in Restaurante.Restaurantes:
            print(i)


Restaurante_praca = Restaurante('Ferrari','Italiano')
Restaurante_pizza = Restaurante('Mercedes','Comida alemã')

Restaurante.listar_Restaurantes()