tamano_tablero = 5

# coordenadas de obstaculos
obstaculos = [(3, 2), (2, 4)]

# movimientos en orden: arriba, derecha, abajo, izquierda
mov_x = [-1, 0, 1, 0]
mov_y = [0, 1, 0, -1]


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(celda) for celda in fila))
    print()


# verifica si una posicion es valida
def es_valido(x, y, tablero):
    if not (0 <= x < tamano_tablero and 0 <= y < tamano_tablero):
        return False  # fuera de los limites
    if tablero[x][y] != 0:
        return False  # ya visitada o marcada
    if (x, y) in obstaculos:
        return False  # es obstaculo
    return True


# funcion recursiva principal
def resolver(tablero, x, y, paso_actual):
    # llegar al final (se termina)
    if (x, y) == (tamano_tablero - 1, tamano_tablero - 1):
        tablero[x][y] = paso_actual  # marcar el ultimo paso
        return True

    # probar los movimientos en el orden: arriba, derecha, abajo, izquierda
    for i in range(4):
        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valido(nx, ny, tablero):
            tablero[nx][ny] = paso_actual + 1  # marca siguiente paso
            if resolver(tablero, nx, ny, paso_actual + 1):
                return True  # detener cuando llegue a la meta
            tablero[nx][ny] = 0  # retrocede

    return False  # no hay camino desde esta ruta


# funcion principal
def laberinto():
    # crear tablero lleno de 0
    tablero = [[0 for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]

    # colocar obstaculos
    for (x, y) in obstaculos:
        tablero[x][y] = "X"

    x_inicial, y_inicial = 0, 0

    # validar inicio o fin bloqueados
    if (x_inicial, y_inicial) in obstaculos or (tamano_tablero - 1, tamano_tablero - 1) in obstaculos:
        print("No hay solución: inicio o final bloqueados.")
        return

    # marcar punto inicial con 1
    tablero[x_inicial][y_inicial] = 1

    # ejecutar busqueda
    if resolver(tablero, x_inicial, y_inicial, 1):
        print("Camino encontrado:\n")
        mostrar_tablero(tablero)
    else:
        print("No hay camino encontrado.")


# ejecutar el programa
laberinto()