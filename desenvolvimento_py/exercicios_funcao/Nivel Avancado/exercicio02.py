# 2. Função com Argumentos Opcionais:
# Crie uma função configurar_perfil(nome, idade, cidade="Desconhecida").

def configurar_perfil(nome, idade, cidade="Desconhecida"):
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Cidade: {cidade}")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
cidade = input("Digite sua cidade (ou deixe em branco para 'Desconhecida'): ")
if cidade:
    configurar_perfil(nome, idade, cidade)
else:
    configurar_perfil(nome, idade)