salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(f"O salario com bonus é: {salario_bonus(500)}")