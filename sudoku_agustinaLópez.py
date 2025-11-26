import time
def imprimir_tablero(tablero):
#funcion para imprimir el tablero de sudoku de manera legible
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if tablero[i][j] == 0:
                print(".", end=" ")
            else:
                print(tablero[i][j], end=" ")
        print()

def encontrar_vacio(tablero):
#encuentra la primera celda vacía
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return (i, j)
    return None

def es_valido(tablero, num, pos):
#verifica si es valido colocar num en pos
    for j in range(9):
        if tablero[pos[0]][j] == num and pos[1] != j:
            return False
    
    # Verificar columna
    for i in range(9):
        if tablero[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Verificar cuadrante 3x3
    cuadrante_x = pos[1] // 3
    cuadrante_y = pos[0] // 3
    
    for i in range(cuadrante_y * 3, cuadrante_y * 3 + 3):
        for j in range(cuadrante_x * 3, cuadrante_x * 3 + 3):
            if tablero[i][j] == num and (i, j) != pos:
                return False
    return True

def resolver_sudoku(tablero):
#funcion principal para resolver el sudoku usando backtracking
    vacio = encontrar_vacio(tablero)
    
    if not vacio:
        return True
    
    fila, col = vacio
    
    # Probar números del 1 al 9
    for num in range(1, 10):
        if es_valido(tablero, num, (fila, col)):
            tablero[fila][col] = num
            
            if resolver_sudoku(tablero):
                return True
            
            tablero[fila][col] = 0
    
    return False

# Ejemplo de uso
if __name__ == "__main__":
    # Tablero de ejemplo (0 representa celdas vacías)
    tablero = [
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
    
    print("Tablero inicial:")
    imprimir_tablero(tablero)
    print("\nResolviendo...\n")
    time.sleep(2.5)  # Pausa para simular el proceso de resolución
    if resolver_sudoku(tablero):
        print("¡Sudoku resuelto!")
        print(imprimir_tablero(tablero))
    else:
        print("No se pudo resolver el Sudoku") 