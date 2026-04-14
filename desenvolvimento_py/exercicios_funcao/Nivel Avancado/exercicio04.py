# 4. Escopo de Variáveis:
# Escreva um programa que demonstra a diferença entre uma variável local e
# uma global dentro de uma função.

contador_global = 0

def incrementar_contador():
    global contador_global
    contador_global += 1

def mostrar_variavel_local():
    contador_local = 10
    print(f"Dentro da função (local): {contador_local}")


def mostrar_variavel_global():
    print(f"Dentro da função (global): {contador_global}")

incrementar_contador()
mostrar_variavel_global()
mostrar_variavel_local()

print(f"Fora da função (global): {contador_global}")
# A linha abaixo causaria erro se fosse executada, porque contador_local
# existe apenas dentro da função mostrar_variavel_local().
# print(contador_local)