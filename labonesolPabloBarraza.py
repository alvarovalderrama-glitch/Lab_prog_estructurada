# Laberinto: 1 = libre, 0 = pared
laberinto = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

# filas (n) y columnas (m) - funciona aunque no sea cuadrado
n = len(laberinto)
m = len(laberinto[0])

# imprimimos la solución de forma clara
def mostrar(sol):
    for fila in sol:
        print(' '.join(str(x) for x in fila))
    print()

# verifica si la celda (r,c) es válida (dentro, camino y no visitada en sol)
def es_valida(r, c, sol):
    return 0 <= r < n and 0 <= c < m and laberinto[r][c] == 1 and sol[r][c] == 0

# backtracking que encuentra una solución y para cuando la encuentra
def encontrar_una(r, c, sol):
    # si la posición actual es la meta
    if r == n - 1 and c == m - 1:
        sol[r][c] = 1
        mostrar(sol)
        return True

    if es_valida(r, c, sol):
        sol[r][c] = 1  # marcamos como parte del camino

        # intentar derecha
        if encontrar_una(r, c + 1, sol):
            return True
        # intentar abajo
        if encontrar_una(r + 1, c, sol):
            return True
        # intentar izquierda
        if encontrar_una(r, c - 1, sol):
            return True
        # intentar arriba
        if encontrar_una(r - 1, c, sol):
            return True

        # retroceder (desmarcar)
        sol[r][c] = 0
    return False

# comprobaciones antes de llamar
if laberinto[0][0] == 0:
    print("La entrada (0,0) está bloqueada. No hay solución.")
elif laberinto[n-1][m-1] == 0:
    print("La salida está bloqueada. No hay solución.")
else:
    # matriz para marcar la solución (0 = no visitado, 1 = camino)
    sol = [[0]*m for _ in range(n)]
    if not encontrar_una(0, 0, sol):
        print("No existe ninguna solución.")

