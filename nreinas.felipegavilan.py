# N-Reinas
#Variable que permite modificar eltamaño del tablero
MAX = int(input("Ingrese el tamaño y cantidad de reinas: "))

#Funcion que valida la colocacion de la reina
def valida(tablero, x, y):

    # Revisa toda la fila para ver si hay otra reina
    for col in range(MAX):
        if tablero[x][col] == 1:
            return False

    # Revisa toda la columna para ver si hay otra reina
    for fila in range(MAX):
        if tablero[fila][y] == 1:
            return False

    # Revisa diagonal principal para ver si hay otra reina
    for i in range(MAX):
        for j in range(MAX):
            if abs(i - x) == abs(j - y) and tablero[i][j] == 1:
                return False

    # Revisa diagonal secundaria para ver si hay otra reina
    for i in range(MAX):
        for j in range(MAX):
            if i + j == x + y and tablero[i][j] == 1:
                return False

    return True

#La funcion nos muestra el tablero con las posiciones de las reinas ("Q")
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print("Q" if tablero[i][j] == 1 else ".", end=" ")
        print("")
    print("")


# Busca todas las soluciones posibles y las enlista enumerandolas
def todas_soluciones(tablero, fila, soluciones):

    #Cuando se completan todas las filas tira solucion
    if fila == MAX:
        soluciones.append([fila[:] for fila in tablero])
        return

    #Intenta poner una reina en cada columna
    for col in range(MAX):

        if valida(tablero, fila, col):
            tablero[fila][col] = 1

            # Llama recursivamente a la funcion
            todas_soluciones(tablero, fila + 1, soluciones)

            tablero[fila][col] = 0


#Programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
soluciones = [] #Guardado de soluciones

print("\nBuscando todas las soluciones posibles\n")
todas_soluciones(tablero, 0, soluciones)

if soluciones:
    print(f"Se encontraron {len(soluciones)} soluciones\n")
    for i, sol in enumerate(soluciones, 1):
        print(f" Solucion {i} ") 
        mostrar_tablero(sol)
else:
    print("No existen solucione")
