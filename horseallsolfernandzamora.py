#horseallsol

# prepara el tablero
def crear_tablero(MAX):
    # Inicializa un tablero MAX x MAX con ceros (0 = casilla no visitada).
    return [[0 for _ in range(MAX)] for _ in range(MAX)]


def mostrar_tablero(tablero, MAX):
    # Imprime el tablero actual, mostrando el orden de los movimientos.
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:3}", end = " ")
        print("")


#elige parametros
def elegir_dimensiones():
    # Pide y valida la dimensión MAX del tablero (debe ser > 2).
    while True:
        try:
            MAX = int(input("Introduzca la dimension para la matriz cuadrada (mayor que 2):\n>"))
        except ValueError:
            print("Error. Introduzca un número entero mayor que 2\n")
            continue
        if MAX <= 2:
            print("Error. Introduzca un número entero mayor que 2\n")
        else:
            return MAX


# funcion posicion
def valida(tablero, candidato, x, y, MAX):
    # Define los 8 movimientos del caballo.
    xdireccion = [1, 2, 2, 1, -1, -2, -2, -1]
    ydireccion = [2, 1, -1, -2, -2, -1, 1, 2]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    
    # Comprueba si el movimiento es válido (dentro de límites y casilla no visitada).
    if xsiguiente < 0 or xsiguiente >= MAX:
        return False
    if ysiguiente < 0 or ysiguiente >= MAX:
        return False
    if tablero[xsiguiente][ysiguiente] == 0:
        return True
    else:
        return False


def siguiente_posicion(candidato, x, y):
    # Devuelve las coordenadas de la siguiente posición.
    xdireccion = [1, 2, 2, 1, -1, -2, -2, -1]
    ydireccion = [2, 1, -1, -2, -2, -1, 1, 2]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    return xsiguiente, ysiguiente


def final(tablero, MAX):
    # Condición de fin: True si todas las casillas han sido visitadas.
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j] == 0):
                return False
    return True


def buscar_xy(tablero, contador, MAX):
    # Busca y devuelve las coordenadas (x, y) de una posición dada por su número de movimiento (contador).
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j


# ---------------- FUNCIONES SOLUCION ---------------- #
# Función recursiva de Backtracking para buscar TODAS las soluciones.
def solucion_todas(candidato, tablero, contador, x, y, xsiguiente, ysiguiente, MAX, soluciones, camino):
    if final(tablero, MAX):
        # Si encuentra una solución completa, la guarda en la lista de soluciones.
        soluciones.append(camino.copy()) 
        return # Continúa la búsqueda para encontrar más soluciones.
    
    while candidato <= 8:
        if valida(tablero, candidato, x, y, MAX):
            # Realizar movimiento y avanzar.
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            camino.append((xsiguiente, ysiguiente)) # Guarda el paso en el camino actual.

            # Llamada recursiva (continúa la búsqueda).
            solucion_todas(1, tablero, contador, xsiguiente, ysiguiente, 0, 0, MAX, soluciones, camino)

            # Retroceder (Backtracking)
            camino.pop() # Elimina el último paso del camino.
            tablero[xsiguiente][ysiguiente] = 0 # Desmarca la casilla.
            contador -= 1
            
        candidato += 1 # Prueba el siguiente movimiento.


# Función de control: inicia la búsqueda de todas las soluciones e imprime el resumen.
def encontrar_solucion(tablero, contador, candidato, MAX, x, y, xsiguiente, ysiguiente, soluciones, camino):
    solucion_todas(candidato, tablero, contador, x, y, xsiguiente, ysiguiente, MAX, soluciones, camino)
    if soluciones:
        print(f"Se han encontrado {len(soluciones)} soluciones:")
        for i, sol in enumerate(soluciones, 1):
            print(f"\nsolucion {i}:")
            # Usa una función auxiliar para mostrar cada solución en formato de tablero.
            mostrar_soluciones_tablero(tablero, sol, MAX)
    else:
        print("No hay solución.")


# Muestra una solución específica (una lista de coordenadas) en formato de tablero.
def mostrar_soluciones_tablero(tablero_original, camino, MAX):
    # Crea una copia limpia y rellena los pasos de la solución encontrada.
    tablero_aux = [fila.copy() for fila in tablero_original]

    for casilla, (x, y) in enumerate(camino, start=1):
        tablero_aux[x][y] = casilla

    mostrar_tablero(tablero_aux, MAX)


# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    # Inicialización. La variable 'soluciones' guardará todas las rutas.
    soluciones = []
    candidato = 1
    contador = 1
    x = y = 0
    MAX = elegir_dimensiones()
    tablero = crear_tablero(MAX)
    
    mostrar_tablero(tablero, MAX)
    tablero[x][y] = 1 # Marca el inicio (movimiento 1).
    
    # El camino inicial incluye la primera posición (0, 0).
    encontrar_solucion(tablero, contador, candidato, MAX, x, y, 0, 0, soluciones, [(0, 0)])

main()