MAX = 6  # tamaño del tablero (6x6)

# movimientos posibles del caballo
mov_x = [-2, -1, 1, 2, 2, 1, -1, -2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

# función para mostrar el tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{x:2}" for x in fila))
    print("")

# verifica si una posición es válida
def valida(x, y, tablero):
    # dentro del tablero y no visitada
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] == 0

# algoritmo de backtracking
def recorrido_caballo(x, y, paso, tablero):
    # si llenamos todas las casillas, ya hay solución
    if paso == MAX * MAX:
        return True

    # probamos los 8 movimientos posibles del caballo
    for k in range(8):
        nx = x + mov_x[k]
        ny = y + mov_y[k]
        if valida(nx, ny, tablero):
            tablero[nx][ny] = paso + 1  # marcamos el movimiento
            if recorrido_caballo(nx, ny, paso + 1, tablero):  # recursión
                return True  # si llega al final, detenemos todo
            tablero[nx][ny] = 0  # backtracking (desmarcar)

    return False  # no hay movimiento válido desde aquí

# programa principal
tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]  # tablero vacío
tablero[0][0] = 1  # empezamos en la esquina superior izquierda

if recorrido_caballo(0, 0, 1, tablero):
    print("✅ Hay una solución encontrada:\n")
    mostrar_tablero(tablero)
else:
    print("❌ No hay solución para este tamaño de tablero.")
