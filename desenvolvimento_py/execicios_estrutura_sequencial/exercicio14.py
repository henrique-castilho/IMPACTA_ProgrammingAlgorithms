# 14. Um pescador paga multa de R$4,00 por quilo excedente caso ultrapasse 50 kg de peixes. 
# Faça um programa que calcule excesso e multa.

peso = float(input("Digite o peso dos peixes (kg): "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
else:
    excesso = 0
    multa = 0

print(f"Excesso: {excesso} kg")
print(f"Multa: R$ {multa}")