# Definição de constantes para as idades
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17 

# Solicita a idade do usuário e converte para inteiro
idade = int(input("Digite a sua idade: "))

# Exemplo 1: Estrutura IF simples (duas condições independentes)
# Neste caso, ambas as condições são avaliadas separadamente
if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH.")

if idade < MAIOR_IDADE:
    print("Menor de idade não pode tirar CNH.")

# Exemplo 2: Estrutura IF-ELSE
# Se a condição for verdadeira, executa o IF. Caso contrário, executa o ELSE.
if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH.")
else:
    print("Menor de idade não pode tirar CNH.")

# Exemplo 3: Estrutura IF-ELIF-ELSE
# Permite verificar múltiplas condições em sequência
# O ELIF só é avaliado se o IF for falso
# O ELSE só é executado se todas as condições anteriores forem falsas
if idade >= MAIOR_IDADE:
    print("Maior de idade pode tirar CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Menor de idade não pode tirar CNH.")