# Cuadrado Mágico con Backtracking

# Este programa genera un cuadrado mágico usando backtracking
import os
N = 3  # Tamaño del cuadrado mágico

# Crear tablero vacío (llenado con ceros)
tablero = [[0 for _ in range(N)] for _ in range(N)]

# Calcular el valor que deben sumar las filas, columnas y diagonales
valor_objetivo = N * (N*N + 1) // 2

def es_final(tab):
    """Retorna True si el tablero está completamente lleno."""
    for fila in tab:
        if 0 in fila:
            return False
    return True


def es_magico(tab):
    """Verifica si el tablero lleno es un cuadrado mágico."""
    # Revisar todas las filas
    for i in range(N):
        if sum(tab[i]) != valor_objetivo:
            return False

    # Revisar todas las columnas
    for j in range(N):
        if sum(tab[i][j] for i in range(N)) != valor_objetivo:
            return False

    # Revisar diagonal principal
    if sum(tab[i][i] for i in range(N)) != valor_objetivo:
        return False

    # Revisar diagonal inversa
    if sum(tab[i][N - 1 - i] for i in range(N)) != valor_objetivo:
        return False

    return True


def valida(tab, candidato, x, y):
    """Verifica si se puede colocar el 'candidato' en la posición (x,y)."""
    if tab[x][y] != 0:
        return False

    # Revisar que el número no esté repetido
    for i in range(N):
        for j in range(N):
            if tab[i][j] == candidato:
                return False

    return True


def siguiente_posicion(x, y):
    """Devuelve la siguiente posición del tablero (recorrido fila por fila)."""
    if y < N - 1:
        return x, y + 1
    else:
        return x + 1, 0


def backtracking(tab, x, y):
    # Si llegamos más allá de la última fila, todo está lleno
    if x == N:
        return es_magico(tab)

    # Probar todos los números posibles
    for candidato in range(1, N*N + 1):
        if valida(tab, candidato, x, y):
            tab[x][y] = candidato

            nx, ny = siguiente_posicion(x, y)

            if backtracking(tab, nx, ny):
                return True

            # Retroceder
            tab[x][y] = 0

    return False


# Ejecutar el algoritmo
os.system ("cls")
if backtracking(tablero, 0, 0):
    print("Cuadrado mágico encontrado:")
    for fila in tablero:
        print(fila)
else:
    print("No existe solución.")