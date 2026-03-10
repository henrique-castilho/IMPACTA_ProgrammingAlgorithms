# 9. Verificação de CPF: Leia um CPF no formato xxx.xxx.xxx-xx e valide os dígitos verificadores.

cpf = input("Digite um CPF (xxx.xxx.xxx-xx): ")

# remove pontos e hífen
cpf = cpf.replace(".", "").replace("-", "")

# verifica se tem 11 dígitos
if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido")
else:
    # cálculo do primeiro dígito
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    dig1 = (soma * 10) % 11
    if dig1 == 10:
        dig1 = 0

    # cálculo do segundo dígito
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    dig2 = (soma * 10) % 11
    if dig2 == 10:
        dig2 = 0

    # verificação
    if dig1 == int(cpf[9]) and dig2 == int(cpf[10]):
        print("CPF válido")
    else:
        print("CPF inválido")