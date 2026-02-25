# 2 Multiplique um número por 3 e subtraia 9. O resultado é igual ao próprio número.

num = int(input("Digite um número: "))

resultado = (num * 3) - 9

if resultado == num:
    print(f"Parabéns! {num} é o número correto!")
    print(f"({num} * 3) - 9 = {resultado}")
else: 
    print(f"O número {num} não é da o mesmo resultado.")
    print(f"({num} * 3) - 9 = {resultado}, não {num}")
