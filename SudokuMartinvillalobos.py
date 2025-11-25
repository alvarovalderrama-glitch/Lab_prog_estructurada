
sudoku = [
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

def encontrar_vacio(sudoku):
    """Busca una casilla vacía (0)."""
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return None

def es_valido(sudoku, fila, col, num):
    """Revisa si num se puede colocar en sudoku[fila][col]."""

    # Revisa fila
    if num in sudoku[fila]:
        return False

    # Revisa columna
    for i in range(9):
        if sudoku[i][col] == num:
            return False

    # Revisa subcuadrado 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3

    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if sudoku[i][j] == num:
                return False

    return True


def resolver_sudoku(sudoku):
    """Backtracking recursivo para resolver el Sudoku."""
    vacio = encontrar_vacio(sudoku)

    if not vacio:
        return True  # Sudoku completo

    fila, col = vacio

    for num in range(1, 10):
        if es_valido(sudoku, fila, col, num):
            sudoku[fila][col] = num  # Colocar número

            if resolver_sudoku(sudoku):  # Recursión
                return True

            sudoku[fila][col] = 0  # Backtracking

    return False


# PROGRAMA PRINCIPAL
if resolver_sudoku(sudoku):
    print("Sudoku resuelto:")
    for fila in sudoku:
        print(fila)
else:
    print("No tiene solución.")
