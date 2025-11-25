
def resolver_cuadrado_magico_principal(N=3):
    """
    Inicializa el tablero y variables, y comienza el proceso de Backtracking.
    """
    if N < 3:
        print("El orden debe ser al menos 3 para un cuadrado mágico estándar.")
        return

    # 1. CONSTANTES Y VARIABLES
    S = N * (N**2 + 1) // 2  # Constante Mágica (ej. N=3 -> S=15)
    cuadrado = [[0] * N for _ in range(N)]
    usado = [False] * (N**2 + 1) # Índice 0 ignorado, números del 1 al N*N

    print(f"Buscando un Cuadrado Mágico de orden {N} (Suma Mágica S={S})...")

    # 2. LLAMADA A LA FUNCIÓN RECURSIVA
    if backtracking_recursivo(N, S, cuadrado, usado, 0, 0):
        print("\n✨ ¡Cuadrado Mágico Encontrado! ✨")
        mostrar_cuadrado(cuadrado)
    else:
        print("\nNo se encontró una solución (esto no debería pasar para N=3).")

# --- Funciones Auxiliares ---

def mostrar_cuadrado(cuadrado):
    """Muestra la matriz de forma legible."""
    for fila in cuadrado:
        print(" ".join(f"{num:2}" for num in fila))

def verificar_suma(linea, S):
    """Verifica si la suma de una línea (fila/columna/diagonal) es S."""
    return sum(linea) == S

def obtener_linea(cuadrado, tipo, indice):
    """Obtiene una fila, columna o diagonal específica."""
    N = len(cuadrado)
    if tipo == 'fila':
        return cuadrado[indice]
    elif tipo == 'columna':
        return [cuadrado[i][indice] for i in range(N)]
    elif tipo == 'diag_principal': # (0,0), (1,1), ...
        return [cuadrado[i][i] for i in range(N)]
    elif tipo == 'diag_secundaria': # (0, N-1), ..., (N-1, 0)
        return [cuadrado[i][N - 1 - i] for i in range(N)]
    return []

# --- Función de Poda/Restricción ---

def es_valido(N, S, cuadrado, fila, columna):
    """
    Verifica las restricciones (sumas completas) en el punto de colocación.
    Se asume que el número ya fue colocado y que la unicidad ya se verificó.
    """
    
    # 1. VERIFICACIÓN DE FILA COMPLETA
    if columna == N - 1:
        if not verificar_suma(cuadrado[fila], S):
            return False

    # 2. VERIFICACIÓN DE COLUMNA COMPLETA
    if fila == N - 1:
        columna_actual = obtener_linea(cuadrado, 'columna', columna)
        if not verificar_suma(columna_actual, S):
            return False

    # 3. VERIFICACIÓN DE DIAGONALES COMPLETAS

    # Diagonal Principal: Celda (i, i) y es la última celda (N-1, N-1)
    if fila == columna and fila == N - 1:
        diag_p = obtener_linea(cuadrado, 'diag_principal', 0)
        if not verificar_suma(diag_p, S):
            return False
            
    # Diagonal Secundaria: Celda (i, N-1-i) y es la última celda (N-1, 0)
    if fila + columna == N - 1 and fila == N - 1:
        diag_s = obtener_linea(cuadrado, 'diag_secundaria', 0)
        if not verificar_suma(diag_s, S):
            return False

    return True

# --- Función de Backtracking Recursivo ---

def backtracking_recursivo(N, S, cuadrado, usado, fila, columna):
    """
    Función recursiva que intenta llenar el cuadrado.
    Retorna True si encuentra una solución, False si necesita hacer Backtrack.
    """
    # 1. CASO BASE (ÉXITO)
    # Si la fila es N, significa que terminamos de llenar la última celda (N-1, N-1)
    if fila == N:
        return True

    # 2. CÁLCULO DE LA SIGUIENTE POSICIÓN
    # Avanzar a la siguiente celda
    siguiente_fila = fila
    siguiente_columna = columna + 1

    # Si se terminó la fila, pasar a la siguiente
    if siguiente_columna == N:
        siguiente_columna = 0
        siguiente_fila = fila + 1

    # 3. EXPLORACIÓN (Iterar sobre números del 1 al N*N)
    for num in range(1, N**2 + 1):
        
        # A. UNICIDAD (Revisión/Poda temprana)
        if not usado[num]:
            
            # B. HACER ELECCIÓN
            cuadrado[fila][columna] = num
            usado[num] = True

            # C. VERIFICAR RESTRICCIONES (Poda)
            if es_valido(N, S, cuadrado, fila, columna):
                
                # D. LLAMADA RECURSIVA (Avanzar)
                if backtracking_recursivo(N, S, cuadrado, usado, siguiente_fila, siguiente_columna):
                    return True # Solución encontrada en esta rama

            # E. BACKTRACK (Vuelta Atrás)
            # Si la rama falló (invalidación o recursión negativa), deshacer la elección
            usado[num] = False
            cuadrado[fila][columna] = 0

    # Si el bucle termina sin éxito, no hay número válido para (fila, columna)
    return False

# --- Ejecución del Programa ---
resolver_cuadrado_magico_principal(N=3)