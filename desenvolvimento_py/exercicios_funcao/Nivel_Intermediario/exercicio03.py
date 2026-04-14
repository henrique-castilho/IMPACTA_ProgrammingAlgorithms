# 3. Contador de Vogais:
# Faça uma função que receba uma string e retorne a quantidade de vogais
# nela.

def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0
    for char in texto:
        if char in vogais:
            contador +=1
    return contador


frase = input("Digite uma frase: ")
quantidade_vogais = contar_vogais(frase)
print(f"A quantidade de vogais na frase é: {quantidade_vogais}")