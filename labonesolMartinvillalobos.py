
# LABERINTO 5x5 (0 = libre, 1 = pared)
laberinto = [
    [0, 0, 1, 0, 0],  
    [0, 0, 1, 0, 0],  
    [0, 1, 0, 0, 0],  
    [0, 0, 0, 1, 0],  
    [1, 0, 0, 0, 0]
]

N = 5

# Movimientos: arriba, abajo, izquierda, derecha
mov_x = [-1, 1, 0, 0]
mov_y = [0, 0, -1, 1]

def es_valido(x, y, lab, visitado):
    return (
        0 <= x < N and
        0 <= y < N and
        lab[x][y] == 0 and
        not visitado[x][y]
    )

def resolver(lab, x, y, fin_x, fin_y, visitado, camino):
    if x == fin_x and y == fin_y:
        camino.append((x, y))
        return True

    visitado[x][y] = True
    camino.append((x, y))

    for i in range(4):
        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valido(nx, ny, lab, visitado):
            if resolver(lab, nx, ny, fin_x, fin_y, visitado, camino):
                return True

    camino.pop()
    return False

visitado = [[False]*N for _ in range(N)]
camino = []

if resolver(laberinto, 0, 0, 0, 4, visitado, camino):
    print("Camino encontrado:")
    print(camino)
else:
    print("No existe solución.")