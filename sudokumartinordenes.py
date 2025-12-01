tab = [
    [1,0,0,0,0,2,0,9,0],
    [0,0,0,0,4,0,0,0,8],
    [0,0,4,1,9,0,0,5,0],
    [0,0,2,0,0,4,5,0,0],
    [8,0,1,0,0,7,6,0,0],
    [5,4,0,0,0,3,0,0,7],
    [0,0,0,3,0,0,0,0,0],
    [0,6,0,0,0,0,1,0,0],
    [0,2,0,0,6,0,3,7,4]
] # muestra un tablero ya hecho para resolver

def mostrar(tablero): # define la funcion de como se mostrara el tablero con el formato de sudoku
    print()
    for fila in range(9):
        if fila % 3 == 0 and fila != 0:
            print('---------------------')
        for colum in range(9):
            if colum % 3 == 0 and colum != 0:
                print('|', end=' ')
            n = tablero[fila][colum]
            print(n if n != 0 else '0', end=' ')  # muestra un 0 si el espacio esta vacio
        print()
    print()

def sud_valid(tablero, fila, colum, num): # define la funcion para saber si numero es valido dentro del sudoku
    if num in tablero[fila]:
        return False # en caso de que el numero ya este en la fila del sudoku completo prueba con otro 
    for f in range(9):
        if tablero[f][colum] == num: # en caso de que el numero ya este en la columna del sudoku completo prueba con otro
            return False
    i_f = (fila // 3) * 3
    i_c = (colum // 3) * 3
    for f in range(i_f, i_f + 3):
        for c in range(i_c, i_c + 3):
            if tablero[f][c] == num:
                return False
    return True

def resolver(tablero): # define la funcion que resuelve el sudoku
    for fila in range(9):
        for colum in range(9):
            if tablero[fila][colum] == 0:  
                for num in range(1, 10):  
                    if sud_valid(tablero, fila, colum, num):
                        tablero[fila][colum] = num  
                        if resolver(tablero):
                            return True
                        tablero[fila][colum] = 0   
                return False  
    return True

print('Tablero inicial:')
mostrar(tab)  

if resolver(tab):
    print('Tablero resuelto:')
    mostrar(tab)  
else:
    print('Este sudoku no tiene solución...')