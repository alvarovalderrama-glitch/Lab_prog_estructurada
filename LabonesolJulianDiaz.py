import random

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(c) for c in fila))
    print()

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

# -------------------------------
# GENERAR TABLERO CON OBSTÁCULOS
# -------------------------------
n = int(input("Ingrese tamaño del laberinto (n x n): "))
tablero = [[0 for _ in range(n)] for _ in range(n)]

porcentaje = 0.3  # 30% de obstáculos

for i in range(n):
    for j in range(n):
        if random.random() < porcentaje:
            tablero[i][j] = -1

# asegurar inicio y fin libres
tablero[0][0] = 0
tablero[n-1][n-1] = 0

soluciones = []
resolver_todas(tablero, 0, 0, soluciones, 1)

if soluciones:
    sol_aleatoria = random.choice(soluciones)
    print("Solución aleatoria encontrada:")
    mostrar_tablero(sol_aleatoria)
else:
    print("Este laberinto NO tiene solución.")
