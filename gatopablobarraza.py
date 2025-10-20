tablero = ["1", "2", "3", "4", "5", "6", "7", "8", "9"] # Crea la lista tablero
jugador = "X"
ganador = False

print(" Juego del Gato ")


def mostrar_tablero(): # Función para mostrar el tablero
    print()
    print(tablero[0], "|", tablero[1], "|", tablero[2])
    print("--+---+--")
    print(tablero[3], "|", tablero[4], "|", tablero[5])
    print("--+---+--")
    print(tablero[6], "|", tablero[7], "|", tablero[8])
    print()

mostrar_tablero() # Llama a la funcion

    # Se genera el bucle for que hace repetir la funcion hasta que hay un ganador o se juegan las 9 casillas

for turno in range(9): # Se repite máximo 9 veces (las 9 casillas)
    print("Turno del jugador", jugador)
    pos = input("Elige una posición (1-9): ")

    # Se verifica si la posición es válida
    if pos not in tablero:
        print("Esa posición no está disponible. Intenta otra.")
        continue

    # Se marca la posición
    for i in range(9):
        if tablero[i] == pos:
            tablero[i] = jugador

    mostrar_tablero()

    # Comprobamos si hay un ganador
    if (tablero[0] == tablero[1] == tablero[2] or
        tablero[3] == tablero[4] == tablero[5] or
        tablero[6] == tablero[7] == tablero[8] or
        tablero[0] == tablero[3] == tablero[6] or
        tablero[1] == tablero[4] == tablero[7] or
        tablero[2] == tablero[5] == tablero[8] or
        tablero[0] == tablero[4] == tablero[8] or
        tablero[2] == tablero[4] == tablero[6]):
        print("¡Jugador", jugador, "ganó!")
        ganador = True
        break

    # Se cambia de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

if not ganador: # Si no hay ganador y se juegan las 9 casillas se declara empate
    print("Empate, no hay ganador.")
