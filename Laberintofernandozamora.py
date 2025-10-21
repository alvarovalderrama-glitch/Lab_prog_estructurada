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
    #print("\n valores x, y", x,y," nuevo nx, ny",nx,ny)
    #input("Enter para continuar")
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
#modulo solucion
def solucion(tablero):
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while(candidato <= 4): #and not solucion):
        #print("\n candidato = ",candidato)
        if(valida(tablero, candidato, x, y)):
            #print("\n entre al valida")
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            #mostrar_tablero(tablero)
            if(final(tablero,nx,ny)):
                mostrar_tablero(tablero)
                input("Enter para continuar")
                tablero[nx][ny] = 0
                candidato = candidato + 1
                while(candidato == 5 and not (x==0 and y==0)):
                    tablero[x][y] = 0
                    contador -=1
                    nx, ny = buscar_xy(tablero, contador)
                    candidato = tablero_aux[nx][ny] +1
                    tablero_aux[nx][ny] = 0
                    x =nx; y=ny
                    #mostrar_tablero(tablero)
                    solucion = True
            else:
                tablero_aux[x][y] = candidato; x = nx; y = ny; contador = contador + 1
                candidato=1
        else:
            candidato = candidato+1
            while(candidato == 5 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador -=1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] +1
                tablero_aux[nx][ny] = 0
                x =nx; y=ny
                #mostrar_tablero(tablero)
    return solucion
#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")
#modulo colocar_obstaculo
def colocar_obstaculo(tablero):
    pass
'''    tablero [MAX-2][MAX-2] = -1
    tablero [MAX-1][MAX-2] = -1
    tablero [MAX-2][MAX-1] = -1'''

#programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] #crea tablero
#mostrar_tablero(tablero)
colocar_obstaculo(tablero)
mostrar_tablero(tablero)

if(solucion(tablero) == True):
    print("Hay solucion")
    mostrar_tablero(tablero)
else:
    print('no hay solucion')
    