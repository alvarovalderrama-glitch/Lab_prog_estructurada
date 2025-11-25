### sudoku ###

# crea el tablero lleno de ceros
def crear_tablero():
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    return tablero

# imprime el tablero con el formato de sudoku
def imprimir_tablero(tablero):
    for fila in range(9):
        for columna in range(9):
            print(tablero[fila][columna], end=" ")
            if (columna+1) % 3 == 0 and columna != 8:
                print("|", end=" ")  # cada 3 numeros, imprime una linea vertical |
            if columna == 8:  # cuando llega al final, baja una linea (como un \n)
                print("")
            if (fila+1) % 3 == 0 and fila != 8 and columna == 8:  # si llega hasta el final de la fila 3 o 6, imprime una linea horizontal
                print("------+-------+------")

def es_valido(tablero, fila, columna, candidato):
    # verificar fila
    for col in range(9):
        if tablero[fila][col] == candidato: # si el numero ya se encuentra en la fila, no es válido
            return False
    
    # verificar columna
    for i in range(9):
        if tablero[i][columna] == candidato:  # si el numero ya está en la columna, no es válido
            return False
        
    # verificar cuadro 3x3
    inicio_fila = (fila // 3) * 3  # si la fila está entre 0 y 2 inicio_fila es 0, si está entre 3 y 5 inicia desde 3, si está entre 6 y 8 inicia desde 6
    inicio_columna = (columna // 3) * 3  # la misma lógica para las columnas
    for i in range(inicio_fila, inicio_fila + 3):  # como cada cuadro es 3x3, las filas y columnas recorren ese rango
        for j in range(inicio_columna, inicio_columna + 3):
            if tablero[i][j] == candidato:  # si el numero ya está dentro del cuadro 3x3, no es válido
                return False
    
    return True

def resolver_sudoku(tablero):
    for fila in range(9):  # fila va de 0 a 8
        for columna in range(9):  # columna va de 0 a 8
            if tablero[fila][columna] == 0:  # encontrar casilla vacía
                for candidato in range(1, 10):  # candidato va de 1 a 9
                    if es_valido(tablero, fila, columna, candidato):
                        tablero[fila][columna] = candidato
                        
                        if resolver_sudoku(tablero):
                            return True
                        
                        # devolverse
                        tablero[fila][columna] = 0
                return False  # si ningún candidato es válido, regresar
    return True  # si no quedan casillas vacías, el sudoku está resuelto

def main():
    tablero = crear_tablero()
    print("tablero inicial:")
    imprimir_tablero(tablero)
    
    if resolver_sudoku(tablero):
        print("\nsudoku resuelto:\n")
        imprimir_tablero(tablero)
    else:
        print("no se encontró solución.")

main()