# Definimos el tamaño del tablero y el límite de soluciones
TAMANO_TABLERO = 8
LIMITE_A_ENCONTRAR = 3  # <-- ¡CAMBIO REALIZADO!

# Variable global para contar las soluciones encontradas
contador_de_soluciones = 0

# --- Funciones Auxiliares ---

def inicializar_tablero():
    """Crea un tablero vacío (con -1 en todas las casillas)."""
    return [[-1 for _ in range(TAMANO_TABLERO)] for _ in range(TAMANO_TABLERO)]

def imprimir_tablero_simple(tablero):
    """Muestra el tablero de la solución encontrada."""
    print(f"--- Solución #{contador_de_soluciones} ---")
    for fila in tablero:
        for casilla in fila:
            print(f"{casilla:2d}", end=" ")
        print()
    print("----------------------------\n")

def es_movimiento_seguro(x, y, tablero):
    """Verifica si la casilla (x, y) está DENTRO del tablero y NO ha sido visitada."""
    return (0 <= x < TAMANO_TABLERO and
            0 <= y < TAMANO_TABLERO and
            tablero[x][y] == -1)

# --- Algoritmo Principal (Backtracking) ---

def encontrar_recorrido_con_limite(x, y, contador_mov, tablero, mov_x, mov_y):
    """
    Función recursiva (backtracking) que busca soluciones
    hasta encontrar el LIMITE.
    """
    global contador_de_soluciones 
    
    # Si ya encontramos las 3, dejamos de buscar en esta rama
    if contador_de_soluciones >= LIMITE_A_ENCONTRAR:
        return

    # Marcar la casilla actual
    tablero[x][y] = contador_mov

    # Caso Base (Éxito): Se completó el tablero
    if contador_mov == (TAMANO_TABLERO * TAMANO_TABLERO) - 1:
        contador_de_soluciones += 1
        imprimir_tablero_simple(tablero)
        
        # Deshacer el movimiento para que la búsqueda pueda continuar
        tablero[x][y] = -1
        return 

    # Paso Recursivo: Probar los 8 movimientos
    for i in range(8):
        
        # Si encontramos las 3 mientras probábamos, paramos el bucle
        if contador_de_soluciones >= LIMITE_A_ENCONTRAR:
            break 

        x_siguiente = x + mov_x[i]
        y_siguiente = y + mov_y[i]

        # Verificar si el movimiento es válido
        if es_movimiento_seguro(x_siguiente, y_siguiente, tablero):
            # Llamada recursiva (probar este camino)
            encontrar_recorrido_con_limite(x_siguiente, y_siguiente, contador_mov + 1, tablero, mov_x, mov_y)

    # Backtracking: Si no hay más movimientos, deshacer el paso
    tablero[x][y] = -1

# --- Función de Inicio ---

def resolver_recorridos_limitados_del_caballo():
    """Prepara todo y comienza la búsqueda de las primeras N soluciones."""
    
    tablero = inicializar_tablero()

    # Movimientos posibles del caballo
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]

    pos_inicial_x = 0
    pos_inicial_y = 0

    print(f"Buscando las primeras {LIMITE_A_ENCONTRAR} soluciones para un tablero {TAMANO_TABLERO}x{TAMANO_TABLERO}...")
    
    encontrar_recorrido_con_limite(pos_inicial_x, pos_inicial_y, 0, tablero, mov_x, mov_y)

    print("\n--- Búsqueda Terminada ---")
    if contador_de_soluciones == LIMITE_A_ENCONTRAR:
        print(f"Se encontraron las primeras {contador_de_soluciones} soluciones.")
    else:
        print(f"Se terminó la búsqueda. Se encontraron solo {contador_de_soluciones} soluciones.")

# --- Ejecutar el programa ---
if __name__ == "__main__":
    resolver_recorridos_limitados_del_caballo()
