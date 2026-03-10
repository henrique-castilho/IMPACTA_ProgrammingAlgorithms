# 26. Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# • Álcool:
# o até 20 litros: desconto de 3% por litro
# o acima de 20 litros: desconto de 5% por litro
# • Gasolina:
# o até 20 litros: desconto de 4% por litro
# o acima de 20 litros: desconto de 6% por litro

# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível
# (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a
# ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 e o
# preço do litro do álcool é R$ 1,90.

# Leitura dos dados
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").strip().upper()

# Preços por litro
preco_alcool = 1.90
preco_gasolina = 2.50

# Inicializa o valor total
valor_total = 0

if tipo == "A":
    # Álcool
    if litros <= 20:
        desconto = 0.03  # 3%
    else:
        desconto = 0.05  # 5%
    valor_total = litros * preco_alcool * (1 - desconto)

elif tipo == "G":
    # Gasolina
    if litros <= 20:
        desconto = 0.04  # 4%
    else:
        desconto = 0.06  # 6%
    valor_total = litros * preco_gasolina * (1 - desconto)

else:
    print("Tipo de combustível inválido!")
    exit()

print(f"Valor a pagar: R$ {valor_total:.2f}")