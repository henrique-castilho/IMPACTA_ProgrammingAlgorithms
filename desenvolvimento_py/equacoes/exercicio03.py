# 3) Três amigos somaram suas idades. 
# João tem o dobro da idade de Pedro. 
# Carlos tem a mesma idade de Pedro. 
# A soma das idades é 60 anos. Qual é a idade de cada um?

# Definindo as variáveis:
# Pedro = x
# João = 2x (dobro da idade de Pedro)
# Carlos = x (mesma idade de Pedro)
# Soma: x + 2x + x = 60
# 4x = 60
# x = 15

soma_idades = 60
idade_pedro = soma_idades / 4
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro

if idade_pedro +  idade_joao + idade_carlos == soma_idades:
    print("\nAs idades corretas são:")
    print(f"Idade de Pedro: {int(idade_pedro)} anos") # Converte para inteiro (remove a parte decimal, não arredonda)
    print(f"Idade de João: {idade_joao:.0f} anos") # Formata para mostrar sem casas decimais (arredonda apenas na exibição)
    print(f"Idade de Carlos: {idade_carlos} anos") # Mostra o valor original (15.0)
else:   
    print("As idades estão incorretas.")