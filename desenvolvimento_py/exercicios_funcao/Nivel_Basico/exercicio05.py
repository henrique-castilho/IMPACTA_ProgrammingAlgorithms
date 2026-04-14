# 5. Média Simples:
# Escreva uma função que receba três notas e retorne a média aritmética
# simples entre elas.

def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print(f"A média das notas é: {media}")