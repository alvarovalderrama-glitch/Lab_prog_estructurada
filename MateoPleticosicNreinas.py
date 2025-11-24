MAX = 8 

# -------------------------------
# MODULO: Mostrar Tablero
# Recorre la matriz e imprime fila por fila para visualizar el juego.

def mostrar_tablero(tablero):
    for fila in tablero:
        print(*fila)
    print()

# -------------------------------
# MODULO: Validar Posicion
# Verifica si es seguro colocar una reina (1) en la coordenada x, y.
# Solo revisa hacia la izquierda porque vamos llenando de izq a der.
def valida(tablero, x, y):
    # 1. Revisa si hay otra reina en la misma fila (hacia la izquierda)
    for j in range(y):
        if tablero[x][j] == 1:
            return False
    
    # 2. Revisa la diagonal superior izquierda (\)
    i, j = x, y
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1: return False
        i -= 1; j -= 1

    # 3. Revisa la diagonal inferior izquierda (/)
    i, j = x, y
    while i < MAX and j >= 0:
        if tablero[i][j] == 1: return False
        i += 1; j -= 1
        
    return True

# -------------------------------
# MODULO: Solucion 
# Intenta colocar las reinas columna por columna (variable y).
def Solucion(tablero, y):
    # Caso Base: Si llegamos a la columna 8
    if y >= MAX:
        return True
    
    # Probamos poner la reina en todas las filas (x) de esta columna
    for x in range(MAX):
        if valida(tablero, x, y):
            tablero[x][y] = 1  # Poner reina
            
            # Llamada Recursiva: Intentamos resolver la siguiente columna
            if Solucion(tablero, y + 1):
                return True
            
            # Backtracking: Si falla, borramos la reina y probamos otra fila
            tablero[x][y] = 0
            
    return False

#------------------MAIN---------------------------
if __name__ == "__main__":
    # Crear matriz vacia de 8x8
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    
    # MOSTRAR ESTADO INICIAL
    print("Tablero Inicial")
    mostrar_tablero(tablero)
    
    print("Calculando solucion...\n")
    
    # EJECUTAR ALGORITMO Y MOSTRAR FINAL
    if Solucion(tablero, 0):
        print("Tablero Final")
        mostrar_tablero(tablero)
    else:
        print("No se encontro solucion.")