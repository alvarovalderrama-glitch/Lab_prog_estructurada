
N = 5  # tamaño del tablero 5x5

# Movimientos posibles del caballo
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

def es_valido(x, y, tablero):
    """Revisa si (x, y) es una posición válida dentro del tablero."""
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

def resolver_caballo(tablero, x, y, paso):
    """Backtracking para encontrar una solución."""
    if paso == N * N:
        return True

    for i in range(8):
        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valido(nx, ny, tablero):
            tablero[nx][ny] = paso

            if resolver_caballo(tablero, nx, ny, paso + 1):
                return True

            tablero[nx][ny] = -1

    return False

# PROGRAMA PRINCIPAL
tablero = [[-1 for _ in range(N)] for _ in range(N)]
tablero[0][0] = 0  # empezar en la esquina

if resolver_caballo(tablero, 0, 0, 1):
    for fila in tablero:
        print(fila)
else:
    print("No hay solución.")
