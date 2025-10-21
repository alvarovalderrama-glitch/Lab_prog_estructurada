


import random

#  Generar el número secreto (por ejemplo "5831")
digitos = list("0123456789")
random.shuffle(digitos)
numero_secreto = "".join(digitos[:4])

intentos = 0

print(" Bienvenido al juego de Toque y Fama ")
print("Debes adivinar un número secreto de 4 dígitos (sin repetir).")
print("Pistas: Fama = número correcto en posición correcta, Toque = número correcto pero en otra posición.\n")

#  Bucle del juego
while True:
    intento = input(" Ingresa un número de 4 dígitos: ")

    # Validar que el intento sea válido
    if len(intento) != 4:
    print(" Debes ingresar exactamente 4 caracteres.\n")
    continue

solo_digitos = True
for numero in intento:
    if numero not in "0123456789":
        solo_digitos = False
        break

if not solo_digitos:
    print(" Debes ingresar solo números.\n")
    continue

repetido = False
for i in range(len(intento)):
    for j in range(i + 1, len(intento)):
        if intento[i] == intento[j]:
            repetido = True
            break
    if repetido:
        break
if repetido:
    print("no se deben repetir numeros")

    continue

    intentos += 1

    #  Calcular toques y famas
    toques = 0
    famas = 0

    for i in range(4):
        if intento[i] == numero_secreto[i]:
            famas += 1
        elif intento[i] in numero_secreto:
            toques += 1

    # Paso 4: Mostrar pistas
    print(f"Famas: {famas} | Toques: {toques}\n")

    #  Verificar si adivinó
    if famas == 4:
        print(f" ¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")

        break
