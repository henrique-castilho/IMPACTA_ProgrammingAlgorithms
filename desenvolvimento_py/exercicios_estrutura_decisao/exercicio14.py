# 14. Faça um programa que lê as duas notas parciais obtidas por um
# aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
# A atribuição de conceitos obedece à tabela abaixo:
# • Entre 9.0 e 10.0 -> A
# • Entre 7.5 e 9.0 -> B
# • Entre 6.0 e 7.5 -> C
# • Entre 4.0 e 6.0 -> D
# • Entre 4.0 e zero -> E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
# conceito for D ou E.

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"

if conceito in ["A", "B", "C"]:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"Nota1: {nota1}")
print(f"Nota2: {nota2}")
print(f"Média: {media}")
print(f"Conceito: {conceito}")
print(f"Situação: {situacao}")