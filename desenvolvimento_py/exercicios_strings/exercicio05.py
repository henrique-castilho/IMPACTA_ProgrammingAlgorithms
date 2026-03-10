# 5. Escada invertida: Mostre o nome em escada decrescente.

nome = input("Digite um nome: ")

for i in range(len(nome), 0, -1):
    print(nome[:i])