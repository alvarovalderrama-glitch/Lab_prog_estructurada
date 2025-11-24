# LABERINTO - BACKTRACKING - UNA SOLUCIÓN
# 0 = camino libre, 1 = pared
# Se busca un camino desde (0, 0) hasta (n-1, n-1)

def imprimir_laberinto(lab):
    for fila in lab:
        print(" ".join(str(x) for x in fila))
    print()


def es_valido(lab, fila, col):
    n = len(lab)
    # Dentro de los límites y no es pared
    return 0 <= fila < n and 0 <= col < n and lab[fila][col] == 0


def resolver_una_solucion(lab, fila, col, solucion):
    n = len(lab)

    # Caso base: llegamos a la meta
    if fila == n - 1 and col == n - 1 and lab[fila][col] == 0:
        solucion[fila][col] = 1
        return True

    if es_valido(lab, fila, col) and solucion[fila][col] == 0:
        # Marcamos esta casilla como parte del camino
        solucion[fila][col] = 1

        # Movimientos: abajo, derecha, arriba, izquierda
        movimientos = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for df, dc in movimientos:
            nueva_fila = fila + df
            nueva_col = col + dc

            if resolver_una_solucion(lab, nueva_fila, nueva_col, solucion):
                return True

        # Si ninguno de los caminos desde aquí funciona, desmarcamos (backtracking)
        solucion[fila][col] = 0

    return False


# ----------------- EJEMPLO DE USO -----------------

if __name__ == "__main__":
    laberinto = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]

    n = len(laberinto)
    solucion = [[0 for _ in range(n)] for _ in range(n)]

    print("Laberinto:")
    imprimir_laberinto(laberinto)

    if resolver_una_solucion(laberinto, 0, 0, solucion):
        print("Camino encontrado (1 = camino):")
        imprimir_laberinto(solucion)
    else:
        print("No existe camino desde el inicio hasta la meta.")
