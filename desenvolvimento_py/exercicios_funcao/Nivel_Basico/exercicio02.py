# 2. Área do Retângulo:
# Escreva uma função calcular_area(base, altura) que retorne a área de um
# retângulo.

def calcular_area(base, altura):
    return base * altura


base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = calcular_area(base, altura)

print(f"A área do retângulo é: {area}")