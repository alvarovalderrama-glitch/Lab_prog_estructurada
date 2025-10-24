import os

MAX = 3

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
    #se agrega las soluciones, los pasos, las soluciones minimas, las soluciones minimas guardadas y todas las soluciones encontradas
    soluciones = 0
    min_pasos = None
    soluciones_minimas= 0
    soluciones_guardadas =[]
    todas_soluciones = []

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
                soluciones +=1 #se le suma 1 cada que haya solucion
                pasos = contador + 1 #contamos los pasos
                input("Enter para continuar")
                tablero[nx][ny] = 0
                candidato = candidato + 1

                tablero_copia = [fila[:] for fila in tablero] #creamos una copia de todas las soluciones

                if min_pasos is None or pasos < min_pasos: #si los pasos minimos es iguala none o es mayor a los pasos contados, se iguala a los pasos contados y se reinicia las soluciones
                    min_pasos = pasos
                    soluciones_minimas = 1
                    soluciones_guardadas = [tablero_copia]
                elif pasos == min_pasos: #si los pasos minimos son igual a los pasos, se suma las soluciones minimas y se agrega al tablero copia
                    soluciones_minimas += 1
                    soluciones_guardadas.append(tablero_copia)

                todas_soluciones.append(tablero_copia) #guarda todas las soluciones en el tablero copia


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
    with open("soluciones_minimas.txt", "w") as archivo: #se crea el archivo soluciones minimas
        archivo.write("Menor cantidad de pasos: " + str(min_pasos) + "\n")
        archivo.write("Cantidad de soluciones mínimas: " + str(soluciones_minimas) + "\n")
        
        for sol in soluciones_guardadas: # escribe todas las soluciones minimas y los caminos
            for fila in sol:
                for num in fila:
                    archivo.write(str(num) + " ")  
                archivo.write("\n")  
            archivo.write("\n") 

    with open("soluciones totales", "w") as archivo_total: #crea el archivo de todas las soluciones
        archivo_total.write("soluciones totales: " + str(soluciones) +"\n")

        #escribe todas las soluciones y caminos
        
        for sol in todas_soluciones:
            for fila in sol:
                for num in fila:
                    archivo_total.write(str(num) + " ")  
                archivo_total.write("\n")  
            archivo_total.write("\n") 
#imprimir pasos minimos, soluciones y cantidad de soluciones con minimos pasos
    print("Total de soluciones:", soluciones)
    print("Menor cantidad de pasos:", min_pasos)
    print("Soluciones con menor cantidad de pasos:", soluciones_minimas)
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
else:
    print("no hay solucion") 