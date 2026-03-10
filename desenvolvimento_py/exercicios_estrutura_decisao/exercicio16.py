# 16. Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. 
# O programa deverá pedir os valores de a, b e c
# e fazer as consistências, informando ao usuário nas seguintes situações:

# • Se o usuário informar o valor de A igual a zero, a equação não é do segundo
# grau e o programa não deve pedir os demais valores, sendo encerrado;

# • Se o delta calculado for negativo, a equação não possui raízes reais.
# Informe ao usuário e encerre o programa;

# • Se o delta calculado for igual a zero a equação possui apenas uma raiz real;
# informe-a ao usuário;

# • Se o delta for positivo, a equação possui duas raízes reais; informe-as aousuário;

import math

a = float(input("Digite o valor de a: "))

if a == 0:
    print("Não é uma equação do segundo grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))

    delta = b**2 - 4*a*c

    if delta < 0:
        print("A equação não possui raízes reais.")

    elif delta == 0:
        x = -b / (2*a)
        print("A equação possui apenas uma raiz real:")
        print("x =", x)
    
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)

        print("A equação possui duas raízes reais:")
        print("x1 =", x1)
        print("x2 =", x2)
