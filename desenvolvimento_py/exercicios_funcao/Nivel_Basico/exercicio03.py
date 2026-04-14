# 3. Maior de Dois:
# Faça uma função maior_valor(a, b) que receba dois números e retorne o
# maior deles.

def maior_valor(a, b):
    if a > b:
        return a
    else:
        return b


num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = maior_valor(num1, num2)

print(f"O maior valor é: {resultado}")