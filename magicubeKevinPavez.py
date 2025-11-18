"""
CUADRADO MAGICO
"""


MAX = 3
SUMA_MAGICA = 15
"""Creamos el tablero"""
def crear_tablero():
    tablero = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return tablero

"""Funcion para imprimir el tablero en la consola"""
def imprimir_tablero(t):
    print("\nCUADRADO MAGICO:")
    for i in range(MAX):
        for j in range(MAX):
            print(t[i][j], end=" ")
        print()

"""Funcion para validar nuneros del tablero"""
def es_valido(t, num, x, y):
    if t[x][y] != 0:
        return False
    
    for i in range(MAX):
        for j in range(MAX):
            if t[i][j] == num:
                return False
    return True


def verificar_suma(t):
    """Verifica si todas las filas, columnas y diagonales suman 15"""
    # Filas
    for i in range(MAX):
        if sum(t[i]) != SUMA_MAGICA:
            return False
    
    # Columnas
    for j in range(MAX):
        suma = t[0][j] + t[1][j] + t[2][j]
        if suma != SUMA_MAGICA:
            return False
    
    # Diagonal principal
    if t[0][0] + t[1][1] + t[2][2] != SUMA_MAGICA:
        return False
    
    # Diagonal secundaria
    if t[0][2] + t[1][1] + t[2][0] != SUMA_MAGICA:
        return False
    
    return True


def backtracking(t, pos):
    """
    BACKTRACKING: Intenta llenar el tablero posicion por posicion (0-9)
    """
    #Validacion si el tablero esta lleno
    if pos == 9:
        if verificar_suma(t):
            return True
        return False
    
    # Calcular fila y columna desde la posicion
    fila = pos // 3
    col = pos % 3
    
    # Probar numeros del 1 al 9
    for num in range(1, 10):
        if es_valido(t, num, fila, col):
            t[fila][col] = num  
            
            # RECURSION: intentar llenar la siguiente posicion
            if backtracking(t, pos + 1):
                return True
            
            # BACKTRACKING: si no funciono, quitar el numero
            t[fila][col] = 0
    
    return False


# PROGRAMA PRINCIPAL
tablero = crear_tablero()

if backtracking(tablero, 0):
    imprimir_tablero(tablero)
    print(f"\nSuma: {SUMA_MAGICA}")
else:
    print("NO HAY SOLUCION")