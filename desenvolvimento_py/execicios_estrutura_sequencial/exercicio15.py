# 15. Faça um programa que calcule o salário com descontos: IR (11%), INSS (8%) e Sindicato (5%).
# Mostrar salário bruto e líquido.

salario_bruto = float(input("Digite o salário bruto: "))

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"IR (11%): R$ {ir:.2f}")
print(f"INSS (8%): R$ {inss:.2f}")
print(f"Sindicato (5%): R$ {sindicato:.2f}")
print(f"Salário líquido: R$ {salario_liquido:.2f}")