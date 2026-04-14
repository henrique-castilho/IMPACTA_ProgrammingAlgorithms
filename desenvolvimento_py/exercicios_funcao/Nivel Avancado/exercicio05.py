# 5. Processamento de Lista com Dicionário:
# Crie uma função que receba uma lista de dicionários (produtos) e retorne o
# produto mais caro


def produto_mais_caro(produtos):
	if not produtos:
		return None
	return max(produtos, key=lambda produto: produto["preco"])


# Exemplo de uso
lista_produtos = [
	{"nome": "Teclado", "preco": 120.0},
	{"nome": "Mouse", "preco": 80.0},
	{"nome": "Monitor", "preco": 950.0},
]

mais_caro = produto_mais_caro(lista_produtos)

if mais_caro:
	print("Produto mais caro:", mais_caro["nome"], "- R$", mais_caro["preco"])
else:
	print("Lista vazia.")

