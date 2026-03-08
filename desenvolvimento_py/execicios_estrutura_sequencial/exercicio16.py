# 16. Uma loja de tintas precisa calcular quantas latas comprar. 1 litro cobre 3 m2, lata tem 18 litros e custa R$80.

area = float(input("Digite a área em m²: "))

latas = int((area + 53) // 54)
preco = latas * 80

print("Quantidade de latas:", latas)
print("Preço total: R$", preco)