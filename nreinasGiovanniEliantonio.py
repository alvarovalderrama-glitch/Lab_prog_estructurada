def es_casilla_segura(fila, col, reinas):
    """
    Verifica si se puede colocar una reina en (fila, col).
    Solo comprobamos filas anteriores porque el algoritmo coloca
    exactamente una reina por fila y nunca ha colocado reinas
    en filas futuras.

    Devuelve True si está libre, False si hay conflicto.
    """
    # Comprobar columna
    for i in range(fila):
        if tablero[i][col] == 1:
            return False        # Ya hay una reina en la misma columna

    # diagonal superior izquierda
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False        # Conflicto en diagonal superior izquierda
        i -= 1
        j -= 1

    # diagonal superior derecha
    i, j = fila - 1, col + 1
    while i >= 0 and j < reinas:
        if tablero[i][j] == 1:
            return False        # Conflicto en diagonal superior derecha
        i -= 1
        j += 1

    return True # no se encontró conflicto

def agregar_reina(tablero, reinas, fila):
    """
    Se va Colocando reinas fila por fila.
    - fila: índice de la fila actual donde intentar colocar una reina.
    - reinas: tamaño del tablero.
    Retorna True si encontró una solución (colocó todas las reinas).
    """

    # Si ya colocamos reinas en todas las filas, Se encontró solución
    if fila == reinas:
        return True

    # Intenta colocar una reina en cada columna de la fila actual
    for col in range(reinas):
        # Si la posición (fila,col) es segura, colocamos la reina
        # Recursivamente intentamos resolver la siguiente fila
        if es_casilla_segura(fila, col, reinas):
            tablero[fila][col] = 1
            
            # Llamada recursiva: intentar resolver para la siguiente fila
            if agregar_reina(tablero, reinas, fila + 1):
                return True     # si la recursión tuvo éxito, propagamos True
            else:
                tablero[fila][col] = 0  # Si no hubo solución con esta colocación, deshacemos

    # Si ninguna columna funcionó en esta fila, devolvemos False
    return False

def mostrar_tablero(tablero):
    """ Imprime el tablero en pantalla """
    
    print("")
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f'{tablero[i][j]:2}', end=" ")
        print("")
    print("")


reinas = int(input("Ingrese el número de reinas a colocar: "))
tamaño_tablero = reinas

if (reinas ==  2) or (reinas == 3): # Estos tableros no tienen solución:
    print('No existe solución')

else:
    print('\nSolución encontrada:')
    # creamos el tablero como matriz de ceros (0 = vacío, 1 = reina)
    tablero = [[0 for fila in range(tamaño_tablero)] for col in range(tamaño_tablero)]
    agregar_reina(tablero, reinas, fila = 0)
    mostrar_tablero(tablero)