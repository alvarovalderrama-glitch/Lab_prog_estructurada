import os
MAX = 5

#modulo valida
def valida(tablero, candidato, x, y):
    #verifica que la posicion alcanzada desde x,y con el candidato está dentro del tablero y vacía
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    if(nx<0 or nx>=MAX):
        return False
    if(ny<0 or ny>=MAX):
        return False
    if(tablero[nx][ny]!=0):
        return False
    return True

#modulo siguiente_posicion
def siguiente_posicion(tablero, candidato, x,y):
    #devuelve la posicion nx,ny alcanzada desde x,y con el candidato 
    posx = [-2,-1,1,2,2,1,-1,-2]
    posy = [1,2,2,1,-1,-2,-2,-1]
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    return nx,ny

#modulo final
def final(tablero):
    #verifica si el tablero está completo
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==0):
                return False
    return True

#modulo buscar_xy
def buscar_xy(tablero, contador):
    #busca la posición del valor 'contador' dentro del tablero
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j]==contador):
                return i,j

#modulo mostrar tablero
def mostrar_tablero(tablero):
    #muestra el tablero por consola
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")

#modulo solucion
def solucion(tablero):
    candidato = 1 ; solucion = False ; x = 0; y = 0; contador = 1
    #se agregan las soluciones, los pasos, las soluciones minimas, las soluciones minimas guardadas y todas las soluciones encontradas
    soluciones = 0
    min_pasos = None
    soluciones_minimas= 0
    soluciones_guardadas =[]
    todas_soluciones = []

    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador
    while(candidato <= 8 and not solucion):
        if(valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(tablero, candidato, x, y)
            tablero[nx][ny] = contador + 1
            mostrar_tablero(tablero)
            if(final(tablero)):
                mostrar_tablero(tablero)
                soluciones +=1 #se le suma 1 cada que haya solucion
                pasos = contador + 1 #contamos los pasos
                tablero[nx][ny] = 0
                candidato = candidato + 1

                tablero_copia = [fila[:] for fila in tablero] #creamos una copia de todas las soluciones

                if min_pasos is None or pasos < min_pasos: #si los pasos minimos es igual a none o es mayor a los pasos contados, se iguala a los pasos contados y se reinicia las soluciones
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
            while(candidato == 9 and not (x==0 and y==0)):
                tablero[x][y] = 0
                contador = contador - 1
                nx, ny = buscar_xy(tablero, contador)
                candidato = tablero_aux[nx][ny] +1
                tablero_aux[nx][ny] = 0
                x =nx; y=ny
                mostrar_tablero(tablero)
  
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
    print("──────────────────────────────")
    print("Total de soluciones:", soluciones)
    print("Menor cantidad de pasos:", min_pasos)
    print("Soluciones con menor cantidad de pasos:", soluciones_minimas)
    print("──────────────────────────────")

    return solucion

#programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] #crea tablero
mostrar_tablero(tablero)
if(solucion(tablero) == True):
    print("Hay solucion")
    mostrar_tablero(tablero)
else:
    print('no hay solucion')