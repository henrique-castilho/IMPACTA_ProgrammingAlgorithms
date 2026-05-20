# (Filtros e Máscaras Booleanas):
# A partir de um array de números inteiros, utilize uma máscara booleana
# para criar um novo array contendo apenas os números que são maiores que 10.

import numpy as np

array_inteiros = np.array([5, 12, 7, 20, 3, 15, 8])
mascara = array_inteiros > 10
array_filtrado = array_inteiros[mascara]

print("Array original:", array_inteiros)
print("Máscara booleana (números maiores que 10):", mascara)
print("Array filtrado (números maiores que 10):", array_filtrado)