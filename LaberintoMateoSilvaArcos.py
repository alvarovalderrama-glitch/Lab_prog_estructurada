FILAS = 8
COLUMNAS = 8

# 0 = camino libre, 1 = pared
laberinto = [
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 0]
]

def imprimir_laberinto():
    #""Muestra el laberinto en pantalla con símbolos."""
    for fila in range(FILAS):
        for columna in range(COLUMNAS):
            if fila == 0 and columna == 0:
                # Inicio
                print("S", end=" ")
            elif fila == FILAS - 1 and columna == COLUMNAS - 1:
                # Salida
                print("E", end=" ")
            else:
                if laberinto[fila][columna] == 1:
                    print("#", end=" ")   # pared
                elif laberinto[fila][columna] == 2:
                    print("*", end=" ")   # camino solución
                else:
                    print(".", end=" ")   # camino libre
        print()
    print()

def resolver_laberinto(fila, columna):
    #""Intenta llegar desde (fila, columna) hasta la salida usando backtracking."""
    # 1) Fuera de límites
    if fila < 0 or fila >= FILAS or columna < 0 or columna >= COLUMNAS:
        return False

    # 2) Pared o casilla ya visitada
    if laberinto[fila][columna] == 1 or laberinto[fila][columna] == 2:
        return False

    # 3) Llegamos a la salida
    if fila == FILAS - 1 and columna == COLUMNAS - 1:
        laberinto[fila][columna] = 2
        return True

    # 4) Marcamos como parte del camino
    laberinto[fila][columna] = 2

    # 5) Probar ABAJO
    if resolver_laberinto(fila + 1, columna):
        return True

    # 6) Probar DERECHA
    if resolver_laberinto(fila, columna + 1):
        return True

    # 7) Probar ARRIBA
    if resolver_laberinto(fila - 1, columna):
        return True

    # 8) Probar IZQUIERDA
    if resolver_laberinto(fila, columna - 1):
        return True

    # 9) Ninguna dirección funcionó → desmarcamos y retrocedemos
    laberinto[fila][columna] = 0
    return False

# ---- PROGRAMA PRINCIPAL ----

print("Laberinto original:")
imprimir_laberinto()

if resolver_laberinto(0, 0):
    print("Se encontró un camino desde S hasta E:")
    imprimir_laberinto()
else:
    print("No existe un camino desde S hasta E.")
