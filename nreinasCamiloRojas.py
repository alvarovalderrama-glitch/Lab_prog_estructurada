import random # Importa el módulo random para elegir una solución aleatoria

N = 8 # Tamaño del tablero (N x N) y número de reinas

# -----------------------------------------------------------------------------------------------------------
# FUNCIÓN PARA IMPRIMIR TABLERO
def imprimir_tablero(tablero): # Define una función que recibe un tablero y lo muestra por pantalla
    for fila in range(N): # Recorre cada índice de fila del tablero
        linea = "" # Inicializa un string vacío para armar la línea a imprimir
        for col in range(N): # Recorre cada índice de columna de la fila actual
            if tablero[fila][col] == 1: # Si en esa posición hay una reina (valor 1)
                linea += " Q " # Agrega la letra Q a la línea para representarla
            else: # Si en esa posición no hay reina (valor 0)
                linea += " . " # Agrega un punto para indicar casilla vacía
        print(linea) # Imprime la línea completa de la fila
    print() # Imprime una línea en blanco después del tablero

# -----------------------------------------------------------------------------------------------------------
# FUNCIÓN QUE VERIFICA SI ES SEGURO (para los movimientos de las reinas)
def es_seguro(tablero, fila, col): # Revisa si es seguro colocar una reina en (fila, col)
    for i in range(fila): # Recorre todas las filas anteriores a la actual
        if tablero[i][col] == 1: # Si encuentra una reina en la misma columna
            return False # No es seguro, retorna False

    i = fila - 1 # Empieza una fila más arriba para revisar diagonal izquierda
    j = col - 1  # Empieza una columna a la izquierda
    while i >= 0 and j >= 0: # Mientras se mantenga dentro de los límites del tablero
        if tablero[i][j] == 1: # Si encuentra una reina en esa diagonal
            return False # No es seguro, retorna False
        i -= 1 # Sube una fila
        j -= 1 # Se mueve una columna a la izquierda

    i = fila - 1 # Empieza una fila más arriba para revisar diagonal derecha
    j = col + 1 # Empieza una columna a la derecha
    while i >= 0 and j < N: # Mientras la columna esté dentro del tablero
        if tablero[i][j] == 1: # Si encuentra una reina en esa diagonal
            return False # No es seguro, retorna False
        i -= 1 # Sube una fila
        j += 1 # Se mueve una columna a la derecha

    return True # Si no encontró conflictos, colocar aquí es seguro

# -----------------------------------------------------------------------------------------------------------
# FUNCIÓN RECURSIVA (BACKTRACKING)
def resolver_n_reinas(tablero, fila, soluciones): # Función recursiva que llena el tablero fila por fila
    if fila == N: # Caso base: si ya se procesaron todas las filas
        copia = [fila_tab[:] for fila_tab in tablero]  # Crea una copia independiente del tablero actual
        soluciones.append(copia) # Guarda la copia del tablero como una solución válida
        return # Termina esta rama de la recursión para seguir buscando más

    for col in range(N): # Recorre todas las columnas posibles de la fila actual
        if es_seguro(tablero, fila, col): # Verifica si es seguro colocar una reina en (fila, col)
            tablero[fila][col] = 1 # Coloca la reina en esa casilla
            resolver_n_reinas(tablero, fila + 1, soluciones) # Llama recursivamente a la siguiente fila
            tablero[fila][col] = 0 # Quita la reina (backtracking) para probar otras columnas

# -----------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
def main(): # Define la función principal del programa
    tablero = [[0 for _ in range(N)] for _ in range(N)] # Crea un tablero N x N lleno de ceros (sin reinas)
    soluciones = [] # Lista vacía donde se guardarán todas las soluciones encontradas

    print(f"Buscando TODAS las soluciones para {N} reinas...\n") # Mensaje informativo inicial

    resolver_n_reinas(tablero, 0, soluciones) # Llama a la función recursiva comenzando desde la fila 0

    total = len(soluciones) # Cuenta cuántas soluciones totales se encontraron

    if total == 0: # Si no se encontró ninguna solución
        print("No existe solución para este valor de N.") # Muestra mensaje de que no hay soluciones
    else: # Si hay una o más soluciones
        print(f"Se encontraron {total} soluciones distintas.\n") # Informa el total de soluciones
        solucion_aleatoria = random.choice(soluciones) # Elige una solución al azar de la lista
        print("Mostrando una solución aleatoria:\n") # Mensaje de qué se va a mostrar
        imprimir_tablero(solucion_aleatoria) # Imprime solo ese tablero elegido al azar
# -----------------------------------------------------------------------------------------------------------
# Punto de entrada del programa
if __name__ == "__main__": # Verifica que este archivo se esté ejecutando directamente
    main() # Llama a la función principal para iniciar el programa
