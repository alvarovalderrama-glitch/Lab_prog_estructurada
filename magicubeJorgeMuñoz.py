### Cuadrado Magico ###

# elegir las dimensiones del cuadrado magico (idealmente 3)
while True:
    try:
        MAX = int(input("Introduzca la dimension para el cuadrado magico: (NOTA: DIMENSIONES MAYORES A 3 DEMORAN MUCHO TIEMPO)\n>"))
    except ValueError:
        print("Error. Introduzca un número entero mayor que 0\n")
        continue
    if MAX <= 0:
        print("Error. Introduzca un número entero mayor que 0\n")
    else:
        break

# asignar variables
candidato = 1
x = y = 0


# crea una matriz cuadrada rellena con ceros para usarla de tablero
def crear_tablero(MAX):
    tablero = [[0 for i in range(MAX)] for j in range(MAX)]
    return tablero


# imprime el tablero fila por fila
def imprimir_tablero(tablero):
    for fila in tablero:
        print(*fila)


# verifica si las sumatorias de todas las lineas son iguales
def es_cuadr_magico(tablero, MAX):
    suma_fila = sum(tablero[0])  # elijo una linea para comparar su suma con el resto (primera fila)

    # verificar filas
    for i in range(MAX):
        if sum(tablero[i]) != suma_fila:
            return False
    

    # verificar columnas
    for j in range(MAX):
        if sum(tablero[i][j] for i in range(MAX)) != suma_fila:
                return False
        

    # verificar diagonales
    if sum(tablero[i][i] for i in range(MAX)) != suma_fila: # diagonal principal
        return False
        
    if sum(tablero[i][MAX - 1 - i] for i in range(MAX)) != suma_fila:  # diagonal secundaria
        return False
    
    return True


# verifica si el tablero está lleno de números distintos de 0
def tablero_completo(tablero, MAX):
    for j in range(MAX):
        for i in range(MAX):
            if tablero[i][j] == 0:
                return False
    return True


# verifica si la casilla deseada está disponible para recorrer
def valida(tablero, x, y, candidato):
    if tablero[x][y] != 0:  # si tiene un número distinto de 0 significa que la casilla está ocupada
        return False
    
    for j in range(MAX):
        for i in range(MAX):
            if tablero[i][j] == candidato:  # recorre toda la matriz para verificar que el candidato no se repita
                return False  # si el número ya está en el tablero entonces no es válido
            
    return True  # si la casilla deseada está vacía y el numero candidato no está en el tablero, es válido


# busca una casilla vacia en el tablero
def siguiente_xy(tablero, MAX):
    for j in range(MAX):
        for i in range(MAX):
            if tablero[i][j] == 0:  # si encuentra una casilla vacía, entonces esa será la siguiente casilla
                return i, j  # devuelve la nueva X y la nueva Y (xsiguiente, ysiguiente)
    return None, None


# backtracking recursivo para encontrar la solucion
def encontrar_solucion(tablero, MAX, candidato, x, y):
    if tablero_completo(tablero, MAX):        # cuando el tablero esté lleno, el modulo encontrar_solución()
        return es_cuadr_magico(tablero, MAX)  # devolverá True o False dependiendo de si es cuadrado magico
    
    for candidato in range(1, MAX**2 + 1):  # recorrerá candidatos entre 1 y el n maximo (en 3x3 sería 9)
        if valida(tablero, x, y, candidato):  # si la casilla es válida
            tablero[x][y] = candidato  # pone el candidato en la casilla

            xsiguiente, ysiguiente = siguiente_xy(tablero, MAX)  # luego busca la siguiente casilla donde haya un 0
            if encontrar_solucion(tablero, MAX, candidato, xsiguiente, ysiguiente):  # toma el xsiguiente e ysiguiente para ejecutar la funcion
                return True
        
            tablero[x][y] = 0  # si no es cuadrado magico, retrocede el último movimiento
    
    return False  # si después de intentar todas las posibilidades no encuentra solucion, devuelve False



# programa principal
def main(MAX, candidato, x, y):
    """
    candidato = 1
    x = 0
    y = 0      # dejo comentada esta asignacion de variables para mejor legibilidad
    """
    tablero = crear_tablero(MAX)
    print("Buscando solución...\n")
    if encontrar_solucion(tablero, MAX, candidato, x, y):  # si encuentra una solución
        print("Solución encontrada:")
        imprimir_tablero(tablero)
    else:
        print("No se ha encontrado solución.")

# ejecuta main
main(MAX, candidato, x, y)



# desde aqui hacia abajo hay trozos de código no utilizados
"""
def encontrar_solucion(tablero, MAX):
    candidato = 1
    x = y = 0
    while candidato <= (MAX**2):
        if valida(tablero, x, y, candidato):
            tablero[x][y] = candidato
        
        if tablero_completo(tablero, MAX):
            if es_cuadr_magico(tablero, MAX):
                return True
            else:
                # backtracking
                tablero[x][y] = 0
                candidato += 1
                while candidato < MAX and not (x == 0 and y == 0):
                    xretroceder, yretroceder = posicion_anterior(tablero, MAX, candidato)
                    candidato += 1
                    x, y = xretroceder, yretroceder

        else:
            x, y = siguiente_xy(tablero, MAX)
            candidato = 1

            
def encontrar solucion()
    if tablero_completo()
        return es_cuadr_magico
    
    while candidato <= MAX**2
        if encontrar solucion()
            return True
        else:
            tablero[x][y] = 0
            candidato += 1


encontrar sol
    if valida:
        if es_cuadr_magico

"""