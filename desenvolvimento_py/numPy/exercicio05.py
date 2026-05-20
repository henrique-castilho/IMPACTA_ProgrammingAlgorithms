# (Indexação Multidimensional): 
# Crie uma matriz 3x3 com valores de sua escolha e acesse especificamente 
# o elemento central (segunda linha, segunda coluna).

import numpy as np

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
elemento_central = matriz[1, 1]

print("Matriz:\n", matriz)
print("Elemento central (segunda linha, segunda coluna):", elemento_central)