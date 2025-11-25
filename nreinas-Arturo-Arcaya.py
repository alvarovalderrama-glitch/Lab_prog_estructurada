n = int(input('de que tamaño requiere el tablero '))  # pide al usuario el tamaño del tablero

# funcion que verifica si se puede poner una reina en la posicion fila col
def verificar(tab, fila, col):
    for c in range(col):  # revisa la fila hacia la izquierda
        if tab[fila][c] == 1: 
            return False
    for r,c in zip(range(fila-1,-1,-1), range(col-1,-1,-1)):  # revisa diagonal superior izquierda
        if tab[r][c] == 1: 
            return False
    for r,c in zip(range(fila+1,n), range(col-1,-1,-1)):  # revisa diagonal inferior izquierda
        if tab[r][c] == 1: 
            return False
    return True  # si no hay conflicto devuelve verdadero

# funcion recursiva que intenta colocar las reinas columna por columna
def resolver(tab, col):
    if col == n:  # caso base cuando ya se llenaron todas las columnas
        print('tablero solucion\n')
        for fila in tab:  # imprime cada fila con espacios
            print(' '.join('R' if c==1 else 'o' for c in fila))
        print('----------------------------------------------')
        return
    for fila in range(n):  # recorre todas las filas de la columna actual
        if verificar(tab, fila, col):  # si es seguro colocar la reina
            tab[fila][col] = 1  # coloca la reina
            resolver(tab, col+1)  # llamada recursiva para la siguiente columna
            tab[fila][col] = 0  # quita la reina si no funciona (backtracking)

# se crea el tablero vacio con ceros
tablero = [[0]*n for _ in range(n)]

# se inicia el proceso desde la columna 0
resolver(tablero, 0)
