from modelo.Restaurante import Restaurante

restaurante1 = Restaurante("don gordone", 'lanches artesanais')
restaurante2 = Restaurante("pastelle", "Pastel")
restaurante3 = Restaurante("Habibs", "Esfiha")

restaurante3.mudar_estado()

def main():
    Restaurante.listar_restaurantes()





if __name__ == '__main__':
    main()
