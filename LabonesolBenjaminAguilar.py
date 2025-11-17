import random

def mostrar_tablero(tablero): # Función para mostrar el tablero de forma ordenada
    for fila in tablero:  # Recorre cada fila del tablero
        print(" ".join(str(c) for c in fila))  # Imprime los valores separados por espacio
    print()  # Línea en blanco para separar tableros

def es_valida(tablero, x, y): # Función que verifica si una posición (x, y) es válida para moverse
    n = len(tablero)  # Tamaño del tablero
    # Devuelve True si está dentro de los límites y la celda está vacía (0)
    return 0 <= x < n and 0 <= y < n and tablero[x][y] == 0

def resolver_todas(tablero, x, y, soluciones, paso): # Función recursiva que busca todas las soluciones posibles
    n = len(tablero)  # Tamaño del laberinto

    if x == n - 1 and y == n - 1:# Caso base: si se llega a la esquina inferior derecha
        tablero[x][y] = paso  # Marca el último paso
        soluciones.append([fila.copy() for fila in tablero])  # Guarda una copia del tablero
        tablero[x][y] = 0  # Desmarca para seguir buscando otras rutas
        return

    # Si la posición es válida, procedemos a explorar
    if es_valida(tablero, x, y):
        tablero[x][y] = paso  # Marca el paso actual

        # Intentar moverse hacia la derecha
        resolver_todas(tablero, x + 1, y, soluciones, paso + 1)
        
        # Intentar moverse hacia abajo
        resolver_todas(tablero, x, y + 1, soluciones, paso + 1)
        
        # Intentar moverse hacia la izquierda
        resolver_todas(tablero, x - 1, y, soluciones, paso + 1)
        
        # Intentar moverse hacia arriba
        resolver_todas(tablero, x, y - 1, soluciones, paso + 1)

        tablero[x][y] = 0  # Desmarcar la celda para permitir otras rutas

n = int(input("Ingrese tamaño del laberinto (n x n): ")) # Entrada del usuario para definir el tamaño del laberinto

tablero = [[0 for _ in range(n)] for _ in range(n)] # Crear un tablero n x n lleno de ceros

soluciones = [] # Lista donde se guardarán todas las soluciones encontradas

resolver_todas(tablero, 0, 0, soluciones, 1) # Llamada inicial a la función de resolución

if soluciones: # Si existen soluciones, se muestra una al azar
    sol_aleatoria = random.choice(soluciones)  # Selecciona solución aleatoria
    print("Solución aleatoria:")
    mostrar_tablero(sol_aleatoria)  # Imprime el tablero
else:
    print("No hay solución.")
