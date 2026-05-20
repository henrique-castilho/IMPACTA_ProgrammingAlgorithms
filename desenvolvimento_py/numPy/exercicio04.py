# (Indexação e Slicing 1D):
# Dado um array de 10 elementos, extraia apenas os elementos
# do índice 3 ao 7 e inverta a ordem dos elementos usando fatiamento.

import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
sub_array = array[3:8][::-1]

print("Array original:", array)
print("Sub-array extraído e invertido:", sub_array)