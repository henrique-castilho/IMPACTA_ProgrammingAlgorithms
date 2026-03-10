# 12. Corrigir telefone: Leia um telefone com 7 ou 8 dígitos e ajuste adicionando o '3' se necessário.

telefone = input("Digite um telefone (7 ou 8 dígitos): ")

# Verificar quantidade de dígitos
if len(telefone) == 7:
    telefone_corrigido = "3" + telefone
    print(f"Telefone corrigido: {telefone_corrigido}")
elif len(telefone) == 8:
    print(f"Telefone já está correto: {telefone}")
else:
    print("Erro: O telefone deve ter 7 ou 8 dígitos!")