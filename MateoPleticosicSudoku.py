MAX = 9  # Tamaño del tablero 9x9

# -------------------------------
# modulo mostrar_tablero
def mostrar_tablero(tablero):
    for fila in tablero:
        # El asterisco desempaqueta la lista para imprimir sin corchetes
        print(*fila) 
    print()

# -------------------------------
# modulo valida
# Revisa si el numero sirve en la posicion x, y
def valida(tablero, x, y, numero):
    # 1. Revisar la Fila (mantenemos x fija, movemos la j)
    for j in range(MAX):
        if tablero[x][j] == numero:
            return False
    
    # 2. Revisar la Columna (movemos la i, mantenemos y fija)
    for i in range(MAX):
        if tablero[i][y] == numero:
            return False
            
    # 3. Revisar Cuadrante 3x3
    # Calculamos la esquina superior izquierda del bloque
    inicio_x = (x // 3) * 3
    inicio_y = (y // 3) * 3
    
    for i in range(3):
        for j in range(3):
            if tablero[inicio_x + i][inicio_y + j] == numero:
                return False
                
    return True 

# -------------------------------
# modulo buscar_vacio
# Busca el primer 0. Retorna x, y (fila, columna)
def buscar_vacio(tablero):
    for x in range(MAX):
        for y in range(MAX):
            if tablero[x][y] == 0:
                return x, y
    return -1, -1

# -------------------------------
# modulo cargar_juego
def valores_preestablecidos(tablero):
    # Asignamos valores iniciales
    tablero[0][0] = 5
    tablero[0][1] = 3
    tablero[0][4] = 7
    
    tablero[1][0] = 6
    tablero[1][3] = 1
    tablero[1][4] = 9
    tablero[1][5] = 5
    
    tablero[2][1] = 9
    tablero[2][2] = 8
    tablero[2][7] = 6
    
    tablero[4][0] = 4
    tablero[4][3] = 8
    tablero[4][5] = 3
    tablero[4][8] = 1

# -------------------------------
# Modulo solucion
def Solucion(tablero):
    
    # Buscamos coordenadas x, y vacias
    x, y = buscar_vacio(tablero)
    
    # Caso base: Si x es -1, no quedan vacios. Fin.
    if x == -1:
        return True
    
    # Intentamos numeros del 1 al 9
    for numero in range(1, 10):
        
        if valida(tablero, x, y, numero):
            
            # Marcamos la casilla
            tablero[x][y] = numero
            
            # Llamada Recursiva
            if Solucion(tablero):
                return True
            
            # Backtracking: Si no funcionó, limpiamos (volvemos a 0)
            tablero[x][y] = 0
            
    return False

# -------------------------------
# programa principal
if __name__ == "__main__":
    # Matriz de 9x9 llena de ceros
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    
    valores_preestablecidos(tablero)
    
    print("Tablero inicial:")
    mostrar_tablero(tablero)
    
    print("Calculando...")
    
    if Solucion(tablero):
        print("Tablero Resuelto:")
        mostrar_tablero(tablero)
    else:
        print("No hay solucion.")