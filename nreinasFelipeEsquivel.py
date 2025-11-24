tab = [[0 for _ in range(8)] for _ in range(8)]  # Tablero de ajedrez 8x8



def imprimir_tab(tab):
    for i in tab:
        for j in i:
            print(j, end=" ")
        print()

def validacion(tab, fila, columna):

    for j in range(8):
        if tab[fila][j] == 1:          #revisa filas
            return False
    
    for i in range(8):
        if tab[i][columna] == 1:       #revisa columnas
            return False
        
    i = fila - 1
    j = columna - 1
    while i >= 0 and j >= 0:        #revisa diagonal superior izquierda
        if tab[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    
    i = fila + 1
    j = columna - 1
    while i < 8 and j >= 0:   #revisa diagonal inferior izquierda
        if tab[i][j] == 1: 
            return False
        i += 1
        j -= 1

    return True

def backtracking_nreinas(tab, columnas):
    if columnas >= 8:
        return True

    for fila in range(8):
        if validacion(tab, fila, columnas):
            tab[fila][columnas] = 1  # Coloca la reina
            if backtracking_nreinas(tab, columnas + 1):
                return True
            tab[fila][columnas] = 0  # Retrocede si no funciona
    return False



print("Solución del problema de las 8 reinas:")
backtracking_nreinas(tab, 0)
imprimir_tab(tab)