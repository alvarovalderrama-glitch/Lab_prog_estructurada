binario=input("Ingrese un número binario: ")
decimal=0
potencia=0

#Se recorre el número binario de derecha a izquierda
for digito in binario[::-1]:
    decimal += int(digito) * (2 ** potencia)
    potencia += 1

print(f"El número decimal es: {decimal}")
# Conversor de binario a decimal