# 23. Faça um programa que peça um número e informe se o número é
# inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Digite um número inteiro: "))

if numero == round(numero):
   print(f"O número {numero} é inteiro")
else:
    print(f"O número {numero} é decimal")