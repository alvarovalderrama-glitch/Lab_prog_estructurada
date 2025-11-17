# Definimos el tamaño del tablero
TAMANO_TABLERO = 8

# Funciones Auxiliares 

def inicializar_tablero():
    "Crea un tablero vacío (con -1 en todas las casillas)."
    # Crea una lista de listas (matriz) llena de -1
    return [[-1 for _ in range(TAMANO_TABLERO)] for _ in range(TAMANO_TABLERO)]

def imprimir_tablero_final(tablero):
    """Muestra el tablero final de la única solución encontrada."""
    print(f"Solución encontrada para un tablero de {TAMANO_TABLERO}x{TAMANO_TABLERO}:")
    # Itera por cada fila
    for fila in tablero:
        # Itera por cada casilla en esa fila
        for casilla in fila:
            # Imprime el número con formato (2 dígitos) y un espacio
            print(f"{casilla:2d}", end=" ")
        # Imprime un salto de línea al final de la fila
        print()

def es_movimiento_seguro(x, y, tablero):
    """Verifica si la casilla (x, y) está DENTRO del tablero y NO ha sido visitada."""
    # Comprueba que X esté entre 0 y 7
    return (0 <= x < TAMANO_TABLERO and
            # Comprueba que Y esté entre 0 y 7
            0 <= y < TAMANO_TABLERO and
            # Comprueba que la casilla esté marcada como no visitada (-1)
            tablero[x][y] == -1)

# --- Algoritmo Principal (Backtracking) ---

def encontrar_recorrido_una_sol(x, y, contador_mov, tablero, mov_x, mov_y):
    """
    Función recursiva que busca UNA solución y para.
    Devuelve True si encuentra solución, False si no.
    """
    # Paso 1: Marcar la casilla actual con el número de movimiento
    tablero[x][y] = contador_mov

    # Paso 2: Caso Base (Éxito)
    # Si el contador llegó a 63 (para 8x8), significa que llenamos el tablero
    if contador_mov == (TAMANO_TABLERO * TAMANO_TABLERO) - 1:
        return True  # ¡Solución encontrada!

    # Paso 3: Paso Recursivo (Probar los 8 movimientos)
    for i in range(8):
        # Calcular la coordenada del próximo movimiento
        x_siguiente = x + mov_x[i]
        y_siguiente = y + mov_y[i]

        # Paso 4: Verificar si el movimiento es válido
        if es_movimiento_seguro(x_siguiente, y_siguiente, tablero):
            
            # Paso 5: Llamada recursiva (probar este camino)
            # Si la llamada recursiva devuelve True, es que encontró la solución
            if encontrar_recorrido_una_sol(x_siguiente, y_siguiente, contador_mov + 1, tablero, mov_x, mov_y):
                # Si la encontró, pasamos el True hacia arriba para detener todo
                return True

    # Paso 6: Backtracking (Vuelta Atrás)
    # Si el bucle 'for' termina, es que no hubo movimientos válidos desde aquí
    # Deshacemos el movimiento (marcamos como -1)
    tablero[x][y] = -1
    # Devolvemos False para indicar que este camino falló
    return False 

# Función de Inicio 

def resolver_recorrido_del_caballo():
    # Prepara todo y comienza la búsqueda de UNA solución.
    
    # Crea el tablero vacío
    tablero = inicializar_tablero()

    # Define los 8 movimientos posibles del caballo (coordenadas X e Y)
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Definimos la posición inicial (esquina 0, 0)
    pos_inicial_x = 0
    pos_inicial_y = 0

    print(f"Buscando UNA solución para un tablero de {TAMANO_TABLERO}x{TAMANO_TABLERO}...")

    # Llama a la función principal
    if encontrar_recorrido_una_sol(pos_inicial_x, pos_inicial_y, 0, tablero, mov_x, mov_y):
        # Si devolvió True, imprimimos el tablero resultante
        imprimir_tablero_final(tablero)
    else:
        # Si devolvió False, no hay solución desde (0,0)
        print("No se encontró ninguna solución.")

# --- Ejecutar el programa ---
if __name__ == "__main__":
    # Esta línea hace que se ejecute la función 'resolver_recorrido_del_caballo'
    resolver_recorrido_del_caballo()