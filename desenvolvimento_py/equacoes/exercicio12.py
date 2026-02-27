# 12) Qual é o número cujo quádruplo subtraído de 5 dá o mesmo que seu dobro somado com 11?
# Equação:
# 4x - 5 = 2x + 11
# 4x - 2x = 11 + 5
# 2x = 16
# x = 8

x = 8

lado_esquerdo = (4 * x) - 5
lado_direito = (2 * x) + 11

if lado_esquerdo == lado_direito:
    print(f"O número que atende ao critério é {x}")
    print(f"Verificação:")
    print(f"Quádruplo de {x} subtraído de 5: (4 * {x}) - 5 = {lado_esquerdo}")
    print(f"Dobro de {x} somado com 11: (2 * {x}) + 11 = {lado_direito}")
else:
    print("O número não atende ao critério.")