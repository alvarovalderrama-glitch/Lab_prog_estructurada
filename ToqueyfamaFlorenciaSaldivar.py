import random

print("=== Juego de FAMAS y TOQUES ===")
print("Adivina el número secreto de 4 cifras (todas distintas)")

# Generar los 4 dígitos distintos (A, B, C, D)
A = random.randint(0, 9)
B = random.randint(0, 9)
while B == A:
    B = random.randint(0, 9)

C = random.randint(0, 9)
while C == A or C == B:
    C = random.randint(0, 9)

D = random.randint(0, 9)
while D == A or D == B or D == C:
    D = random.randint(0, 9)

# Guardar el número secreto como lista
secreto = [A, B, C, D]

intentos = 0
fama = 0

# Mientras no haya ganado y tenga menos de 3 intentos
while intentos < 3 and fama != 4:
    fama = 0
    toque = 0
    intentos += 1

    numero = input(f"Intento {intentos}: Ingresa tu número de 4 cifras: ")

    # Convertir el número del jugador en lista de enteros
    if len(numero) != 4 or not numero.isdigit():
        print("Entrada inválida. Debe ser un número de 4 dígitos.")
        continue

    jugador = [int(numero[0]), int(numero[1]), int(numero[2]), int(numero[3])]

    # Comparar con el número secreto
    for i in range(4):
        if jugador[i] == secreto[i]:
            fama += 1
        elif jugador[i] in secreto:
            toque += 1

    print("Famas:", fama, " Toques:", toque)

# Resultado final
if fama == 4:
    print("Adivinaste el número secreto:", secreto)
else:
    print("Perdiste. El número secreto era:", secreto)
