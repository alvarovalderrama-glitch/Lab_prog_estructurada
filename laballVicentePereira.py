MAX = 3
#modulo solucion
'''def solucion(tablero):
    while(hay candidtos y no solucion):
        if(valida):
            avanza
            if(final):
                solucion = True
            else:
                dejo pistas
        else:
            siguiente candidato
            while(no hay candidatos y not inicio):
                retroceder
'''
#modulo valida
def valida(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    if (nx < 0 or nx >= MAX):
        return False
    if (ny < 0 or ny >= MAX):
        return False
    if (tablero[nx][ny]== 0):
        return True
    else:
        return False
#modulo siguiente_posicion 
def siguiente_posicion(tablero,candidato,x,y):
    posx = [0,1,0,-1]
    posy = [1,0,-1,0]
    nx = x+posx [candidato-1]
    ny = y+posy [candidato-1]
    return nx,ny
#modulo final
def final(tablero,nx,ny):
    if (nx == MAX -1 and ny == MAX -1):
        return True
    return False
#modulo buscar_xy
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]== contador):
                return i,j
#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")
def encontrar_todas_las_soluciones(tablero):
    candidato = 1 ; x = 0 ; y = 0 ; contador = 1
    contador_soluciones = 0
    
    tablero_aux = [[0 for _ in range(MAX)] for _ in range (MAX)]
    tablero[x][y] = contador
    while(candidato <=4):
        if(valida(tablero, candidato, x, y )):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1

            if(final(tablero, nx,ny)):
                contador_soluciones += 1
                print('soluciones encontradas: ' + str(contador_soluciones))
                mostrar_tablero(tablero)
                tablero[nx][ny]=0

                candidato = candidato + 1
            else: 
                tablero_aux[x][y]=candidato
                x = nx ; y = ny ; contador = contador + 1
                candidato=1
        else:
            candidato = candidato + 1
            while(candidato == 5 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador -=1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] +1
                tablero_aux[nx][ny] = 0
                x = nx; y = ny
    return contador_soluciones
tablero_uno = [[0 for _ in range(MAX)] for _ in range(MAX)]
if encontrar_todas_las_soluciones(tablero_uno):
    print('soluciones')
else:
    print("No se encontro solucion.")