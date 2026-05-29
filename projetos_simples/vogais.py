def verificar_vogal(texto):
    quantidade = 0;
    vogal = 'aeiou'
    for i in texto.lower():
        if i in vogal:
            quantidade += 1
    
    return quantidade

texto = input("digite um texto: ")
print(f"o texto contem {verificar_vogal(texto)} vogais")
