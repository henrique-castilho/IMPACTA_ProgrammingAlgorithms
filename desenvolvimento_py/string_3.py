# String para demonstrar indexação e fatiamento
nome = "Guilherme Arthur de Carvalho"

# Acessa o primeiro caractere (índice 0)
print(nome[0])

# Acessa o penúltimo caractere da string.
# Índices negativos começam do final: -1 é o último, -2 é o penúltimo.
print(nome[-2])

# Retorna os caracteres do início (índice 0) até o índice 8.
# O índice final (9) NÃO é incluído no fatiamento.
print(nome[:9])

# Retorna os caracteres do índice 10 até o final da string.
# Quando o índice final não é informado, o Python considera até o último caractere.
print(nome[10:])

# Retorna os caracteres do índice 10 até o índice 15.
# O índice 16 não é incluído
print(nome[10:16])

# Retorna os caracteres do índice 10 até o 15,
# pulando de 2 em 2 caracteres (step = 2).
# O índice 16 não é incluído
print(nome[10:16:2])

# Copia a string inteira.
# Como nenhum índice é informado, a string inteira é retornada.
print(nome[:])

# Inverte a string usando step negativo.
# O passo -1 percorre a string do fim para o início.
print(nome[::-1])
