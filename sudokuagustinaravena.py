N = 9


# módulo valida
def valida(tablero, fila, col, num):
    # revisar fila
    for j in range(N):
        if tablero[fila][j] == num:
            return False
    
    # revisar columna
    for i in range(N):
        if tablero[i][col] == num:
            return False
    
    # revisar subcuadrícula 3x3
    inicio_f = fila - (fila % 3)
    inicio_c = col  - (col % 3)

    for i in range(3):
        for j in range(3):
            if tablero[inicio_f + i][inicio_c + j] == num:
                return False
    
    return True



# módulo siguiente_posicion
def siguiente_posicion(fila, col):
    col += 1
    if col == N:
        col = 0
        fila += 1
    return fila, col


# módulo final

def final(fila, col):
    return fila == N   # si fila llegó a 9, ya terminamos


# módulo mostrar_tablero
def mostrar_tablero(tablero):
    for i in range(N):
        
        # línea horizontal cada 3 filas
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        
        for j in range(N):
            
            # línea vertical cada 3 columnas
            if j % 3 == 0 and j != 0:
                print("|", end=" ")

            print(tablero[i][j], end=" ")

        print("")  # salto de línea al final de cada fila
    print("")      # línea extra al final


# módulo solucion (RECURSIVA)
def solucion(tablero, fila=0, col=0):

    if final(fila, col):
        return True

    # si esta celda ya tiene número, seguir con la siguiente
    if tablero[fila][col] != 0:
        nf, nc = siguiente_posicion(fila, col)
        return solucion(tablero, nf, nc)   # llamada recursiva

    # intentar números del 1 al 9
    for num in range(1, 10):
        if valida(tablero, fila, col, num):
            tablero[fila][col] = num

            nf, nc = siguiente_posicion(fila, col)

            # llamada recursiva para seguir resolviendo
            if solucion(tablero, nf, nc):
                return True

            # si no funcionó, retroceder
            tablero[fila][col] = 0

    return False  # no hay número válido para esta celda



# programa principal
def principal():
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

    print("Sudoku inicial:\n")
    mostrar_tablero(tablero)

    if solucion(tablero):
        print("Sudoku resuelto:\n")
        mostrar_tablero(tablero)
    else:
        print("No tiene solución")


principal()
