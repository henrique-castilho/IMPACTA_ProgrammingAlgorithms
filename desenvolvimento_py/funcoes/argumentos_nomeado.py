# Função que recebe 4 parâmetros obrigatórios
def salvar_carro(marca, modelo, ano, placa):
    # Exibe uma mensagem com os dados do carro
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


# 1️⃣ Argumentos posicionais
# A ordem importa: marca, modelo, ano, placa
salvar_carro("Fiat", "Palio", "1998", "ABC-1234")


# 2️⃣ Argumentos nomeados (keyword arguments)
# A ordem não importa, pois estamos indicando o nome de cada parâmetro
salvar_carro(marca="Fiat", modelo="Palio", ano=1998, placa="ABC-1234")


# 3️⃣ Desempacotamento de dicionário (**kwargs)
# O dicionário precisa ter as mesmas chaves dos parâmetros da função
salvar_carro(**{
    "marca": "Fiat",
    "modelo": "Palio",
    "ano": 1998,
    "placa": "ABC-1234"
})