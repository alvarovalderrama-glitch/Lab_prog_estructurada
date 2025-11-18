MAX = 5 #tamaño tablero

fila= [2, 1, -1 , -2 , -2, -1 ,1 ,2]
columna= [1, 2 ,2 ,1 , -1 , -2 , -2 , -1]

def validar (x,y , tablero):
    # print('a')
    # print('b')
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == -1
    #valida la posicion del caballo a usar si esta fuera del tablero o si es un movimiento valido

def tableroo(tablero): 
    for i in tablero:
        print(" ".join(f'{c:2}' for c in i)) #imprime tablero con una separacio en cada movimiento
    print('-----------------------') #separacion de tablero

def devolver(x, y, paso, tablero, soluciones):
    if paso == MAX * MAX: #verifica que el tablero esta lleno
        soluciones.append([fila[:] for fila in tablero]) #ingresa el tablero y guarda
    for i in range(8): #movimiento de caballo
        nx = x+fila[i] #utiliza los movimientos en x (plano cartesiano)
        ny = y+columna[i] #utiliza los movimientos en y (plano cartesiano)
        if validar(nx, ny, tablero): 
            tablero[nx][ny] = paso #si es validada la nueva posicion del caballo este guarda en el mismo lugar 
            devolver(nx, ny, paso + 1, tablero, soluciones) #se vuelve mover el caballo y a seguir el siclo
            tablero[nx][ny] = -1


tablero= [[-1 for _ in range(MAX)]for _ in range(MAX)] #se crea un tablero
tablero[0][0] = 0 #posiciona caballo
soluciones = [] #guarda soluciones
devolver(0,0,1, tablero, soluciones)
for i, o in enumerate(soluciones, 1):  #separa los tableros existentes y les asigna un numero de serie empezando por el 1
    print(f'Solucion {i}:') #imprime numero de serie
    tableroo(o) #imprime tableros guardados


