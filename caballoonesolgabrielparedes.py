import numpy as np

def mostrar_tablero(tablero):
    for fila in tablero:
        print("  ".join(f"{int(celda):2}" for celda in fila))
    print()

def casilla_valida(f, c, tablero, N):
    return 0 <= f < N and 0 <= c < N and tablero[f][c] == -1# la fila esta dentro del tablero, la columna igual, y la casilla esta vacia retorna true

def backtracking(fila, columna, paso, tablero, N):
    if paso == N * N:#paso es 
        return True

    mov_fila = [1, 2, 2, 1, -1, -2, -2, -1]
    mov_col  = [2, 1, -1, -2, -2, -1, 1, 2]

    candidato = 0
    

    while candidato < 8:
        nueva_f = fila + mov_fila[candidato]
        nueva_c = columna + mov_col[candidato]

        if casilla_valida(nueva_f, nueva_c, tablero, N):
            tablero[nueva_f][nueva_c] = paso

            if backtracking(nueva_f, nueva_c, paso + 1, tablero, N):
                return True
            else:
                tablero[nueva_f][nueva_c] = -1
        else:
            pass

        candidato += 1

    return False

def caballo():
    N = 3 #tamaño de la matriz
    tablero = np.full((N, N), -1, dtype=int)#crea la matriz con la libreria numpy lleno de -1
    tablero[0][0] = 0 #la posicion 0,0 de la matriz será 0 en vez de -1


    if backtracking(0, 0, 1, tablero, N):
        mostrar_tablero(tablero)
    else:
        print("No hay solución para N =", N)

caballo()
