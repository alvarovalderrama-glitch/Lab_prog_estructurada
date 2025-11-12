### Laberinto ###
import random

# Asignar variables
soluciones = []
candidato = 1
contador = 1
x = y = xsiguiente = ysiguiente = 0

# ---------------- PREPARAR TABLERO ---------------- #
def crear_tablero(MAX):
    return [[0 for _ in range(MAX)] for _ in range(MAX)]


def colocar_obstaculos(tablero, MAX):
    for _ in range(MAX):
        x, y = random.randint(0, MAX - 1), random.randint(0, MAX - 1)
        if (x, y) not in [(0, 0), (MAX - 1, MAX - 1)]:
            tablero[x][y] = "X"


def mostrar_tablero(tablero, MAX):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end = " ")
        print("")
    print("")


# ---------------- ELEGIR PARÁMETROS ---------------- #
def elegir_modo():
    while True:
        opcion_modo = input("""
-------------------- ELEGIR MODO --------------------
    2. Mostrar todas las soluciones
    3. Mostrar la solución mas corta
-----------------------------------------------------

Escoja una opción:
>""")
        if opcion_modo in ("2", "3"):
            return opcion_modo
        else:
            print("Opción inválida.\n")
        

# seleccionar el tamaño del tablero
def elegir_dimensiones():
    while True:
        try:
            MAX = int(input("Introduzca la dimension para la matriz cuadrada (mayor que 1):\n>"))
        except ValueError:
            print("Error. Introduzca un número entero mayor que 1\n")
            continue
        if MAX <= 1:
            print("Error. Introduzca un número entero mayor que 1\n")
        else:
            return MAX


# ---------------- FUNCIONES POSICION ---------------- #

# consulta si la direccion a la que se quiere ir está dentro del tablero y está vacía
def valida(tablero, candidato, x, y, MAX):
    xdireccion = [0,1,0,-1]
    ydireccion = [1,0,-1,0]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    if xsiguiente < 0 or xsiguiente == MAX:
        return False
    if ysiguiente < 0 or ysiguiente == MAX:
        return False
    if tablero[xsiguiente][ysiguiente] == 0:
        return True
    else:
        return False


# devuelve las x e y del siguiente movimiento
def siguiente_posicion(candidato, x, y):
    xdireccion = [0,1,0,-1]
    ydireccion = [1,0,-1,0]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    return xsiguiente, ysiguiente


def final(x, y, MAX):
    if x == MAX - 1 and y == MAX - 1:
        return True
    return False


# ---------------- FUNCIONES SOLUCION ---------------- #

# buscar todas las soluciones
def solucion_todas(candidato, tablero, contador, x, y, xsiguiente, ysiguiente, MAX, soluciones, camino):
    if final(x, y, MAX):
        soluciones.append(camino.copy())
        return
    
    while candidato <= 4:
        if valida(tablero, candidato, x, y, MAX):
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            camino.append((xsiguiente, ysiguiente))

            solucion_todas(1, tablero, contador, xsiguiente, ysiguiente, 0, 0, MAX, soluciones, camino)

            # retroceder
            camino.pop()
            tablero[xsiguiente][ysiguiente] = 0
            contador -= 1
        
        candidato += 1


# mostrar las soluciones como matrices
def mostrar_soluciones_tablero(tablero_original, camino, MAX):
    # crea una copia del tablero original
    tablero_aux = [fila.copy() for fila in tablero_original]

    for casilla, (x, y) in enumerate(camino, start=1):
        tablero_aux[x][y] = casilla

    mostrar_tablero(tablero_aux, MAX)


# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    MAX = elegir_dimensiones()
    tablero = crear_tablero(MAX)
    colocar_obstaculos(tablero, MAX)
    print("Tablero creado:\n")
    mostrar_tablero(tablero, MAX)
    opcion_modo = elegir_modo()
    tablero[x][y] = 1
    camino = [(0, 0)]


    print("Buscando soluciones...")
    solucion_todas(candidato, tablero, contador, x, y, xsiguiente, ysiguiente, MAX, soluciones, camino)
    if soluciones:
        print("Se han encontrado las siguientes soluciones:")
        if opcion_modo == "2":
            for i, sol in enumerate(soluciones, 1):
                print(f"\nsolucion {i}:")
                mostrar_soluciones_tablero(tablero, sol, MAX)
        else:
            sol_mas_corta = min(soluciones, key=len)
            print("\nSolucion mas corta:")
            mostrar_soluciones_tablero(tablero, sol_mas_corta, MAX)
    else:
        print("No hay solución.")

main()