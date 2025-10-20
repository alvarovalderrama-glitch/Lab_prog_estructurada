# GATO (Tres en raya) usando arreglos (listas)

# Creamos el tablero como una lista de listas (3x3)
tablero = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"]]

# Símbolo del jugador actual (X empieza)
turno = "X"

# Función para mostrar el tablero en pantalla
def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))  # une los elementos de la fila con espacios

# Empezamos el juego
while True:
    mostrar_tablero()
    jugada = input("Turno de " + turno + ". Elige casilla (1-9): ")

    # Recorremos el tablero para encontrar la casilla elegida
    encontrado = False
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == jugada:
                tablero[i][j] = turno
                encontrado = True
                break
        if encontrado:
            break

    # Si no se encontró o estaba ocupada
    if not encontrado:
        print("Casilla inválida o ya ocupada, intenta de nuevo.")
        continue

    # Revisamos si alguien ganó (filas, columnas o diagonales)
    if any(all(tablero[i][j] == turno for j in range(3)) for i in range(3)) or \
       any(all(tablero[i][j] == turno for i in range(3)) for j in range(3)) or \
       all(tablero[i][i] == turno for i in range(3)) or \
       all(tablero[i][2 - i] == turno for i in range(3)):
        mostrar_tablero()
        print("¡Ganó", turno + "!")
        break

    # Cambiamos el turno
    turno = "O" if turno == "X" else "X"


