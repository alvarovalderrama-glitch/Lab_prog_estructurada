
import random

def generar_numero():
    """Genera un número secreto de 3 dígitos distintos."""
    digitos = random.sample(range(0, 10), 3)
    return ''.join(map(str, digitos))

def comparar_numeros(secreto, intento):
    """Compara el número del jugador con el secreto y retorna toques y famas."""
    toques = 0
    famas = 0
    for i in range(3):
        if intento[i] == secreto[i]:
            famas += 1
        elif intento[i] in secreto:
            toques += 1
    return toques, famas

def juego():
    """Función principal del juego."""
    secreto = generar_numero()
    print("Bienvenido al juego TOQUE Y FAMA")
    # print("DEBUG:", secreto)  # Quita el comentario si quieres ver el número secreto
    intentos = 0

    while True:
        intento = input("Ingresa un número de 3 dígitos distintos: ")
        if len(intento) != 3 or not intento.isdigit():
            print("Por favor, ingresa exactamente 3 números.")
            continue

        intentos += 1
        toques, famas = comparar_numeros(secreto, intento)
        print(f"Toques: {toques}, Famas: {famas}")

        if famas == 3:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

juego()
