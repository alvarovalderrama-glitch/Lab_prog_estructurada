# JUEGO: EL GATO 
import random
import os

# Función para mostrar el tablero actual
def mostrar_tablero(tablero):
    print("")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+--")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print("")

# Función para elegir la ficha
def elegir_ficha():
    while True:
        eleccion = input("Elige tu ficha (X u O): ").upper()
        if eleccion in ['X', 'O']:
            return eleccion
        else:
            print("Opción no válida, intenta de nuevo.")

# Función para verificar si hay un ganador
def hay_ganador(tablero, ficha):
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8], # Filas
        [0,3,6], [1,4,7], [2,5,8], # Columnas
        [0,4,8], [2,4,6]           # Diagonales
    ]
    for combo in combinaciones:
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == ficha:
            return True
    return False

# Función para verificar si hay empate
def tablero_lleno(tablero):
    return " " not in tablero

# Función principal del juego
def jugar_gato():
    os.system("cls")
    print("===============================")
    print("     JUEGO: EL GATO      ")
    print("===============================")
    print("Reglas: Logra tres en línea para ganar.")
    print("")

    tablero = [" "] * 9
    jugador = elegir_ficha()
    bot = "O" if jugador == "X" else "X"

    turno = random.choice(["Jugador", "Bot"])
    print("Comienza:", turno)

    while True:
        mostrar_tablero(tablero)

        if turno == "Jugador":
            try:
                pos = int(input("Elige una posición (1-9): ")) - 1
                if pos < 0 or pos > 8:
                    print("Posición fuera de rango.")
                    continue
                if tablero[pos] != " ":
                    print("Esa posición ya está ocupada.")
                    continue
                tablero[pos] = jugador
            except ValueError:
                print("Debes ingresar un número del 1 al 9.")
                continue

            if hay_ganador(tablero, jugador):
                mostrar_tablero(tablero)
                print("¡Felicidades! Ganaste")
                break

            turno = "Bot"

        else:
            pos_bot = random.choice([i for i, x in enumerate(tablero) if x == " "])
            tablero[pos_bot] = bot
            print("El bot jugó en la posición", pos_bot + 1)

            if hay_ganador(tablero, bot):
                mostrar_tablero(tablero)
                print("Oh ¡Perdiste!. El bot ganó.")
                break

            turno = "Jugador"

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

# Ejecución del juego
jugar_gato()
