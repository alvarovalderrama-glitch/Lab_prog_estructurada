def encontrar_inicio(laberinto):
    """Busca y retorna las coordenadas (fila, columna) de 'S' (Inicio)."""
    for r in range(len(laberinto)):
        for c in range(len(laberinto[0])):
            if laberinto[r][c] == 'S':
                return r, c
    return None

def resolver_laberinto_todas_soluciones(laberinto, inicio):

    # Lista para almacenar todas las soluciones encontradas
    soluciones_encontradas = [] 
    
    # Clonamos el laberinto para permitir el marcado y el backtracking sin 
    # modificar la estructura original para las búsquedas posteriores.
    laberinto_mutable = [list(fila) for fila in laberinto]

    def buscar_camino(fila, columna, camino_actual):
        nonlocal soluciones_encontradas

        # 1. Chequeos de límite, pared ('#') y celda visitada ('*')
        if (fila < 0 or fila >= len(laberinto_mutable) or
            columna < 0 or columna >= len(laberinto_mutable[0]) or
            laberinto_mutable[fila][columna] == '#' or
            laberinto_mutable[fila][columna] == '*'):
            return 
        
        # 2. Verificar si es la SALIDA ('E')
        if laberinto_mutable[fila][columna] == 'E':
            # ¡Solución encontrada! Guardamos la ruta y hacemos backtracking
            # para seguir buscando otros caminos.
            solucion_completa = camino_actual + [(fila, columna)]
            soluciones_encontradas.append(solucion_completa)
            return 
        
        # 3. Marcar la celda actual como visitada si no es 'S'
        original_char = laberinto_mutable[fila][columna]
        if original_char != 'S':
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
            # Llamada recursiva
            buscar_camino(fila + dr, columna + dc, nuevo_camino)

        # 5. Deshacer la marca (Backtracking)
        # Esto es crucial: restablece el estado de la celda para que otros caminos
        # la puedan considerar como una celda libre (' ') en el futuro.
        if original_char != 'S':
            laberinto_mutable[fila][columna] = original_char

    # Obtener las coordenadas de inicio
    fila_inicio, columna_inicio = inicio
    
    # Iniciar la búsqueda
    buscar_camino(fila_inicio, columna_inicio, camino_actual=[])
    
    return soluciones_encontradas


# --- Ejemplo de Uso ---

# NOTA: Este laberinto tiene múltiples rutas cortas, lo que es ideal para DFS.
LABERINTO_EJEMPLO = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['S', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', 'E'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#']
]

# Función auxiliar para imprimir las soluciones
def imprimir_laberinto_con_solucion(lab, ruta):
    temp_lab = [list(fila) for fila in lab]
    
    for r, c in ruta:
        if temp_lab[r][c] != 'S' and temp_lab[r][c] != 'E':
            temp_lab[r][c] = '.'
    
    for fila in temp_lab:
        print(' '.join(fila))

# 1. Encontrar el punto de inicio
inicio_coords = encontrar_inicio(LABERINTO_EJEMPLO)

if inicio_coords:
    # 2. Resolver (sin límite)
    print("Iniciando búsqueda de todas las soluciones...")
    soluciones = resolver_laberinto_todas_soluciones(LABERINTO_EJEMPLO, inicio_coords)

    print("\n=== Laberinto: Todas las Soluciones Posibles ===")

    if soluciones:
        print(f"\n ¡Búsqueda Finalizada! Se encontraron un total de **{len(soluciones)}** soluciones.")
        
        # Mostramos las primeras 3 soluciones para mantener la salida concisa, 
        # pero la lista `soluciones` contiene todas.
        num_a_mostrar = min(3, len(soluciones))
        print(f"Mostrando las primeras {num_a_mostrar} (de {len(soluciones)} encontradas):")
        
        # Opcionalmente, puedes ordenar las soluciones por longitud para ver las más cortas primero
        soluciones.sort(key=len) 
        
        for i, sol in enumerate(soluciones[:num_a_mostrar]):
            print(f"\n--- Solución {i+1} (Longitud: {len(sol)}) ---")
            print("Ruta de coordenadas:", sol)
            imprimir_laberinto_con_solucion(LABERINTO_EJEMPLO, sol)
            
    else:
        print("\n No se encontró ninguna solución para este laberinto.")
else:
    print("Error: No se encontró el punto de inicio ('S') en el laberinto.")