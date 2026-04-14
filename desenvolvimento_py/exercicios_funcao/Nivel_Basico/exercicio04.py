# 4. Par ou Ímpar:
# Crie uma função verificar_par(numero) que retorne True se o número for par e
# False caso contrário.

def verificar_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input("Digite um número: "))
if verificar_par(num):
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é ímpar.")