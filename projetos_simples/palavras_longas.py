import string

def verificar_tam(texto):
    # 1. Validação: Verifica se o texto está vazio ou só tem espaços
    if not texto or texto.isspace():
        return "Erro: O texto não pode estar vazio."
        
    # 2. Validação: Verifica se o texto é composto apenas por números
    # (Removendo espaços antes de testar se é digital)
    if texto.replace(" ", "").isdigit():
        return "Erro: O texto deve conter palavras, não apenas números."

    palavras_longas = []
    
    palavras = texto.split()

    for palavra in palavras:
        # Limpa a pontuação grudada nas palavras (ex: "olá!" vira "olá")
        palavra_limpa = palavra.strip(string.punctuation)
        
        # Só valida se a palavra limpa for composta por letras e tiver 10+ caracteres
        if palavra_limpa.isalpha() and len(palavra_limpa) >= 10:
            palavras_longas.append(palavra_limpa)
            
    return palavras_longas


frase = input("Digite o texto a ser avaliado: ")

resultado = verificar_tam(frase)

if isinstance(resultado, str):
    print(resultado)
elif resultado:
    print("Palavras longas encontradas:")
    print(*resultado, sep=", ")
else:
    print("Não há palavras longas no texto válido.")