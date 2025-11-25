import random

def valida(fila,columna,digito,tablero):
    
    if digito in tablero[fila]:
        return False
    
    for i in range(9):
        if tablero[i][columna] == digito:
            return False
        
    start_row = fila-fila%3
    start_col = columna-columna%3
    for i in range(3):
        for j in range(3):
            if tablero[start_row+i][start_col+j] == digito:
                return False
            
    return True

def validar_completacion(tablero):
    for fila in range(9):
        if 0 in tablero[fila]:
            return False
    return True

def generar_sudoku(tablero):
    
    if validar_completacion(tablero):
        return True
    
    for fila in range(9):
        for col in range(9):
            if tablero[fila][col] == 0:
                digitos = list(range(1, 10))
                random.shuffle(digitos)
                
                for dig in digitos:
                    if valida(fila,col,dig,tablero):
                        tablero[fila][col] = dig
                        
                        if generar_sudoku(tablero):
                            return True
                        
                        tablero[fila][col] = 0
                        
                return False

def mostrar_sudoku(tablero):
    for i,linea in enumerate(tablero):
        print(' '.join(str(x) for x in linea))
        if i in [2,5]:
            print('------------------')
        

# ---- Main ----

tablero = [[0]*9 for i in range(9)]
generar_sudoku(tablero)
print('Sudoku aleatorio:')
mostrar_sudoku(tablero)
    