# 5. Inverter String:
# Crie uma função que receba uma frase e retorne a frase invertida
# (ex: "python" -> "nohtyp")

def inverter_string(frase):
    return frase[::-1]


frase = input("Digite uma frase: ")
frase_invertida = inverter_string(frase)
print(f"A frase invertida é: {frase_invertida}")