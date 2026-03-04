# Operadores de associação verificam se um valor está presente dentro de uma sequência.
# Usamos:
# in     → verifica se ESTÁ dentro
# not in → verifica se NÃO ESTÁ dentro

frutas = ["limao", "uva"]  # Lista de frutas
curso = "Curso de python"  # String (texto)

# Verifica se "laranja" NÃO está dentro da lista frutas
# Como "laranja" não está na lista, o resultado será True
print("laranja" not in frutas)

# Verifica se "limao" está dentro da lista frutas
# Como está na lista, o resultado será True
print("limao" in frutas)

# Verifica se "Python" está dentro da string
# Atenção: Python diferencia maiúsculas e minúsculas
# Como no texto está "python" (minúsculo), o resultado será False
print("Python" in curso)