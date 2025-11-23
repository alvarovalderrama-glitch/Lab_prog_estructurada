import random
import copy

# 1. Regla Básica: ¿Es Válido? 
def es_valido(tablero, fila, col, num):
    """Revisa si 'num' no está en la fila, columna o cuadrado 3x3."""
    
    # Revisa Fila y Columna
    for i in range(9):
        if tablero[fila][i] == num or tablero[i][col] == num:
            return False
            
    # Revisa Cuadrado 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False
    return True

# 2. Solucionador (Prueba y Error)
def resolver_sudoku(tablero):
    """Busca el 0 y prueba números hasta llenar el tablero."""
    
    # Buscar el 0 (casilla vacía)
    for r in range(9):
        for c in range(9):
            if tablero[r][c] == 0:
                fila, col = r, c
                break
        else: continue
        break
    else: return True # Si no hay 0s, esta resuelto

    numeros = list(range(1, 10))
    random.shuffle(numeros) 
    
    for num in numeros:
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            
            if resolver_sudoku(tablero): # Llamada recursiva
                return True
                
            tablero[fila][col] = 0 # Vuelve atrás (Backtrack)
            
    return False

#  3. Generador de Puzzle
def generar_sudoku():
    """Crea un tablero completo y luego quita 40-50 números al azar."""
    
    tablero = [[0] * 9 for _ in range(9)]
    resolver_sudoku(tablero) # Lo llena

    # Quita casillas
    casillas_a_quitar = random.randint(40, 50)
    for _ in range(casillas_a_quitar):
        r, c = random.randint(0, 8), random.randint(0, 8)
        tablero[r][c] = 0
            
    return tablero

#  4. Impresión Bonita 
def imprimir_tablero(tablero):
    """Muestra el tablero con líneas para que se vea bien."""
    print("-----------------------")
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("|-------+-------+-------|")
            
        linea = "| "
        for j in range(9):
            valor = str(tablero[i][j]) if tablero[i][j] != 0 else "."
            if j % 3 == 0 and j != 0:
                linea += "| "
                
            linea += valor + " "
            
        linea += "|"
        print(linea)
    print("-----------------------")

#
# Ejecución Principal

# Generar un nuevo puzzle
puzzle = generar_sudoku()
print("--- PUZZLE INICIAL ('.' = Vacío) ---")
imprimir_tablero(puzzle)

# Resolver el puzzle
solucion = copy.deepcopy(puzzle)
resolver_sudoku(solucion)

print("\n--- SOLUCIÓN ---")
imprimir_tablero(solucion)