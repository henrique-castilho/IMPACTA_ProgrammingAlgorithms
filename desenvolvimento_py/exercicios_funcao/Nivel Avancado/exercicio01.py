# 1. Validação de Entrada (leiaInt):
# Crie uma função leiaInt() que funciona como a função input(), mas só aceita
# valores numéricos inteiros, ignorando letras ou símbolos.

def leiaInt():
    while True:
        try:
            valor = int(input("Digite um número inteiro: "))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

numero = leiaInt()
print(f"Você digitou o número: {numero}")

