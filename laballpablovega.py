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

lab = [list(fila) for fila in laberinto_texto]

inicio = None
salida = None
for i in range(len(lab)):
    for j in range(len(lab[0])):
        if lab[i][j] == 'S':
            inicio = (i, j)
        if lab[i][j] == 'E':
            salida = (i, j)

if inicio is None or salida is None:
    print("Falta S o E, no puedo seguir.")
    raise SystemExit

movs = [(-1,0),(1,0),(0,-1),(0,1)]

def dentro(i, j):
    return 0 <= i < len(lab) and 0 <= j < len(lab[0])

def libre(i, j):
    return lab[i][j] != '#'

def imprimir_con_camino(camino):
    marcas = set(camino)
    for i in range(len(lab)):
        fila = []
        for j in range(len(lab[0])):
            if (i, j) in marcas and lab[i][j] == ' ':
                fila.append('.')
            else:
                fila.append(lab[i][j])
        print("".join(fila))
    print("-" * len(lab[0]))

todas = []
visitado = [[False]*len(lab[0]) for _ in range(len(lab))]

def backtrack(i, j, camino):
    # Si llego a la salida, guardo una copia del camino
    if (i, j) == salida:
        print("¡Llegué a E! Camino completo guardado.")
        todas.append(camino[:])
        imprimir_con_camino(camino)
        return

    # Probar cada movimiento posible
    for di, dj in movs:
        ni, nj = i + di, j + dj
        if dentro(ni, nj) and libre(ni, nj) and not visitado[ni][nj]:
            visitado[ni][nj] = True
            camino.append((ni, nj))
            # print para ver por dónde voy
            print("Paso a", (ni, nj), "camino actual len:", len(camino))
            backtrack(ni, nj, camino)
            # deshacer
            camino.pop()
            visitado[ni][nj] = False

# Preparar punto de partida
i0, j0 = inicio
visitado[i0][j0] = True
print("Inicio:", inicio, "Salida:", salida)
print("Buscando todas las rutas...")

backtrack(i0, j0, [inicio])

print("Cantidad total de soluciones encontradas:", len(todas))
for k, cam in enumerate(todas, start=1):
    print(f"Solución {k} (longitud {len(cam)}):")
print(cam)