# 10. Número por extenso: Leia um número até 99 e mostre-o por extenso.

numero = int(input("Digite um número (0-99): "))

if 0 <= numero <= 99:
    unidades = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenas = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezenas_maiores = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

    if numero < 10:
        print(unidades[numero])
    elif 10 <= numero < 20:
        print(dezenas[numero - 10])
    else:
        dezena = numero // 10
        unidade = numero % 10
        if unidade == 0:
            print(dezenas_maiores[dezena - 2])
        else:
            print(f"{dezenas_maiores[dezena - 2]} e {unidades[unidade]}")