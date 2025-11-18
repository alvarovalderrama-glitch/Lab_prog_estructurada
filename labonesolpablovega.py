# El laberinto se ve así:
# 'S' = inicio, 'E' = salida, '#' = pared, ' ' (espacio) = camino

laberinto_texto = [
    "S  #     ",
    "## # ### ",
    "   #   # ",
    " #   #   ",
    " ### ### ",
    "   #     ",
    " #   ### ",
    " # #   E ",
]

# Pasar a lista de listas para poder modificar si quiero
lab = [list(fila) for fila in laberinto_texto]

# Buscar S (inicio) y E (salida) recorriendo todo
inicio = None
salida = None
for i in range(len(lab)):
    for j in range(len(lab[0])):
        if lab[i][j] == 'S':
            inicio = (i, j)
        if lab[i][j] == 'E':
            salida = (i, j)

if inicio is None or salida is None:
    print("No se encontró 'S' o 'E' en el laberinto. Revisa el mapa.")
    raise SystemExit

# Movimientos: arriba, abajo, izquierda, derecha (nada diagonal)
movs = [(-1,0),(1,0),(0,-1),(0,1)]

# Para marcar visitados uso una matriz de False/True
visitado = [[False]*len(lab[0]) for _ in range(len(lab))]

def dentro(i, j):
    return 0 <= i < len(lab) and 0 <= j < len(lab[0])

def es_transitable(i, j):
    return lab[i][j] != '#'

def imprimir_laberinto(camino=None):
    # Dibuja el laberinto y, si hay camino, lo marca con '.'
    # (sin pisar la S ni la E)
    marcas = {pos for pos in (camino or [])}
    for i in range(len(lab)):
        fila_armada = []
        for j in range(len(lab[0])):
            if (i, j) in marcas and lab[i][j] == ' ':
                fila_armada.append('.')
            else:
                fila_armada.append(lab[i][j])
        print("".join(fila_armada))
    print("-" * len(lab[0]))

def dfs_una_solucion():
    # Pila manual: cada elemento tiene (i, j, siguienteMovimiento, caminoActual)
    i0, j0 = inicio
    pila = [(i0, j0, 0, [(i0, j0)])]
    visitado[i0][j0] = True
    print("Empiezo en:", inicio)
    imprimir_laberinto([inicio])

    while pila:
        i, j, idx, camino = pila[-1]

        if (i, j) == salida:
            print("¡Listo! Llegué a la salida:", salida)
            return camino

        if idx >= len(movs):
            # No hay más movimientos desde aquí, retrocedo (backtracking)
            pila.pop()
            print("Retrocediendo desde", (i, j))
            continue

        # Probar el siguiente movimiento
        di, dj = movs[idx]
        # Actualizar el índice en la cima de la pila (para probar el próximo mov la próxima vez)
        pila[-1] = (i, j, idx + 1, camino)

        ni, nj = i + di, j + dj
        if dentro(ni, nj) and es_transitable(ni, nj) and not visitado[ni][nj]:
            visitado[ni][nj] = True
            nuevo_camino = camino + [(ni, nj)]
            print("Voy a", (ni, nj))
            pila.append((ni, nj, 0, nuevo_camino))
            # Puedo ir mostrando el camino parcial
            imprimir_laberinto(nuevo_camino)

    print("No encontré salida :(")
    return None

sol = dfs_una_solucion()

if sol:
    print("Camino encontrado (en orden):")
    print(sol)
    print("Laberinto con el camino marcado con '.'")
    imprimir_laberinto(sol)
else:
    print("No hay camino desde S hasta E en este mapa.")