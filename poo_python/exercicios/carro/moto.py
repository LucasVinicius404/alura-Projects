from .veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, nome, marca,tipo):
        super().__init__(nome, marca)
        self.tipo = tipo

    def __str__(self):
        return f'{super().__str__()} | {self.tipo}'