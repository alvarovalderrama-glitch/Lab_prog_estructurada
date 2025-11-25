
N = 8  

tablero = [[0] * N for _ in range(N)]

def es_seguro(tablero, fila, col):
    """Verifica si se puede colocar una reina en (fila, col)."""

    # Revisa la misma columna hacia arriba
    for i in range(fila):
        if tablero[i][col] == 1:
            return False

    # Revisa diagonal superior izquierda
    i, j = fila, col
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Revisa diagonal superior derecha
    i, j = fila, col
    while i >= 0 and j < N:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def resolver_reinas(fila):
    """Backtracking recursivo para colocar las N reinas."""
    if fila == N:
        return True  # Se colocaron todas

    for col in range(N):
        if es_seguro(tablero, fila, col):
            tablero[fila][col] = 1  # Colocar reina

            if resolver_reinas(fila + 1):  # Recursión
                return True

            tablero[fila][col] = 0  # Backtracking

    return False


# PROGRAMA PRINCIPAL
if resolver_reinas(0):
    print("Solución encontrada:")
    for fila in tablero:
        print(fila)
else:
    print("No existen soluciones.")