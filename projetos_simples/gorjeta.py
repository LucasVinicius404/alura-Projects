def calc_gorjeta(valor,porc_gorjeta):
    gorjeta = (porc_gorjeta / 100) * valor
    return gorjeta

valor = float(input("valor da conta: "))
porc_gorjeta = float(input("porcentagem do garçom: "))

gorjeta = calc_gorjeta(valor,porc_gorjeta)
valor_final  = valor + gorjeta

print(f"o valor da gorjeta foi de R$: {gorjeta:.2f}")
print(f"o valor total da conta foi de R$: {valor_final:.2f}")