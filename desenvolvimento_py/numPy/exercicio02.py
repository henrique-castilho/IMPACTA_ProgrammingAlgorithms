#(Propriedades do Array):
# Construa um array bidimensional (matriz) e utilize comandos 
# para exibir a sua forma (shape), o número de dimensões (ndim) e o 
# tipo de dado dos elementos (dtype).

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6]])
print("Matriz:\n", matriz)
print("Forma (shape):", matriz.shape)
print("Número de dimensões (ndim):", matriz.ndim)
print("Tipo de dado dos elementos (dtype):", matriz.dtype)