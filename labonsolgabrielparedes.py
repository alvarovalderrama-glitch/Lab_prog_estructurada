import numpy as np

def backtracking(fila, columna, movimientos, tablero, N):
    if fila == N - 1 and columna == N - 1: 
        tablero[fila][columna] = movimientos
        return True
    
    tablero[fila][columna] = movimientos
    movimientos_posibles = [(1,0), (0,1), (-1,0), (0,-1)]#crea una lista de los posibles movimientos del objeto
    candidato = 0#es el contador de los posibles movimientos
    while candidato < 4:
        #calcula la nueva posicion 
        nueva_fila = fila + movimientos_posibles[candidato][0]
        nueva_columna = columna + movimientos_posibles[candidato][1]

        
        if 0 <= nueva_fila < N and 0 <= nueva_columna < N: #si casilla la casilla esta dentro de la matriz

            
            if tablero[nueva_fila][nueva_columna] == -1:#solo entra si la casilla esta libre, es decir = -1

                
                if backtracking(nueva_fila, nueva_columna, movimientos + 1, tablero, N):#recursivamente se llama de nuevo a la funcion con otros parametros
                    return True#si encuentra solucion retorna true
                else:
                  
                    tablero[nueva_fila][nueva_columna] = -1#sino encuentra solucion la casilla vuelve a estar libre, o sea = -1

        
        candidato += 1#aumenta candidado +1 final de cada loop

    
    return False
    

def mostrar_tablero(tablero):
    print("\nLaberinto: ")
    for fila in tablero:
        for celda in fila:
            if celda == -2:
                print("X", end=" ")#bloqueo
            elif celda == -1:
                print(".", end=" ")#camino disponible
            else:
                print(celda, end=" ")
        print()
    print()

def obstaculos(tablero):#crea los lugares por los que no puede ir el objeto
    tablero[1][1] = -2
    tablero[2][1] = -2
    tablero[3][3] = -2
    tablero[1][3] = -2
    tablero[1][4] = -2
    tablero[3][4] = -2
    tablero[4][0] = -2
   
def laberinto():
    N = 5 #numero para limitar la matriz
    tablero = np.full((N,N), -1, dtype = int) #creacion de la matriz
    obstaculos(tablero)#llama funcion para poner obstaculos en el laberinto
    tablero[0][0] = 0 #posicion inicial
    mostrar_tablero(tablero)
    
    fila = 0
    columna = 0
    movimientos = 0
    if backtracking(fila, columna, movimientos, tablero, N):
        print("Solución encontrada:")
        mostrar_tablero(tablero)
    else:
        print("No hay solución :(")
    
laberinto()