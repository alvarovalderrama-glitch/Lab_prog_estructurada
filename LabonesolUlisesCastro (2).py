import random
x = 5 # Tamaño del tablero
tablero = [[0 for _ in range(x)] for _ in range(x)]     # Crear un tablero vacío de tamaño XxX
movimientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]  #movimientos posibles
max_tablero = len(tablero)
inicio = (0, 0)
final = (max_tablero - 1, max_tablero - 1)
def imprimir_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()
def  obstaculos(tablero):
    obs = max_tablero + max_tablero // 2 + 1
    piedras = 0
    while piedras < obs:
        ox = random.randint(0, max_tablero - 1)
        oy = random.randint(0, max_tablero - 1)
        if [ox, oy] != [0, 0] and [ox, oy] != [max_tablero - 1, max_tablero - 1]:
            if tablero[ox][oy] != "X":
                tablero[ox][oy] = "X"
                piedras += 1
    return tablero 
def validacion(tablero, x, y):
    return (0 <= x < max_tablero) and (0 <= y < max_tablero) and (tablero[x][y] != "X") and (tablero[x][y] != ".")
def backtracking(tablero):
    camino = []
    if not validacion(tablero, *inicio) or not validacion(tablero, *final): #si inicio o final son obstaculos
        return []
    def dfs(x, y):
        if not validacion(tablero, x, y):
            return False
        # marcar en sitio
        origen = tablero[x][y]
        tablero[x][y] = "."
        camino.append((x, y))
        if (x, y) == final:
            return True
        for dr, dc in movimientos:
            if dfs(x+dr, y+dc):
                return True
        camino.pop()
        tablero[x][y] = origen
        return False
    return camino if dfs(*inicio) else []
def marcar_camino(tablero, camino):
    # limpiar los puntos de recorrido del DFS que no forman parte del camino final
    for i in range(max_tablero):
        for j in range(max_tablero):
            if tablero[i][j] == ".":
                tablero[i][j] = 0
    if not camino:
        return tablero
    # marcar camino final
    (sx, sy) = camino[0]
    (gx, gy) = camino[-1]
    tablero[sx][sy] = "I"
    for (x, y) in camino[1:-1]:
        tablero[x][y] = "*"
    tablero[gx][gy] = "F"
    return tablero
print(f"Tablero de tamaño {x}x{x}:")
obstaculos(tablero)
imprimir_tablero(tablero)
cc = backtracking(tablero)
if cc:
    print("se encontro camino encontrado:")
    imprimir_tablero(marcar_camino(tablero, cc))
else:
    print("No se encontró camino alguno.")