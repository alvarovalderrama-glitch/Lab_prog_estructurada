
def buscar_vacio(tablero):
    """
    Devuelve (f,c) de la primera celda vacía (valor 0)
    """

    # Recorre el tablero buscando la primera posición cuyo valor sea 0
    tamaño_tablero = len(tablero)
    for f in range(tamaño_tablero):
        for c in range(tamaño_tablero):
            if tablero[f][c] == 0:      # Detecta celda vacía
                return f, c             # Retorna su ubicación

def es_valido(tablero, f, c, candidato):
    """
    Chequea si 'candidato' puede colocarse en tablero[f][c] sin violar reglas.
    """

    tamaño_tablero = len(tablero)
    
    # Determina el tamaño k del subcuadro (k x k). N debe ser un cuadrado perfecto.
    k = int(tamaño_tablero**0.5)
    if k * k != tamaño_tablero:
        return False                # Si el tablero no es de tamaño válido, retornará 'False'
    
    # Calcula la fila y columna donde comienza el subcuadro que contiene a (f,c)
    inicio_fila_bloque = (f // k) * k
    inicio_columna_bloque = (c // k) * k

    # Recorre el bloque k x k y revisa si el candidato ya existe ahí
    for i in range(inicio_fila_bloque, inicio_fila_bloque + k):
        for j in range(inicio_columna_bloque, inicio_columna_bloque + k):
            if tablero[i][j] == candidato:
                return False        # No es válido si el número se repite en el bloque
    
    # # Verificación de la fila 
    for j in range(tamaño_tablero):
        if tablero[f][j] == candidato:
            return False            # No es válido si el número ya está en la fila

    # Verificación de la columna
    for i in range(tamaño_tablero):
        if tablero[i][c] == candidato:
            return False            # No es válido si el número ya está en la columna
    
    
    return True                     # Si pasa todas las verificaciones, es un movimiento válido

def encontrar_solucion(tablero):
    """
    Resuelve el Sudoku. Devuelve True si hay solución
    """
   
    # Busca la siguiente celda vacía del tablero
    vacio = buscar_vacio(tablero)

    # Si no hay celdas vacías, significa que el tablero está completamente resuelto
    if not vacio:
        return True  # Solución encontrada
    
    # Obtiene las coordenadas de la celda vacía encontrada
    f, c = vacio
    tamaño_tablero = len(tablero)

    # Intenta colocar cada número posible en la celda vacía
    for candidato in range(1, tamaño_tablero + 1):

        # Verifica si el número cumple todas las reglas del Sudoku
        if es_valido(tablero, f, c, candidato):
            # Asignación temporal del número
            tablero[f][c] = candidato

            # Llamada recursiva: intenta resolver el resto del tablero
            if encontrar_solucion(tablero):
                return True         # Si devuelve True, la solución está completa
            
            # Si no funcionó, se deshace el movimiento
            tablero[f][c] = 0

    # Si ningún candidato funciona, la solución no es posible desde este camino
    return False

def mostrar_tablero(tablero):
    """ 
    Imprime el tablero en pantalla 
    """
    
    print("")
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f'{tablero[i][j]:2}', end=" ")
        print("")
    print("")

# Progama Principal

tamaño_tablero = 4
# Genera un tablero vacío tamaño
tablero = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]

# Intenta resolver el tablero
if encontrar_solucion(tablero):
    print(f'\nSolución para un tablero {tamaño_tablero}x{tamaño_tablero}:')
    mostrar_tablero(tablero)
else:
    print(f'No hay solución para un tablero {tamaño_tablero}x{tamaño_tablero}') 