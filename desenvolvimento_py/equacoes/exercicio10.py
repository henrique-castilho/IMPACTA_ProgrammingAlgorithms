# 10) Cinco vezes um número somado com 2 é igual ao número multiplicado por 7.
# Equação:
# 5x + 2 = 7x
# 5x - 7x = -2
# -2x = -2
# x = -2 / -2
# x = 1

x = 1

lado_esquerdo = (5 * x) + 2
lado_direito = 7 * x

if lado_esquerdo == lado_direito:
    print(f"O número que atende ao critério é {x}")
    print(f"Verificação:")
    print(f"Cinco vezes {x} somado com 2: (5 * {x}) + 2 = {lado_esquerdo}")
    print(f"Número multiplicado por 7: 7 * {x} = {lado_direito}")
else:    
    print("O número não atende ao critério.")