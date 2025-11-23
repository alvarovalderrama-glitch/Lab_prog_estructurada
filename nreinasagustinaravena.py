N = 4   # tamaño del tablero y número de reinas

# módulo validar
def valida(tablero, fila, col):
    # verificar columna hacia arriba
    for i in range(fila):
        if tablero[i] == col:
            return False
    
    # verificar diagonal 
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i] == j:
            return False
        i -= 1
        j -= 1
    
    # verificar diagonal 
    i, j = fila - 1, col + 1
    while i >= 0 and j < N:
        if tablero[i] == j:
            return False
        i -= 1
        j += 1
    
    return True

# módulo mostrar_tablero
def mostrar_tablero(tablero):
    for i in range(N):
        fila = ["Q" if tablero[i] == j else "." for j in range(N)]
        print(" ".join(fila))
    print("")

# módulo solución (recursivo)
def solucion(tablero, fila=0):
    # caso base: todas las reinas puestas
    if fila == N:
        return True
    
    # intentar poner una reina en cada columna
    for col in range(N):
        if valida(tablero, fila, col):
            tablero[fila] = col  # colocar reina
            
            if solucion(tablero, fila + 1):  # avanzar recursivamente
                return True
            
            tablero[fila] = -1  # retroceder (backtracking)
    
    return False

# programa principal
def principal():
    tablero = [-1] * N  # tablero representado por columnas
    
    if solucion(tablero):
        print("Solución encontrada:\n")
        mostrar_tablero(tablero)
    else:
        print("No hay solución")

principal()
