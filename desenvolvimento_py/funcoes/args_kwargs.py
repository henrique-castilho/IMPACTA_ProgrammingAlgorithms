# Função que recebe:
# - data_extenso: parâmetro obrigatório
# - *args: vários argumentos posicionais (texto do poema)
# - **kwargs: vários argumentos nomeados (metadados)
def exibir_poema(data_extenso, *args, **kwargs):
    
    # Junta todas as linhas do poema separando por quebra de linha
    texto = "\n".join(args)
    
    # Cria uma lista com "Chave: Valor" para cada item de kwargs
    # .title() deixa a primeira letra maiúscula (ex: autor -> Autor)
    meta_dados = "\n".join([
        f"{chave.title()}: {valor}" 
        for chave, valor in kwargs.items()
    ])
    
    # Monta a mensagem final com:
    # título + texto + metadados
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    
    # Exibe tudo formatado
    print(mensagem)


# Chamando a função:
exibir_poema(
    "Zen of Python",  # data_extenso (título)

    # *args → cada string vira uma linha do poema
    "Beautiful is better than ugly.",
    "Explicit is better than implicit.",
    "Simple is better than complex.",
    "Complex is better than complicated.",
    "Flat is better than nested.",
    "Sparse is better than dense.",
    "Readability counts.",
    "Special cases aren't special enough to break the rules.",
    "Although practicality beats purity.",
    "Errors should never pass silently.",
    "Unless explicitly silenced.",
    "In the face of ambiguity, refuse the temptation to guess.",
    "There should be one-- and preferably only one --obvious way to do it.",
    "Although that way may not be obvious at first unless you're Dutch.",
    "Now is better than never.",
    "Although never is often better than *right* now.",
    "If the implementation is hard to explain, it's a bad idea.",
    "If the implementation is easy to explain, it may be a good idea.",
    "Namespaces are one honking great idea -- let's do more of those!",

    # **kwargs → vira metadados (dicionário)
    autor="Tim Peters",
    ano=1999,
)