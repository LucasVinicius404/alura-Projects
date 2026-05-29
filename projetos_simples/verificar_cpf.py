def verificar_cpf(cpf):
    if not cpf.isdigit():
        return "Cpf deve conter apenas número validos"
    if len(cpf) != 11:
        return "o cpf deve conter 11 digitos"
    return "CPF Valído"

cpf = input("digite o seu cpf: ")
print(verificar_cpf(cpf))