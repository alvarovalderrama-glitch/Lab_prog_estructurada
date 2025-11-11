
N = 5

mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

soluciones = []

def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

def resolver_todo(tablero, x, y, paso):
    if paso == N * N:
        soluciones.append([fila[:] for fila in tablero])
        return

    for i in range(8):
        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valido(nx, ny, tablero):
            tablero[nx][ny] = paso
            resolver_todo(tablero, nx, ny, paso + 1)
            tablero[nx][ny] = -1

tablero = [[-1 for _ in range(N)] for _ in range(N)]
tablero[0][0] = 0

resolver_todo(tablero, 0, 0, 1)

print("Total soluciones:", len(soluciones))
for sol in soluciones:
    for fila in sol:
        print(fila)
    print()
