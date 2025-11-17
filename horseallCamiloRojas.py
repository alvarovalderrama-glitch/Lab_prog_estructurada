# Recorrido del caballo (todas las soluciones)

N = 5  # Tamaño del tablero
mov_x = [2, 1, -1, -2, -2, -1, 1, 2] # Movimientos en "X" del caballo
mov_y = [1, 2, 2, 1, -1, -2, -2, -1] # Movimientos en "Y" del caballo

soluciones = []  # Lista para guardar todas las soluciones

def es_valido(x, y, tablero): # Verifica si la posición es válida
    return 0 <= x < N and 0 <= y < N and tablero[x][y] == -1 # Verifica que esté dentro del tablero y no visitado

def imprimir_tablero(tablero): # Imprime el tablero
    for fila in tablero: # Imprime cada fila del tablero
        print(" ".join(f"{c:2}" for c in fila)) # Formatea cada celda con ancho 2
    print() 

def copiar_tablero(tablero): # Crea una copia del tablero
    return [fila[:] for fila in tablero] # Copia cada fila del tablero

def resolver_todas(x, y, mov, tablero): # Función recursiva para encontrar todas las soluciones
    if mov == N * N: # Si se han hecho todos los movimientos
        soluciones.append(copiar_tablero(tablero))  # Agrega una copia del tablero a la lista
        return # Retorna para seguir buscando otras soluciones

    for i in range(8): # Probar todos los movimientos posibles
        nx = x + mov_x[i] # Nueva posición "X"
        ny = y + mov_y[i] # Nueva posición "Y"
        if es_valido(nx, ny, tablero): # Verifica si la nueva posición es válida
            tablero[nx][ny] = mov # Marca movimiento
            resolver_todas(nx, ny, mov + 1, tablero) # Llamada recursiva
            tablero[nx][ny] = -1  # Backtracking

def main(): # Función principal
    tablero = [[-1 for _ in range(N)] for _ in range(N)] # Tablero inicial
    tablero[0][0] = 0 # Empezamos desde (0,0)
    resolver_todas(0, 0, 1, tablero) # Inicia la resolución

    print(f"Se encontraron {len(soluciones)} soluciones.") # Muestra el número de soluciones encontradas
    for i, sol in enumerate(soluciones[:3]):  # Mostrar primeras 3 soluciones
        print(f"Solución {i+1}:") # Indica el número de solución
        imprimir_tablero(sol) # Imprime la solución

if __name__ == "__main__": # Punto de entrada del programa
    main() # Ejecuta la función principal

