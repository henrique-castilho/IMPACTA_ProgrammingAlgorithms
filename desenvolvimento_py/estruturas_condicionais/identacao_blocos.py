# Função para realizar saque
def sacar(valor):
    # Saldo disponível na conta
    saldo = 500

    # Verifica se há saldo suficiente para o saque
    # BLOCO IF: identado com 4 espaços
    if saldo >= valor:
        # Estas duas linhas pertencem ao bloco IF (identadas com 8 espaços)
        # Só executam se a condição for verdadeira
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    # Esta linha está no mesmo nível do IF (identação de 4 espaços)
    # Pertence ao bloco da função, MAS NÃO ao bloco do IF
    # Executa SEMPRE, independente da condição
    print("Obrigado por ser nosso cliente, tenha um bom dia!")


# Função para realizar depósito
def depositar(valor):
    # Saldo inicial
    saldo = 500
    # Adiciona o valor depositado ao saldo
    saldo += valor


# Chamada da função com valor de 1000
# Como saldo (500) < valor (1000), não entra no bloco IF
# Mas a mensagem final sempre aparece
sacar(1000)