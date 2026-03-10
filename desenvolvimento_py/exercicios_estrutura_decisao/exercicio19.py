# 19. Faça um programa que leia um número inteiro menor que 1000 e
# imprima a quantidade de centenas, dezenas e unidades do mesmo. Observando
# os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# • 326 = 3 centenas, 2 dezenas e 6 unidades
# • 12 = 1 dezena e 2 unidades

numero = int(input("Digite um número inteiro: "))

if numero < 1000:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10
    print(centenas, "centenas,", dezenas, "dezenas e", unidades, "unidades")

else:
    print("Número tem que ser menor que 1000")
