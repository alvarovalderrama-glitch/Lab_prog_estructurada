MAX = 4

# -------------------------------
# modulo valida
def valida(tablero, x, y):
    if x < 0 or x >= MAX:
        return False
    if y < 0 or y >= MAX:
        return False
    return tablero[x][y] == 0   # 0 = libre

# -------------------------------
# modulo final
def final(x, y):
    return x == MAX - 1 and y == MAX - 1

# -------------------------------
# modulo mostrar_tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        print(*fila)
    print()

# -------------------------------
# modulo colocar_obstaculo
def colocar_obstaculo(tablero):
    tablero[0][1] = -1
    tablero[0][2] = -1
    tablero[1][1] = -1
    tablero[1][2] = -1

# -------------------------------
# Solucion Modulo 
def Solucion(tablero, x, y, contador):
    # Caso base: ¿llegamos al final?
    if final(x, y):
        tablero[x][y] = contador
        mostrar_tablero(tablero)
        return True

    # Direcciones: derecha, abajo, izquierda, arriba
    movimientos = [(0,1), (1,0), (0,-1), (-1,0)]

    tablero[x][y] = contador  # marco la celda actual

    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if valida(tablero, nx, ny):
            if Solucion(tablero, nx, ny, contador + 1):
                return True   # si una rama funciona → listo

    # Si no funcionó ningún movimiento → retroceder
    tablero[x][y] = 0
    return False

# -------------------------------
# programa principal
if __name__ == "__main__":
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    colocar_obstaculo(tablero)

    print("Tablero inicial:")
    mostrar_tablero(tablero)

    if Solucion(tablero, 0, 0, 1):
        print("Hay solución")
    else:
        print("No hay solución.")
