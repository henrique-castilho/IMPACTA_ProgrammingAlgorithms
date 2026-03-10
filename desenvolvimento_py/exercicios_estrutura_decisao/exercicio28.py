# O Hipermercado Tabajara está com uma promoção de carnes que é
# imperdível. Confira:
# • File Duplo: Até 5 Kg -> R$ 4,90 por Kg | Acima de 5 Kg -> R$ 5,80 por Kg
# • Alcatra: Até 5 Kg -> R$ 5,90 por Kg | Acima de 5 Kg -> R$ 6,80 por Kg
# • Picanha: Até 5 Kg -> R$ 6,90 por Kg | Acima de 5 Kg -> R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos
# de carne da promoção, porém não há limites para a quantidade de carne por
# cliente. Se a compra for feita no cartão Tabajara o cliente receberá ainda um
# desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e
# a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo
# as informações da compra: tipo e quantidade de carne, preço total, tipo de
# pagamento, valor do desconto e valor a pagar.

tipo = input("Digite o tipo de carne (F-File Duplo, A-Alcatra, P-Picanha): ").upper()
kg = float(input("Digite a quantidade (Kg): "))
cartao = input("Pagamento no cartão Tabajara? (S/N): ").upper()

# Definir preço
if tipo == "F":
    carne = "File Duplo"
    
    if kg <= 5:
        preco = 4.90
    else:
        preco = 5.80

elif tipo == "A":
    carne = "Alcatra"
    
    if kg <= 5:
        preco = 5.90
    else:
        preco = 6.80

elif tipo == "P":
    carne = "Picanha"
    
    if kg <= 5:
        preco = 6.90
    else:
        preco = 7.80

else:
    print("Tipo inválido")
    exit()

total = kg * preco

# Desconto
if cartao == "S":
    desconto = total * 0.05
else:
    desconto = 0

valor_pagar = total - desconto

# Cupom
print("\n----- CUPOM FISCAL -----")
print(f"Tipo de carne: {carne}")
print(f"Quantidade: {kg} Kg")
print(f"Preço total: R$ {total:.2f}")

if cartao == "S":
    pagamento = "Cartão Tabajara"
else:
    pagamento = "Outro"

print(f"Tipo de pagamento: {pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {valor_pagar:.2f}")