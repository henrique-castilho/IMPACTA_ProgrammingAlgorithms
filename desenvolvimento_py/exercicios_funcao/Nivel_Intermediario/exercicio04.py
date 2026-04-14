# 4. Fatorial:
# Escreva uma função recursiva ou iterativa para calcular o fatorial de um
# número inteiro positivo.

def fatorial(n):
    if n < 0:
        return "Fatorial não é definido para números negativos."
    elif n == 0 or n == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

num = int(input("Digite um número inteiro positivo para calcular o fatorial: "))
resultado = fatorial(num)
print(f"O fatorial de {num} é: {resultado}")