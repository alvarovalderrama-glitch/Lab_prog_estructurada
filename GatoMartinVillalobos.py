
def mostrar_tablero(tablero):
    """Muestra el tablero en pantalla."""
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 9)

def hay_ganador(tablero, jugador):
    """Verifica si el jugador tiene tres en línea."""
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] == jugador:
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    """Verifica si el tablero ya no tiene espacios vacíos."""
    for fila in tablero:
        if " " in fila:
            return False
    return True

def juego():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"

    print("Bienvenido al juego del GATO (Tres en línea)")

    while True:
        mostrar_tablero(tablero)
        print(f"Turno del jugador {jugador}")
        fila = int(input("Fila (0, 1, 2): "))
        col = int(input("Columna (0, 1, 2): "))

        if tablero[fila][col] != " ":
            print("Esa posición ya está ocupada, intenta otra.")
            continue

        tablero[fila][col] = jugador

        if hay_ganador(tablero, jugador):
            mostrar_tablero(tablero)
            print(f"¡El jugador {jugador} ganó!")
            break

        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡Empate!")
            break

        jugador = "O" if jugador == "X" else "X"

juego()
