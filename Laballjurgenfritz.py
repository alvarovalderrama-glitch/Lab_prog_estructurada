def generar_todas_sucesiones_3x3():
    """
    Encuentra todas las posibles soluciones del laberinto numérico 3x3:
    - Empieza con 1 en la esquina superior izquierda.
    - Cada número siguiente está en una celda adyacente al anterior.
    - No se repiten celdas.
    """
    N = 3
    tablero = [[0 for _ in range(N)] for _ in range(N)]
    soluciones = []

    # Movimientos posibles: derecha, izquierda, abajo, arriba
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def backtrack(x, y, num):
        # Colocar el número actual
        tablero[x][y] = num

        # Si llegamos al 9, guardamos la solución
        if num == 9:
            soluciones.append([fila[:] for fila in tablero])
            tablero[x][y] = 0
            return

        # Probar todos los movimientos posibles
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and tablero[nx][ny] == 0:
                backtrack(nx, ny, num + 1)

        # Retroceder
        tablero[x][y] = 0

    # Iniciar desde la esquina superior izquierda
    backtrack(0, 0, 1)
    return soluciones


def mostrar_laberinto(laberinto):
    for fila in laberinto:
        print(" | ".join(f"{n:2}" for n in fila))
    print()


# Ejecución
soluciones = generar_todas_sucesiones_3x3()
print(f"\nTotal de soluciones encontradas: {len(soluciones)}\n")

# Mostrar las primeras 5 soluciones como ejemplo
for i, sol in enumerate(soluciones[:5], 1):
    print(f"Solución #{i}:")
    mostrar_laberinto(sol)
