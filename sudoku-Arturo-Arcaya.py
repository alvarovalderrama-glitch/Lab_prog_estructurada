MAX = 9  # tamaño del tablero 9x9

# funcion que verifica si un numero puede colocarse en la posicion fila col
def validar(tablero, fila, col, num):
    for c in range(MAX):  # recorre todas las columnas de la fila
        if tablero[fila][c] == num:  
            return False
    for f in range(MAX):  # recorre todas las filas de la columna
        if tablero[f][col] == num:  
            return False
    inicio_f = (fila // 3) * 3  
    inicio_c = (col // 3) * 3  
    for f in range(inicio_f, inicio_f + 3):  
        for c in range(inicio_c, inicio_c + 3):  
            if tablero[f][c] == num:  
                return False
    return True  

# funcion que busca la primera casilla vacia en el tablero
def buscar(tablero):
    for f in range(MAX):  
        for c in range(MAX):  
            if tablero[f][c] == 0:  
                return f, c  
    return None  

# funcion recursiva que intenta resolver el sudoku usando backtracking
def resolver(tablero):
    vacio = buscar(tablero)  
    if not vacio:  
        return True  
    fila, col = vacio  
    for num in range(1, MAX+1):  
        if validar(tablero, fila, col, num):  
            tablero[fila][col] = num  
            if resolver(tablero):  
                return True  
            tablero[fila][col] = 0  
    return False  

# tablero de prueba con ceros en las casillas vacias
tablero = [
    [0,2,0,0,0,0,0,6,3],
    [0,0,0,0,0,5,0,0,0],
    [0,0,0,0,9,0,0,0,1],
    [0,0,0,5,0,0,4,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,7,0,0,0],
    [7,0,0,0,2,0,0,0,0],
    [0,0,0,6,0,0,0,0,0],
    [5,8,0,0,0,0,0,0,0]
]

# se llama a la funcion principal y se imprime el resultado
if resolver(tablero):  
    for fila in tablero:  
        print(" ".join(str(x) for x in fila))  
else:
    print("no tiene solucion")  