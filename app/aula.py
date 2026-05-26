import os

vet = [{'nome':'don Gordone','categoria':'Lanches','ativo':False},
       {'nome':'pizza mais','categoria':'pizza ','ativo':True},
       {'nome':'oakBerry','categoria':'açai e sorvetes','ativo':False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar estado do restaurante')
    print('4. Sair\n')

def mandar_para_main():
    input("\ndigite qualquer tecla para voltar para o menu: ")
    main()

def exibir_subtitle(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def finalizar_app():
    exibir_subtitle('Finalizando o app') 

def opcao_invalida():
    print('Opção inválida')
    mandar_para_main()

def cadastra_novo_restaurante():
    '''Função que cadastra novo restaurante descrito pelo usuario
        Inputs:
        - nome do restaurante
        -categoria

        output:
        -mostra que o restaurante foi cadastrado
    '''
    exibir_subtitle('Cadastro de novo restaurante')
    nome_restaurante = str(input('digite o nome do restaurante a ser cadastrado: '))
    categoria_restaurante = str(input(f"digite a categoria do restaurante {nome_restaurante}: "))
    vet.append({'nome': nome_restaurante, 'categoria':categoria_restaurante,'ativo':False})
    print(f'O restaurante {nome_restaurante} foi registado com sucesso!')
    mandar_para_main()

def listar_restaurantes():
    '''função responsavel por imprimir todos os restaurantes cadastrados'''
    exibir_subtitle("Os restaurantes listados são: ")
    print(f'{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Status')
    for restaurantes in vet:
        nome = restaurantes['nome']
        categoria = restaurantes['categoria']
        ativo = 'sim' if restaurantes['ativo'] else 'não' 
        print(f"{nome.ljust(20)} | {categoria.ljust(20)} | está ativo: {ativo}")
    mandar_para_main()

def alternar_estado():
    '''função que alterna os estados entre true e false'''
    exibir_subtitle("alternando estado do restaurante")
    nome_restaurante = str(input("digite o nome do restaurante que deseja alternar o estado: "))
    restaurante_encontrado = False

    for i in vet:
        if nome_restaurante == i['nome']:
            restaurante_encontrado = True
            i['ativo'] = not i['ativo']
            mensagem = f'o restaurante {i['nome']} foi ativado com sucesso' if i['ativo'] else f'o restaurante {i['nome']} foi desativo com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print("o restaurante não foi encontrado")
    mandar_para_main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastra_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alternar_estado()
        elif opcao_escolhida == 4: 
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()    

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()