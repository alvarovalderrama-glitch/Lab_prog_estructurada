MAX = 3

# módulo valida
def valida(tablero, fila, col, num):
    # si el número ya está en el tablero, no se puede usar
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == num:
                return False
    
    tablero[fila][col] = num  # colocar temporalmente para probar

    # verificar fila completa
    if all(tablero[fila][j] != 0 for j in range(MAX)):
        if sum(tablero[fila]) != 15:
            tablero[fila][col] = 0
            return False
    
    # verificar columna completa
    if all(tablero[i][col] != 0 for i in range(MAX)):
        if sum(tablero[i][col] for i in range(MAX)) != 15:
            tablero[fila][col] = 0
            return False
    
    # verificar diagonal principal
    if fila == col:
        if all(tablero[i][i] != 0 for i in range(MAX)):
            if sum(tablero[i][i] for i in range(MAX)) != 15:
                tablero[fila][col] = 0
                return False
    
    # verificar diagonal secundaria
    if fila + col == MAX - 1:
        if all(tablero[i][MAX-1-i] != 0 for i in range(MAX)):
            if sum(tablero[i][MAX-1-i] for i in range(MAX)) != 15:
                tablero[fila][col] = 0
                return False
    
    tablero[fila][col] = 0  # restaurar
    return True

# módulo siguiente_posicion
def siguiente_posicion(fila, col):
    col += 1
    if col == MAX:
        col = 0
        fila += 1
    return fila, col

# módulo final
def final(fila, col):
    return fila == MAX

# módulo mostrar_tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end=" ")
        print("")
    print("")

# módulo solucion (backtracking)
def solucion(tablero, fila=0, col=0):
    if final(fila, col):
        return True  # solución completa encontrada
    
    for num in range(1, 10):
        if valida(tablero, fila, col, num):
            tablero[fila][col] = num
            nf, nc = siguiente_posicion(fila, col)
            if solucion(tablero, nf, nc):  # si encontramos una solución, detenemos todo
                return True
            tablero[fila][col] = 0  # retroceso
    
    return False  # no hay solución

# programa principal
def principal():
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    if solucion(tablero):
        print("Solución encontrada:\n")
        mostrar_tablero(tablero)
    else:
        print("No se encontró solución")

principal()

