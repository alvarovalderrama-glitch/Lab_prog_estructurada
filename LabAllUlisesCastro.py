import random

SOLUCIONES_A_IMPRIMIR = 100 #define las soluciones que quiera imprimir

x = 5 #define el tamaño del tablero
tablero = [[0 for _ in range(x)] for _ in range(x)]
movimientos = [[0, 1], [1, 0], [0, -1], [-1, 0]] #los movimientos posibles de el laberinto
max_tablero = len(tablero)
inicio = (0, 0) #desde donde se inicia
final = (max_tablero - 1, max_tablero - 1) #la salida

def imprimir_tablero(tablero): #lo que imprime el  tablero
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()
    print("-" * (max_tablero * 2))

def  obstaculos(tablero): #los obstaculos del laberinto
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

def validacion(tablero, x, y): #revisa si es valido el movimiento del tablro
    return (0 <= x < max_tablero) and (0 <= y < max_tablero) and (tablero[x][y] != "X") and (tablero[x][y] != ".")

def backtracking_todas(tablero):
    soluciones = []
    
    if not validacion(tablero, *inicio) or not validacion(tablero, *final):
        return []

    def dfs(x, y, camino_actual):
        if not validacion(tablero, x, y):
            return 
        
        origen = tablero[x][y]
        tablero[x][y] = "."
        camino_actual.append((x, y))

        if (x, y) == final:
            soluciones.append(list(camino_actual))
        
        for dr, dc in movimientos:
            dfs(x + dr, y + dc, camino_actual)
            
        camino_actual.pop()
        tablero[x][y] = origen
    
    dfs(*inicio, [])
    return soluciones

def marcar_camino_solucion(tablero_original, camino):
    tablero_copia = [fila[:] for fila in tablero_original]
    
    if not camino:
        return tablero_copia
        
    (sx, sy) = camino[0]
    (gx, gy) = camino[-1]
    
    for (x, y) in camino[1:-1]:
        tablero_copia[x][y] = "*"
        
    tablero_copia[sx][sy] = "I"
    tablero_copia[gx][gy] = "F"
    
    return tablero_copia

print(f"Tablero de tamaño {x}x{x}:")
obstaculos(tablero)
imprimir_tablero(tablero)

todos_los_caminos = backtracking_todas(tablero)

if todos_los_caminos:
    num_soluciones_encontradas = len(todos_los_caminos)
    
    limite_impresion = min(SOLUCIONES_A_IMPRIMIR, num_soluciones_encontradas)
    
    print(f"Se encontraron {num_soluciones_encontradas} caminos en total.")
    print(f"Mostrando {limite_impresion} caminos (según SOLUCIONES_A_IMPRIMIR = {SOLUCIONES_A_IMPRIMIR}):")
    
    for i in range(limite_impresion):
        print(f"\nSolución #{i + 1}:")
        imprimir_tablero(marcar_camino_solucion(tablero, todos_los_caminos[i])) #esto imprime el tablero resuelto y todas sus soluciones
    
else:
    print("No se encontró camino alguno.")