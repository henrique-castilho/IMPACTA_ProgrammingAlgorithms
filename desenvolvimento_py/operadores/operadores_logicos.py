# AND = Só será True se TODAS as condições forem True
# OR  = Será True se pelo menos UMA condição for True

# Exemplos usando AND
print(True and True and True)      # True  → todas são True
print(True and False and True)     # False → existe um False na expressão
print(False and False and False)   # False → todas são False

# Exemplos usando OR
print(True or True or True)        # True  → todas são True
print(True or False or False)      # True  → existe pelo menos um True
print(False or False or False)     # False → nenhuma é True


saldo = 1000
saque = 250
limite = 200
conta_especial = True

# Expressão sem parênteses.
# O Python avalia primeiro os AND e depois os OR.
# A lógica é:
# (saldo suficiente E dentro do limite)
# OU
# (é conta especial E saldo suficiente)
exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(exp)


# Mesma expressão, mas agora com parênteses para deixar a prioridade explícita.
# O resultado será o mesmo, porém fica mais legível.
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(exp_2)


# Aqui quebramos a lógica em partes para facilitar o entendimento.

# Verifica se é conta normal com saldo suficiente e dentro do limite
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite

# Verifica se é conta especial com saldo suficiente
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

# Se qualquer uma das duas condições for verdadeira, o resultado final será True
exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(exp_3)


# NOT = Inverte o valor lógico (True vira False / False vira True)

# Exemplos simples com NOT
print(not True)   # False → inverte True
print(not False)  # True  → inverte False


# Usando NOT com comparação
# saldo >= saque é True (1000 >= 250)
# Ao usar NOT, o resultado é invertido
print(not saldo >= saque)  # False → porque estava True e foi invertido


# Usando NOT com variável booleana
# conta_especial é True
# NOT inverte para False
print(not conta_especial)  # False → porque conta_especial é True e foi invertido


# NOT também pode negar uma expressão inteira
# Aqui estamos dizendo:
# "Não é conta normal com saldo suficiente"
negacao = not (saldo >= saque and saque <= limite)
print(negacao)