
# TODAS las posibles soluciones del recorrido del caballo en un tablero N x N.
N = 5

# Movimientos posibles del caballo en el ajedrez
MOVS_CABALLO = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def crear_tablero(n):
    # Crea un tablero n x n lleno de -1 (no visitado).
    return [[-1 for _ in range(n)] for _ in range(n)]

def es_valido(f, c, tablero):
    # Revisa que la casilla (f, c) esté dentro del tablero y libre.
    return 0 <= f < N and 0 <= c < N and tablero[f][c] == -1

def copiar_tablero(tablero):
    # Crea una copia del tablero para guardar una solución.
    return [fila[:] for fila in tablero]

def imprimir_tablero(tablero):
    # Muestra una solución visualmente en consola.
    for fila in tablero:
        print(" ".join(f"{x:2}" for x in fila))
    print()

def backtracking_todas(tablero, fila, col, paso, soluciones):
    # Versión recursiva que encuentra TODAS las soluciones posibles.
    # - tablero: estado actual del recorrido
    # - fila, col: posición actual
    # - paso: número de movimiento
    # - soluciones: lista donde se guardan las soluciones completas
    
    # Si se completó el tablero, guardar la solución encontrada
    if paso == N * N:
        soluciones.append(copiar_tablero(tablero))
        return

    # Recorre todos los movimientos posibles del caballo
    for mov in MOVS_CABALLO:
        nf = fila + mov[0]
        nc = col + mov[1]
        if es_valido(nf, nc, tablero):
            tablero[nf][nc] = paso  # marcar paso actual
            backtracking_todas(tablero, nf, nc, paso + 1, soluciones)
            tablero[nf][nc] = -1    # desmarcar (retroceder)

def main():
    # Función principal del programa.
    tablero = crear_tablero(N)
    soluciones = []

    # Punto de inicio del caballo
    inicio_fila = 0
    inicio_col = 0
    tablero[inicio_fila][inicio_col] = 0  # primera posición

    # Ejecutar el algoritmo para encontrar todas las soluciones
    backtracking_todas(tablero, inicio_fila, inicio_col, 1, soluciones)

    # Mostrar los resultados
    if not soluciones:
        print("❌ No se encontraron soluciones.")
    else:
        print(f"✅ Se encontraron {len(soluciones)} soluciones.\n")
        # Imprimir todas las soluciones encontradas
        for i, sol in enumerate(soluciones, start=1):
            print(f"Solución {i}:")
            imprimir_tablero(sol)

# Punto de entrada del programa
if __name__ == "__main__":
    main()
