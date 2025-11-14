max = 5
inicio = (0, 0)
meta = (max - 1, max - 1)


tablero = [[0 for _ in range (max)]for _ in range(max)] #genera tablero
tablero[3][2]= -1 #asignacion de paredes y espacios
tablero[4][2]= -1
tablero[4][3]= -1
tablero[4][0]= -1
tablero[2][1]= -1
tablero[0][1]= -1
tablero[1][3]= -1
tablero[2][4]= -1
tablero[4][4]= 0
for i in tablero: 
   print(" ".join(f'{c:2}' for c in i)) #genera espacios entre verticales


def jugar(tablero, inicio, meta):
    direcciones = [(-1,0), (1,0), (0,-1), (0,1)] #iz der arr ab
    visitado = [[False]*max for _ in range(max)] #verifica si la celda ya fue tomada como camino
    back = [[None]*max for _ in range(max)] #guarda para poder devolverse
    backtracking = [inicio] #regresa a inicio
    visitado[inicio[0]][inicio[1]] = True #guarda la posicion antes del backtracking

    while backtracking:
        x, y = backtracking[0]   #obtiene el primer digito del backtracking
        backtracking = backtracking[1:] 
        if (x, y) == meta: #verifica si se llego al final
            break
        for dx, dy in direcciones: #verifica las coordenadas
            nx, ny = x + dx, y + dy #verifica con los movimientos
            if 0 <= nx < max and 0 <= ny < max: #verifica que la celda pueda ser elegida
                if not visitado[nx][ny] and tablero[nx][ny] != -1: #si peude ser elegida se guarda la visita, el back y backtraking
                    visitado[nx][ny] = True
                    back[nx][ny] = (x, y)
                    backtracking.append((nx, ny))

    
    camino = [] #crea lista camino
    actual = meta #ubica el comienzo en la meta
    while actual != inicio: 
        camino.append(actual) #ingresa la ubicacion de la meta en camino
        actual = back[actual[0]][actual[1]] #recorre por las pistas usando back
        if actual is None:
            return []  # No hay camino
    camino.append(inicio) #agrega inicio
    camino.reverse() #reinvierte la lista para que esta este en el orden correcto
    return camino


camino = jugar(tablero, inicio, meta)


if camino:
    print("\nCamino encontrado:") 
    
    for x, y in camino:
        for i in range(max):
            for j in range(max):
                if tablero[i][j] == 2:
                    tablero[i][j] = str('X') #coloca una X en los movimientos 
        tablero[x][y] = 2 #coloca el jugador en la nueva posicion
        print("----------------")
        for fila in tablero:
            print(" ".join(f'{c:2}' for c in fila)) # genera la lisat con espacios
else:
    print("\nNo hay camino disponible hasta la meta.")
