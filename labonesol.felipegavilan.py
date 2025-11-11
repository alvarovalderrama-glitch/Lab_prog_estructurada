#Laberinto con obstaculos (o no) de una sola solucion

# Esta variable nos modifica el tamaño del tablero 
MAX = int(input('Ingrese el tamaño de su tablero: '))  # Esta variable nos modifica el tamaño del tablero ok

#Funcion que valida los movimientos de la pieza
def valida(tablero, candidato, x, y): 
    posx = [0, 1, 0, -1] #Movimiento de la pieza en x
    posy = [1, 0, -1, 0] #Movimiento de la pieza en y
    nx = x + posx[candidato - 1] #Nueva posicion de la pieza en x
    ny = y + posy[candidato - 1] #Nueva posicion de la pieza en y
    if (nx < 0 or nx >= MAX): 
        return False
    if (ny < 0 or ny >= MAX):
        return False
    if (tablero[nx][ny] == 0):
        return True
    else:
        return False

#Tras hacer el movimiento de la pieza la funcion elije el siguiente movimiento
def siguiente_posicion(candidato, x, y):
    posx = [0, 1, 0, -1] #Movimiento de la pieza en x
    posy = [1, 0, -1, 0] #Movimiento de la pieza en y
    nx = x + posx[candidato - 1] #Nueva posicion de la pieza en x
    ny = y + posy[candidato - 1] #Nueva posicion de la pieza en y
    return nx, ny

#La funcion comprueba si se llego a la posición final del tablero
def final(nx, ny):
    return nx == MAX - 1 and ny == MAX - 1

#La funcion muestra el tablero como este en el momento
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ")
        print("")
    print("")

#La funcion permite al usuario colocar obstaculos en las posiciones de su preferencia
def colocar_obstaculo(tablero):
    print('Coloque la ubicacion de sus obstaculos')
    print(f'En la matriz de tamaño {MAX}x{MAX}')
    print('De orden fila y columna respectivamente')
    print('Si desea terminar de colocar obstaculos o ninguno coloque -1 -1')
    while True:
        fila, col = map(int, input("Fila y columna: ").split())
        if fila == -1 and col == -1:
            break
        if 0 <= fila < MAX and 0 <= col < MAX:
            tablero[fila][col] = -1
        else:
            print("Coordenadas fuera del laberinto, reintentar")

#La funcion perite corroborar si el movimiento realizado llego la solucion (final)
def buscar_solucion(tablero, x, y, contador):
    if final(x, y):
        return True

    # Se prueban los 4 movimientos para ver si llega al final
    for candidato in range(1, 5):
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1
            if buscar_solucion(tablero, nx, ny, contador + 1):
                return True
            tablero[nx][ny] = 0  # retrocede en caso de que no lo logre
    return False

#Programa final
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
colocar_obstaculo(tablero)
print("Tablero con obstaculos:")
mostrar_tablero(tablero)

tablero[0][0] = 1  #Inicio del laberinto
if buscar_solucion(tablero, 0, 0, 1):
    print("Hay solucion:")
    mostrar_tablero(tablero)
else:
    print("No hay solucion.")
