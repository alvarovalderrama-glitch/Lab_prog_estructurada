#  LABERINTO 

import os

# --- Función mostrar_tablero ---
def mostrar_tablero (tablero):
    for fila in range(MAX):
        for col in range(MAX):
            print (tablero[fila][col], end = " ")
        print ("")
    print("")

# --- Función colocar_obstaculo ---
def colocar_obstaculo(tablero):
    tablero [1][2] = "*"
    tablero [2][1] = "*"
    tablero [3][2] = "*"

# --- Función para verificar si la celda es válida ---
def es_valida(tablero, x, y):
    if 0<= x < MAX and 0<= y < MAX and tablero[x][y] == 0: #posición dentro de la matriz y la celda esta desocupada
        return True
    else:
        return False
   
# --- Función para comprobar si llegamos al final ---
def es_final(x, y): #coordenadas de la celda
    if x== MAX -1 and y==MAX-1:
        return True
    else:
        return False

# --- Función principal: resolver laberinto con backtracking ---
def resolver_laberinto(tablero, x, y, paso):
# Si llegamos al final, mostramos el resultado
    if es_final(x, y):
        tablero[x][y] = paso
        print("¡Camino de solución encontrado!")
        print ("")
        mostrar_tablero(tablero)
        return True

    # Posibles movimientos: derecha, abajo, izquierda, arriba
    movimientos = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # Marcamos la posición actual con el número de paso
    tablero[x][y] = paso

    # Intentamos moverse en las 4 direcciones
    for dx, dy in movimientos:
        nx, ny = x + dx, y + dy
        if es_valida(tablero, nx, ny):
            if resolver_laberinto(tablero, nx, ny, paso + 1):
                return True  # Si encuentra solución, termina

    # Si ninguna dirección funcionó, retrocede
    tablero[x][y] = 0
    return False

# --- Inicio Programa ---
os.system ("cls")
print("----------")
MAX = 4
tab = [[0 for _ in range(MAX)] for _ in range(MAX)] 
mostrar_tablero(tab)
colocar_obstaculo(tab)


mostrar_tablero(tab)
if resolver_laberinto(tab, 0, 0, 1):
    print("Camino completo encontrado.")
else:
    print("No hay solución posible.")