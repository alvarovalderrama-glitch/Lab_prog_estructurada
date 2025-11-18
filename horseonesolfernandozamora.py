#horseonesol

# ---------------- PREPARAR TABLERO ---------------- #
def crear_tablero(MAX):
    # Inicializa un tablero MAX x MAX con ceros (0 = casilla no visitada).
    return [[0 for _ in range(MAX)] for _ in range(MAX)]


def mostrar_tablero(tablero, MAX):
    # Imprime el tablero, mostrando el orden de los movimientos.
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:3}", end = " ")
        print("")


# ---------------- ELEGIR PARÁMETROS ---------------- #
def elegir_dimensiones():
    # Pide y valida la dimensión MAX del tablero (debe ser un entero mayor que 2).
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


# ---------------- FUNCIONES POSICION ---------------- #
def valida(tablero, candidato, x, y, MAX):
    # Direcciones de movimiento del caballo (8 posibles).
    xdireccion = [1, 2, 2, 1, -1, -2, -2, -1]
    ydireccion = [2, 1, -1, -2, -2, -1, 1, 2]
    # Calcula la posición siguiente.
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    
    # Comprueba: 1) Dentro de límites, 2) Casilla no visitada (valor 0).
    if xsiguiente < 0 or xsiguiente >= MAX:
        return False
    if ysiguiente < 0 or ysiguiente >= MAX:
        return False
    if tablero[xsiguiente][ysiguiente] == 0:
        return True
    else:
        return False


def siguiente_posicion(candidato, x, y):
    # Devuelve las coordenadas de la siguiente posición basada en el candidato.
    xdireccion = [1, 2, 2, 1, -1, -2, -2, -1]
    ydireccion = [2, 1, -1, -2, -2, -1, 1, 2]
    xsiguiente = x + xdireccion[candidato - 1]
    ysiguiente = y + ydireccion[candidato - 1]
    return xsiguiente, ysiguiente


def final(tablero, MAX):
    # Comprueba si todas las casillas han sido visitadas (ningún 0 restante).
    for i in range(MAX):
        for j in range(MAX):
            if(tablero[i][j] == 0):
                return False
    return True # Es el estado final (solución encontrada).


# ---------------- FUNCIONES SOLUCION ---------------- #
# Función recursiva de Backtracking para buscar la primera solución.
def solucion_unica(candidato, tablero, contador, x, y, MAX):
    if final(tablero, MAX):
        return True # Condición base: se encontró la solución.
    
    while candidato <= 8:
        if valida(tablero, candidato, x, y, MAX):
            xsiguiente, ysiguiente = siguiente_posicion(candidato, x, y)
            
            # Realiza el movimiento: actualiza contador y tablero.
            contador += 1
            tablero[xsiguiente][ysiguiente] = contador
            
            # Llamada recursiva: si encuentra la solución en esta rama, propaga True.
            if solucion_unica(1, tablero, contador, xsiguiente, ysiguiente, MAX):
                return True
            
            # Backtracking: deshace el movimiento fallido.
            tablero[xsiguiente][ysiguiente] = 0  # Borra el movimiento.
            contador -= 1
            
        candidato += 1  # Prueba el siguiente movimiento.

    return False # No hay solución posible desde esta posición.


# Función de control que inicia la búsqueda e imprime el resultado.
def encontrar_solucion(tablero, contador, candidato, MAX, x, y, xsiguiente, ysiguiente, soluciones, camino):
    if solucion_unica(candidato, tablero, contador, x, y, MAX):
        print("Solución encontrada:\n")
        mostrar_tablero(tablero, MAX)
    else:
        print("No hay solución.")


# ---------------- PROGRAMA PRINCIPAL ---------------- #
def main():
    # Inicializa variables y obtiene la dimensión.
    candidato = 1
    contador = 1
    x = y = 0
    MAX = elegir_dimensiones()
    tablero = crear_tablero(MAX)
    
    mostrar_tablero(tablero, MAX)
    tablero[x][y] = 1 # Marca el inicio (movimiento 1).
    
    # Llama a la función que inicia el proceso de búsqueda.
    encontrar_solucion(tablero, contador, candidato, MAX, x, y, 0, 0, [], [(0, 0)])

main()