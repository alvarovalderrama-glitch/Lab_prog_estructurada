import time

# Constante que representa el tamaño del Sudoku (9x9)
N = 9 

def encontrar_celda_vacia(tablero):
    """
    Encuentra la primera celda vacía (representada por 0) en el tablero.

     tablero (list): La matriz 9x9 del Sudoku.

     tuple or None: (fila, columna) de la celda vacía, o None si no hay.
    """
    for fila in range(N):
        for col in range(N):
            if tablero[fila][col] == 0:
                return (fila, col)
    return None

def es_valido(tablero, num, pos):
    """
    Verifica si colocar 'num' en 'pos' (fila, columna) es un movimiento válido.
    Debe ser único en su fila, columna y su caja 3x3.

    Args:
        tablero (list): La matriz 9x9 del Sudoku.
        num (int): El número que se intenta colocar (1-9).
        pos (tuple): (fila, columna) de la celda.

    Returns:
        bool: True si el movimiento es válido, False en caso contrario.
    """
    fila, col = pos

    # 1. Comprobar Fila
    # Busca si 'num' ya existe en la fila actual.
    for c in range(N):
        if tablero[fila][c] == num and col != c:
            return False

    # 2. Comprobar Columna
    # Busca si 'num' ya existe en la columna actual.
    for r in range(N):
        if tablero[r][col] == num and fila != r:
            return False

    # 3. Comprobar Caja 3x3
    # Calcula el inicio de la caja 3x3 a la que pertenece la posición.
    caja_fila_inicio = (fila // 3) * 3
    caja_col_inicio = (col // 3) * 3

    for r in range(caja_fila_inicio, caja_fila_inicio + 3):
        for c in range(caja_col_inicio, caja_col_inicio + 3):
            if tablero[r][c] == num and (r, c) != pos:
                return False

    return True

def resolver_sudoku(tablero):
    """tablero (list): La matriz 9x9 del Sudoku."""

    # 1. CASO BASE: Si no quedan celdas vacías, el Sudoku está resuelto.
    vacio = encontrar_celda_vacia(tablero)
    if not vacio:
        return True
    
    fila, col = vacio

    # 2. CASO RECURSIVO: Probar números del 1 al 9.
    for num in range(1, N + 1):
        # a. Comprobar si es un número válido para la posición actual
        if es_valido(tablero, num, (fila, col)):
            
            # b. Colocar el número (MOVIMIENTO / ELECCIÓN)
            tablero[fila][col] = num
            
            # c. Llamada recursiva (EXPLORACIÓN)
            # Intenta resolver el resto del tablero
            if resolver_sudoku(tablero):
                return True
            
            # d. Deshacer el movimiento (BACKTRACKING)
            # Si la llamada recursiva no retorna True, significa que esta elección
            # fue incorrecta, así que se restablece la celda a vacía (0) y
            # el bucle 'for' prueba el siguiente número.
            tablero[fila][col] = 0

    # Si ningún número del 1 al 9 funcionó para esta celda, 
    # se retorna False, lo que desencadena el backtracking 
    # a la celda anterior.
    return False

def imprimir_tablero(tablero):
    """
    Imprime el tablero con formato de Sudoku.
    """
    for i in range(len(tablero)):
        # Imprimir línea divisoria horizontal cada 3 filas
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(tablero[0])):
            # Imprimir línea divisoria vertical cada 3 columnas
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            # Imprimir el número.
            if j == N - 1:
                print(tablero[i][j])
            else:
                print(str(tablero[i][j]) + " ", end="")

# --- EJECUTAR EL ALGORITMO ---
if __name__ == "__main__":
    # Sudoku de ejemplo (0 representa celda vacía)
    tablero_ejemplo = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("--- Sudoku a Resolver ---")
    imprimir_tablero(tablero_ejemplo)
    
    print("\nIniciando resolución con Backtracking...")
    inicio = time.time()
    
    if resolver_sudoku(tablero_ejemplo):
        fin = time.time()
        print("\n¡Sudoku Resuelto! ✅")
        imprimir_tablero(tablero_ejemplo)
        print(f"\nTiempo de ejecución: {fin - inicio:.4f} segundos.")
    else:
        print("El Sudoku no tiene solución.")