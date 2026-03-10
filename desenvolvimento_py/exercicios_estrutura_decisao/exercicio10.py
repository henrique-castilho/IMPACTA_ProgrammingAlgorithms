# 10. Faça um programa que pergunte em que turno você estuda. Peça para digitar:
# • M - Matutino
# • V - Vespertino
# • N - Noturno. 
# Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
# ou "Valor Inválido!", conforme o caso.

turno = input("Em que turno você estuda? (M/V/N): ").lower()

if turno == "m" or turno == "matutino":
    print("Bom dia!")
elif turno == "v" or turno == "vespertino":
    print("Boa Tarde!")
elif turno == "n" or turno == "noturno":
    print("Boa Noite!")
else:
    print("Valor Iválido")
