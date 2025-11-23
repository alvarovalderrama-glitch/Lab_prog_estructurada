###============N-Reinas============###

# Asignación de variables.
# Se solicita al usuario el tamaño del tablero (NxN)
n = int(input("Ingrese el tamaño (NxN) que desea el tablero: \n> "))

# Se crea una matriz llena de ceros que representará el tablero
tablero = [[0 for _ in range(n)]for _ in range(n)]

# Lista donde se almacenarán todas las soluciones encontradas
soluciones = []

# Contador que indica el orden de colocación de las reinas
contador = 1

# Creación del tablero #
def crear_tablero():
    # Recorre filas del tablero
    for i in range(n):
        # Recorre columnas del tablero
        for j in range(n):
            # Imprime cada valor con formato de ancho fijo
            print(f"{tablero[i][j]:3}", end = " ")
        # Salto de línea al terminar cada fila
        print("")
    # Salto extra para separar visualmente tableros
    print("")

# Backtracking para buscar soluciones #
def back_recursivo(fila, tablero, contador):
    # Caso base: si se llegó a la última fila, se encontró una solución
    if fila == n:
       # Se guarda una copia del tablero actual en la lista de soluciones
       soluciones.append([fila[:] for fila in tablero])
       return

    # Se intenta colocar una reina en cada columna de la fila actual
    for colum in range(n):
        # Se verifica si la posición es válida
        if valido(fila, colum) == True:
            # Se coloca la reina (representada por el valor del contador)
            tablero[fila][colum] = contador

            # Llamada recursiva para la siguiente fila
            back_recursivo(fila + 1, tablero, contador + 1)

            # Se deshace el movimiento (backtracking)
            tablero[fila][colum] = 0 

# Validación de casillas #
def valido(fila, colum):
    # Verifica que no haya otra reina en la misma columna
    for i in range(fila):
        if tablero[i][colum] != 0:
            return False

    # Diagonal principal #    
    # Se revisa la diagonal superior izquierda
    i = fila - 1
    j = colum - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] != 0:
            return False 
        i -= 1
        j -=1   

    # Diagonal secundaria #
    # Se revisa la diagonal superior derecha
    i = fila - 1
    j = colum + 1
    while i >= 0 and j < n:
        if tablero[i][j] != 0:
            return False 
        i -= 1
        j +=1   

    # Si pasa todas las validaciones, la posición es válida
    return True

# Para poder mostrar las soluciones #
def mostrar_tablero(tablero):
    # Recorre cada fila del tablero solución
    for fila in tablero:
        # Recorre cada valor de la fila
        for valor in fila:
            # Imprime el valor sin formato especial
            print(valor, end=" ")
        print()
    # Salto extra para separar soluciones
    print()

### Main ###

# Se inicia el algoritmo de backtracking desde la fila 0
back_recursivo(0, tablero, contador)

# Se muestra la cantidad total de soluciones encontradas
print(f"\nTotal de soluciones encontradas: {len(soluciones)}\n")

# Se recorren y muestran todas las soluciones en consola
for i, sol in enumerate(soluciones, 1):
    print(f"Solución #{i}")
    mostrar_tablero(sol)

# Se vuelve a llamar la función para asegurar que las soluciones estén cargadas
back_recursivo(0, tablero, 1) # Llama la función "solucion(tablero)", con parámetro "tablero".

# Verifica si existen soluciones
if soluciones:
    # Se guardan las soluciones posibles en un archivo .txt
    with open("Soluciones posibles (N-Reinas).txt", "w") as f: 
        for i, sol in enumerate(soluciones, 1):
            # Escribe el número de la solución
            f.write(f"Solución N°{i}: \n")
            # Escribe el contenido del tablero
            for fila in sol:
                f.write(" ".join(f"{num:3}" for num in fila) + "\n")
            # Línea en blanco entre soluciones
            f.write("\n")
    print(f"\nSe encontraron {len(soluciones)} soluciones y se almacenaron en [Soluciones posibles (N-Reinas).txt].\n")
else:
    # Mensaje en caso de no existir soluciones
    print("\nNo hay soluciones posibles.\n")
