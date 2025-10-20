import random  # Importa el módulo para generar números aleatorios

def generarNumeroAleatorio():
    # Genera un número aleatorio de 4 dígitos sin repetir cifras
    adivinar = ""
    while len(adivinar) < 4:
        posible = str(random.randint(0, 9))
        if posible not in adivinar:
            adivinar += posible
    return adivinar  # Devuelve el número generado

def obtenerNumerosUsuario(mensaje):
    # Pide al usuario un número de 4 dígitos y valida su longitud
    adivinado = input(mensaje)
    while len(adivinado) != 4:
        print("La longitud del número tiene que ser de 4 dígitos.")
        adivinado = input(mensaje)
    return adivinado  # Devuelve el número ingresado

def jugar():
    adivinar = generarNumeroAleatorio()  # Número secreto a adivinar
    
    print("Ingrese el número que desea encontrar: ")
    numero_ingresado = input()
    adivinado = numero_ingresado  # Primer intento del usuario
    
    intentos = 1  # Contador de intentos

    # Repite hasta que el usuario adivine el número
    while adivinado != adivinar:
        fama = 0 
        toque = 0  

        # Compara cada dígito del número ingresado con el número secreto
        for i in range(4):
            if adivinar[i] == adivinado[i]:
                fama += 1
            elif adivinar[i] in adivinado:
                toque += 1

        print(f"Tu número tiene {fama} fama(s) y {toque} toque(s).")
        adivinado = obtenerNumerosUsuario("Escribe otro número: ")
        intentos += 1  # Aumenta el número de intentos

    # Mensaje final cuando el usuario acierta
    print("¡Felicitaciones! Has acertado en " + intentos + " intentos")

# Inicia el juego
jugar()