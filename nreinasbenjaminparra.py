import time

def resolver_n_reinas(n):

    # Inicializa el tablero como una lista donde 'tablero[i]' representa 
    # la columna de la reina en la fila 'i'. Usamos -1 para indicar que 
    # no hay reina colocada aún.
    tablero = [-1] * n
    soluciones = []
    
    # Inicia el proceso de backtracking desde la primera fila (fila 0)
    backtracking_n_reinas(tablero, 0, n, soluciones)
    
    # Imprime los resultados
    print(f"--- Problema de las {n} Reinas ---")
    print(f"Total de soluciones encontradas: {len(soluciones)}")
    
    # Imprime la primera solución encontrada (si existe)
    if soluciones:
        print("\nPrimera solución (representación de filas y columnas):")
        print(soluciones[0])
        print("\nRepresentación visual de la primera solución:")
        imprimir_tablero_visual(soluciones[0], n)
    else:
        print("No se encontraron soluciones para N =", n)

def es_seguro(tablero, fila, col):

    # Comprobación de filas/columnas:
    # Como 'tablero[i]' es la columna de la reina en la fila 'i', si 'tablero[i] == col', 
    # ya hay una reina en la misma columna.
    for i in range(fila):
        # 1. Columna (tablero[i] == col)
        if tablero[i] == col:
            return False
        
        # 2. Diagonales (abs(tablero[i] - col) == abs(i - fila))
        # La diferencia en las filas debe ser igual a la diferencia en las columnas.
        # Diagonales principales: (fila - i) == (col - tablero[i])
        # Diagonales secundarias: (fila - i) == (tablero[i] - col)
        # Esto se simplifica a la igualdad de valores absolutos de las diferencias.
        if abs(tablero[i] - col) == abs(i - fila):
            return False
            
    return True

def backtracking_n_reinas(tablero, fila, n, soluciones):

    # CASO BASE: Si ya se han colocado reinas en todas las filas (0 a n-1),
    # se ha encontrado una solución completa.
    if fila == n:
        # Crea una copia de la solución y la guarda.
        soluciones.append(list(tablero))
        return

    # CASO RECURSIVO: Intenta colocar la reina en cada columna de la fila actual.
    for col in range(n):
        # 1. Comprobar si es seguro colocar la reina en (fila, col)
        if es_seguro(tablero, fila, col):
            
            # 2. Colocar la reina (MOVIMIENTO / ELECCIÓN)
            tablero[fila] = col
            
            # 3. Llamada recursiva para la siguiente fila (EXPLORACIÓN)
            # El algoritmo avanza una fila.
            backtracking_n_reinas(tablero, fila + 1, n, soluciones)
            
            # 4. Deshacer la colocación (BACKTRACKING)
            # Esto no es estrictamente necesario en este modelo donde la 
            # asignación 'tablero[fila] = col' es sobrescrita en la 
            # siguiente iteración o al volver del stack, pero se puede 
            # hacer explícito:
            # tablero[fila] = -1 
            pass # El backtracking ocurre implícitamente al salir del stack 
                 # y la siguiente iteración del bucle 'for' sobrescribe el valor.

def imprimir_tablero_visual(solucion, n):
    """
    Imprime una solución del tablero de forma visual.
    'Q' para la reina, '.' para casilla vacía.
    """
    for i in range(n):
        fila_str = ""
        for j in range(n):
            if solucion[i] == j:
                fila_str += "Q "  # Reina
            else:
                fila_str += ". "  # Vacío
        print(fila_str)

# --- EJECUTAR EL ALGORITMO ---
if __name__ == "__main__":
    # Puedes cambiar el valor de N
    N = 8 
    
    inicio = time.time()
    resolver_n_reinas(N)
    fin = time.time()
    
    print(f"\nTiempo de ejecución: {fin - inicio:.4f} segundos.")