# Função simples sem parâmetros
def exibir_mensagem():
    # Exibe uma mensagem fixa
    print("Olá mundo!")


# Função com parâmetro obrigatório
def exibir_mensagem2(nome):
    # Exibe uma mensagem personalizada usando o nome recebido
    print(f"Seja bem vindo {nome}!")


# Função com parâmetro opcional (valor padrão)
def exibir_mensagem3(nome = "Antônio"):
    # Se nenhum nome for passado, usa "Antônio" como padrão
    print(f"Seja bem vindo {nome}!")


# Chamando a função sem argumentos
exibir_mensagem()

# Passando argumento de forma posicional
exibir_mensagem2("Henrique")

# Passando argumento de forma nomeada (keyword argument)
exibir_mensagem2(nome = "Guilherme")

# Chamando sem passar valor → usa o padrão "Antônio"
exibir_mensagem3()

# Sobrescrevendo o valor padrão
exibir_mensagem3(nome = "Chappie")