N = 8  # tamaño del tablero

# Movimientos posibles del caballo
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]

def es_valido(x, y, tablero):
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1

def solucion_caballo(tablero, x, y, mov):
    if mov == N*N:
        return True  # si llenó el tablero

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if es_valido(nx, ny, tablero):
            tablero[nx][ny] = mov
            if solucion_caballo(tablero, nx, ny, mov + 1):
                return True
            # backtracking
            tablero[nx][ny] = -1
    return False

def main():
    tablero = [[-1 for _ in range(N)] for _ in range(N)]
    # Posición inicial del caballo
    tablero[0][0] = 0

    if solucion_caballo(tablero, 0, 0, 1):
        for fila in tablero:
            print(' '.join(f'{c:2}' for c in fila))
    else:
        print("No se encontró solución.")

if __name__ == "__main__":
    main()
