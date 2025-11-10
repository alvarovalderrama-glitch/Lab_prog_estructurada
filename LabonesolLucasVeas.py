import random
# se genera un tablero vacío de tamaño MAX x MAX
MAX = int(input("Se generará un tablero cuadrado con el numero que ingrese:  \n> ")) # Tamaño del tablero
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]     # Crear un tablero vacío de tamaño XxX
movimientos = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # derecha, abajo, izquierda, arriba
max_tablero = len(tablero) 
inicio = (0, 0)
final = (max_tablero - 1, max_tablero - 1)

# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        for celda in fila:
            print(celda, end=" ")
        print()

# Función que coloca obstáculos aleatorios en el tablero
def obstaculos(tablero, porcentaje=0.20):
    tamaño_tablero = len(tablero) * len(tablero)
    cantidad_obstaculos = int(tamaño_tablero * porcentaje)
    obstaculo_puestos = 0
    while obstaculo_puestos < cantidad_obstaculos:
        ox = random.randint(0, max_tablero - 1)
        oy = random.randint(0, max_tablero - 1)
        if [ox, oy] != [0, 0] and [ox, oy] != [max_tablero - 1, max_tablero - 1]:
            if tablero[ox][oy] != "X":
                tablero[ox][oy] = "X"
                obstaculo_puestos += 1
    return tablero 

# Función que valida si una posición es válida para moverse
def validacion(tablero, x, y):
    return (0 <= x < max_tablero) and (0 <= y < max_tablero) and (tablero[x][y] != "X") and (tablero[x][y] != ".")

# Función principal de backtracking para encontrar un camino
def backtracking(tablero):
    camino = [] # lista para almacenar el camino
    if not validacion(tablero, *inicio) or not validacion(tablero, *final): #si inicio o final son obstaculos
        return [] 
    
# Función recursiva DFS para explorar el tablero
    def dfs(x, y): 
        if not validacion(tablero, x, y): 
            return False 
        
        origen = tablero[x][y] # guarda el valor original
        tablero[x][y] = "."      # marca como visitado
        camino.append((x, y)) # agrega la posición al camino

        if (x, y) == final: 
            return True

        for df, dc in movimientos: # intenta moverse en cada dirección
            if dfs(x+df, y+dc): 
                return True # si encuentra el camino, retorna True

            
        camino.pop() # backtrack: elimina la posición del camino
        tablero[x][y] = origen # restaura el valor original
        return False 
    return camino if dfs(*inicio) else [] # retorna el camino si se encontró, sino lista vacía

# Función para marcar el camino encontrado en el tablero    
def marcar_camino(tablero, camino): 
    

    # restaurar el tablero a su estado original
    for i in range(max_tablero): 
        for j in range(max_tablero): 
            if tablero[i][j] == ".": 
                tablero[i][j] = 0 

    if not camino: # si no hay camino, retorna el tablero original
        return tablero

    # marca el camino en el tablero
    (sx, sy) = camino[0] 
    (gx, gy) = camino[-1]
    tablero[sx][sy] = "E" 
    for (x, y) in camino[1:-1]: 
        tablero[x][y] = "*"
    tablero[gx][gy] = "S"
    return tablero
    

# Generar y mostrar el tablero con obstáculos
print(f"Tablero de tamaño {MAX}x{MAX}:")
obstaculos(tablero, porcentaje=0.20)
imprimir_tablero(tablero)

solución = backtracking(tablero)
# Mostrar resultados
if solución:
    print("Camino a la salida encontrado:")
    imprimir_tablero(marcar_camino(tablero, solución))
else:
    print("No se encontró un camino a la salida.")
