import random

def generar_laberinto_sucesivo_3x3():
    """
    Genera un laberinto numérico 3x3:
    - Comienza con 1 en la esquina superior izquierda.
    - Cada número sucesor (2..9) está en una celda adyacente al anterior.
    - No se repiten números.
    """
    # Tablero vacío
    laberinto = [[0 for _ in range(3)] for _ in range(3)]
    laberinto[0][0] = 1  # inicio fijo
    
    # Posición inicial
    x, y = 0, 0

    # Direcciones posibles (abajo, arriba, derecha, izquierda)
    direcciones = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for num in range(2, 10):
        posibles = []
        # Buscar posiciones adyacentes vacías
        for dx, dy in direcciones:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3 and laberinto[nx][ny] == 0:
                posibles.append((nx, ny))
        
        # Si no hay espacio, se reinicia (para evitar bloqueos)
        if not posibles:
            return generar_laberinto_sucesivo_3x3()
        
        # Escoge aleatoriamente una celda adyacente
        x, y = random.choice(posibles)
        laberinto[x][y] = num

    return laberinto


def mostrar_laberinto(laberinto):
    print("\nLaberinto numérico 3x3 (1–9 sucesivos y adyacentes):")
    for fila in laberinto:
        print(" | ".join(f"{n:2}" for n in fila))
    print()


# Ejemplo de uso
laberinto = generar_laberinto_sucesivo_3x3()
mostrar_laberinto(laberinto)