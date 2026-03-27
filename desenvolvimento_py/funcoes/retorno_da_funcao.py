# Função que recebe uma lista de números
def calcular_total(numeros):
    # A função sum() soma todos os elementos da lista
    return sum(numeros)


# Função que retorna o antecessor e o sucessor de um número
def retrona_antecessor_e_sucessor(numero):
    # Calcula o antecessor (número - 1)
    antecessor = numero - 1
    
    # Calcula o sucessor (número + 1)
    sucessor = numero + 1

    # Retorna os dois valores (em forma de tupla)
    return antecessor, sucessor


# Chamando a função passando uma lista de números
print(calcular_total([10, 20, 34]))

# Chamando a função passando um número
# O retorno será uma tupla: (antecessor, sucessor)
print(retrona_antecessor_e_sucessor(10))