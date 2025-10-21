def es_valido(x, y, tablero, n):
    """Verifica si la posición (x, y) está dentro del tablero y no ha sido visitada."""
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == -1


def resolver_caballo(x, y, movi, tablero, mov_x, mov_y, n):
    """Usa backtracking para intentar recorrer todo el tablero."""
    if movi == n * n:  # Si el caballo ha visitado todas las casillas
        return True

    for i in range(8):  # El caballo tiene 8 posibles movimientos
        sig_x = x + mov_x[i]
        sig_y = y + mov_y[i]
        if es_valido(sig_x, sig_y, tablero, n):
            tablero[sig_x][sig_y] = movi
            if resolver_caballo(sig_x, sig_y, movi + 1, tablero, mov_x, mov_y, n):
                return True
            # Retrocede (backtracking)
            tablero[sig_x][sig_y] = -1
    return False


def imprimir_tablero(tablero):
    """Imprime el tablero de forma ordenada."""
    for fila in tablero:
        print(" ".join(f"{celda:2}" for celda in fila))
    print()


# --- Programa principal ---

n = int(input("Ingrese el tamaño del tablero (n x n): "))

# Crear el tablero inicial lleno de -1
tablero = [[-1 for _ in range(n)] for _ in range(n)]

# Posibles movimientos del caballo
mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

# Posición inicial
tablero[0][0] = 0

# Resolver y mostrar resultado
if resolver_caballo(0, 0, 1, tablero, mov_x, mov_y, n):
    print("\nSolución encontrada:\n")
    imprimir_tablero(tablero)
else:
    print("\nNo existe solución para este tamaño de tablero.")
