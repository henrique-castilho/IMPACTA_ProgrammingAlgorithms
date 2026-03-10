# 8. Faça um programa que pergunte o preço de três produtos e informe
# qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input("Digite o preço do primeiro produto: "))
produto2 = float(input("Digite o preço do segundo produto: "))
produto3 = float(input("Digite o preço do terceiro produto: "))

menor = min(produto1, produto2, produto3)

if produto1 == produto2 == produto3:
    print("Todos os produtos têm o mesmo preço.")
elif produto1 == menor and produto2 == menor:
    print(f"Você pode comprar o produto 1 ou 2, ambos custam R${menor}")
elif produto1 == menor and produto3 == menor:
    print(f"Você pode comprar o produto 1 ou 3, ambos custam R${menor}")
elif produto2 == menor and produto3 == menor:
    print(f"Você pode comprar o produto 2 ou 3, ambos custam R${menor}")
elif produto1 == menor:
    print(f"Você deve comprar o produto 1, custa R${produto1}")
elif produto2 == menor:
    print(f"Você deve comprar o produto 2, custa R${produto2}")
else:
    print(f"Você deve comprar o produto 3, custa R${produto3}")