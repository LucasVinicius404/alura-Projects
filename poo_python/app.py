from modelo.Restaurante import Restaurante

restaurante1 = Restaurante("don gordone", 'lanches artesanais')
restaurante1.mudar_estado()
restaurante1.receber_avaliacao("Lucas", 10)
restaurante1.receber_avaliacao("Lui", 8)


def main():
    Restaurante.listar_restaurantes()





if __name__ == '__main__':
    main()
