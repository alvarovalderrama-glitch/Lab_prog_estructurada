def encontrar_inicio(laberinto):
    """Busca y retorna las coordenadas (fila, columna) de 'S'."""
    for r in range(len(laberinto)):
        for c in range(len(laberinto[0])):
            if laberinto[r][c] == 'S':
                return r, c
    return None

def resolver_laberinto_una_solucion(laberinto_mutable, inicio):
    
    def buscar_camino(fila, columna, camino_actual):
        # 1. Verificar límites y si es una pared ('#') o ya visitada ('*')
        # La condición de límite debe ser la primera para evitar errores de índice.
        if (fila < 0 or fila >= len(laberinto_mutable) or
            columna < 0 or columna >= len(laberinto_mutable[0])):
            return None # Fuera de límites

        celda_actual = laberinto_mutable[fila][columna]
        
        if celda_actual == '#' or celda_actual == '*':
            return None # Movimiento inválido (Pared o ya visitada)
        
        # 2. Verificar si es la SALIDA ('E')
        if celda_actual == 'E':
            # ¡Encontramos la salida! 
            return camino_actual + [(fila, columna)]

        # 3. Marcar la celda actual como visitada
        # No marcamos 'S' para que sepamos dónde empezó.
        if celda_actual != 'S':
            laberinto_mutable[fila][columna] = '*'
        
        # Guardamos la posición actual en el camino
        nuevo_camino = camino_actual + [(fila, columna)]

        # 4. Intentar moverse en las 4 direcciones
        movimientos = [
            (0, 1),   # Derecha
            (0, -1),  # Izquierda
            (1, 0),   # Abajo
            (-1, 0)   # Arriba
        ]
        
        for dr, dc in movimientos:
            # Intenta moverse a la nueva posición
            resultado = buscar_camino(fila + dr, columna + dc, nuevo_camino)
            
            # Si el resultado no es None, significa que encontramos la solución
            if resultado is not None:
                return resultado
                
        # 5. Backtracking (Deshacer marca si es necesario, aunque aquí retornamos None)
        # Esto es solo importante si queremos que la celda pueda ser usada por OTROS caminos
        # después de un fallo, pero como este algoritmo solo busca UNA, no es estrictamente necesario,
        # pero es buena práctica de DFS. Lo mantendremos marcado como '*' para eficiencia.
        
        return None # No hay ruta desde esta celda

    # Obtener las coordenadas de inicio
    fila_inicio, columna_inicio = inicio
    
    # Llamar a la función recursiva
    return buscar_camino(fila_inicio, columna_inicio, camino_actual=[])


# --- Ejemplo de Uso ---

# Un laberinto de ejemplo 
LABERINTO_ORIGINAL = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['S', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', 'E'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

# Función para imprimir la ruta en el laberinto
def imprimir_laberinto_con_solucion(lab, ruta):
    # Clonar el laberinto original para la impresión
    temp_lab = [list(fila) for fila in lab]
    
    # Marcar la ruta con '.'
    for r, c in ruta:
        if temp_lab[r][c] != 'S' and temp_lab[r][c] != 'E':
            temp_lab[r][c] = '.'
    
    # Imprimir
    for fila in temp_lab:
        print(' '.join(fila))


# 1. Encontrar el punto de inicio
inicio_coords = encontrar_inicio(LABERINTO_ORIGINAL)

if inicio_coords:
    # 2. Clonar el laberinto justo antes de resolverlo
    # Esto asegura que la función recursiva trabaja con una copia desechable.
    laberinto_para_resolver = [list(fila) for fila in LABERINTO_ORIGINAL]
    
    # 3. Resolver
    solucion = resolver_laberinto_una_solucion(laberinto_para_resolver, inicio_coords)

    print("=== Laberinto: Encontrar UNA Solución (Corregido) ===")

    if solucion:
        print("\n¡Solución Encontrada!")
        print(f"Longitud del camino: {len(solucion)}")
        print("\nRepresentación visual de la ruta ('.' es el camino):")
        # Usamos el laberinto ORIGINAL para la impresión
        imprimir_laberinto_con_solucion(LABERINTO_ORIGINAL, solucion)
    else:
        print("\nNo se encontró ninguna solución para este laberinto.")
else:
    print("Error: No se encontró el punto de inicio ('S') en el laberinto.")