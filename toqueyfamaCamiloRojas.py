import random  # Importa el módulo random para generar números aleatorios

# Función que genera un número secreto de 4 dígitos distintos
def generar_numero_secreto():
    digitos = list(range(10))      # Crea una lista con los dígitos del 0 al 9
    random.shuffle(digitos)        # Mezcla los dígitos al azar
    return digitos[:4]             # Devuelve los primeros 4 dígitos (sin repetir)

# Función que compara el número secreto con el intento del jugador
def comparar_numeros(secreto, intento):
    fama = 0   # Contador de "famas" (dígito correcto en la posición correcta)
    toque = 0  # Contador de "toques" (dígito correcto pero en posición incorrecta)

    for i in range(4):  # Recorre cada posición del número
        if intento[i] == secreto[i]:     # Si el dígito coincide en valor y posición
            fama += 1
        elif intento[i] in secreto:      # Si el dígito está pero en otra posición
            toque += 1

    return toque, fama  # Devuelve ambos contadores

## Programa principal
secreto = generar_numero_secreto()  # Llama a la función para crear el número secreto
intentos = 0  # Inicializa contador de intentos

## Mensaje de bienvenida
print("Bienvenido a TOQUE Y FAMA")
print("Adivina el número secreto de 4 cifras (sin repetir dígitos)")

## Bucle principal del juego
while True:
    entrada = input("Ingresa tu número: ")  # Pide número al usuario como cadena

    # Validaciones: debe tener 4 cifras, ser numérico y no repetir dígitos
    if len(entrada) != 4 or not entrada.isdigit() or len(set(entrada)) != 4:
        print("Entrada inválida. Deben ser 4 dígitos distintos.")
        continue  # Vuelve al inicio del bucle si la entrada no es válida

    intento = [int(c) for c in entrada]  # Convierte la entrada a lista de enteros
    intentos += 1  # Aumenta el número de intentos

    toque, fama = comparar_numeros(secreto, intento)  # Compara con el número secreto

    # Muestra el resultado del intento
    print(f"Toques: {toque}, Famas: {fama}")

    if fama == 4:  # Si se acertaron los 4 dígitos en la posición correcta
        print(f"¡Felicidades! Descubriste el número en {intentos} intentos.")
        break  # Termina el juego
