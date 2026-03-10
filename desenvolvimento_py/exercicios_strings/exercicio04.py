# 4. Nome em escada: Mostre o nome em formato de escada crescente (F, FU, FUL...).

nome = input("Digite um nome: ")

for i in range(1, len(nome) + 1):
    print(nome[:i])