# | CUADRADO MAGICO | MARTYNAROJAS |
# Para que sea un cuadrado magico nxn, la suma de los numeros de las filas, columnas y diagonales deben dar igual que la suma de todos los numeros dividido en n
# Uso el de 3x3 porque es mas simple
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

MAX = 3  # tablero 3x3

#--------------------------------------------------------
# Busco que el cubo siga la logica de que el valor que deben sumar las lineas debe ser la suma de los numeros del 1 al 9/ en 3
def suma(MAX): # creo una lista de numeros desde nxn, esto crea algo asi como [1,2,3,4,5,6,7,8,9]
    return list(range(1, MAX * MAX + 1))
   
def sumar_numeros(lista): #esta funcion suma todos los numeros de esa lista
    suma = 0
    for num in lista:
        suma += num
    return suma

def suma(MAX):
    valor = sum(range(1, MAX*MAX + 1)) 
    return valor // MAX 
#suma los numeros de 1 a 3x3, los divide por 3 y ese sera el valor que compararemos

#_________________________________________

def verificar_sumas(tablero):
    valor =suma(MAX) #el valor que debe obtenerse de la suma de cada fila

    #EN FILAS
    for i in range(MAX): 
        if sum(tablero[i]) != valor:
            return False
    #EN COLUMNAS
    for j in range(MAX):
        if sum(tablero[i][j] for i in range(MAX)) != valor:
            return False

    #EN DIAGONALES
    if sum(tablero[i][i] for i in range(MAX)) != valor:
        return False

    if sum(tablero[i][MAX - 1 - i] for i in range(MAX)) != valor:
        return False

    return True


def resolver(tablero, pos):
    
    if pos == MAX * MAX: #SI el tablero esta lleno
        if verificar_sumas(tablero): #llamara a verificar, si es asi, es una solucion
            print("\nSOLUCIÓN:")
            for fila in tablero:
                print(fila)
        return
    #--------------------- #esto sirve para definir coordenadas facilmente
    x = int(pos / MAX) # filas
    y = pos - x * MAX  # columnas

    #[BACKTRACKING]-------------
    if tablero[x][y] != 0: 
        resolver(tablero, pos + 1) 
        return
        #si esta ocupado ese lugar, sigue con otro

    #en uno vacio:
    for num in range(1, MAX*MAX + 1):

        if any(num in fila for fila in tablero):
            continue
    # evita las repeticiones de numeros, solo se pueden usar una vez
#___________________________
#IMPORTANTE DEL BACKTRACKING
        tablero[x][y] = num #pone numero en espacio
        resolver(tablero, pos + 1) #sigue resolviendo
        tablero[x][y] = 0  #si luego el uso de ese numero no funciona, puede borrarlo e intentar otro

#--------------------------------------------------------------------
#EJECUCION
tablero = [[0]*MAX for _ in range(MAX)] #crea tablero vacio
resolver(tablero, 0) #llamado a resolver desde el primer espacio
