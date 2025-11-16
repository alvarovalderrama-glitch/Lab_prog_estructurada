MAX = 3  # tamaño del tablero 3x3
suma = 15  # suma que debe tener cada fila columna y diagonal

tablero = [[0]*MAX for _ in range(MAX)]  # se crea el tablero vacio con ceros
marca = [False]*10  # lista para marcar si un numero del 1 al 9 ya fue usado

# funcion que verifica si el tablero cumple con las reglas del cuadrado magico
def es_valido(tablero):
    for i in range(3):
        if sum(tablero[i]) != suma:  # verifica que cada fila sume 15
            return False
    for j in range(3):
        if tablero[0][j] + tablero[1][j] + tablero[2][j] != suma:  # verifica que cada columna sume 15
            return False
    if tablero[0][0] + tablero[1][1] + tablero[2][2] != suma and tablero[0][2] + tablero[1][1] + tablero[2][0] != suma: # verifica que las diagonales sumen 15
        return False 
    return True  # si todo esta bien devuelve True

# funcion que imprime el tablero con formato
def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(f'{c:2}' for c in fila))  # imprime cada fila con espacios
    print()  # salto de linea para separar tableros

# funcion recursiva que intenta llenar el tablero con numeros del 1 al 9
def backtrack(fila, columna):
    if fila == MAX:  # si ya se llenaron todas las filas
        if es_valido(tablero):  # verifica si el tablero es valido
            imprimir_tablero(tablero)  # si lo es lo imprime
            return True  # termina la busqueda
        return False  # si no es valido regresa

    for i in range(1, 10):  # prueba con los numeros del 1 al 9
        if not marca[i]:  # si el numero no ha sido usado
            tablero[fila][columna] = i  # lo coloca en el tablero
            marca[i] = True  # lo marca como usado

            # calcula la siguiente posicion en el tablero
            vertical = fila
            horizontal = columna + 1
            if horizontal == MAX:  # si se acaba la fila pasa a la siguiente
                horizontal = 0
                vertical += 1

            if backtrack(vertical, horizontal):  # llama recursivamente al siguiente paso
                return True  # si encuentra solucion termina

            tablero[fila][columna] = 0  # si no funciono borra el numero
            marca[i] = False  # lo desmarca

    return False  # si no se pudo colocar ningun numero valido

# se inicia el proceso desde la posicion 0 0
fila = 0
columna= 0
backtrack(fila, columna)
