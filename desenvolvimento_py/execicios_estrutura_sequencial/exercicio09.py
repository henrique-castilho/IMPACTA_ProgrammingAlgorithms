# 9. Faça um programa que peça a temperatura em Fahrenheit e converta para Celsius. 
# Fórmula: C = 5 * ((F - 32) / 9).

temp_Fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

temp_Celsius = 5 * ((temp_Fahrenheit - 32) / 9)

print(f"A temperatura em Celsius é {temp_Celsius:.1f} ºC")