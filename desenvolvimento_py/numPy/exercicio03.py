# (Sequências Numéricas): 
# Utilize as funções np.arange() para
# criar um array de 0 a 20 com passos de 2, e np.linspace() para criar 5 valores
# igualmente espaçados entre 0 e 1.

import numpy as np

array_arange = np.arange(0, 21, 2)
array_linspace = np.linspace(0, 1, 5)

print("Array criado com np.arange():", array_arange)
print("Array criado com np.linspace():", array_linspace)