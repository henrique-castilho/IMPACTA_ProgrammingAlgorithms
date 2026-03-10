# 13. Palavra embaralhada: Mostre uma palavra com letras embaralhadas e permita que o usuário
# adivinhe.

# Lista de palavras pré-embaralhadas
palavras_originais = ["python", "computador", "teclado", "programacao", "internet"]
palavras_embaralhadas = ["htyonp", "codarmutop", "tacdelo", "pograramoca", "tenirent"]

print("=== JOGO DA PALAVRA EMBARALHADA ===\n")
print("Escolha uma palavra para adivinhar (0 a 4):")
for i in range(len(palavras_originais)):
    print(f"{i}: ???")

escolha = int(input("\nDigite o número: "))
palavra_original = palavras_originais[escolha]
palavra_embaralhada = palavras_embaralhadas[escolha]

tentativas = 3
print(f"\nPalavra embaralhada: {palavra_embaralhada}")
print(f"Dica: tem {len(palavra_original)} letras")
print(f"Você tem {tentativas} tentativas\n")

acertou = False
for i in range(tentativas):
    resposta = input(f"Tentativa {i + 1}/{tentativas}: ").lower()
    
    if resposta == palavra_original:
        print(f"\n🎉 PARABÉNS! Você acertou!")
        print(f"A palavra era: {palavra_original}")
        acertou = True
        break
    else:
        if i < tentativas - 1:
            print(f"✗ Errado! Tente novamente.")
        else:
            print(f"✗ Errado!")

if not acertou:
    print(f"\n💀 Você perdeu!")
    print(f"A palavra era: {palavra_original}")