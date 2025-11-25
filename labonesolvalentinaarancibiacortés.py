# -----------------------------------------------
# LABERINTO (BACKTRACKING) UNA SOLUCIÓN
# -----------------------------------------------

''' Este código resuelve un laberinto usando backtracking iterativo.
    El camino se marca con números desde 1 hasta llegar al final. '''

MAX = int(input("ingrese las dimensiones del tablero: "))

# ---- Función que valida si se puede mover a la posición nx, ny ----
def valida(tablero, candidato, x, y):
    # Movimientos posibles (derecha, abajo, izquierda, arriba)
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]

    # Cálculo de la nueva posición según el candidato
    nx = x + posx[candidato-1]
    ny = y + posy[candidato-1]

    # Verifica si está dentro de los límites del tablero
    if not (0 <= nx < MAX and 0 <= ny < MAX):
        return False

    # Devuelve True solo si la celda está libre (0)
    return tablero[nx][ny] == 0


# ---- Calcula la siguiente posición según el movimiento ----
def siguiente_posicion(x, y, candidato):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    return x + posx[candidato-1], y + posy[candidato-1]


# ---- Verifica si llegamos a la meta del laberinto ----
def final(nx, ny):
    return nx == MAX - 1 and ny == MAX - 1


# ---- Busca las coordenadas de un número en el tablero ----
def buscar_xy(tablero, contador):
    # Recorre todo el tablero buscando el número "contador"
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j
    return None, None  # Si no se encuentra


# ---- Backtracking iterativo para buscar una solución ----
def solucion(tablero):
    x, y = 0, 0         # Inicio
    contador = 1        # Número que marca el camino
    tablero_aux = [[0]*MAX for _ in range(MAX)]  # Guarda el movimiento que se probó en cada celda
    tablero[x][y] = contador
    candidato = 1       # Primer movimiento a intentar
    solucion_encontrada = False

    while not solucion_encontrada:
        # Primera parte: intentar avanzar
        if candidato <= 4 and valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(x, y, candidato)
            tablero[nx][ny] = contador + 1  # Marca la celda con el siguiente número

            # Si llegamos al final, terminamos
            if final(nx, ny):
                solucion_encontrada = True
                break

            # Si no es final, seguimos avanzando
            tablero_aux[x][y] = candidato  # Guardamos el camino tomado
            x, y = nx, ny
            contador += 1
            candidato = 1  # Reiniciar movimientos

        # Segunda parte: no pudimos avanzar → retroceder
        else:
            candidato += 1

            # Si ya probamos los 4 movimientos, retroceder
            while candidato > 4 and not (x == 0 and y == 0):
                tablero[x][y] = 0        # Desmarcar la celda
                contador -= 1            # Volver al número anterior
                x, y = buscar_xy(tablero, contador)  # Buscar dónde está el contador previo

                if x is None:
                    return False  # No existe camino válido

                candidato = tablero_aux[x][y] + 1  # Reintentar el siguiente candidato
                tablero_aux[x][y] = 0             # Limpiar el auxiliar

    return True  # Si encontramos solución


# ---- Función que muestra el tablero en pantalla ----
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{c:2}" for c in fila))
    print("")


# ---- Colocar obstáculos fijos en el tablero ----
def colocar_obstaculo(tablero):
    # Lista de obstáculos predefinidos
    obstaculos = [(0, 3), (1, 1), (2, 1), (2, 2), (2, 3)]

    for x, y in obstaculos:
        # Solo poner obstáculo si:
        # - Está dentro del tablero
        # - No es la casilla inicial
        # - No es la casilla final
        if 0 <= x < MAX and 0 <= y < MAX:
            if (x, y) not in [(0, 0), (MAX-1, MAX-1)]:
                tablero[x][y] = -1


# ---- Programa principal ----
tablero = [[0]*MAX for _ in range(MAX)]  # Crear tablero vacío

print("Tablero inicial:")
mostrar_tablero(tablero)

# Colocar obstáculos
colocar_obstaculo(tablero)
print("Tablero con obstáculos:")
mostrar_tablero(tablero)

# Resolver
if solucion(tablero):
    print("¡Hay solución!")
    mostrar_tablero(tablero)
else:
    print("No hay solución")
