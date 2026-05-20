# (Manipulação de Forma - Reshape):
# Crie um array unidimensional de 12 elementos e transforme-o em uma matriz 3x4. 
# Em seguida, mude-o novamente para uma matriz 2x6.

import numpy as np

array_unidimensional = np.arange(1, 13)
matriz_3x4 = array_unidimensional.reshape(3, 4)
matriz_2x6 = matriz_3x4.reshape(2, 6)

print("Array unidimensional:", array_unidimensional)
print("Matriz 3x4:\n", matriz_3x4)
print("Matriz 2x6:\n", matriz_2x6)