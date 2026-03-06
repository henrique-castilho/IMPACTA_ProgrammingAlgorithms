# Programa para simular operações de saque bancário com diferentes tipos de conta

# Definição do tipo de conta (apenas uma pode ser True)
conta_normal = False
conta_universitaria = False
conta_especial = True

# Valores da conta e operação
saldo = 2000
saque = 1500  
cheque_especial = 450

# Verifica o tipo de conta e as condições para realizar o saque
if conta_normal:
    # Conta normal: verifica se há saldo suficiente
    if saldo >= saque:
        print("Saque autorizado com sucesso")
    # Se não houver saldo, verifica se pode usar o cheque especial
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial")
    # Se mesmo com cheque especial não for suficiente
    else:
        print("Não foi possível realizar o saque, saldo insuficiente")
# Se não for conta normal, verifica se é conta universitária
elif conta_universitaria:
    # Conta universitária: não tem cheque especial
    if saldo >= saque:
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
# Se não for conta normal nem universitária, verifica se é conta especial
elif conta_especial:
    print("Conta especial selecionada")
# Se não for nenhum dos tipos conhecidos
else:
    print("Sistema não reconheceu seu tipo de conta, entre em contato com o seu gerente.")