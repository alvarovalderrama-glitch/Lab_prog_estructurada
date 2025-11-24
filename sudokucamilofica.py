def es_valido(tablero, fila, col, num):
    # Verificar fila
    for c in range(9):
        if tablero[fila][c] == num:
            return False

    # Verificar columna
    for f in range(9):
        if tablero[f][col] == num:
            return False

    # Verificar subcuadrícula 3×3
    inicio_f = (fila // 3) * 3
    inicio_c = (col // 3) * 3
    for f in range(inicio_f, inicio_f + 3):
        for c in range(inicio_c, inicio_c + 3):
            if tablero[f][c] == num:
                return False

    return True


def buscar_vacio(tablero):
    for f in range(9):
        for c in range(9):
            if tablero[f][c] == 0:  # 0 representa casilla vacía
                return f, c
    return None  # no hay vacíos significa que el  Sudoku esta completo


def resolver_sudoku(tablero):
    vacio = buscar_vacio(tablero)
    if not vacio:
        return True  # Sudoku resuelto

    fila, col = vacio

    for num in range(1, 10):  # probar números del 1 al 9
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num

            if resolver_sudoku(tablero):#funcion
                return True

            # backtracking
            tablero[fila][col] = 0

    return False  # no se pudo poner ningún número


#creamos una tabla de sudoku para probar el codigo si todo esta en orden
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

if resolver_sudoku(sudoku):
    for fila in sudoku:
        print(fila)
else:
    print("No tiene solución")
