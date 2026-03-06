saldo = 2000
saque = 2500

# Operador Ternário (Condicional Ternária)
# Sintaxe: valor_se_verdadeiro if condição else valor_se_falso
# Se saldo >= saque, status recebe "Sucesso"
# Caso contrário, status recebe "Saldo insuficiente"
status = "Sucesso" if saldo >= saque else "Saldo insuficiente"

# Exibindo o resultado da operação
print(f"{status} ao realizar o saque!")