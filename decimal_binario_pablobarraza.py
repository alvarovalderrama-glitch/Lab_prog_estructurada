# Pedimos al usuario un número decimal
decimal = int(input("Ingresa un número decimal: "))

# Variable para ir guardando el binario como texto
binario = ""

# Mientras el número sea mayor que 0
while decimal > 0:
    # Tomamos el resto (0 o 1) y lo agregamos al inicio del texto
    binario = str(decimal % 2) + binario
    # Dividimos el número entre 2 (descartando decimales)
    decimal = decimal // 2

# Mostramos el resultado
print("El número binario es:", binario)
