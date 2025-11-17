# Programa que genera un Cuadrado Mágico de tamaño N usando Backtracking.

N = 3  # Tamaño del cuadrado mágico (3x3 por defecto)

# FUNCIONES 

def imprimir_cuadrado(tablero):  # Función para mostrar el cuadrado formateado
    for fila in tablero:  # Recorre cada fila del cuadrado
        print(" ".join(f"{c:2}" for c in fila))  # Imprime valores alineados
    print()  # Línea en blanco final

def es_valido(tablero, x, y, num):  # Verifica si el número se puede colocar
    for i in range(N):  # Recorre filas y columnas
        for j in range(N):
            if tablero[i][j] == num:  # Si ya existe el número en el cuadrado
                return False  # No se puede repetir
    return True  # Si no se repite, es válido

def suma_correcta(tablero):  # Verifica si las sumas son iguales
    suma_ref = sum(tablero[0])  # Guarda la suma de la primera fila como referencia

    # Verifica filas
    for fila in tablero:
        if sum(fila) != suma_ref:
            return False

    # Verifica columnas
    for j in range(N):
        if sum(tablero[i][j] for i in range(N)) != suma_ref:
            return False

    # Verifica diagonales
    if sum(tablero[i][i] for i in range(N)) != suma_ref:
        return False
    if sum(tablero[i][N - 1 - i] for i in range(N)) != suma_ref:
        return False

    return True  # Si todas las sumas coinciden

def esta_lleno(tablero):  # Comprueba si todas las celdas están ocupadas
    for i in range(N): # Recorre filas
        for j in range(N): # Recorre columnas
            if tablero[i][j] == 0: # Si encuentra un cero
                return False # No está lleno
    return True # Está lleno

# FUNCIÓN PRINCIPAL DE BACKTRACKING

def backtracking(tablero, x, y):  # Función recursiva que llena el cuadrado

    if esta_lleno(tablero):  # Si el tablero está lleno
        if suma_correcta(tablero):  # Comprueba si cumple las sumas
            imprimir_cuadrado(tablero)  # Muestra el cuadrado mágico completo
            return True  # Termina (encontró una solución)
        else:
            return False  # No cumple las sumas, se descarta

    for num in range(1, N * N + 1):  # Intenta colocar números del 1 al N^2
        if es_valido(tablero, x, y, num):  # Si no está repetido
            tablero[x][y] = num  # Coloca el número en la celda
            # Calcula la siguiente celda (mueve en orden por filas)
            if y + 1 < N:
                nx, ny = x, y + 1  # Avanza en la misma fila
            else:
                nx, ny = x + 1, 0  # Salta a la siguiente fila
            if backtracking(tablero, nx, ny):  # Llama recursivamente
                return True  # Si encontró una solución, detiene la búsqueda
            tablero[x][y] = 0  # Si no resulta, borra el número (retrocede)
    return False  # Si no se pudo colocar ningún número, retorna falso

# PROGRAMA PRINCIPAL

def main():
    tablero = [[0 for _ in range(N)] for _ in range(N)]  # Crea tablero vacío
    print(f"Generando cuadrado mágico de tamaño {N}x{N}...\n")  # Mensaje inicial
    exito = backtracking(tablero, 0, 0)  # Llama al backtracking
    if not exito:  # Si no encontró cuadrado mágico
        print("No se pudo generar un cuadrado mágico válido.")  # Mensaje de fallo

if __name__ == "__main__":  # Ejecuta el programa principal
    main()