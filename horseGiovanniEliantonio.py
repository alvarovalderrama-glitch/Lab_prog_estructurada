
def valida(tablero, candidato, x, y):
    """Verifica si la posición alcanzada con el movimiento es válida"""
    nx = x + pos_x[candidato - 1]
    ny = y + pos_y[candidato - 1]
    if nx < 0 or nx >= tamaño_tablero:
        return False
    if ny < 0 or ny >= tamaño_tablero:
        return False
    if tablero[nx][ny] != 0:
        return False
    return True


def siguiente_posicion(candidato, x, y):
    """Devuelve la nueva posición (nx, ny) alcanzada con el movimiento"""
    nx = x + pos_x[candidato - 1]
    ny = y + pos_y[candidato - 1]
    return nx, ny


def final(tablero):
    """Devuelve True si todas las casillas están llenas"""
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if tablero[i][j] == 0:
                return False
    return True


def mostrar_tablero(tablero):
    """Muestra el tablero en consola"""
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f"{tablero[i][j]:2}", end=" ")
        print("")
    print("")


def solucion(tablero, x=0, y=0, contador=1):
    """Módulo principal: busca una solución con backtracking"""
    if final(tablero):
        return True  # se llenaron todas las casillas

    # probar todos los movimientos posibles del caballo
    for candidato in range(1, 9):
        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1  # colocar el número de paso

            # llamada recursiva
            if solucion(tablero, nx, ny, contador + 1):
                return True  # solución encontrada

            # retroceso
            tablero[nx][ny] = 0

    # si no hay movimientos válidos, regresar False
    return False


# Programa principal

tamaño_tablero = 5  # tamaño del tablero

# movimientos posibles del caballo
pos_x = [-2, -1, 1, 2, 2, 1, -1, -2]
pos_y = [1, 2, 2, 1, -1, -2, -2, -1]

tablero = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]  # crea el tablero
tablero[0][0] = 1  # posición inicial del caballo
print("Tablero inicial:\n")
mostrar_tablero(tablero)

if solucion(tablero, 0, 0, 1):
    print("Hay solución:\n")
    mostrar_tablero(tablero)
else:
    print("No hay una solución posible.")
