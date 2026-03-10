# 1. Tamanho de strings: Leia duas strings, mostre o conteúdo e o tamanho de cada uma.
# Informe se possuem o mesmo tamanho e se o conteúdo é igual ou diferente.

string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

print(f"String 1: '{string1}' - Tamanho: {len(string1)}")
print(f"String 2: '{string2}' - Tamanho: {len(string2)}")

if len(string1) == len(string2):
    print("As strings possuem o mesmo tamanho.")
else:
    print("As strings possuem tamanhos diferentes.")

if string1 == string2:
    print("As strings possuem o mesmo conteúdo.")
else:
    print("As strings possuem conteúdo diferente.")