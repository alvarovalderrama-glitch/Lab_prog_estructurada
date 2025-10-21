#Binario a decimal
# Convierte una cadena binaria (0 y 1) a base 10 con validación.

binario = input("Ingresa un número binario: ").strip()               # Lee texto
if all(c in "01" for c in binario) and binario != "":                # Valida dígitos
    decimal = 0                                                      # Acumulador
    for c in binario:                                                # Recorre bits
        decimal = decimal * 2 + int(c)                               # Desplaza y suma
    print(f"{binario} (bin) = {decimal} (dec)")                      # Muestra
else:
    print("Entrada inválida: usa solo 0 y 1.")
