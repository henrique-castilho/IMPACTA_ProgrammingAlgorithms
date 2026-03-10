# 6. Data por extenso: Leia uma data (dd/mm/aaaa) e mostre no formato '29 de Outubro de 1973'.

data = input("Digite uma data (dd/mm/aaaa): ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:10]

meses = {"01": "Janeiro", "02": "Fevereiro", "03": "Março", "04": "Abril",
    "05": "Maio", "06": "Junho", "07": "Julho", "08": "Agosto", "09": "Setembro",
    "10": "Outubro", "11": "Novembro", "12": "Dezembro"
}

mes_extenso = meses[mes]
print(f"{dia} de {mes_extenso} de {ano}")