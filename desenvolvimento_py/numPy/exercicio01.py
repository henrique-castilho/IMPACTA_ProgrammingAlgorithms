# (Criação Básica): Crie um array NumPy a partir de uma lista
# contendo os números de 1 a 5 e imprima o resultado e o tipo do objeto para
# confirmar que é um ndarray.

import numpy as np

lista = [1, 2, 3, 4, 5]

array_nump = np.array(lista)

print("Lista original:", lista)
print("Array NumPy criado a partir da lista:", array_numpy)
print("Tipo do array:", type(array_numpy))