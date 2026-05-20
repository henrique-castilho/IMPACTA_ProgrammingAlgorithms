# (Funções de Agregação): 
# Gere um array com 20 números aleatórios e calcule o valor máximo, o valor mínimo, 
# a média e a soma total dos elementos.

import numpy as np

array_aleatorio = np.random.rand(20) * 100
valor_maximo = np.max(array_aleatorio)
valor_minimo = np.min(array_aleatorio)
media = np.mean(array_aleatorio)
soma_total = np.sum(array_aleatorio)

print("Array de números aleatórios:", array_aleatorio)
print("Valor máximo:", valor_maximo)
print("Valor mínimo:", valor_minimo)
print("Média:", media)
print("Soma total:", soma_total)