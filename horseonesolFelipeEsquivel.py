MAX = 5  # Tamaño del tablero

def valida(tablero, candidato, x, y):  #valida las posiciones 
    posx = [-2, -1, 1, 2, 2, 1, -1, -2]
    posy = [1, 2, 2, 1, -1, -2, -2, -1]
    nx = x + posx[candidato - 1] 
    ny = y + posy[candidato - 1]
    if nx < 0 or nx >= MAX:  #si se sale del tablero por filas 
        return False  
    if ny < 0 or ny >= MAX: #si se sale del tablero por columna
        return False
    if tablero[nx][ny] != 0:   #si fue visitada
        return False 
    return True 

def copiar_tablero(tab):          
    return [fila[:] for fila in tab]

def siguiente_posicion(tablero, candidato, x, y):  #funcion para moverse a la siguiente posición 
    posx = [-2, -1, 1, 2, 2, 1, -1, -2] 
    posy = [1, 2, 2, 1, -1, -2, -2, -1]        #movimientos
    nx = x + posx[candidato - 1] 
    ny = y + posy[candidato - 1]        #movimiento hecho
    return nx, ny         #retorna nueva posición

def final(tablero):        #comprueba si el recorrido está hecho 
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0: 
                return False 
    return True 

def buscar_xy(tablero, contador):    #busca la casilla de un numero en especifico
    for i in range(MAX):
        for j in range(MAX):           
            if tablero[i][j] == contador:
                return i, j
    return None, None

def mostrar_tablero(tablero):      #muestra el tablero
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ") 
        print("")
    print("")

def solucion(tablero):                
    candidato = 1       #primer candidato 
    soluciones = []        #lista vacia 
    x, y, contador = 0, 0, 1   #donde empieza y el numero de movimiento 
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)] #guarda el movimiento en un tablero aparte 
    tablero[x][y] = contador   #se marca como visitada la casilla 

    while True:
        if 1 <= candidato <= 8:   #se ocupa un candidato 
            if valida(tablero, candidato, x, y):   # si es valido el movimiento
                nx, ny = siguiente_posicion(tablero, candidato, x, y) # se mueve 
                tablero[nx][ny] = contador + 1 #se marca en la casilla 
                
                if final(tablero):   # si llegó al final 
                    soluciones.append(copiar_tablero(tablero)) #se agrega la solución a la lista 
                    return soluciones #retorna la lista 
                else:
                    tablero_aux[x][y] = candidato # que movimiento se ocupo 
                    x, y = nx, ny #nueva posición del caballo 
                    contador += 1   #siguiente numero 
                    candidato = 1   #se empieza desde el primer candidato 
            else:
                candidato += 1
        else:
            if x == 0 and y == 0: # si volvimos al inicio 
                break

            tablero[x][y] = 0 #desmarca la casilla 
            contador -= 1   #retrocede el contador
            nx, ny = buscar_xy(tablero, contador)  #retrocede en la matriz
            candidato = tablero_aux[nx][ny] + 1     # se ocupa otro candidato
            tablero_aux[nx][ny] = 0  #limpia la matriz aux 
            x, y = nx, ny    #mueve a casilla 

    return soluciones  #retorna lista completa 

# programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]

soluciones = solucion(tablero)
print("Solución encontrada:")
mostrar_tablero(soluciones[0])



