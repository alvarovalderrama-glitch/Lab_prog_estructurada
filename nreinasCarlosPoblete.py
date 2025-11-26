tamano_tablero = 9

tablero = [-1] * tamano_tablero

'''tablero es una lista donde tiene una cantidad de elementos dependiendo del tamaño del tablero,
tablero[0] = fila 0, tablero[1] = fila 1 y asi sucesivamente
si se encuetra una posicion valida se guarda la columna con el numero de esa fila
ejemplo tablero[2,0,3,1]
tablero[3] seria la fila 3 y se revisa una por uno los elemontos [2,0,3,1] como el 3 esta en el elemento 2
la reina estaria en la fila 3, columna 2
si en la lista hay un -1 significa que es un espacio vacio'''

encontrado = False


def es_valido(fila, col):
    for fila_anterior in range(fila):
        col_reina_antes = tablero[fila_anterior]

        if col_reina_antes == col:                               # revisa que no esten en la misma columna
            return False
        
        if (fila - col) == (fila_anterior - col_reina_antes):    # revisa que no esten en la diagonal principal (\)
            return False

        if (fila + col) == (fila_anterior + col_reina_antes):    # revisa que no esten en la diagona secundaria (/)
            return False

    return True     # si no coincide en columna y diagonale retorna True


def imprimir_solucion():
    for fila in range(tamano_tablero):
        linea = ""
        for col in range(tamano_tablero):
            if tablero[fila] == col:               # donde tablero[fila] coincide con un elemento de la lista o sea columna se le pone R
                linea += " R "
            else:
                linea += " - "                     # si no coincide se pone un -
        print(linea)
    print()


def resolver(fila):
    global encontrado

    if tamano_tablero == 2 or tamano_tablero == 3:      # tablero 2x2 y 3x3 no tienen solucion
        print('No hay solucion.')
        return

    if encontrado:                      # frena el codigo 
        return

    if fila == tamano_tablero:          #  si estan todas las reinas significa que ya se encontro un resultado
        imprimir_solucion()
        encontrado = True
        return
    
    for col in range(tamano_tablero):      # revisa todas las columnas
        if es_valido(fila, col):           # si es valido sigue
            tablero[fila] = col            # se guardamos la posicion de la columna con el mismo valor de la fila
            resolver(fila + 1)             # avanza una fila
            tablero[fila] = -1             # si no hay solucion mas adelante retrocede para ver mas opciones


resolver(0)   