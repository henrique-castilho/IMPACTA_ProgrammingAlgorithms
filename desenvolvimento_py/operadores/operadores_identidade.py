# Operadores de identidade verificam se duas variáveis
# apontam para o MESMO espaço na memória (não apenas se têm o mesmo valor).

saldo = 1000
limite = 1000

# "is" verifica se as duas variáveis são o mesmo objeto na memória.
# Mesmo tendo o mesmo valor (1000), podem ou não ser o mesmo objeto.
print(saldo is limite)

# "is not" verifica se NÃO são o mesmo objeto na memória.
print(saldo is not limite)