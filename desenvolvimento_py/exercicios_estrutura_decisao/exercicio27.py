# 27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:
# • Morango: Até 5 Kg -> R$ 2,50 por Kg | Acima de 5 Kg -> R$ 2,20 por Kg
# • Maçã: Até 5 Kg -> R$ 1,80 por Kg | Acima de 5 Kg -> R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar
# R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um
# algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de
# maçãs adquiridas e escreva o valor a ser pago pelo cliente.

kg_morango = float(input("Digite a quantidade de morangos (Kg): "))
kg_maca = float(input("Digite a quantidade de maçãs (Kg): "))

# Preço do morango
if kg_morango <= 5:
    preco_morango = kg_morango * 2.50
else:
    preco_morango = kg_morango * 2.20

# Preço da maçã
if kg_maca <= 5:
    preco_maca = kg_maca * 1.80
else:
    preco_maca = kg_maca * 1.50

# Total
total = preco_morango + preco_maca
peso_total = kg_morango + kg_maca

# Desconto de 10%
if peso_total > 8 or total > 25:
    total = total * 0.90

print(f"Valor a pagar: R$ {total:.2f}")