# crea un tablero con nueve espacios y define al jugador inicial como 'X'
tablero = [' '] * 9
jugador = 'X'

# función para mostrar el tablero en pantalla
def mostrar_tablero(): 
    print(f"\n{tablero[6]} | {tablero[7]} | {tablero[8]}")
    print('---------')
    print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
    print('---------')
    print(f"{tablero[0]} | {tablero[1]} | {tablero[2]}\n")

# función para verificar si hay ganador
def hay_ganador():
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],   # filas
        [0,3,6], [1,4,7], [2,5,8],   # columnas
        [0,4,8], [2,4,6]             # diagonales
    ]
    for c in combinaciones: 
        if tablero[c[0]] == tablero[c[1]] == tablero[c[2]] != ' ':
            return True
    return False

# bucle principal del juego (máx 12 turnos)
for turno in range(12):
    mostrar_tablero()
    print(f"Turno de {jugador}")

    # pedir posición al jugador
    try:
        pos = int(input("Elige una posición (0-8): "))
    except ValueError:
        print("Debes ingresar un número válido.")
        continue

    # verificar si la posición está dentro del rango
    if pos < 0 or pos > 8:
        print("Casilla no disponible. Elige un número entre 0 y 8.")
        continue

    # verificar si la posición está vacía
    if tablero[pos] == ' ':
        tablero[pos] = jugador
    else:
        print("Esa posición ya está ocupada.")
        continue

    # verificar si el jugador actual ganó
    if hay_ganador():
        mostrar_tablero()
        print(f"¡Gana {jugador}!")
        break

    # cambiar de jugador
    jugador = 'O' if jugador == 'X' else 'X'

# si se completan los turnos sin ganador hay empate
else:
    mostrar_tablero()
    print("¡Empate!")