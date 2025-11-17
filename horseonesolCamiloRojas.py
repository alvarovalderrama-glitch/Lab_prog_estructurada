# Recorrido del caballo (una solución)

N = 5  # Tamaño del tablero

mov_x = [2, 1, -1, -2, -2, -1, 1, 2]  # Movimientos en X del caballo
mov_y = [1, 2, 2, 1, -1, -2, -2, -1]  # Movimientos en Y del caballo

def es_valido(x, y, tablero): # Verifica si la posición es válida
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1  # Verifica que esté dentro del tablero y no visitado

def imprimir_tablero(tablero): # Imprime el tablero
    for fila in tablero: # Imprime cada fila del tablero
        print(" ".join(f"{c:2}" for c in fila)) # Formatea cada celda con ancho 2
    print() 

def resolver_caballo(x, y, mov, tablero): # Función recursiva para resolver el problema del caballo
    if mov == N * N: # Si se han hecho todos los movimientos
        return True  # Se completó todo el recorrido

    for i in range(8):  # Probar todos los movimientos posibles
        nx = x + mov_x[i] # Nueva posición "X"
        ny = y + mov_y[i] # Nueva posición "Y"
        if es_valido(nx, ny, tablero): # Verifica si la nueva posición es válida
            tablero[nx][ny] = mov  # Marca movimiento
            if resolver_caballo(nx, ny, mov + 1, tablero): # Llamada recursiva
                return True  # Solución encontrada
            tablero[nx][ny] = -1  # Backtracking
    return False # No se encontró solución desde esta posición

def main(): # Función principal
    tablero = [[-1 for _ in range(N)] for _ in range(N)]  # Tablero inicial
    tablero[0][0] = 0  # Empezamos desde (0,0)

    if resolver_caballo(0, 0, 1, tablero): # Inicia la resolución
        imprimir_tablero(tablero) # Imprime el tablero con la solución
    else:
        print("No hay solución") # No se encontró solución

if __name__ == "__main__": # Punto de entrada del programa
    main() # Ejecuta la función principal


