### n reinas ###

"""
tener un tablero nxn
tener una reina en cada fila y cada columna
que no coincidan en sus lineas de vision

fila = 0
def buscar_solucion(candidato, fila, tablero):
    if fila = MAX:
        return True

    for columna in range(MAX):
        if valido():
            tablero[fila][columna] = candidato

            if buscar_solucion(candidato+1, fila+1, tablero):
                return True
            
            tablero[fila][columna] = 0
            
    return False

"""
#--------------------------------------------------------#
while True:
    try:
        n = int(input("Introduzca la dimension para el cuadrado magico:\n>"))
    except ValueError:
        print("Error. Introduzca un número entero mayor que 1\n")
        continue
    if n <= 0:
        print("Error. Introduzca un número entero mayor que 1\n")
    else:
        break

candidato = 1
tablero = [[0 for _ in range(n)] for _ in range(n)]



#-----------------------------------------------------------------------------------#

def crear_tablero(MAX):
    return [[0 for i in range(MAX)] for j in range(MAX)]

def valido(fila, columna):
    # verificar fila
    for col in range(n):
        if tablero[fila][col] != 0:
            return False
    
    # verificar columna
    for i in range(n):
        if tablero[i][columna] != 0:
            return False
        
    # diagonal \
    i = fila - 1
    j = columna - 1
    while 0 <= i < n and 0 <= j < n:
        if tablero[i][j] != 0:
            return False
        i -= 1
        j -= 1
    
    # diagonal /
    i = fila - 1
    j = columna + 1
    while 0 <= i < n and 0 <= j < n:
        if tablero[i][j] != 0:
            return False
        i -= 1
        j += 1

    return True

def mostrar_tablero(tablero):
    for fila in tablero:
        print(*fila)

def buscar_solucion(candidato, fila, tablero):
    # caso base (se llegó a la ultima fila)
    if fila == n:
        return True
    for columna in range(n):
        if valido(fila, columna):
            tablero[fila][columna] = candidato

            if buscar_solucion(candidato+1, fila+1, tablero):  # recorrer la siguiente fila (de arriba hacia abajo)
                return True  # solo devolverá True cuando encuentre la solución
            
            # devolverse
            tablero[fila][columna] = 0  # devuelve el ultimo movimiento y prueba con la siguiente columna (izquierda a derecha)
    return False

def main():
    fila = 0
    print("se ha creado el tablero:")
    mostrar_tablero(tablero)  # muestra el tablero lleno de ceros
    if buscar_solucion(candidato, fila, tablero):
        print("\nse ha encontrado una solución:\n")
        mostrar_tablero(tablero)
    else:
        print("no se encontró solución")

main()