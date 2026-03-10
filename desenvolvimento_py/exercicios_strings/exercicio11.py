# 11. Jogo da Forca: Desenvolva um jogo simples da forca usando uma lista de palavras.

# Lista de palavras
palavras = ["python", "programacao", "computador", "teclado", "mouse", "internet"]

# Escolher palavra (sem import random)
print("Escolha uma palavra (0 a 5):")
for i in range(len(palavras)):
    print(f"{i}: ???")
    
escolha = int(input("Digite o número: "))
palavra_secreta = palavras[escolha]

# Configurações do jogo
tentativas_max = 6
tentativas_erradas = 0
letras_certas = []
letras_erradas = []

print(f"\n=== JOGO DA FORCA ===")
print(f"A palavra tem {len(palavra_secreta)} letras")
print(f"Você tem {tentativas_max} tentativas\n")

# Loop principal do jogo
while tentativas_erradas < tentativas_max:
    # Mostrar palavra com letras descobertas
    palavra_exibida = ""
    for letra in palavra_secreta:
        if letra in letras_certas:
            palavra_exibida += letra + " "
        else:
            palavra_exibida += "_ "
    
    print(f"Palavra: {palavra_exibida}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")
    print(f"Tentativas restantes: {tentativas_max - tentativas_erradas}")
    
    # Verificar vitória
    vitoria = True
    for letra in palavra_secreta:
        if letra not in letras_certas:
            vitoria = False
            break
    
    if vitoria:
        print(f"\n🎉 PARABÉNS! Você venceu!")
        print(f"A palavra era: {palavra_secreta}")
        break
    
    # Pedir letra
    chute = input("\nDigite uma letra: ").lower()
    
    # Validar entrada
    if len(chute) != 1 or not chute.isalpha():
        print("Digite apenas uma letra!")
        continue
    
    # Verificar se já foi usada
    if chute in letras_certas or chute in letras_erradas:
        print("Você já tentou essa letra!")
        continue
    
    # Verificar se a letra está na palavra
    if chute in palavra_secreta:
        letras_certas.append(chute)
        print(f"✓ Letra '{chute}' está na palavra!")
    else:
        letras_erradas.append(chute)
        tentativas_erradas += 1
        print(f"✗ Letra '{chute}' NÃO está na palavra!")
    
    print()

# Verificar derrota
if tentativas_erradas >= tentativas_max:
    print(f"\n💀 GAME OVER!")
    print(f"A palavra era: {palavra_secreta}")
