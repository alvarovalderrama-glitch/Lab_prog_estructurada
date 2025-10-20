MAX = 4

# ---- Función que valida si se puede mover a la posición nx, ny ----
def valida(tablero, candidato, x, y):
    posx = [0, 1, 0, -1]  # derecha, abajo, izquierda, arriba
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato-1]
    ny = y + posy[candidato-1]

    # Verifica límites
    if nx < 0 or nx >= MAX:
        return False
    if ny < 0 or ny >= MAX:
        return False
    # Verifica que la posición no esté ocupada ni sea obstáculo
    if tablero[nx][ny] == 0:
        return True
    else:
        return False

# ---- Siguiente posición según candidato ----
def siguiente_posicion(x, y, candidato):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    return x + posx[candidato-1], y + posy[candidato-1]

# ---- Verifica si llegamos al final ----
def final(nx, ny):
    return nx == MAX - 1 and ny == MAX - 1

# ---- Busca las coordenadas de un número en el tablero ----
def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j
    return None, None

# ---- Backtracking para encontrar el camino ----
def solucion(tablero):
    x, y = 0, 0
    contador = 1
    tablero_aux = [[0]*MAX for _ in range(MAX)]
    tablero[x][y] = contador
    candidato = 1
    solucion_encontrada = False

    while not solucion_encontrada:
        if candidato <= 4 and valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(x, y, candidato)
            tablero[nx][ny] = contador + 1

            if final(nx, ny):
                solucion_encontrada = True
                break
            else:
                tablero_aux[x][y] = candidato
                x, y = nx, ny
                contador += 1
                candidato = 1
        else:
            candidato += 1
            while candidato > 4 and not (x == 0 and y == 0):
                # Retroceder
                tablero[x][y] = 0
                contador -= 1
                x, y = buscar_xy(tablero, contador)
                if x is None:
                    return False
                candidato = tablero_aux[x][y] + 1
                tablero_aux[x][y] = 0
    return True

# ---- Muestra el tablero ----
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{c:2}" for c in fila))
    print("")

# ---- Colocar obstáculos ----
def colocar_obstaculo(tablero):
    tablero[0][3] = -1
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[2][2] = -1
    tablero[2][3] = -1

# ---- Programa principal ----
tablero = [[0]*MAX for _ in range(MAX)]
print("Tablero inicial:")
mostrar_tablero(tablero)

colocar_obstaculo(tablero)
print("Tablero con obstáculos:")
mostrar_tablero(tablero)

if solucion(tablero):
    print("¡Hay solución!")
    mostrar_tablero(tablero)
else:
    print("No hay solución")
