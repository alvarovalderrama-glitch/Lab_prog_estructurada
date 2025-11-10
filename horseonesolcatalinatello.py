
# UNA solución posible del recorrido del caballo en un tablero N x N.
N = 5

# Lista con todos los posibles movimientos del caballo
# Cada tupla representa (filas que avanza, columnas que avanza)
MOVS_CABALLO = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def crear_tablero(n):
    # Crea una matriz n x n llena con -1.
    # El valor -1 indica que la casilla aún no ha sido visitada.
    return [[-1 for _ in range(n)] for _ in range(n)]

def es_valido(f, c, tablero):
    # Revisa si una posición (f, c) está dentro del tablero y no ha sido visitada.
    return 0 <= f < N and 0 <= c < N and tablero[f][c] == -1

def imprimir_tablero(tablero):
    # Imprime el tablero mostrando el orden en que el caballo visitó las casillas.
    for fila in tablero:
        print(" ".join(f"{x:2}" for x in fila))
    print()  # línea en blanco al final

def backtracking_una_sol(tablero, fila, col, paso):
    # Algoritmo recursivo que intenta recorrer el tablero.
    # - fila, col → posición actual del caballo
    # - paso → número de movimiento actual
    # Retorna True si logra llenar todo el tablero (una solución completa).
    
    # Si ya completó todos los movimientos, hay solución
    if paso == N * N:
        return True

    # Probar los 8 movimientos posibles del caballo
    for mov in MOVS_CABALLO:
        nf = fila + mov[0]
        nc = col + mov[1]
        if es_valido(nf, nc, tablero):
            tablero[nf][nc] = paso  # Marco la casilla con el número de paso
            # Llamada recursiva para continuar
            if backtracking_una_sol(tablero, nf, nc, paso + 1):
                return True  # si encontró solución, terminamos
            tablero[nf][nc] = -1  # Si no funcionó, deshago el movimiento (backtracking)

    # Si ninguno de los movimientos funcionó, no hay solución
    return False

def main():
    # Función principal: inicializa el tablero y busca una solución.
    tablero = crear_tablero(N)

    # Posición inicial del caballo (fila 0, columna 0)
    inicio_fila = 0
    inicio_col = 0
    tablero[inicio_fila][inicio_col] = 0  # primer movimiento

    # Llamamos al algoritmo de backtracking
    if backtracking_una_sol(tablero, inicio_fila, inicio_col, 1):
        print("SI Se encontró una solución:")
        imprimir_tablero(tablero)
    else:
        print("NO No hay solución para este tamaño de tablero.")

# Punto de inicio del programa
if __name__ == "__main__":
    main()
