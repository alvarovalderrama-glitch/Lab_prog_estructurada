
# ----------------------------------------
#   N-QUEENS (BACKTRACKING RECURSIVO)
#   Una reina por columna
# ----------------------------------------

# ----- Verifica si la reina se puede colocar en fila, columna -----
def es_seguro(tablero, fila, col, n):

    # Revisar misma fila a la izquierda
    for c in range(col):
        if tablero[fila][c] == 1:
            return False

    # Revisar diagonal ↖ (arriba-izquierda)
    f, c = fila, col
    while f >= 0 and c >= 0:
        if tablero[f][c] == 1:
            return False
        f -= 1
        c -= 1

    # Revisar diagonal ↙ (abajo-izquierda)
    f, c = fila, col
    while f < n and c >= 0:
        if tablero[f][c] == 1:
            return False
        f += 1
        c -= 1

    return True


# ----- Función recursiva de backtracking -----
def resolver(tablero, col, n, soluciones):
    # Si se colocaron reinas en todas las columnas → solución válida
    if col == n:
        # Guardar una copia de la solución
        solucion = [fila[:] for fila in tablero]
        soluciones.append(solucion)
        return

    reina_colocada = False  # para saber si esta columna consiguió reina

    # Intentar colocar una reina en alguna fila de esta columna
    for fila in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 1  # colocar reina
            reina_colocada = True

            # Recursión a la siguiente columna
            resolver(tablero, col + 1, n, soluciones)

            # Backtracking
            tablero[fila][col] = 0

    # Si no se logró poner una reina en esta columna, backtracking recursivo ocurre solo
    # porque la función retorna y se deshace el estado previo


# ----- Mostrar tablero -----
def mostrar(tablero):
    for fila in tablero:
        print(" ".join("Q" if c == 1 else "." for c in fila))
    print()


# ----- PROGRAMA PRINCIPAL -----
n = int(input("Ingrese dimensión del tablero (ej: 8): "))
tablero = [[0] * n for _ in range(n)]
soluciones = []

resolver(tablero, 0, n, soluciones)

print(f"\nTotal de soluciones encontradas: {len(soluciones)}\n")

for i, sol in enumerate(soluciones):
    print(f"Solución #{i+1}:")
    mostrar(sol)