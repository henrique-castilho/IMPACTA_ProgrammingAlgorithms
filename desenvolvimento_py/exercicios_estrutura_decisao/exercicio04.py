# 4. Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ").lower()

if letra in "aeiou":
    print("Você digitou uma vogal")
else:
    print("Vc digitou uma consoante")