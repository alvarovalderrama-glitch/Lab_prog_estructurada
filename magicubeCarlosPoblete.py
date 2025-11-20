suma_total = 15           # suma total de filas, columnas y diagonales
encontrado = False        # se usa para detener cuando se encuentre una solucion

def es_valido(tablero, fila, col):
    # suma fila
    if sum(tablero[fila]) > suma_total:
        return False
    
    # suma columna   
    if sum(tablero[i][col] for i in range(3)) > suma_total:
        return False

    # suma diagonal principal (\)
    if fila == col:
        if tablero[0][0] + tablero[1][1] + tablero[2][2] > suma_total:
            return False

    # suma diagonal secundaria (/)
    if fila + col == 2:
        if tablero[0][2] + tablero[1][1] + tablero[2][0] > suma_total:
            return False
    
    return True


def cuadrado_magico(tablero):
    # filas
    for i in range(3):
        if sum(tablero[i]) != suma_total:
            return False
   
    # columnas
    for j in range(3):
        if sum(tablero[i][j] for i in range(3)) != suma_total:
            return False

    # las dos diagonales
    if tablero[0][0] + tablero[1][1] + tablero[2][2] != suma_total:
        return False
    if tablero[0][2] + tablero[1][1] + tablero[2][0] != suma_total:
        return False

    return True


def imprimir(tablero):
    for fila in tablero:
        print(fila)
    print()


def programa_principal(tablero, num_guardados, fila, col):
    global encontrado
    if encontrado:
        return

    if fila == 3:  # tablero lleno
        if cuadrado_magico(tablero):
            imprimir(tablero)
            encontrado = True
        return

    for num in range(1, 10):              # genera numero al azar del 1 al 9
        if num not in num_guardados:      # verifica si el numero creado no esta guardado para poder continuar, si es asi vuele a generar un numero 
            tablero[fila][col] = num      

            if es_valido(tablero, fila, col):
                num_guardados.add(num)         # guarda el numero en la lista en set()

                # en esta parte se va completando el tablero
                if col == 2:    # si esta em la columna 2 o sea la final, baja a la siguiente fila y vuelve a la columna 0
                    programa_principal(tablero, num_guardados, fila + 1, 0)
                else:           # si no esta col 2 significa que tiene que avanzar en la fila por eso se le suma col + 1
                    programa_principal(tablero, num_guardados, fila, col + 1)

                num_guardados.remove(num)   # con esto se borra el num guardado

            tablero[fila][col] = 0          # deja la casilla en 0 para otro metodo


tablero = [[0] * 3 for _ in range(3)]
num_guardados = set()

programa_principal(tablero, num_guardados, 0, 0)