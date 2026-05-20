# (Operações Aritméticas): 
# Crie dois arrays de tamanho 4 e realize as quatro operações básicas 
# (soma, subtração, multiplicação e divisão) entre eles, observando como o NumPy 
# processa elemento por elemento.

import numpy as np

array1 = np.array([1, 2, 3, 4])
array2 = np.array([5, 6, 7, 8])

somar = array1 + array2
subtrair = array1 - array2
multiplicar = array1 * array2
dividir = array1 / array2

print("Array 1:", array1)
print("Array 2:", array2)
print("Soma:", somar)
print("Subtração:", subtrair)
print("Multiplicação:", multiplicar)
print("Divisão:", dividir)