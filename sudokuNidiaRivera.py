import math
def Imprimir_Tablero(tablero):
    for fila in tablero:
        print(fila)
    print()
def es_valido(tablero, fila, col, num):
    tamaño = len(tablero)
    sub = int(math.sqrt(tamaño))   # tamaño del subcuadro

    # Revisar fila
    for c in range(tamaño):
        if tablero[fila][c] == num:
            return False

    # Revisar columna
    for f in range(tamaño):
        if tablero[f][col] == num:
            return False

    # Revisar subcuadro
    inicio_f = (fila // sub) * sub
    inicio_c = (col // sub) * sub

    for f in range(inicio_f, inicio_f + sub):
        for c in range(inicio_c, inicio_c + sub):
            if tablero[f][c] == num:
                return False

    return True

def buscar_celda_vacia(tablero):
    tamaño = len(tablero)
    for f in range(tamaño):
        for c in range(tamaño):
            if tablero[f][c] == 0:
                return f, c  # devuelve posición
    return None  # no hay celdas vacías

def resolver_sudoku(tablero):
    
    pos = buscar_celda_vacia(tablero) #llamada a función que Busca celda vacía

    if pos is None:
        return True  # Se han completado todas las celdas, se ha completado el SUDOKU

    fila, col = pos
    tamaño = len(tablero)

    for num in range(1, tamaño + 1):
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num  # poner número en la ubicacion del tablero

            if resolver_sudoku(tablero): #llamada de recursividad
                return True

            tablero[fila][col] = 0   #Usando Backtracking, si no funciona número se anula ultimo movimiento

    return False


#Sudoku que se utiliza inicialmente (al cual deben completarse o cambiarse las celdas con valor 0)
print("SUDOKU INICIAL Ejemplo de 4*4:")
sudoku = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],

    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],

    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9]
]

Imprimir_Tablero(sudoku)

if resolver_sudoku(sudoku):
    print("SOLUCIÓN AL SUDOKU:")
    Imprimir_Tablero(sudoku)
else:
    print("No se encontró Solución")