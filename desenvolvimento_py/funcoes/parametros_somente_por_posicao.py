def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


# Correto
criar_carro(
    "Palio", 1999, "ABC-1234",  # esses 3 são posicionais (obrigatório)
    marca="Fiat", motor="1.0", combustivel="Gasolina"
)


#  Inválido
criar_carro(
    modelo="Palio",  # ERRO: 'modelo' está antes do /, então não pode ser nomeado
    ano=1999,        # ERRO: 'ano' também é positional-only
    placa="ABC-1234",# ERRO: 'placa' também é positional-only
    marca="Fiat", 
    motor="1.0", 
    combustivel="Gasolina"
)

# Motivo do erro:
# O símbolo "/" na definição da função indica que
# tudo que vem antes dele (modelo, ano, placa)
# só pode ser passado de forma POSICIONAL.
#
# Ou seja, NÃO pode usar:
# modelo=..., ano=..., placa=...
#
# ✔ O correto seria sempre:
# criar_carro("Palio", 1999, "ABC-1234", ...)