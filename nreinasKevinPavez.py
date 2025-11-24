"""Comenzamos creando un tablero 9x9 llenos de 0's 
"""
def crear_tablero(n):
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        tablero.append(fila)
    return tablero

"""Seguimos con la funcion para imprimir el tablero en
la terminal y utilizamos un ciclo for para su impresion"""
def imprimir_tablero(tablero, n):
    print("\n" + "="*(n*4+1))
    for i in range(n):
        print("| ", end="")
        for j in range(n):
            if tablero[i][j] == 1:
                print("Q | ", end="")  
            else:
                print("_ | ", end="") 
        print()
        print("="*(n*4+1))
        
def es_seguro(tablero, fila, columna, n):
    """
    Comprobar que sea seguro colocar una reina en tablero[fila][columna]
    """
    # Verificar la columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False
        
    """Comprobar la diagonal izquierda"""
    i = fila - 1
    j = columna - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    """Comprobar la diagonal derecha"""
    i = fila - 1
    j = columna + 1
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    return True

def resolver_n_reinas(tablero, fila, n):
    """
    Resuelver el problema de las N Reinas usando backtracking
    """
    "Caso base: Coloca reinas en todas las filas"""
    if fila >= n:
        return True
    
    """Recursividad"""
    for columna in range(n):
        if es_seguro(tablero, fila, columna, n):
            """Se puede colocar la reina?"""
            tablero[fila][columna] = 1
            
            """Llamamos la recursividad"""
            if resolver_n_reinas(tablero, fila + 1, n):
                return True
            
            """Backtracking"""
            tablero[fila][columna] = 0
    
    """Si ninguna funciono, retornamos false"""
    return False

"""Programa main"""
if __name__ == "__main__":
    print("="*40)
    print("  PROBLEMA DE LAS N REINAS")
    print("="*40)

    n = int(input("\n¿Cuántas reinas quieres colocar? (N): "))
    
    tablero = crear_tablero(n)
    
    print(f"\nResolviendo el problema de las {n} reinas...")

    if resolver_n_reinas(tablero, 0, n):
        print(f"\n SOLUCIÓN ENCONTRADA para {n} reinas:")
        imprimir_tablero(tablero, n)
    else:
        print(f"\n No existe solucion para {n} reinas")