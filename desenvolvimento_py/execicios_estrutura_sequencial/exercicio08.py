# 8. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o salário total do mês.

salario_hora = float(input("Quanto você ganha por hora? "))
hora_trabalhadas = float(input("Quantas hora você trabalhou no mês? "))

salario_total = salario_hora * hora_trabalhadas
1
print(f"O seu salário todal é: {salario_total:.2f}")