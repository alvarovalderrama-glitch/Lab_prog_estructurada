binario = input("ingresa un número binario: ")
decimal = 0
potencia = 0

# Recorremos el número de derecha a izquierda
for digito in binario[::-1]:
    decimal += int(digito) * (2 ** potencia)
    potencia += 1

print("El número decimal es:", decimal)