import random
opcoes = ['pedra','papel','tesoura']

def verificar_escolha(jogada):
    if jogada not in opcoes:
        return False
    return True

def gerador_escolha():
    escolha = random.choice(opcoes)
    return escolha

def ver_resultado(escolha_usu,escolha_computador):
    if escolha_usu == escolha_computador:
        return "empate"
    elif (
        (escolha_usu == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_usu == 'tesoura' and escolha_computador == 'papel') or
        (escolha_usu == 'papel' and escolha_computador == 'pedra')   
    ):
        return "Você venceu"
    else:
        return "Você perdeu"

def jogo():
    usuario = input("pedra, pedra, tesoura....: ").lower().strip()
    

    if verificar_escolha(usuario) == False:
        print("Jogada invalida")
        return

    jogada_computador = gerador_escolha()

    print(f"o computador escolheu: {jogada_computador}")

    print(ver_resultado(usuario,jogada_computador))

jogo()