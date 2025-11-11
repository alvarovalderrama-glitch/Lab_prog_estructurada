# Laberinto: 1 = libre, 0 = pared
laberinto = [
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 1]
]

n = len(laberinto)
m = len(laberinto[0])

def mostrar(sol):
    for fila in sol:
        print(' '.join(str(x) for x in fila))
    print()

def es_valida(r, c, sol):
    return 0 <= r < n and 0 <= c < m and laberinto[r][c] == 1 and sol[r][c] == 0

# contador global para soluciones
contador = 0

def encontrar_todas(r, c, sol):
    global contador

    # si llegamos a la meta
    if r == n - 1 and c == m - 1:
        sol[r][c] = 1
        contador += 1
        print(f"Solución #{contador}:")
        mostrar(sol)
        sol[r][c] = 0
        return

    if es_valida(r, c, sol):
        sol[r][c] = 1  # marcamos como visitado

        # intentar en 4 direcciones (derecha, abajo, izquierda, arriba)
        encontrar_todas(r, c + 1, sol)
        encontrar_todas(r + 1, c, sol)
        encontrar_todas(r, c - 1, sol)
        encontrar_todas(r - 1, c, sol)

        # desmarcamos al retroceder para permitir otras rutas
        sol[r][c] = 0

# comprobaciones
if laberinto[0][0] == 0:
    print("La entrada (0,0) está bloqueada. No hay soluciones.")
elif laberinto[n-1][m-1] == 0:
    print("La salida está bloqueada. No hay soluciones.")
else:
    solucion = [[0]*m for _ in range(n)]
    encontrar_todas(0, 0, solucion)
    if contador == 0:
        print("No se encontró ninguna solución.")
    else:
        print(f"Total de soluciones encontradas: {contador}")
