# Declaração de variáveis para demonstração de formatação de strings
nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

# Dicionário para agrupar informações do usuário para facilitar a formatação e reutilização
dados = {"nome": "Guilherme", "idade": 28}

# Formatação antiga usando % (estilo C)
# %s = string, %d = inteiro, %f = float/decimal
print("1) Nome: %s Idade: %d" % (nome, idade))

# Formatação com .format() - argumentos posicionais
print("2) Nome: {} Idade: {}".format(nome,idade))

# Formatação com .format() - argumentos indexados
# {1} pega o segundo argumento, {0} pega o primeiro
print("3) Nome: {1} Idade: {0}".format(idade, nome))
print("4) Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

# Formatação com .format() - argumentos nomeados
print("5) Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("6) Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))

# Desempacotamento de dicionário com **
print("7) Nome: {nome} Idade: {idade}".format(**dados))

# f-strings (Python 3.6+) - forma mais moderna e legível
print(f"8) Nome: {nome} Idade: {idade}")
# f-string com formatação numérica - .2f = 2 casas decimais
print(f"9) Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
# f-string com formatação - 10 caracteres de largura, 1 casa decimal
print(f"10) Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}")