# 18. Faça um programa que peça uma data no formato dd/mm/aaaa e
# determine se a mesma é uma data válida.

data = input("Digite uma data (dd/mm/aaaa): ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

data_valida = True

if mes < 1 or mes > 12:
    data_valida = False

elif mes in [4, 6, 9, 11] and dia > 30:
    data_valida = False

elif mes == 2:
    if dia > 29:
        data_valida = False
    elif dia == 29:
        if not ((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)):
            data_valida = False

elif dia < 1 or dia > 31:
    data_valida = False


if data_valida:
    print("Data válida")
else:
    print("Data inválida")
