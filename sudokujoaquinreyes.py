def imprimir_tablero(tablero):
    for i in range(9):
        for j in range(9):
            print(tablero[i][j], end=" ")
        print()
    print()


def es_valido(tablero, fila, col, num):
    # Revisar fila
    for j in range(9):
        if tablero[fila][j] == num:
            return False

    # Revisar columna
    for i in range(9):
        if tablero[i][col] == num:
            return False

    # Revisar subcuadrícula 3×3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False

    return True


def resolver_sudoku(tablero):

    # Buscar celda vacía
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:

                # Probar números del 1 al 9
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        tablero[fila][col] = num

                        if resolver_sudoku(tablero):
                            return True

                        tablero[fila][col] = 0  # retroceso

                return False  # no hay número válido

    return True  # tablero completo

tablero = [#define previamente el tablero
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

print("Sudoku inicial:")
imprimir_tablero(tablero)

if resolver_sudoku(tablero):
    print("Sudoku resuelto:")
    imprimir_tablero(tablero)
else:
    print("No tiene solución.")
