from modelo.Restaurante import Restaurante
from modelo.cardapio.bebida import Bebida
from modelo.cardapio.prato import Prato
from modelo.cardapio.item_cardapio import ItemCardapio

restaurante1 = Restaurante("don gordone", 'lanches artesanais')
restaurante1.mudar_estado()
Bebida_suco = Bebida('suco de melancia', '12.0', 'Grande')
prato = Prato('X-burguer', '20.50',"x-burguer grande")



def main():
    pass
    



if __name__ == '__main__':
    main()
