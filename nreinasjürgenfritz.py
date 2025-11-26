# N - Reinas - Problema de las N reinas

def es_seguro(tablero, fila, col, n):
    """
    Verifica si una reina puede ser colocada en tablero[fila][col].
    """
    # Revisar esta fila a la izquierda
    for i in range(col):
        if tablero[fila][i] == 1:
            return False

    # Revisar la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    # Revisar la diagonal inferior izquierda
    for i, j in zip(range(fila, n, 1), range(col, -1, -1)):
        if tablero[i][j] == 1:
            return False

    return True

def resolver_n_reinas_util(tablero, col, n, soluciones):
    """
    Función recursiva de retroceso para resolver el problema de las N reinas.
    """
    # Caso base: Si se colocan todas las reinas, agregar la solución
    if col >= n:
        soluciones.append([fila[:] for fila in tablero])
        return

    # Probar colocar una reina en cada fila de la columna actual
    for i in range(n):
        if es_seguro(tablero, i, col, n):
            # Si es seguro, colocar la reina
            tablero[i][col] = 1

            # Llamar recursivamente para la siguiente columna
            resolver_n_reinas_util(tablero, col + 1, n, soluciones)

            # Si colocar la reina no lleva a la solución,
            # retroceder (quitar la reina)
            tablero[i][col] = 0

def resolver_n_reinas(n):
    """
    Función principal que inicializa el tablero y llama a la función recursiva.
    """
    # Inicializar el tablero con ceros
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    soluciones = []
    resolver_n_reinas_util(tablero, 0, n, soluciones)
    return soluciones

def imprimir_soluciones(soluciones):
    """
    Imprime las soluciones en un formato legible.
    """
    if not soluciones:
        print("No se encontraron soluciones.")
        return
    for i, solucion in enumerate(soluciones):
        print(f"Solución {i+1}:")
        for fila in solucion:
            print(" ".join(map(str, fila)))
        print("-" * 10)

# Ejemplo de uso para 4 reinas
n = 4
soluciones = resolver_n_reinas(n)
imprimir_soluciones(soluciones)