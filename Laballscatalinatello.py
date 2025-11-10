
# genera un laberinto con obstáculos al azar
# TODAS las soluciones posibles desde el inicio hasta la salida

import random  # para generar posiciones aleatorias de obstáculos

N = 5               # tamaño del laberinto (matriz de 5x5)
NUM_OBSTACULOS = 4  # cuántos obstáculos se van a poner

INICIO = (0, 0)          # casilla de inicio (fila 0, columna 0)
SALIDA = (N - 1, N - 1)  # casilla de salida (última fila, última columna)


def crear_matriz(n):
    # Crea una matriz n x n llena de 0.
    # 0 significa "camino libre".
    return [[0 for _ in range(n)] for _ in range(n)]


def poner_obstaculos(matriz, cantidad, inicio, salida):
    # Coloca "cantidad" de obstáculos (1) en posiciones aleatorias.
    # No coloca obstáculos sobre el inicio ni sobre la salida.
    n = len(matriz)
    colocados = 0
    while colocados < cantidad:
        # elegir una posición al azar
        f = random.randint(0, n - 1)
        c = random.randint(0, n - 1)
        # solo colocar si está libre y no es inicio o salida
        if (f, c) != inicio and (f, c) != salida and matriz[f][c] == 0:
            matriz[f][c] = 1   # 1 = obstáculo
            colocados += 1     # contamos cuántos llevamos


def imprimir_matriz(matriz):
    # Muestra la matriz en pantalla para ver cómo quedó el laberinto
    # 0 = libre, 1 = obstáculo
    for fila in matriz:
        print(" ".join(str(x) for x in fila))
    print()  # línea en blanco al final


def es_valida(matriz, fila, col, visitado):
    # Revisa si una casilla se puede visitar.
    # Debe cumplir:
    # - estar dentro de los límites
    # - no ser obstáculo
    # - no haber sido visitada antes
    n = len(matriz)
    return (
        0 <= fila < n and           # dentro de filas
        0 <= col < n and            # dentro de columnas
        matriz[fila][col] == 0 and  # no es obstáculo
        not visitado[fila][col]     # no la he visitado
    )


def dfs_todas(matriz, actual, salida, visitado, camino_actual, todas):
    # Función recursiva que busca TODAS las rutas desde "actual" hasta "salida".
    #  matriz: el laberinto
    # actual: posición donde estoy ahora (fila, col)
    # salida: posición objetivo
    # visitado: matriz booleana para no repetir casillas
    # camino_actual: lista con el recorrido que llevo
    # todas: lista que almacenará todos los caminos encontrados

    # 1. Si ya llegué a la salida, guardo este camino
    if actual == salida:
        # agrego una copia del camino actual + la casilla final
        todas.append(list(camino_actual) + [actual])
        return  # regreso porque ya terminé este camino

    # 2. Marco la casilla actual como visitada y la agrego al camino
    fila, col = actual
    visitado[fila][col] = True
    camino_actual.append(actual)

    # 3. Defino los 4 movimientos posibles (arriba, derecha, abajo, izquierda)
    movs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 4. Recorro cada movimiento
    for df, dc in movs:
        nf = fila + df   # nueva fila
        nc = col + dc    # nueva columna
        # si es válido moverme ahí, sigo recursivamente
        if es_valida(matriz, nf, nc, visitado):
            dfs_todas(matriz, (nf, nc), salida, visitado, camino_actual, todas)

    # 5. BACKTRACKING:
    # si ya probé todas las opciones desde aquí, deshago los cambios
    camino_actual.pop()         # saco esta casilla del camino
    visitado[fila][col] = False # la marco como no visitada para futuros caminos


def main():
    # 1. Crear el laberinto vacío
    lab = crear_matriz(N)

    # 2. Colocar obstáculos aleatorios
    poner_obstaculos(lab, NUM_OBSTACULOS, INICIO, SALIDA)

    print("Laberinto generado (0 = libre, 1 = obstáculo):")
    imprimir_matriz(lab)

    # 3. Crear la matriz de visitados (todas en False al inicio)
    visitado = [[False] * N for _ in range(N)]

    # 4. Lista donde se guardarán todas las rutas que se encuentren
    todas = []

    # 5. Llamar al backtracking para buscar TODAS las soluciones
    dfs_todas(lab, INICIO, SALIDA, visitado, [], todas)

    # 6. Mostrar resultados
    if not todas:
        print("No se encontraron caminos.")
    else:
        print(f"Se encontraron {len(todas)} caminos:")
        for i, ruta in enumerate(todas, start=1):
            print(f"Camino {i}: {ruta}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
