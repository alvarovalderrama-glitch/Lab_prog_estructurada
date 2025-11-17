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
#modulo mostrar tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")
def encontrar_una_solucion(tablero):
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1
    
    # tablero_aux guarda QUÉ candidato (movimiento) usamos para llegar a (x,y)
    # Esto es vital para saber por dónde seguir al retroceder.
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    
    # El bucle se detiene si probamos todos los candidatos (1-4) O SI ENCONTRAMOS SOLUCION
    while(candidato <= 4 and not solucion):
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            
            if(final(tablero,nx,ny)):
                # ¡Solución encontrada!
                solucion = True # Ponemos la bandera en True para detener el while
            else:
                # Avanzamos: guardamos el candidato usado y nos movemos
                tablero_aux[x][y] = candidato
                x = nx; y = ny; contador = contador + 1
                candidato = 1 # Reiniciamos candidatos para la nueva casilla
        else:
            # No es válido (pared o fuera), probamos el siguiente candidato
            candidato = candidato+1
            
            # Si ya probamos los 4 candidatos (candidato == 5) y no estamos en el inicio...
            while(candidato == 5 and not (x==0 and y==0)):
                # Retroceder (Backtrack)
                tablero[x][y] = 0 # Borramos el paso actual
                contador -=1
                nx, ny = buscar_xy(tablero, contador) # Buscamos la casilla anterior
                
                # Vemos qué candidato usamos para llegar aquí (guardado en tablero_aux)
                # e intentamos con el siguiente.
                candidato = tablero_aux[nx][ny] + 1 
                
                tablero_aux[nx][ny] = 0 # Borramos la pista del tablero_aux
                x =nx; y=ny
    
    return solucion # Devuelve True si la encontró, False si no
tablero_uno = [[0 for _ in range(MAX)] for _ in range(MAX)]
if encontrar_una_solucion(tablero_uno):
    print('Solucion:')
    mostrar_tablero(tablero_uno)
else:
    print("No se encontro solucion.")