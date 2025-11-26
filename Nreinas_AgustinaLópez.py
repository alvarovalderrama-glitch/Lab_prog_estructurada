import math
# Funciones auxiliares para clonar el tablero y crear un tablero nuevo
def clone(tablero):
    tablero_nuevo=[]
    for i in range(len(tablero)):
        fila=[]
        for j in range(len(tablero[i])):
            fila.append(tablero[i][j])
        tablero_nuevo.append(fila)
    return tablero_nuevo
#funcion para crear un tablero nuevo de tamaño nxn
def tablero_nuevo(n):
    tablero=[]
    for i in range(n):
        tablero.append(n*[False])
    return tablero
#funcion para verificar si es valido colocar una reina en la posicion (i,j)
def es_valido(tablero, i, j):
    n=len(tablero)
    for k in range(n):
        if tablero[i][k] or tablero[k][j]:
            return False
    for k in range(-n, n):
        if 0 <= i+k < n and 0 <= j+k < n:
            if tablero[i+k][j+k]:
                return False
        if 0 <= i+k < n and 0 <= j-k < n:
            if tablero[i+k][j-k]:
                return False
    return True
#funcion recursiva para resolver N reinas
def resolver_n_reinas(tablero, fila=0):
    n=len(tablero)
    if fila==n:
        return [clone(tablero)]
    soluciones=[]
    for j in range(n):
        if es_valido(tablero, fila, j):
            tablero[fila][j]=True
            soluciones+=resolver_n_reinas(tablero, fila+1)
            tablero[fila][j]=False
    return soluciones  
#funcion principal para resolver N reinas
def n_reinas(n):
    tablero=tablero_nuevo(n)
    return resolver_n_reinas(tablero)
# N Reinas: Encuentra todas las formas de colocar N reinas en un tablero NxN
if __name__ == "__main__":
    n = 4  # se puede cambiar este valor para probar con diferentes tamaños de tablero
    soluciones = n_reinas(n)
    print(f"Se encontraron {len(soluciones)} soluciones para {n} reinas.")
    for idx, solucion in enumerate(soluciones):
        print(f"Solución {idx + 1}:")
        for fila in solucion:
            print(" ".join('Q' if celda else '.' for celda in fila))
        print()
