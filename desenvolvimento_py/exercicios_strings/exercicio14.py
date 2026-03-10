# 14. Leet Speak: Leia um texto e converta para a escrita estilo leet (ex: 1337).

texto = input("Digite um texto: ")

# Dicionário de conversão leet speak
leet = {
    'a': '4', 'A': '4',
    'e': '3', 'E': '3',
    'i': '1', 'I': '1',
    'o': '0', 'O': '0',
    's': '5', 'S': '5',
    't': '7', 'T': '7',
    'l': '1', 'L': '1',
    'g': '9', 'G': '9',
    'b': '8', 'B': '8'
}

# Converter texto para leet speak
texto_leet = ""
for letra in texto:
    if letra in leet:
        texto_leet += leet[letra]
    else:
        texto_leet += letra

print(f"Texto original: {texto}")
print(f"Leet speak: {texto_leet}")