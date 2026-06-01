def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ",.!|\?;()[]"
    for char in caracteres:
        texto = texto.replace(char,"")
    return texto

def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    palavras = frase.split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra,0)+ 1 
    return contagem

frase = input("digite uma frase: ").strip()

if not frase:
    print("Nenhuma palavra foi digitada.")
else:
    resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de palavras:")
        for palavra,quantidade in resultado.items():
            print(f"{palavra}:{quantidade}")
    else:
        print(f"Nenhuma palavra valida foi encontrada")

