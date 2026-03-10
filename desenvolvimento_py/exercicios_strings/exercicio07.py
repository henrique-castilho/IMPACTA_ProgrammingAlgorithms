# 7. Contar espaços e vogais: Dada uma frase, conte quantos espaços 
# existem e quantas vezes aparecem as vogais.

frase = input("Digite uma frase: ")

contador_espacos = 0
contador_vogais = 0

for char in frase:
    if char == " ":
        contador_espacos += 1
    elif char.lower() in "aeiou":
        contador_vogais += 1
        
print(f"Quantidade de espaços: {contador_espacos}")
print(f"Quantidade de vogais: {contador_vogais}")
