#  JUEGO: TOQUE Y FAMA

import os
import random

# Función 1: generar_numero_secreto
# Genera un número aleatorio de 4 cifras sin repetir los dígitos.
def generar_numero_secreto():
    digitos = []
    for i in range(4):
        while True:
            # El primer dígito no puede ser 0
            if i == 0:
                digito = random.randint(1, 9)
            else:
                digito = random.randint(0, 9)
            if str(digito) not in digitos:
                digitos.append(str(digito))
                break
    return digitos


# Función 2: pedir_numero_usuario
# Solicita al jugador un número válido (4 cifras sin repetir).
def pedir_numero_usuario():
    while True:
        try:
            numero = input("Ingresa un número de 4 cifras (sin repetir dígitos): ")

            # Verificar que tenga exactamente 4 caracteres
            if len(numero) != 4:
                print("Debe tener exactamente 4 cifras.")
                continue

            # Verificar que sean solo dígitos
            if not numero.isdigit():
                print("Solo se permiten números.")
                continue

            # Verificar que los dígitos no se repitan
            if len(set(numero)) != 4:
                print("Los dígitos no deben repetirse.")
                continue

            return list(numero)  # Se retorna como lista de caracteres
        except ValueError:
            print("Entrada no válida. Inténtalo de nuevo.")


# Función 3: comparar_numeros
# Compara el número del jugador con el número secreto.
# Devuelve el número de toques y famas.

def comparar_numeros(secreto, intento):
    famas = 0
    toques = 0

    for i in range(4):
        if intento[i] == secreto[i]:
            famas += 1
        elif intento[i] in secreto:
            toques += 1
    return famas, toques


# Función principal: juego_toque_y_fama
# Controla todo el flujo del juego.

def juego_toque_y_fama():
    print("========================================")
    print("¡BIENVENIDO AL JUEGO!: TOQUE Y FAMA")
    print("========================================\n")
    print("Reglas:")
    print("1 El sistema genera un número de 4 cifras sin repetir.")
    print("2 Tienes 7 intentos.")
    print("3 'FAMA' = dígito correcto en la posición correcta.")
    print("4 'TOQUE' = dígito correcto pero en la posición incorrecta.")
    print("")

    numero_secreto = generar_numero_secreto()
    intentos = 7
    famas = 0

    while intentos > 0 and famas != 4:
        print("Intentos restantes: "+ str (intentos))
        intento = pedir_numero_usuario()

        famas, toques = comparar_numeros(numero_secreto, intento)

        print("FAMAS:" +str(famas)+ "| TOQUES: "+ str(toques))

        if famas == 4:
            print("¡MUY BIEN! Adivinaste el número secreto")
            print("")
            break

        intentos -= 1

    if famas != 4:
        print("\n Te quedaste sin intentos. Perdiste")
        print(f"El número era: {''.join(numero_secreto)}")


# Ejecución del juego
os.system ("cls")
juego_toque_y_fama()