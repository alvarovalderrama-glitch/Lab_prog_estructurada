def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            print(tablero[i][j], end = " ") 
        print(" ")
    print(" ")


def es_valido(tablero, fila, col):

    # Revisar misma fila en columnas anteriores
    for j in range(col):
        if tablero[fila][j] == 1:
            return False

    # Revisar diagonal superior izquierda
    i, j = fila - 1, col - 1
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Revisar diagonal inferior izquierda
    i, j = fila + 1, col - 1
    while i < n and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True


def resolver_tablero(n):
    tablero = [[0] * n for _ in range(n)]
    def backtracking(col):
        if col == n:
            return [fila[:] for fila in tablero]#crea una copia del tablero

        for fila in range(n):#recorre las filas
            if es_valido(tablero, fila, col):
                tablero[fila][col] = 1

                resultado = backtracking(col + 1)#se mueve a la siguiente columna
                if resultado:
                    return resultado#devuelve la solucion para la  fila

                tablero[fila][col] = 0  #retroceso

        return None

    return backtracking(0)


n = int(input("Ingresa el tamaño del tablero: "))#le asigna a una variable n el tamaño del tablero
solucion = resolver_tablero(n)

if solucion:
    imprimir_tablero(solucion)
else:
    print("No hay solución para un tablero de tamaño", n)

