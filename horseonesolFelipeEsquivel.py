MAX = 5 # Tamaño del tablero

# módulo valida
def valida(tablero, candidato, x, y): # verifica si el movimiento es válido
    posx = [-2, -1, 1, 2, 2, 1, -1, -2]
    posy = [1, 2, 2, 1, -1, -2, -2, -1]
    nx = x + posx[candidato - 1] 
    ny = y + posy[candidato - 1]
    if nx < 0 or nx >= MAX:  #que no se salga del tablero
        return False  
    if ny < 0 or ny >= MAX: 
        return False
    if tablero[nx][ny] != 0: # que no haya sido visitado
        return False 
    return True 

# módulo siguiente_posicion
def siguiente_posicion(tablero, candidato, x, y): # calcula la siguiente posición del caballo
    posx = [-2, -1, 1, 2, 2, 1, -1, -2] 
    posy = [1, 2, 2, 1, -1, -2, -2, -1]
    nx = x + posx[candidato - 1] 
    ny = y + posy[candidato - 1]
    return nx, ny

# módulo final
def final(tablero): # verifica si el tablero está completo
    for i in range(MAX): # fila
        for j in range(MAX): # columna
            if tablero[i][j] == 0: # si hay alguna celda vacía
                return False 
    return True 

# módulo buscar_xy
def buscar_xy(tablero, contador): # busca la posición (x,y) del contador en el tablero
    for i in range(MAX): # fila
        for j in range(MAX): # columna
            if tablero[i][j] == contador: 
                return i, j
    return None, None

# módulo mostrar_tablero
def mostrar_tablero(tablero): 
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ") 
        print("")
    print("")

# módulo solucion (principal)
def solucion(tablero): # intenta resolver el problema del caballo usando backtracking
    candidato = 1 
    resuelto = False
    x, y, contador = 0, 0, 1 
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)] # tablero auxiliar para guardar los candidatos probados
    tablero[x][y] = contador # marca la primera posición

    while candidato <= 8 and not resuelto: # mientras haya candidatos y no esté resuelto
        if valida(tablero, candidato, x, y): # si el movimiento es válido
            nx, ny = siguiente_posicion(tablero, candidato, x, y) # calcula la siguiente posición
            tablero[nx][ny] = contador + 1
            mostrar_tablero(tablero)
            if final(tablero): # si el tablero está completo
                resuelto = True # marca como resuelto
            else:
                tablero_aux[x][y] = candidato # guarda el candidato probado
                x, y = nx, ny # actualiza la posición
                contador += 1
                candidato = 1
        else:
            candidato += 1
            while candidato == 9 and not (x == 0 and y == 0):# si no hay más candidatos y no está en la posición inicial
                tablero[x][y] = 0  # desmarca la posición
                contador -= 1  
                nx, ny = buscar_xy(tablero, contador) # busca la posición del contador
                if nx is None: 
                    return False
                candidato = tablero_aux[nx][ny] + 1 # obtiene el siguiente candidato
                tablero_aux[nx][ny] = 0
                x, y = nx, ny
                mostrar_tablero(tablero)
    return resuelto

# programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # inicializa el tablero
mostrar_tablero(tablero)

if solucion(tablero):  # si se encontró solución
    print("Hay solución encontrada:") 
    mostrar_tablero(tablero)
else: # si no se encontró solución
    print("No hay solución")




