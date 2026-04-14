# 1. Calculadora de Média de Lista:
# Crie uma função calcular_media(notas) que recebe uma lista de notas e
# retorna a média, usando sum() e len()

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    media = sum(notas) / len(notas)
    return media

notas = []
while True:
    nota = float(input("Digite uma nota (0 ou número negativo para encerrar): "))
    if nota < 0:
        break
    notas.append(nota)

media = calcular_media(notas)
print(f"A média das notas é: {media}")