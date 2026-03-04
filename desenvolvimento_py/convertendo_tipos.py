# Convertendo um número decimal (float) para inteiro (int)
# A parte decimal é removida (não arredonda, apenas corta)
print(int(1.97348728))

# Arredondando um número decimal para o inteiro mais próximo
# Round arredonda para o inteiro mais próximo, e em caso de .5, arredonda para o número par mais próximo
print(round(1.97348728))

# Arredondando um número decimal para 2 casas decimais
print(round(1.97348728, 2))

# Convertendo uma string que contém número para inteiro
print(int("10")) 

# Convertendo uma string que contém número decimal para float
print(float("10.10"))

# Convertendo um número inteiro para float
print(float(100))

# Convertendo número para booleano
# 0 é considerado False
print(bool(0))

# Qualquer número diferente de 0 é considerado True
print(bool(1))

# Criando uma variável inteira
valor = 10

# Convertendo o inteiro para string
valor_str = str(valor)

# Mostrando o tipo da variável original
print(type(valor))

# Mostrando o tipo da variável convertida
print(type(valor_str))

# Concatenando (juntando) string com string
# Aqui precisamos converter o número para string para poder juntar com texto
print(str(valor) + " é um número inteiro passado para string")

# Divisão normal (sempre retorna float)
print(100/3)

# Formatando a saída para mostrar apenas 2 casas decimais
print(f"{100/3:.2f}")

# Divisão inteira (retorna apenas a parte inteira da divisão)
print(100//3)