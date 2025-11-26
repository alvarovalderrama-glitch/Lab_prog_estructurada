# Ejemplo de implementacion en Python

def es_seguro(grid, fila, col, num):
    """Verifica si es seguro colocar `num` en la celda (fila, col)."""
    # Verificar fila y columna
    for i in range(9):
        if grid[fila][i] == num or grid[i][col] == num:
            return False

    # Verificar subcuadrícula 3x3
    start_row = fila - fila % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

def encontrar_vacia(grid):
    """Encuentra la próxima celda vacía (representada por 0)."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # fila, columna
    return None # Todas las celdas están llenas

def resolver_sudoku(grid):
    """Resuelve el Sudoku usando backtracking recursivo."""
    encontrado = encontrar_vacia(grid)
    if not encontrado:
        return True # ¡Se encontró una solución!
    else:
        fila, col = encontrado

    for num in range(1, 10):
        if es_seguro(grid, fila, col, num):
            grid[fila][col] = num

            if resolver_sudoku(grid): # Llamada recursiva
                return True

            grid[fila][col] = 0 # ¡Se hizo un movimiento incorrecto, deshacerlo!

    return False # No hay solución posible para este camino

# Ejemplo de uso
# (0 representa celdas vacías)
ejemplo_sudoku = [
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

if resolver_sudoku(ejemplo_sudoku):
    print("Sudoku resuelto:")
    for fila in ejemplo_sudoku:
        print(fila)
else:
    print("No se encontró solución.")