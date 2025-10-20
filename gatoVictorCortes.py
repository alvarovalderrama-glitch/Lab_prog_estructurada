def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

def mostrar_tablero(tablero):
    print("\n")
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)
    print("\n")

def hay_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    # Verificar columnas
    for c in range(3):
        if tablero[0][c] == tablero[1][c] == tablero[2][c] == jugador:
            return True
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def gato():
    tablero = crear_tablero()
    jugador_actual = "X"
    ganador = False

    print("Bienvenido al juego del GATO ")
    mostrar_tablero(tablero)

    while not ganador and not tablero_lleno(tablero):
        print(f"Turno del jugador {jugador_actual}")
        try:
            fila = int(input("Elige la fila (0, 1, 2): "))
            col = int(input("Elige la columna (0, 1, 2): "))
        except ValueError:
            print("Por favor, ingresa números válidos (0, 1 o 2).")
            continue

        if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == " ":
            tablero[fila][col] = jugador_actual
            mostrar_tablero(tablero)

            if hay_ganador(tablero, jugador_actual):
                print(f" ¡El jugador {jugador_actual} ha ganado! ")
                ganador = True
            else:
                jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print(" Movimiento inválido. Intenta de nuevo.")

    if not ganador:
        print("¡Empate!")

# Ejecutar el juego
gato()
