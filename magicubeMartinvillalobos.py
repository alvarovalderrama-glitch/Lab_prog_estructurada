
N = 3  # tamaño del cuadrado mágico 3x3
M = 15  # suma mágica del cuadrado 3x3

# Inicializar cuadrado vacío
cuadrado = [[0] * N for _ in range(N)]

# Para registrar cuáles números del 1 al 9 están usados
usado = [False] * 10

def es_valido():
    """Revisa si filas, columnas y diagonales que están completas cumplen la suma."""
    # Revisar filas
    for fila in cuadrado:
        if 0 not in fila:  # fila completa
            if sum(fila) != M:
                return False
    
    # Revisar columnas
    for col in range(N):
        columna = [cuadrado[f][col] for f in range(N)]
        if 0 not in columna:  # columna completa
            if sum(columna) != M:
                return False

    # Revisar diagonal principal
    diag1 = [cuadrado[i][i] for i in range(N)]
    if 0 not in diag1:  # completa
        if sum(diag1) != M:
            return False

    # Revisar diagonal secundaria
    diag2 = [cuadrado[i][N - 1 - i] for i in range(N)]
    if 0 not in diag2:  # completa
        if sum(diag2) != M:
            return False

    return True

def resolver(pos):
    """Backtracking para llenar el cuadrado mágico."""
    if pos == N * N:  
        return True  # completado

    x = pos // N
    y = pos % N

    for num in range(1, 10):  
        if not usado[num]:
            cuadrado[x][y] = num
            usado[num] = True

            if es_valido():  
                if resolver(pos + 1):  
                    return True

            cuadrado[x][y] = 0
            usado[num] = False

    return False

# PROGRAMA PRINCIPAL
if resolver(0):
    print("Cuadrado mágico encontrado:")
    for fila in cuadrado:
        print(fila)
else:
    print("No existe solución.")