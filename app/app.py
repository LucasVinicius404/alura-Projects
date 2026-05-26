import os

vet = []

def nome_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
 
def exibir_subtitle(texto):
    os.system('cls')
    print(texto)
    print()


def opcao_invalida():
    print("opcao invalida")
    input("essa opção é invalida digite qualquer tecla para voltar ao menu")
    print()

def cadastrar():
    exibir_subtitle("cadastro de restaurante")
    vet.append(str(input("digite o nome do restaurante a cadastrar: ")))
    print("o restaurante foi registrado com sucesso\n")

def listar():
    exibir_subtitle("listando todos os restaurantes")
    print(*vet,sep='\n')
    print()

def menu():
    opcao = -1
    while opcao != 4:
        print("""\t1. Cadastrar Restaurante
            2. listar Restaurante
            3. ativar Restaurante
            4. Sair
            """)

        try:
            opcao = int(input("digite a opção desejada: "))
            
        except ValueError:
            opcao_invalida()
            
        else:
            print(f"voce escolheu a opção {opcao}\n")

            match opcao:
                case 1:
                    cadastrar()
                case 2:
                    listar()
                case 3:
                    print("ativar restaurante\n")
                case 4:
                    os.system('cls')
                    print("encerrando programa")
                case _:
                    opcao_invalida()

def main():

    nome_programa()
    menu()
    
if __name__ == '__main__':
    main()


