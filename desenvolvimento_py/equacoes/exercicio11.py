# 11) Um número somado ao triplo de seu sucessor resulta em 74. Qual é esse número?
# Equação:
# x + 3(x + 1) = 74
# x + 3x + 3 = 74
# 4x + 3 = 74
# 4x = 71
# x = 71 / 4

x = 71 / 4

lado_esquerdo = x + (3 * (x + 1))
lado_direito = 74

if lado_esquerdo == lado_direito:
    print(f"O número que atende ao critério é {x}")
    print(f"Verificação:")
    print(f"O número {x} somado ao triplo de seu sucessor: {x} + (3 * ({x} + 1)) = {lado_esquerdo}")
    print(f"Resultado esperado: {lado_direito}")
else:
    print("O número não atende ao critério.")