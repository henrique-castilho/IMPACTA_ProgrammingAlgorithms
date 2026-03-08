# 10. Faça um programa que peça a temperatura em Celsius e converta para Fahrenheit.
#  Fórmula: F = (C * 9/5) + 32.

temp_Celsius = float(input("Digite a temperatura em Celsius: "))

temp_Fahrenheit = (temp_Celsius * 9 / 5) + 32

print(f"A temperatura em Fahrenheit é {temp_Fahrenheit:.1f}")