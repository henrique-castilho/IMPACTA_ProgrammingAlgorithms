# Solicita o nome do usuário
nome = input("Digite seu nome: ")
# Solicita a idade do usuário
idade = input("Digite sua idade: ")

# Imprime nome e idade com separador padrão (espaço) e fim padrão (quebra de linha)
print(nome, idade)
# Imprime nome e idade com fim personalizado "...\n"
print(nome, idade, end="...\n")
# Imprime nome e idade com separador personalizado "#"
print(nome, idade, sep="#")
# Imprime nome e idade com separador "#" e fim personalizado "...\n"
print(nome, idade, sep="#", end="...\n")

