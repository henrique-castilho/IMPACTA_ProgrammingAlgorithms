# 09) O quádruplo de um número mais 10 é igual ao triplo do mesmo número mais 22.

# Equação
# 4x + 10 = 3x + 22
# 4x - 3x = 22 - 10
# x = 12

x = 12

lado_esquerdo = (4 * x) + 10
lado_direito = (3 * x) + 22

if lado_esquerdo == lado_direito:
    print(f"O número que atende ao critério é {x}")
    print(f"Verificação:")
    print(f"Quádruplo de {x} mais 10: (4 * {x}) + 10 = {lado_esquerdo}")
    print(f"Triplo de {x} mais 22: (3 * {x}) + 22 = {lado_direito}")
else:
    print("O número não atende ao critério.")

