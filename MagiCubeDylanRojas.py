# Variables del problema
N = 3
META = 15 

# 1. Verificacion de Diagonales
def revisar_diagonales(c):
    # Diagonal principal (esquina superior izquierda a inferior derecha)
    if c[0][0] + c[1][1] + c[2][2] != META: return False
    # Diagonal secundaria (esquina superior derecha a inferior izquierda)
    if c[0][2] + c[1][1] + c[2][0] != META: return False
    return True

# 2. La función que busca
def buscar(pos):
    # Caso 1: ¡Tablero Lleno! (pos llega a 9)
    if pos == 9:
        if revisar_diagonales(tablero):
            print("\n SOLUCIÓN ENCONTRADA:")
            for fila in tablero: print(fila)
            return True
        return False

    f, c = pos // N, pos % N

    # Probar números del 1 al 9
    for num in range(1, 10):
        if not usados[num]:
            # 1. Intentar: Poner el número en el tablero y marcarlo como usado
            usados[num] = True
            tablero[f][c] = num
            
            # 2. Chequeo Temprano: ¿Ya fallo?
            fallo = False
            
            # Si se completa una fila y no suma 15, ¡FALLO!
            if c == N - 1 and sum(tablero[f]) != META:
                fallo = True
            
            # Si completamos una columna y no suma 15, ¡FALLO!
            elif f == N - 1:
                suma_col = tablero[0][c] + tablero[1][c] + tablero[2][c]
                if suma_col != META:
                    fallo = True
            
            # 3. Continuar la búsqueda solo si NO hubo fallo
            if not fallo:
                if buscar(pos + 1):
                    return True 
                
            # 4. Deshacer: Si no funcionó, borrar el número (Backtrack)
            usados[num] = False
            tablero[f][c] = 0
            
    return False

# --- Inicialización y Arranque ---
tablero = [[0] * N for _ in range(N)] # Matriz vacía 3x3
usados = [False] * 10 # Control de números (1 a 9)

buscar(0)