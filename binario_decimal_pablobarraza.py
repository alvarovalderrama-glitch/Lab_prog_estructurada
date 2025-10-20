binario = input("Ingresa un número binario: ")
decimal = 0
potencia = 0

for digito in binario[::-1]:
    decimal += int(digito) * (2 ** potencia)
    potencia += 1

print("El número decimal es:", decimal)
