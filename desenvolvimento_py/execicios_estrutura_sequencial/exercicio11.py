# 11. Peça dois números inteiros e um número real. Calcule: (a) o produto do dobro do primeiro com 
# metade do segundo; (b) a soma do triplo do primeiro com o terceiro; (c) o terceiro elevado ao cubo.

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))
n3 = float(input("Digite um número real: "))

a = (2 * n1) * (n2 / 2)
b = (3 * n1) + n3
c = n3 ** 3

print(f"a) O produto do dobro do primeiro com metade do segundo é: {a}")
print(f"b) A soma do triplo do primeiro com o terceiro é: {b}")
print(f"c) O terceiro elavado ao cubo: {c:.2f}")