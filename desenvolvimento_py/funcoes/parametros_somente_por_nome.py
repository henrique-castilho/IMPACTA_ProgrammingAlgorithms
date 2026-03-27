# Função com tipos especiais de parâmetros:
# /  → tudo antes dele é SOMENTE posicional
# *  → tudo depois dele é SOMENTE nomeado (keyword)

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# ✅ Forma correta:
# - modelo, ano, placa → posicionais (SEM nome)
# - marca, motor, combustivel → obrigatoriamente nomeados
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")


# ❌ Forma inválida:
# modelo, ano, placa foram passados como nomeados,
# mas a função exige que sejam posicionais (por causa do /)
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")