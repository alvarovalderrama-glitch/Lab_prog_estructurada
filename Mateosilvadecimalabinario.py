#Decimal a binario
# Convierte un entero decimal >= 0 a su representación binaria.

texto = input("Ingresa un entero >= 0: ").strip()   # Lee texto
if texto.isdigit():                                 # Verifica entero no negativo
    n = int(texto)                                  # Convierte
    if n == 0:                                      # Caso especial 0
        print("0")
    else:
        bits = ""                                   # Acumula bits al revés
        while n > 0:                                # Repite divisiones por 2
            bits = str(n % 2) + bits               # Añade resto (0/1) al inicio
            n //= 2                                 # Divide entero entre 2
        print(bits)                                 # Imprime binario
else:
    print("Entrada inválida.")
