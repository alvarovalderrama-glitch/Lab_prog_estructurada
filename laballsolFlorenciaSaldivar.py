import random #importar la biblioteca random para generar números aleatorios

def crear_tablero(tamaño):      #función para crear un tablero de tamaño dado
    return [['.' for _ in range(tamaño)] for _ in range(tamaño)]        #crear una matriz de tamaño x tamaño llena de '.'

def agregar_obstaculos(tablero, porcentaje=0.2):        #función para agregar obstáculos al tablero
    tamano = len(tablero)       #obtener el tamaño del tablero
    total_casillas = tamano * tamano        #calcular el total de casillas en el tablero    
    cantidad_obstaculos = int(total_casillas * porcentaje)      #calcular la cantidad de obstáculos a agregar

    puestos = 0     #contador de obstáculos puestos
    while puestos < cantidad_obstaculos:     #mientras no se hayan puesto todos los obstáculos
        x = random.randint(0, tamano - 1)    #generar una posición x aleatoria
        y = random.randint(0, tamano - 1)   #generar una posición y aleatoria#

        if (x, y) in [(0, 0), (tamano - 1, tamano - 1)]:        #si la posición es la de inicio o fin, no poner obstáculo
            continue

        if tablero[x][y] == '.':        #si la posición está libre, poner un obstáculo
            tablero[x][y] = '#'      #poner el obstáculo
            puestos += 1    #incrementar el contador de obstáculos puestos


def imprimir_tablero(tablero):      #función para imprimir el tablero
    for fila in tablero:        #para cada fila en el tablero
        print(" ".join(f"{c:2}" for c in fila))     #imprimir la fila con formato
    print()

def copiar_tablero(tablero):        #función para copiar el tablero
    return [fila[:]for fila in tablero]  #devolver una copia del tablero#

def buscar_camino(tablero, x, y, paso, soluciones):   #función para buscar un camino en el tablero
    tamano = len(tablero)       #obtener el tamaño del tablero

    if x < 0 or x >= tamano or y < 0 or y >= tamano:        #si la posición está fuera del tablero, devuelve falso
        return False    

    if tablero[x][y] == '#':    #si la posición es un obstáculo, devuelve falso
        return False

    
    if isinstance(tablero[x][y], int):  #si la posición ya ha sido visitada, devuelve falso
        return False
    anterior=tablero[x][y]  #guardar el valor anterior de la posición
    tablero[x][y]= paso
    
    if x == tamano - 1 and y == tamano - 1:
        soluciones.append(copiar_tablero(tablero))  #si se ha llegado al final, guardar la solución
        tablero[x][y]= anterior     #restaurar el valor anterior
        return True

    
    movimientos = [
        (1, 0),   # abajo
        (0, 1),   # derecha
        (-1, 0),  # arriba
        (0, -1)   # izquierda
    ]

    for dx, dy in movimientos:     #para cada movimiento posible
        if buscar_camino(tablero, x+dx, y+dy, paso+1, soluciones):      #si se encuentra un camino, devuelve verdadero
            pass
    tablero[x][y]=anterior   #restaurar el valor anterior
    return False


def resolver_laberinto(tamano):     #función principal para resolver el laberinto
    tablero = crear_tablero(tamano)
    agregar_obstaculos(tablero, porcentaje=0.2)   #agregar obstáculos al tablero
    print("Laberinto generado ('.' = libre, '#' = obstáculo):") 
    imprimir_tablero(tablero)
    if tablero[0][0] == '#' or tablero[tamano - 1][tamano - 1] == '#':   #si el inicio o el final están bloqueados
        print("inicio o final bloqueados")
        return
    soluciones=[]   #lista para guardar las soluciones
    buscar_camino(tablero, 0, 0, 1, soluciones) #buscar caminos desde la posición (0,0)

    if len(soluciones) == 0:    #si no se encontraron soluciones
        print("No se encontró ningún camino")
        return
    print(f"Se encontraron {len(soluciones)} camino(s):\n") #imprimir todas las soluciones encontradas
    for i, sol in enumerate(soluciones, start=1):   #para cada solución encontrada
        print(f"Camino {i}:")
        imprimir_tablero(sol)

if __name__ == "__main__":
    n = int(input("Ingrese el tamaño del laberinto: ")) #pedir al usuario el tamaño del laberinto
    resolver_laberinto(n)
