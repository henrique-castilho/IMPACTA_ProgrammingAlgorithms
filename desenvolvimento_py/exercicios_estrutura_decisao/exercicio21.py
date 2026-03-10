# 21. Faça um programa para um caixa eletrônico. O programa deverá
# perguntar ao usuário o valor do saque e depois informar quantas notas de cada
# valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
# O valor mínimo é de 10 reais e o máximo de 600 reais. 
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# • Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas
# notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# • Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três
# notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro
# notas de 1.

valor_saque = float(input("Digite o valor do saque: "))

if valor_saque < 10 or valor_saque > 600:
    print("Valor inválido! O saque deve ser entre 10 e 600 reais.")
else:
    restante = valor_saque

    notas100 = restante // 100
    restante = restante % 100

    notas50 = restante // 50
    restante = restante % 50

    notas10 = restante // 10
    restante = restante % 10

    notas5 = restante // 5
    restante = restante % 5

    notas1 = restante

    print(f"Notas de 100: {notas100:.0f}")
    print(f"Notas de 50: {notas50:.0f}")
    print(f"Notas de 10: {notas10:.0f}")
    print(f"Notas de 5: {notas5:.0f}")
    print(f"Notas de 1: {notas1:.0f}")