# 18. Faça um programa que calcule o tempo aproximado de download de um arquivo dado seu
# tamanho (MB) e velocidade da internet (Mbps).

tamanho = float(input("Digite o tamanho do arquivo (MB): "))
velocidade = float(input("Digite a velocidade da internet (Mbps): "))

tempo = (tamanho * 8) / velocidade

print(f"Tempo aproximado de download: {tempo:.2f} segundos")