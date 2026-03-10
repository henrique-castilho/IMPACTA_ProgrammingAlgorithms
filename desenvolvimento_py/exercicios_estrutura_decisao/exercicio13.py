# 13. Faça um programa que leia um número e exiba o dia correspondente
# da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer
# valor inválido.

dias = {
    1: "Domingo",
    2: "Segunda-feira",
    3: "Terça-feira",
    4: "Quarta-feira",
    5: "Quinta-feira",
    6: "Sexta-feira",
    7: "Sábado"
}


numero = int(input("Digite um número (1 a 7): "))

if numero in dias:
    print(dias[numero])
else:
    print("Número inválido")

