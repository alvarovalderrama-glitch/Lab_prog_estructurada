import random

def mostrar_tablero(tablero):
    return "\n".join(" ".join(str(c) for c in fila) for fila in tablero) + "\n"

def es_valida(tablero, x, y):
    n = len(tablero)
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == 0

def resolver_todas(tablero, x, y, soluciones, paso):
    n = len(tablero)
    if x == n - 1 and y == n - 1:
        tablero[x][y] = paso
        soluciones.append([fila.copy() for fila in tablero])
        tablero[x][y] = 0
        return

    if es_valida(tablero, x, y):
        tablero[x][y] = paso
        resolver_todas(tablero, x + 1, y, soluciones, paso + 1)
        resolver_todas(tablero, x, y + 1, soluciones, paso + 1)
        resolver_todas(tablero, x - 1, y, soluciones, paso + 1)
        resolver_todas(tablero, x, y - 1, soluciones, paso + 1)
        tablero[x][y] = 0

n = int(input("Ingrese tamaño del laberinto (n x n): "))
tablero = [[0 for _ in range(n)] for _ in range(n)]
soluciones = []
resolver_todas(tablero, 0, 0, soluciones, 1)

with open("soluciones_numeradas.txt", "w") as f:
    for i, sol in enumerate(soluciones, start=1):
        f.write(f"Solución #{i}\n")
        f.write(mostrar_tablero(sol))
        f.write("\n" + "-" * 30 + "\n")

print(f"Se encontraron {len(soluciones)} soluciones y se guardaron en 'soluciones_numeradas.txt'")
