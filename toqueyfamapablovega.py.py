import random

# Juego: Toque y Fama (versión simple)
# El jugador debe adivinar un número secreto entre 0 y 9.
# "Fama" = número correcto en la posición correcta.
# "Toque" = número correcto en posición incorrecta.

print("TOQUE Y FAMA")

# Generar número secreto de 3 dígitos (sin repetidos)
secreto = "".join(random.sample("0123456789", 3))

intentos = 0

while True:
    intento = input("Adivina el número de 3 dígitos: ")
    if len(intento) != 3 or not intento.isdigit():
        print("Debes ingresar exactamente 3 dígitos.")
        continue

    intentos += 1

    # Calcular toques y famas
    famas = sum(intento[i] == secreto[i] for i in range(3))
    toques = sum(d in secreto for d in intento) - famas

    print(f"{famas} fama(s), {toques} toque(s)")

    if famas == 3:
        print(f"¡Correcto! El número era {secreto}.")
        print(f"Intentos: {intentos}")
        break
