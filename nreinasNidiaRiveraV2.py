import os
def imprimir_board(Lista):
    print("Contenido de board:")
    for fila in range(len(Lista)):
        print(f"Fila {fila}: columna {Lista[fila]}")

def imprimir_matriz(sol):
    n = len(sol)
    print("─ " * n)#imprime linea superior de la matriz 
    for fila in range(n): #recorre las filas de la matriz sol
        for col in range(n): #recorre cada columna
            if sol[fila] == col:
                print("R", end=" ") #imprime R sin salto de linea al final
            else:
                print(".", end=" ") #imprime la celda que no tiene Reina
        print()   # salto de línea
    print("─ " * n)      #imprime linea inferior de la matriz 
    print (" ") #imprime linea de separacion



def es_posible(tablero, fila, col, n):
   
    #imprimir_board(tablero)
    # Revisar si hay una reina en la misma columna
    for i in range(fila):
        if tablero[i] == col:
            print ("**")
            return False

    # Revisar si hay una reina en la diagonal superior izquierda
    for i, j in zip(range(fila, -1, -1), range(col, -1, -1)):
        if tablero[i] == j:
            return False

    # Revisar si hay una reina en la diagonal superior derecha
    for i, j in zip(range(fila, -1, -1), range(col, n)):
        if tablero[i] == j:
            return False

    return True


# Backtracking para colocar reinas
def resolver_n_reinas(matriz, fila, n, soluciones):
    
    if fila == n:  # Si ya colocamos las reinas en todas las filas, entonces llegamos a la solución
        soluciones.append(matriz.copy())   # guardamos la matriz en el conjunto de soluciones
        return

    for col in range(n):
        if es_posible(matriz, fila, col, n):
            matriz[fila] = col       # colocar reina
            #print ("["+str(fila)+","+str(col)+"]")
            resolver_n_reinas(matriz, fila + 1, n, soluciones) #Evaluar avance a la siguiente fila
            matriz[fila] = -1        # si llega aqui no era posible avanzar en la fila, aplicar backtracking
            #print ("[back"+str(fila)+"]")
        #else:
            #print ("["+str(fila)+","+str(col)+"]=X")

os.system("cls")
dimension = int(input("Ingrese Dimension del Tablero :"))
tablero = [-1] * dimension #Inicio del tablero sin ninguna Reina ubicada
soluciones = []
resolver_n_reinas(tablero, 0, dimension, soluciones)

print("Total de soluciones encontradas:", len(soluciones))
print()
i=0
# Mostrar todas las soluciones
for s in soluciones:
    i+=1
    print ("Solucion "+ str(i))
    imprimir_matriz(s)