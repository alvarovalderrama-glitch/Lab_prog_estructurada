
# =====================================
#  MAGIC CUBE BACKTRACKING (ITERATIVO)
# =====================================

import random

# --- Configuración Inicial ---
MAX = int(input("Ingrese la dimensión del tablero (ej: 3): "))
SUMATORIA_MAGICA = (MAX * (MAX**2 + 1)) // 2 #valor de la sumatoria
print(f"cuadrado mágico de {MAX}x{MAX}. La suma debe ser: {SUMATORIA_MAGICA}")

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]

# -------- FUNCIÓN MOSTRAR TABLERO --------
def mostrar_tablero(tablero):
    print("\n" + "-" * (MAX * 6 + 1))
    for fila in tablero:
        for celda in fila:
            print(f"| {celda:4}", end=" ")
        print("|")
        print("-" * (MAX * 6 + 1))
    print("")

# -------- FUNCIÓN BUSCAR CELDAS DISPONIBLES --------
def encontrar_vacio(tablero):
    """Encuentra la próxima celda vacía (con 0) y devuelve (fila, col)"""
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return (i, j)
    return None

# -------- FUNCIÓN CONFIRMAR SOLUCIÓN --------
def es_valido_parcial(tablero):
    """Revisa si el tablero en su estado actual aún puede llegar a una solución"""

    # ---------- 1. Revisar filas ----------
    for fila in range(MAX):
        suma_fila = 0
        fila_llena = True
        for col in range(MAX):
            if tablero[fila][col] == 0:
                fila_llena = False
            suma_fila += tablero[fila][col]
        
        if fila_llena and suma_fila != SUMATORIA_MAGICA:
            return False
        if not fila_llena and suma_fila >= SUMATORIA_MAGICA:
            return False

    # ---------- 2. Revisar columnas ----------
    for col in range(MAX):
        suma_col = 0
        col_llena = True
        for fila in range(MAX):
            if tablero[fila][col] == 0:
                col_llena = False
            suma_col += tablero[fila][col]
        
        if col_llena and suma_col != SUMATORIA_MAGICA:
            return False
        if not col_llena and suma_col >= SUMATORIA_MAGICA:
            return False

    # ---------- 3. Revisar diagonal principal ----------
    suma_diag1 = 0
    diag1_llena = True
    for i in range(MAX):
        if tablero[i][i] == 0:
            diag1_llena = False
        suma_diag1 += tablero[i][i]

    if diag1_llena and suma_diag1 != SUMATORIA_MAGICA:
        return False
    if not diag1_llena and suma_diag1 >= SUMATORIA_MAGICA:
        return False

    # ---------- 4. Revisar diagonal secundaria ----------
    suma_diag2 = 0
    diag2_llena = True
    for i in range(MAX):
        if tablero[i][MAX - 1 - i] == 0:
            diag2_llena = False
        suma_diag2 += tablero[i][MAX - 1 - i]

    if diag2_llena and suma_diag2 != SUMATORIA_MAGICA:
        return False
    if not diag2_llena and suma_diag2 >= SUMATORIA_MAGICA:
        return False

    return True

# -------- FUNCIÓN VALIDAR SOLUCIÓN --------
def es_solucion_completa(tablero):
    """Revisa si un tablero lleno es un cuadrado mágico"""
    # 1. Revisar filas y columnas
    for i in range(MAX):
        if sum(tablero[i]) != SUMATORIA_MAGICA:
            return False
        if sum(tablero[j][i] for j in range(MAX)) != SUMATORIA_MAGICA:
            return False
            
    # 2. Revisar diagonales
    if sum(tablero[i][i] for i in range(MAX)) != SUMATORIA_MAGICA:
        return False
    if sum(tablero[i][MAX - 1 - i] for i in range(MAX)) != SUMATORIA_MAGICA:
        return False
        
    return True


# -------- FUNCIÓN RESOLVER MAGIC CUBE (ITERATIVO) --------
def solucion(tablero):
    # Lista de números a usar, del 1 al N^2
    numeros = list(range(1, MAX**2 + 1))
    random.shuffle(numeros) # barajamos para obtener diferentes soluciones
    
    # Usamos un 'set' para saber qué números están disponibles
    numeros_disponibles = set(numeros)
    
    # Guardará tuplas: (fila, col, indice_numero_probado)
    stack = []
    
    celda = encontrar_vacio(tablero)
    if not celda:
        return es_solucion_completa(tablero) # Ya está lleno (caso raro)

    fila, col = celda
    indice_num = 0 # Empezamos a probar desde el primer número de la lista 'numeros'

    while True:
        # --- 1. Fase de Avance (Buscar un número válido) ---
        num_encontrado = False
        for i in range(indice_num, len(numeros)):
            num = numeros[i]
            
            # Intentamos poner un número que estpé disponible
            if num in numeros_disponibles:
                tablero[fila][col] = num
                
                # Verificamos si este movimiento es prometedor
                if es_valido_parcial(tablero):
                    # ¡Movimiento válido! Guardamos el checkpoint y avanzamos.
                    stack.append((fila, col, i)) # Guardamos la celda Y el índice del número
                    numeros_disponibles.remove(num)
                    num_encontrado = True
                    
                    # Buscamos la siguiente celda vacía
                    siguiente_celda = encontrar_vacio(tablero)
                    if not siguiente_celda:
                        # ¡Tablero lleno!
                        if es_solucion_completa(tablero):
                            return True # ¡Solución encontrada!
                        else:
                            # Lleno pero incorrecto, forzamos backtracking
                            num_encontrado = False 
                            numeros_disponibles.add(num) # Devolvemos el num
                            stack.pop() # desapilamos
                            tablero[fila][col] = 0 # Limpiamos celda
                            break # Salimos del 'for i'
                    
                    # Preparamos la siguiente iteración del 'while'
                    fila, col = siguiente_celda
                    indice_num = 0 # Para la nueva celda, empezamos desde el índice 0
                    break # Salimos del 'for i'
                
                # Si no es válido parcialmente, deshacemos
                tablero[fila][col] = 0
        
        # --- 2. Fase retroceso de "Backtracking" ---
        if not num_encontrado:
            # Si el 'for' terminó sin encontrar un número, debemos retroceder.
            
            if not stack:
                # Si la pila está vacía, hemos probado todo. No hay solución.
                return False
                
            # Sacamos el último checkpoint guardado
            last_fila, last_col, last_indice_num = stack.pop()
            last_num = numeros[last_indice_num]
            
            # Deshacemos ese movimiento
            tablero[last_fila][last_col] = 0
            numeros_disponibles.add(last_num) # Devolvemos el número
            
            # Preparamos la siguiente iteración del 'while'
            # para que intente con el siguiente número en esa misma celda
            fila, col = last_fila, last_col
            indice_num = last_indice_num + 1


# --- Ejecución ---
print("Tablero inicial:")
mostrar_tablero(tablero)

if solucion(tablero):
    print("¡Solución encontrada!")
    mostrar_tablero(tablero)
else:
    print("No se encontró una solución.")
    mostrar_tablero(tablero)
