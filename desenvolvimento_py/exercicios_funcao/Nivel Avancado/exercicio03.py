# 3. Recursão (Fibonacci):
# Crie uma função recursiva que retorne o n-ésimo termo da sequência de
# Fibonacci.

def fibonacci(n):
    if n <= 0:
        return "O número deve ser maior que zero."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Digite um número inteiro positivo: "))
resultado = fibonacci(num)
print(f"O {num}-ésimo termo da sequência de Fibonacci é: {resultado}") 