# Problema del recorrido del caballo 

N = 5  # Tamaño del tablero 

# Movimientos posibles del caballo
MOV_X = [2, 1, -1, -2, -2, -1, 1, 2]
MOV_Y = [1, 2, 2, 1, -1, -2, -2, -1]


def es_valido(tablero, x, y):
    """Verifica si la posición (x, y) está dentro del tablero y libre."""
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1


def mostrar_tablero(tablero):
    """Muestra el tablero en formato bonito."""
    for fila in tablero:
        print(" ".join(f"{c:2d}" for c in fila))
    print()


def posibles_movimientos(tablero, x, y):
    """Devuelve la lista de movimientos válidos desde (x, y)."""
    moves = []
    for i in range(8):
        nx, ny = x + MOV_X[i], y + MOV_Y[i]
        if es_valido(tablero, nx, ny):
            moves.append((nx, ny))
    return moves


def solucion(tablero, x, y, paso, usar_heuristica=True):
    """Resuelve el recorrido del caballo con backtracking."""
    if paso == N * N:
        return True

    # Ordena movimientos por número de caminos siguientes 
    movimientos = posibles_movimientos(tablero, x, y)
    if usar_heuristica:
        movimientos.sort(key=lambda m: len(posibles_movimientos(tablero, m[0], m[1])))

    for nx, ny in movimientos:
        tablero[nx][ny] = paso
        if solucion(tablero, nx, ny, paso + 1, usar_heuristica):
            return True
        tablero[nx][ny] = -1  # Retrocede si no hay salida
    return False


# Ejecución del programa
tablero = [[-1 for _ in range(N)] for _ in range(N)]
inicio_x, inicio_y = 0, 0  # Posición inicial del caballo
tablero[inicio_x][inicio_y] = 0

print(f"Buscando recorrido del caballo en un tablero de {N}x{N}...\n")

if solucion(tablero, inicio_x, inicio_y, 1, usar_heuristica=True):
    print("Recorrido completo encontrado:\n")
    mostrar_tablero(tablero)
else:
    print("No hay solución.")
