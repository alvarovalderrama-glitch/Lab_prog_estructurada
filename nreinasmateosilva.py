def es_valido(tablero, fila, columna, n):
    # Revisar misma columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

    # Revisar diagonal superior izquierda
    i, j = fila - 1, columna - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Revisar diagonal superior derecha
    i, j = fila - 1, columna + 1
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join("*" if x == 1 else "0" for x in fila))
    print()


def resolver_n_reinas(tablero, fila, n):
    # Caso base: ya coloqué reinas en todas las filas
    if fila == n:
        imprimir_tablero(tablero)
        return True   # si queremos solo UNA solución

    # Intentar poner una reina en cada columna de esta fila
    for columna in range(n):
        if es_valido(tablero, fila, columna, n):
            tablero[fila][columna] = 1  # pongo la reina

            if resolver_n_reinas(tablero, fila + 1, n):
                return True             # encontramos solución

            tablero[fila][columna] = 0  # backtracking: quito la reina

    # Si ninguna columna sirvió, no hay solución desde esta configuración
    return False


# --- "main" ---
n = 8  # por ejemplo
tablero = [[0 for _ in range(n)] for _ in range(n)]

if not resolver_n_reinas(tablero, 0, n):
    print("No tiene solución")