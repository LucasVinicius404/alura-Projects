from .veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, nome, marca,portas):
        super().__init__(nome, marca)
        self.portas = portas
    
    def __str__(self):
        return f'{super().__str__()} | {self.portas} Portas'