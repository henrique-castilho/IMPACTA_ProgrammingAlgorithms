# 25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
# As perguntas são:
# 1. "Telefonou para a vítima?"
# 2. "Esteve no local do crime?"
# 3. "Mora perto da vítima?"
# 4. "Devia para a vítima?"
# 5. "Já trabalhou com a vítima?"
# O programa deve no final emitir uma classificação sobre a participação da pessoa
# no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
# classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

print("Responda as perguntas com 'sim' ou 'não'.")

respostas_positivas = 0

resposta1 = input("1. Telefonou para a vítima? ").strip().lower()
if resposta1 == "sim":
    respostas_positivas += 1

resposta2 = input("2. Esteve no local do crime? ").strip().lower()
if resposta2 == "sim":
    respostas_positivas += 1

resposta3 = input("3. Mora perto da vítima? ").strip().lower()
if resposta3 == "sim":
    respostas_positivas += 1

resposta4 = input("4. Devia para a vítima? ").strip().lower()
if resposta4 == "sim":
    respostas_positivas += 1

resposta5 = input("5. Já trabalhou com a vítima? ").strip().lower()
if resposta5 == "sim":
    respostas_positivas += 1

# Classificação
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print(f"\nClassificação: {classificacao}")