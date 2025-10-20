import random
"""def juego_toque_y_fama():
        generarnumero_secreto (4 dígitos distintos)
        intentos = 0
        max_intentos = 10
        solucion = False

    while(intentos < max_intentos and not solucion):
        pedir intento al jugador

        if(intento no es válido):
            mostrar "Entrada inválida"
            continuar

        calcular toques y famas entre intento y secreto

        if(famas == 4):
            mostrar "Ganaste"
             solucion = True
            else:
                mostrar cantidad de toques y famas

        aumentar contador de intentos

     if(not solucion):
            mostrar "Perdiste"
            mostrar numero_secreto
"""
def generar_numero():
    """Genera un número secreto de 4 dígitos distintos"""
    cifras = random.sample('0123456789', 4)
    if cifras[0] == '0':
        cifras[0], cifras[1] = cifras[1], cifras[0]
    return ''.join(cifras)

def evaluar_intento(secreto, intento):
    """Compara el intento del jugador con el número secreto"""
    fama = sum(a == b for a, b in zip(secreto, intento))
    toque = sum(c in secreto for c in intento) - fama
    return toque, fama

def juego_toque_y_fama():
    print(" Bienvenido al juego TOQUE Y FAMA ")
    secreto = generar_numero()
    intentos = 0
    MAX_INTENTOS = 10

    while intentos < MAX_INTENTOS:
        intento = input(f"\n Intento {intentos + 1}/{MAX_INTENTOS} → Ingresa un número de 4 cifras distintas: ")

        # Validar entrada
        if len(intento) != 4 or not intento.isdigit() or len(set(intento)) != 4:
            print(" Entrada inválida. Asegúrate de que sean 4 dígitos distintos.")
            continue

        intentos += 1
        toque, fama = evaluar_intento(secreto, intento)
        print(f" Toques: {toque}, Famas: {fama}")

        if fama == 4:
            print(f"\n ¡Felicitaciones! Adivinaste el número {secreto} en {intentos} intentos.")
            break
    else:
        # Solo se ejecuta si el while termina sin break
        print(f"\n Se acabaron los intentos. El número secreto era: {secreto}")

# Ejecutar el juego
juego_toque_y_fama()