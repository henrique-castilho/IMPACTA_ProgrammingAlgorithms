# Função que realiza a soma de dois números
def somar(a, b):
    return a + b


# Função que recebe outra função como parâmetro
def exibir_resultado(a, b, funcao):
    # Chama a função recebida (funcao) passando a e b
    resultado = funcao(a, b)
    
    # Exibe o resultado
    print(f"O resultado da operação {a} + {b} = {resultado}")


# Passando a função "somar" como argumento (SEM parênteses)
exibir_resultado(10, 10, somar)