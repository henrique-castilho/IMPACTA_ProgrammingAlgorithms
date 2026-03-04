# Define uma string com letras maiúsculas e minúsculas
nome ="JoHanN"

# Converte toda a string para maiúsculas
print(nome.upper())
# Converte toda a string para minúsculas
print(nome.lower())
# Converte a primeira letra de cada palavra para maiúscula
print(nome.title())

# String com espaços no início e no final
texto = "   Olá mundo!      "

# Imprime o texto com espaços + "."
print(texto + ".")
# Remove espaços do início e do final (strip) + "."
print(texto.strip() + ".")
# Remove espaços apenas do final (right strip) + "."
print(texto.rstrip() + ".")
# Remove espaços apenas do início (left strip) + "."
print(texto.lstrip() + ".")

# String para demonstrar formatação
menu = "Python"

# Imprime "Python" cercado por "#" manualmente
print("####" + menu + "####")
# Centraliza "Python" em 14 caracteres com espaços
print(menu.center(14))
# Centraliza "Python" em 14 caracteres preenchendo com "#"
print(menu.center(14, "#"))
# Junta cada letra de "Python" com "-" entre elas
print("-".join(menu))
