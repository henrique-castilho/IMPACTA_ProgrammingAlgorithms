# 17. Versão avançada da tinta: 1 litro cobre 6 m2. Lata 18L (R$80) e galão 3,6L (R$25). 
# Calcular melhor opção com 10% de folga.

area = float(input("Digite a área em m²: "))

area_total = area * 1.10
litros = area_total / 6

latas = int(litros // 18)
resto = litros % 18

galoes = int(resto // 3.6)
if resto % 3.6 != 0:
    galoes += 1

preco = latas * 80 + galoes * 25

print(f"Área com folga: {area_total:.2f} m²")
print(f"Litros necessários: {litros:.2f} L")
print(f"Latas: {latas}")
print(f"Galões: {galoes}")
print(f"Preço total: R$ {preco:.2f}")