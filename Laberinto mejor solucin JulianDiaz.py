def es_valida(tablero, x, y):
    n = len(tablero)
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == 0

def resolver_mejor(tablero, x, y, camino, mejor):
    n = len(tablero)
    if x == n - 1 and y == n - 1:
        camino.append((x, y))
        if not mejor[0] or len(camino) < len(mejor[0]):
            mejor[0] = camino.copy()
        camino.pop()
        return

    if es_valida(tablero, x, y):
        tablero[x][y] = 2
        camino.append((x, y))
        resolver_mejor(tablero, x + 1, y, camino, mejor)
        resolver_mejor(tablero, x, y + 1, camino, mejor)
        resolver_mejor(tablero, x - 1, y, camino, mejor)
        resolver_mejor(tablero, x, y - 1, camino, mejor)
        camino.pop()
        tablero[x][y] = 0

def mostrar_camino(mejor, n):
    if not mejor[0]:
        print("No hay solución.")
        return
    tablero = [[0 for _ in range(n)] for _ in range(n)]
    for paso, (x, y) in enumerate(mejor[0], start=1):
        tablero[x][y] = paso
    for fila in tablero:
        print(" ".join(str(c) for c in fila))
    print(f"\nLargo del camino: {len(mejor[0])}")

n = int(input("Ingrese tamaño del laberinto (n x n): "))
tablero = [[0 for _ in range(n)] for _ in range(n)]
mejor = [None]
resolver_mejor(tablero, 0, 0, [], mejor)
mostrar_camino(mejor, n)
