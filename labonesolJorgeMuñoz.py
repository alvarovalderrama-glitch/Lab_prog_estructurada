### Laberinto una solucion ###
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

# buscar la primera solucion
def solucion_unica(candidato, tablero, contador, x, y, MAX):
    if final(x, y, MAX):
        return True
    
    while candidato <= 4:
        if valida(tablero, candidato, x, y, MAX):
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            if solucion_unica(1, tablero, contador, xsiguiente, ysiguiente, MAX):  # va a proseguir con la siguiente posición hasta llegar al final
                return True  # si encuentra el final, devuelve True
            
            # si no encuentra el final, se devuelve
            tablero[xsiguiente][ysiguiente] = 0  # borra el ultimo movimiento
            contador -= 1
        candidato += 1

    return False


# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    MAX = elegir_dimensiones()
    tablero = crear_tablero(MAX)
    colocar_obstaculos(tablero, MAX)
    print("Tablero creado:\n")
    mostrar_tablero(tablero, MAX)
    tablero[x][y] = 1

    if solucion_unica(candidato, tablero, contador, x, y, MAX):
        print("Solución encontrada:\n")
        mostrar_tablero(tablero, MAX)
    else:
        print("No hay solución.")

main()