N = 4

def es_seguro(tablero, fila, col, n):
    for i in range(fila):  #Verifica la columna hacia arriba
        if tablero[i][col] == 'R':
            return False
    
    for i, j in zip(range(fila-1, -1, -1), range(col-1, -1, -1)): #Verifica la diagonal superior izquierda
        if tablero[i][j] == 'R':
            return False
    
    for i, j in zip(range(fila-1, -1, -1), range(col+1, n)): #Verifica la diagonal superior derecha
        if tablero[i][j] == 'R':
            return False
    
    return True

def resolver_n_reinas(tablero, fila, n, soluciones):
    if fila == n:
        soluciones.append([''.join(fila) for fila in tablero]) #Al encontrar una solución, la guarda
        return
    
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila][col] = 'R'
            resolver_n_reinas(tablero, fila + 1, n, soluciones)
            tablero[fila][col] = '#'

def n_reinas(n):
    tablero = [['#' for _ in range(n)] for _ in range(n)] #Crea un tablero con '#' en las filas y columnas
    soluciones = []
    resolver_n_reinas(tablero, 0, n, soluciones)
    return soluciones

soluciones = n_reinas(N)
for i, sol in enumerate(soluciones):
    print(f"Solución {i + 1}:")
    for fila in sol:
        print(fila)
    print()