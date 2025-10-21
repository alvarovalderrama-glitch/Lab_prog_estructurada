binario = int(input("Ingrese un número binario: "))
decimal = 0
potencia = 1

while binario > 0:
    digito = binario % 10
    decimal += digito * potencia
    potencia *= 2
    binario //= 10

print(decimal)
