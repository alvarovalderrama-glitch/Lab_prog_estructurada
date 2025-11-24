# CUADRADO MÁGICO CON BACKTRACKING (RECURSIVO)


def suma_magica(n):
    """Devuelve la suma mágica para un cuadrado de tamaño n."""
    return n * (n * n + 1) // 2


def imprimir_tablero(tablero):
    """Imprime el tablero."""
    for fila in tablero:
        print(" ".join(f"{num:2d}" for num in fila))
    print()


def es_magico(tablero, n):
    """
    Verifica si el tablero completo es un cuadrado mágico válido.
    (Se usa al final para confirmar solución).
    """
    valor_sum = suma_magica(n)

    # Verificar que se usan exactamente los números 1..n^2
    numeros = []
    for fila in tablero:
        numeros.extend(fila)
    if sorted(numeros) != list(range(1, n * n + 1)):
        return False

    # Filas
    for i in range(n):
        if sum(tablero[i]) != valor_sum:
            return False

    # Columnas
    for j in range(n):
        if sum(tablero[i][j] for i in range(n)) != valor_sum:
            return False

    # Diagonal principal
    if sum(tablero[i][i] for i in range(n)) != valor_sum:
        return False

    # Diagonal secundaria
    if sum(tablero[i][n - 1 - i] for i in range(n)) != valor_sum:
        return False

    return True


def es_valido_parcial(tablero, fila, col, num, n, suma_mag):
    """
    Verifica si es razonable poner 'num' en (fila, col)
    según las sumas parciales de filas, columnas y diagonales.
    No permite que se pase de la suma mágica y, si se completa
    una fila/columna/diagonal, exige que sea exactamente la suma mágica.
    """

    # --- FILA ---
    fila_vals = tablero[fila][:]       # copia de la fila
    fila_vals[col] = num               # simulamos colocar num
    suma_fila = sum(fila_vals)

    if suma_fila > suma_mag:           # ya nos pasamos -> inválido
        return False
    if 0 not in fila_vals and suma_fila != suma_mag:
        # fila completa pero no suma lo que debe
        return False

    # --- COLUMNA ---
    col_vals = [tablero[i][col] for i in range(n)]
    col_vals[fila] = num
    suma_col = sum(col_vals)

    if suma_col > suma_mag:
        return False
    if 0 not in col_vals and suma_col != suma_mag:
        return False

    # --- DIAGONAL PRINCIPAL (si aplica) ---
    if fila == col:
        diag_vals = [tablero[i][i] for i in range(n)]
        diag_vals[fila] = num
        suma_diag = sum(diag_vals)

        if suma_diag > suma_mag:
            return False
        if 0 not in diag_vals and suma_diag != suma_mag:
            return False

    # --- DIAGONAL SECUNDARIA (si aplica) ---
    if fila + col == n - 1:
        diag2_vals = [tablero[i][n - 1 - i] for i in range(n)]
        diag2_vals[fila] = num
        suma_diag2 = sum(diag2_vals)

        if suma_diag2 > suma_mag:
            return False
        if 0 not in diag2_vals and suma_diag2 != suma_mag:
            return False

    return True


def backtracking_cuadrado_magico(tablero, n, pos, suma_mag, usados):
    """
    Backtracking recursivo:
    - pos va de 0 a n*n - 1 y recorre el tablero en orden fila por fila.
    - 'usados' es un conjunto con los números ya colocados.
    """
    # Caso base: tablero lleno
    if pos == n * n:
        # Confirmamos que realmente es mágico
        return es_magico(tablero, n)

    fila = pos // n
    col = pos % n

    # Si la casilla ya viene rellena (por si quieres fijar números iniciales)
    if tablero[fila][col] != 0:
        return backtracking_cuadrado_magico(tablero, n, pos + 1, suma_mag, usados)

    # Probamos números del 1 al n^2
    for num in range(1, n * n + 1):
        if num in usados:
            continue  # no repetir números

        if es_valido_parcial(tablero, fila, col, num, n, suma_mag):
            # Colocamos el número
            tablero[fila][col] = num
            usados.add(num)

            # Llamada recursiva a la siguiente casilla
            if backtracking_cuadrado_magico(tablero, n, pos + 1, suma_mag, usados):
                return True

            # Backtracking: deshacer el movimiento
            tablero[fila][col] = 0
            usados.remove(num)

    # Si ningún número funciona aquí, no hay solución por este camino
    return False


# ----------------- EJEMPLO DE USO -----------------

if __name__ == "__main__":
    n = 3  # tamaño del cuadrado mágico (3x3, 4x4, etc.)

    # Tablero inicialmente vacío (puedes fijar algunos números si quieres)
    tablero = [[0 for _ in range(n)] for _ in range(n)]

    valor_suma = suma_magica(n)
    usados = set()

    print(f"Suma mágica para n={n}: {valor_suma}\n")
    print("Intentando construir un cuadrado mágico...\n")

    if backtracking_cuadrado_magico(tablero, n, 0, valor_suma, usados):
        print("Cuadrado mágico encontrado:")
        imprimir_tablero(tablero)
    else:
        print("No se encontró solución.")
