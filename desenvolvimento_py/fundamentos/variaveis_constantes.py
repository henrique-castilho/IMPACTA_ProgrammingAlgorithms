# Ele mostra exemplos de VARIÁVEIS (que podem mudar)
# e de CONSTANTES (valores que não deveriam mudar).

# Variável: guarda um valor que pode ser alterado durante o programa
nome = "Henrique"
idade = 21

print(nome, idade)

# Aqui estamos mudando os valores das variáveis
# Isso é possível porque são variáveis (o valor pode variar)
nome, idade = "Giovanna", 20

print(nome, idade)

# Outra variável comum (pode ser alterada se necessário)
limite_saque_diario = 1000

# Constante (por convenção)
# Em Python não existe constante "de verdade",
# mas quando escrevemos em LETRAS MAIÚSCULAS
# indicamos que esse valor NÃO deve ser alterado.
BRAZILIAN_STATES = ["SP", "RJ", "SC", "RS"]

print(BRAZILIAN_STATES)