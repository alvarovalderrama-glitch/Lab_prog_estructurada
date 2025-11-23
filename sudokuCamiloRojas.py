# ---------------------------------------------------------------------------------------
# TABLERO INICIAL DE SUDOKU
tablero = [ # Matriz 9x9 que representa el Sudoku
    [5, 3, 0, 0, 7, 0, 0, 0, 0], # 0 significa casilla vacía
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
] # Fin del tablero inicial

# ---------------------------------------------------------------------------------------
# FUNCIÓN PARA IMPRIMIR TABLERO
def imprimir_tablero(tab): # Define una función que recibe un tablero de Sudoku
    for fila in range(9): # Recorre las 9 filas del tablero
        linea = "" # Variable para ir construyendo la línea de texto
        for col in range(9): # Recorre las 9 columnas de la fila actual
            linea += str(tab[fila][col]) + " " # Agrega el número seguido de un espacio
        print(linea) # Imprime la fila completa
    print() # Imprime una línea en blanco al final

# ---------------------------------------------------------------------------------------
# FUNCIÓN PARA BUSCAR VACÍO
def buscar_vacio(tab): # Busca una casilla vacía (con valor 0)
    for fila in range(9): # Recorre todas las filas
        for col in range(9): # Recorre todas las columnas de cada fila
            if tab[fila][col] == 0: # Si encuentra un 0 significa casilla vacía
                return fila, col # Devuelve la posición (fila, columna)
    return None # Si no encuentra 0, no hay casillas vacías

# ---------------------------------------------------------------------------------------
# FUNCIÓN QUE VERIFICA SI ES VÁLIDO
def es_valido(tab, fila, col, num): # Revisa si se puede poner 'num' en (fila, col)
    # Revisar fila
    for j in range(9): # Recorre todas las columnas de la fila
        if tab[fila][j] == num: # Si el número ya está en la fila
            return False # No es válido ponerlo

    # Revisar columna
    for i in range(9): # Recorre todas las filas de la columna
        if tab[i][col] == num: # Si el número ya está en la columna
            return False # No es válido ponerlo

    # Revisar subcuadro 3x3
    inicio_fila = (fila // 3) * 3 # Calcula la fila inicial del subcuadro
    inicio_col = (col // 3) * 3 # Calcula la columna inicial del subcuadro
    for i in range(inicio_fila, inicio_fila + 3):# Recorre las 3 filas del subcuadro
        for j in range(inicio_col, inicio_col + 3): # Recorre las 3 columnas del subcuadro
            if tab[i][j] == num: # Si el número ya está en el subcuadro
                return False # No es válido ponerlo

    return True # Si pasó todas las pruebas, es válido

# ---------------------------------------------------------------------------------------
# FUNCIÓN RECURSIVA (BACKTRACKING)
def resolver_sudoku(tab): # Función recursiva que resuelve el Sudoku
    vacio = buscar_vacio(tab) # Busca una casilla vacía en el tablero
    if vacio is None: # Si no hay casillas vacías
        return True # El Sudoku está completo y solucionado

    fila, col = vacio # Desempaqueta la posición vacía encontrada

    for num in range(1, 10): # Prueba números del 1 al 9
        if es_valido(tab, fila, col, num): # Verifica si el número es válido en esa posición
            tab[fila][col] = num # Coloca el número en la casilla

            if resolver_sudoku(tab): # Llama recursivamente para resolver el resto
                return True # Si la llamada recursiva tuvo éxito, termina

            tab[fila][col] = 0 # Si no funcionó, vuelve a poner 0 (backtracking)

    return False # Si ningún número es válido, no hay solución desde aquí

# ---------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL
def main(): # Define la función principal
    print("Sudoku inicial:\n") # Mensaje de encabezado
    imprimir_tablero(tablero) # Muestra el Sudoku original

    if resolver_sudoku(tablero): # Intenta resolver el Sudoku con backtracking
        print("Sudoku resuelto:\n") # Mensaje si se encontró solución
        imprimir_tablero(tablero) # Imprime el Sudoku ya resuelto
    else: # Si la función devolvió False
        print("No existe solución para este Sudoku.") # Mensaje si no se puede resolver

# Punto de entrada del programa
if __name__ == "__main__": # Verifica que el archivo se ejecute directamente
    main() # Llama a la función principal
