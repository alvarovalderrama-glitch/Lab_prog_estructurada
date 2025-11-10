
# laberinto con obstáculos al azar
# UNA sola solución desde el inicio hasta la salida
import random

# Parámetros del laberinto
N = 5               # tamaño del laberinto N x N
NUM_OBSTACULOS = 4  # cantidad de obstáculos aleatorios

INICIO = (0, 0)
SALIDA = (N - 1, N - 1)


def crear_matriz(n):
    # Crea una matriz n x n llena de 0 (camino libre)
    return [[0 for _ in range(n)] for _ in range(n)]


def poner_obstaculos(matriz, cantidad, inicio, salida):
    # Coloca 'cantidad' de obstáculos (1) en posiciones aleatorias
    n = len(matriz)
    colocados = 0
    while colocados < cantidad:
        f = random.randint(0, n - 1)
        c = random.randint(0, n - 1)
        # No poner obstáculo encima del inicio o de la salida
        if (f, c) != inicio and (f, c) != salida and matriz[f][c] == 0:
            matriz[f][c] = 1
            colocados += 1


def imprimir_matriz(matriz):
    # Imprime la matriz en consola
    for fila in matriz:
        print(" ".join(str(x) for x in fila))
    print()


def es_valida(matriz, fila, col, visitado):
    # Devuelve True si la casilla está dentro de la matriz,
    # no es un obstáculo y no ha sido visitada.
    n = len(matriz)
    return (
        0 <= fila < n and
        0 <= col < n and
        matriz[fila][col] == 0 and
        not visitado[fila][col]
    )


def dfs_una_sol(matriz, actual, salida, visitado, camino):
    # Busca UNA solución desde 'actual' hasta 'salida'
    if actual == salida:
        camino.append(actual)
        return True

    fila, col = actual
    visitado[fila][col] = True
    camino.append(actual)

    # movimientos: arriba, derecha, abajo, izquierda
    movs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for df, dc in movs:
        nf = fila + df, col + dc
        if es_valida(matriz, nf, nc := col + dc, visitado):
            if dfs_una_sol(matriz, (nf, nc), salida, visitado, camino):
                return True

    # si no resultó, deshacemos el paso
    camino.pop()
    return False


def main():
    # 1. crear laberinto
    lab = crear_matriz(N)

    # 2. poner obstáculos al azar
    poner_obstaculos(lab, NUM_OBSTACULOS, INICIO, SALIDA)

    print("Laberinto generado (0 = libre, 1 = obstáculo):")
    imprimir_matriz(lab)

    # 3. preparar estructuras
    visitado = [[False] * N for _ in range(N)]
    camino = []

    # 4. buscar UNA solución
    if dfs_una_sol(lab, INICIO, SALIDA, visitado, camino):
        print("Se encontró un camino:")
        for paso in camino:
            print(paso)
    else:
        print("No hay camino desde el inicio hasta la salida.")


if __name__ == "__main__":
    main()
