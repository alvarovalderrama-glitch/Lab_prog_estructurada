
#modulo valida
""" Verifica si una posible posición es válida (dentro de los límites
    del tablero y sin obstáculos) """
def valida(tablero,candidato,x,y):
    nx = x+pos_x [candidato - 1]
    ny = y+pos_y [candidato - 1]

    #Verifica límites del tablero
    if (nx < 0 or nx >= tamaño_tablero):
        return False
    if (ny < 0 or ny >= tamaño_tablero):
        return False
    
    #Verifica si la celda está libre
    if (tablero[nx][ny]== 0):
        return True
    else:
        return False

#modulo siguiente_posicion 
""" Devuelve las coordenadas (nx, ny) de la siguiente
    posición según el movimiento candidato """
def siguiente_posicion(tablero,candidato,x,y):
    nx = x+pos_x [candidato - 1]
    ny = y+pos_y [candidato - 1]
    return nx,ny

#modulo final
""" Determina si se ha llegado al final del laberinto """
def final(tablero,nx,ny):
    if (nx == tamaño_tablero - 1 and ny == tamaño_tablero - 1):
        return True
    return False

#modulo buscar_xy
""" Busca las coordenadas (x, y) donde se encuentra
    un valor específico dentro del tablero """
def buscar_xy(tablero, contador):
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if(tablero[i][j]== contador):
                return i,j
            
#modulo solucion
""" Algoritmo principal, busca una
    ruta válida desde (0,0) hasta (n-1,n-1)"""
def solucion(tablero):
   
    candidato = 1       # Movimiento actual (1: derecha, 2: abajo, 3: izquierda, 4: arriba)
    solucion = False    # Bandera que indica si se encontró una solución
    x = 0               # Posición inicial
    y = 0               # Contador de pasos
    contador = 1
    tablero_aux = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]
    tablero[x][y] = contador # Marca el punto inicial

    while(candidato <= 4 and not solucion):  #Detenemos si ya hay solución
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1

            if(final(tablero, nx, ny)):
                solucion = True     #Se encontró una solución
            else:
                 # Avanza al siguiente paso
                tablero_aux[x][y] = candidato
                x = nx
                y = ny
                contador += 1
                candidato = 1

        else:
            candidato += 1
            #Retroceso
            while(candidato == 5 and not (x == 0 and y == 0)):
                tablero[x][y] = 0
                contador -= 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] + 1     # Retrocede al paso anterior
                tablero_aux[nx][ny] = 0                 # Prueba siguiente dirección
                x = nx
                y = ny

    return solucion

#Modulo mostrar tablero
#Imprime el tablero en consola

def mostrar_tablero(tablero):
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#modulo colocar_obstaculo
#Se coloca manualmente obstáculos (-1) en el tablero
def colocar_obstaculo(tablero):

    tablero[0][2] = -1
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[2][2] = -1
    tablero[2][3] = -1

#programa principal

tamaño_tablero = 4      # Dimensión del tablero

pos_x = [0,1,0,-1]      #Desplazamientos posibles en X (derecha, abajo, izquierda, arriba)
pos_y = [1,0,-1,0]      #Desplazamientos posibles en Y (derecha, abajo, izquierda, arriba)


tablero = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)] #crea tablero

colocar_obstaculo(tablero)
mostrar_tablero(tablero)

#Busca solución
if(solucion(tablero) == True):
    print("Hay solucion")
    mostrar_tablero(tablero)
else:
    print('no hay solucion')