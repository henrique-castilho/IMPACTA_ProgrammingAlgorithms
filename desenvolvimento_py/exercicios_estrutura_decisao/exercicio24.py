# 24. Faça um programa que leia 2 números e em seguida pergunte ao
# usuário qual operação ele deseja realizar. O resultado da operação deve ser
# acompanhado de uma frase que diga se o número é:
# • par ou ímpar;
# • positivo ou negativo;
# • inteiro ou decimal.

# Leitura dos números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Pergunta a operação
operacao = input("Qual operação deseja realizar? (+, -, *, /): ")

# Calcula o resultado
if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '*':
    resultado = numero1 * numero2
elif operacao == '/':
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        print("Erro: divisão por zero!")
        exit()
else:
    print("Operação inválida!")
    exit()

# Verifica se é positivo ou negativo
if resultado >= 0:
    pos_neg = "positivo"
else:
    pos_neg = "negativo"

# Verifica se é inteiro ou decimal
if resultado == round(resultado):
    tipo = "inteiro"
else:
    tipo = "decimal"

# Verifica se é par ou ímpar (só faz sentido para inteiros)
if tipo == "inteiro":
    if int(resultado) % 2 == 0:
        par_impar = "par"
    else:
        par_impar = "ímpar"
else:
    par_impar = "não se aplica"

# Mostra o resultado
print(f"Resultado: {resultado}")
print(f"O número é {pos_neg}, {tipo} e {par_impar}.")