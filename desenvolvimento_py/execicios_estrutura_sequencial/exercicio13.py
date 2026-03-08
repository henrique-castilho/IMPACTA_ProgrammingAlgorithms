# 13. Converta um valor em Gigabytes para Megabytes e Kilobytes.

gb = float(input("Digite o valor em Gigabytes: "))

mb = gb * 1024
kb = gb * (1024 ** 2)

print(f"Megabytes: {mb:.2f} MB")
print(f"Kilobytes: {kb:.2f} KB")