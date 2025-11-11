def encontrar_una_solucion(maze):
    # Dimensiones del laberinto
    filas, columnas = len(maze), len(maze[0])
    camino = []  # Almacenará el camino encontrado

    def backtrack(x,y):
        if x < 0 or x >= filas or y < 0 or y >= columnas or maze [x][y] == 0:
            return False
        if (x,y) in camino:
            return False
        
        # Agregar posición actual al camino
        camino.append((x, y))
        # Verificar si llegamos al destino
        if (x, y) == (filas - 1, columnas - 1):
            return True
        # Explorar las 4 dirrecciones posibles
        if (backtrack(x + 1, y)or  # Abajo
        backtrack(x - 1, y)or   # Arriba
        backtrack(x, y + 1)or   # Derecha
        backtrack(x, y -1)):    # Izquerda
            return True
        # backtrack: si ninguna posición funcionó, remover esta posición del camino
        camino.pop()
        return False
    # Ejecutaar algoritmo desde la posición inicial (0,0)
    if backtrack(0, 0):
        return camino   # Retornar al camino si se encontró solución
    else:
        return None     # Retornar None si no hay solución
    
def mostrar_laberinto(maze, camino=None):
    # Muestra el laberinto de forma visual
    filas, columnas = len(maze), len(maze[0])
    # Crear una copia del laberinto para no modificar el original
    laberinto_visual = [fila[:] for fila in maze]

    # Si no hay camino, marcarlo en el laberinto visual
    if camino:
        for x, y in camino:
             laberinto_visual[x][y] = 2     # 2 representa el camino

    # Imprimir el laberinto con símbolos visuales
    print("Laberinto:")
    print(" # = pared, . = camino libre, * = ruta solución")
    print()

    for i in range(filas):
        for j in range(columnas):
            if laberinto_visual[i][j] == 0:
                print('#', end = " ")   # Pared
            elif laberinto_visual[i][j] == 1:
                print(".", end = " ")   # Camino libre
            elif laberinto_visual[i][j] == 2:
                print("*", end = " ")   # Ruta de solución
        print()     # Nueva línea después de cada fila

# Ejemplo de uso
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1]
]

# Mostrar laberinto original
mostrar_laberinto(laberinto)

# Econtrar solución 
solucion = encontrar_una_solucion(laberinto)

if solucion:
    print("\n ¡Solución encontrada!")
    print("Coordenadas del camino:", solucion)
    print("\n leberinto con solucón:")
    mostrar_laberinto(laberinto, solucion)
else:
    print("\n No se encontró solución para este labeerinto.")
    