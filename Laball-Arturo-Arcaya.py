max = 5
inicio = (0, 0)
meta = (max - 1, max - 1)

tablero = [[0 for _ in range(max)] for _ in range(max)] #crea tablero
tablero[3][2] = -1 #paredes
tablero[4][0] = -1
tablero[2][1] = -1
tablero[0][1] = -1
tablero[1][3] = -1
tablero[4][4] = 0

def imprimir_tablero(tablero): #imprime tablero
    for fila in tablero:
        print(" ".join(f'{c:2}' for c in fila))
    print()

def buscar(x, y, camino, a, visitado, soluciones):
    if x < 0 or x >= max or y < 0 or y >= max: #veririca la posicion
        return
    if tablero[x][y] == -1 or visitado[x][y]: #si la celda es una pared se descarta
        return

    camino[a] = (x, y)  #guarda la posición actual en el camino
    visitado[x][y] = True #marca la celda como visitada

    if (x, y) == meta: #si se llega a la meta la solucion se guarda
        soluciones.appent(1) #añade un contador
        tablero_solucion = [fila[:] for fila in tablero] #guarda una copia del tablero
        for i in range(a): #recorre el camino hasta llegar a 'a'
            cx, cy = camino[i] #
            tablero_solucion[cx][cy] = str('x') #marca con una X el rastro del camino
        tablero_solucion[x][y] = str('G') #marca la meta con la ficha del jugador 'G'
        print(f"Solución {len(soluciones)}:") 
        imprimir_tablero(tablero_solucion) #imprime el numero de la solucion y la solucion
    else:
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]: #si no se lelga a la meta explora las 4 direcciones posibles
            buscar(x + dx, y + dy, camino, a + 1, visitado, soluciones) #vuelve a llamar a la funcion 

    visitado[x][y] = False #quita la marca de la celda para seguir explorando

camino = [None] * (max * max)  #genera espacios vacios segun el tablero
visitado = [[False]*max for _ in range(max)] #genera otros espacios vacios segun el tablero para que no se vuelva a visitar
soluciones = [] 

buscar(inicio[0], inicio[1], camino, 0, visitado, soluciones)

print(f"\nTotal de soluciones encontradas: {len(soluciones)}")
