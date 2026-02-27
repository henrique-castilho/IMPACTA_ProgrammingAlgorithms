# 5) O triplo de um número menos 5 é igual ao dobro do mesmo número mais 1."

# Equação:
# 3x - 5 = 2x + 1
# 3x -2x = 5 + 1
# x = 6

numero = 6

lado_esquerdo = (3 * numero) - 5
lado_direito = (2 * numero) + 1

print(f"O número é: {numero}")
print(f"Verificação:")
print(f"Triplo do {numero} menos 5: (3 * {numero}) - 5 = {lado_esquerdo}")
print(f"Dobro do {numero} mais 1: (2 * {numero}) + 1 = {lado_direito}")
print(f"Verificação: {lado_esquerdo} == {lado_direito} ? {lado_esquerdo == lado_direito}")