class Veiculo:
    def __init__(self,nome,marca):
        self.nome = nome
        self.marca = marca
        self._ligado = False


    def __str__(self):
        return f'{self.nome.ljust(25)} | {self.marca.ljust(25)} | {self.ligado.ljust(25)}'
    
    @property
    def ligado(self):
         return 'ligado' if self._ligado else 'desligado'
    
    