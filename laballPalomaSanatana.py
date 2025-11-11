def encontrar_todas_soluciones(maze):
    # Dimensiones del laberinto
    filas, columnas = len(maze), len(maze[0])
    soluciones = []  # Almacenará todas las soluciones encontradas
    camino_actual = []  # Almacenará el camino actual durante la exploración

    def backtrack(x, y):
        # Verificar si la posición es válida
        if (x < 0 or x >= filas or y < 0 or y >= columnas or 
            maze[x][y] == 0 or (x, y) in camino_actual):
            return
        
        # Agregar posición actual al camino
        camino_actual.append((x, y))
        
        # Verificar si llegamos al destino
        if (x, y) == (filas - 1, columnas - 1):
            # Encontramos una solución, agregar copia del camino
            soluciones.append(camino_actual[:])
        else:
            # Explorar las 4 direcciones posibles en orden
            backtrack(x + 1, y)  # Abajo
            backtrack(x - 1, y)  # Arriba
            backtrack(x, y + 1)  # Derecha
            backtrack(x, y - 1)  # Izquierda
        
        # Backtrack: remover esta posición del camino actual
        camino_actual.pop()
    
    # Ejecutar algoritmo desde la posición inicial (0,0)
    backtrack(0, 0)
    return soluciones

def mostrar_laberinto(maze, camino=None):
    # Muestra el laberinto de forma visual
    filas, columnas = len(maze), len(maze[0])
    # Crear una copia del laberinto para no modificar el original
    laberinto_visual = [fila[:] for fila in maze]

    # Si se proporciona un camino, marcarlo en el laberinto visual
    if camino:
        for x, y in camino:
            laberinto_visual[x][y] = 2  # 2 representa el camino

    # Imprimir el laberinto con símbolos visuales
    print("Laberinto:")
    print("# = pared, . = camino libre, * = ruta solucion")
    print()

    for i in range(filas):
        for j in range(columnas):
            if laberinto_visual[i][j] == 0:
                print('#', end=" ")  # Pared
            elif laberinto_visual[i][j] == 1:
                print(".", end=" ")  # Camino libre
            elif laberinto_visual[i][j] == 2:
                print("*", end=" ")  # Ruta de solucion
        print()  # Nueva línea después de cada fila

def mostrar_todas_soluciones(maze, soluciones):
    # Muestra cada solución individualmente
    for i, solucion in enumerate(soluciones, 1):
        print(f"\n--- Solucion {i} ---")
        print(f"Longitud del camino: {len(solucion)} pasos")
        print(f"Coordenadas: {solucion}")
        mostrar_laberinto(maze, solucion)

# Ejemplo de uso
laberinto = [
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 0, 1, 1]
]

# Mostrar laberinto original
print("Laberinto original:")
mostrar_laberinto(laberinto)

# Encontrar todas las soluciones
todas_soluciones = encontrar_todas_soluciones(laberinto)

if todas_soluciones:
    print(f"\nSe encontraron {len(todas_soluciones)} soluciones:")
    mostrar_todas_soluciones(laberinto, todas_soluciones)
    
    # Mostrar estadísticas
    longitudes = [len(sol) for sol in todas_soluciones]
    print(f"\n--- Estadisticas ---")
    print(f"Solucion mas corta: {min(longitudes)} pasos")
    print(f"Solucion mas larga: {max(longitudes)} pasos")
    print(f"Longitud promedio: {sum(longitudes)/len(longitudes):.1f} pasos")
else:
    print("\nNo se encontraron soluciones para este laberinto.")