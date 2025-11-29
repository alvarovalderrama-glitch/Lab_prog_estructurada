import numpy as np


def mostrar_tablero(tablero, N): #Crea el tablero más bonito y luego lo muestra
    for fila in range(N):
        for col in range(N):
            print(" | ", tablero[fila][col], end=" ")#imprime con col = 0 con _ simulando el espacio al lado: | 0 _, col = 1: | 0 | 0 _, col = 2: | 0 | 0 | 0 _
        print(" | ")
    print()
    
    
def casilla_valida(fila, col, tablero, N):
    if 0 <= fila < N and 0 <= col < N:#si la casilla esta dentro del tablero
        return tablero[fila][col] == 0 # retornara true o falso, dependiendo de si la casilla[fila][col] es igual a 0, es decir, que esta vacia.
    return False#si esta fuera del tablero retorna false

def cuadrado_magico(tablero, N):
    numero_ganador = N*((N*N)+1) // 2
    for fila in range(N):# suma filas como listas enteras
        if sum(tablero[fila]) != numero_ganador:
            return False
    
    for col in range(N):#suma columnas paso a paso tablero empieza posicion [0][x]
        suma_col = 0 #crea variable suma_col que inicia en 0
        for fila in range(N):#posicion [0][0] hasta [0][N-1]
            suma_col +=  tablero[fila][col] #suma suma_col + el numero en la posicion tablero[fila][col]
        if suma_col != numero_ganador: #si la suma total de columnas es distina a numero_ganador retorna falso
            return False
    
    #suma diagonales [0][0]  [1][1]  [2][2] tengo que hacer que posicion 0 se guarde para cuando llegue a i= 1 sea diagonal 0 + diagonal 1
    diag1 = 0
    for i in range(N):
        diag1 += tablero[i][i]
        
    if diag1 != numero_ganador:
        return False
        
        
    diag2 = 0
    for i in range(N):#segunda diagonales [2][0] [1][1] [0][2] = i = 2 disminuye j = 0 aumenta
        diag2 += tablero[i][N - 1 - i]
    if diag2 != numero_ganador:
        return False
    return True
    

def backtracking(fila, col, usados, tablero, N):
    
    if fila == N:  #si filas llega al limite retorna cuadrado magico
        return cuadrado_magico(tablero, N)

    nueva_fila = fila #avanza a sgte fila
    nueva_col = col + 1
    if nueva_col == N:     
        nueva_fila += 1
        nueva_col = 0

    for candidato in range(1, N*N + 1):  #candidato los numeros posibles, en este caso 1 al 9
        
        if (candidato not in usados) and casilla_valida(fila, col, tablero, N): #si candidato no esta usado y casilla vacia
            
            tablero[fila][col] = candidato #coloca el numero
            usados.add(candidato)          #marca usado
            
            if backtracking(nueva_fila, nueva_col, usados, tablero, N):
                return True  #si al avanzar se completo todo
            
            tablero[fila][col] = 0  #si no funciona, vacio
            usados.remove(candidato)

    return False  #si ningun candidato sirve, retrocede



def main():
    N = 3
    tablero = np.full((N,N), 0 , dtype=int)#crea el tablero lleno de 0
    usados = set()
   
    if backtracking(0, 0, usados, tablero, N):
        print("es cuadrado magico: ")
        mostrar_tablero(tablero, N)
    else:
        print("no se ha encontrado solución")
   
main()