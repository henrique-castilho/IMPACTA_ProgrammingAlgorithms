# 8. Palíndromo: Leia uma sequência de caracteres e informe se é um palíndromo.

frase = input("Digite uma frase: ")

frase_invertida = frase[::-1]

if frase == frase_invertida:
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")
