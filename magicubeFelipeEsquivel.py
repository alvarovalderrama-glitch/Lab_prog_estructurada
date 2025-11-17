import random  # Se importa la librería random (no la usamos, pero la dejamos por si luego quieres barajar números)

# Función para verificar si el tablero es un cuadrado mágico completo
def es_magico(tablero, n):
    valor_sum = sum(tablero[0])  # La suma mágica que deben tener todas las filas y columnas (suma de la primera fila)

    # Verifica las sumas de todas las filas
    for i in range(n):
        if sum(tablero[i]) != valor_sum:  # Si alguna fila no suma lo mismo, no es mágico
            return False
    
    # Verifica las sumas de todas las columnas
    for j in range(n):
        if sum(tablero[i][j] for i in range(n)) != valor_sum:  # Suma de cada columna
            return False

    # Verifica la suma de la diagonal principal
    if sum(tablero[i][i] for i in range(n)) != valor_sum:
        return False

    # Verifica la suma de la diagonal secundaria
    if sum(tablero[i][n - 1 - i] for i in range(n)) != valor_sum:
        return False

    return True  # Si todas las sumas son iguales, es un cuadrado mágico


# Función para verificar si el tablero está completamente lleno
def tablero_completo(tablero, n):
    for fila in range(n):
        for columna in range(n):
            if tablero[fila][columna] == 0:  # Si hay un 0, la casilla está vacía
                return False
    return True  # No hay ceros, el tablero está completo


# Función para validar si se puede poner un número en una posición (x, y)
def valida(tablero, x, y, num, n, suma_magica):
    # 1) Verificar que el número no esté repetido en todo el tablero
    for i in range(n):
        for j in range(n):
            if tablero[i][j] == num:  # Si ya existe el número en alguna casilla, no es válido
                return False

    # 2) Verificar fila y columna respecto a la suma mágica (poda básica)

    # Comprobar suma parcial de la fila si ya está llena
    fila_valores = [tablero[x][j] if j != y else num for j in range(n)]  # Reemplazamos la posición (x,y) por num
    if 0 not in fila_valores:  # Si ya no hay ceros, la fila está completa
        if sum(fila_valores) != suma_magica:  # Si no suma la suma mágica, no sirve
            return False

    # Comprobar suma parcial de la columna si ya está llena
    columna_valores = [tablero[i][y] if i != x else num for i in range(n)]  # Reemplazamos la posición (x,y) por num
    if 0 not in columna_valores:  # Si la columna está completa
        if sum(columna_valores) != suma_magica:
            return False

    # Comprobar diagonal principal si (x, y) está en ella
    if x == y:
        diag_principal = [tablero[i][i] if (i, i) != (x, y) else num for i in range(n)]
        if 0 not in diag_principal:  # Si la diagonal está completa
            if sum(diag_principal) != suma_magica:
                return False

    # Comprobar diagonal secundaria si (x, y) está en ella
    if x + y == n - 1:
        diag_secundaria = [tablero[i][n - 1 - i] if (i, n - 1 - i) != (x, y) else num for i in range(n)]
        if 0 not in diag_secundaria:  # Si la diagonal está completa
            if sum(diag_secundaria) != suma_magica:
                return False

    return True  # Si pasa todas las validaciones, se puede colocar el número


# Función recursiva de backtracking
def backtracking(tablero, n, pos, suma_magica):
    # Si el tablero está completo, verificamos si es mágico
    if tablero_completo(tablero, n):
        return es_magico(tablero, n)

    # Si pos se sale del rango, no hay solución por este camino
    if pos >= n * n:
        return False

    fila = pos // n      # Calcula la fila actual a partir de pos
    columna = pos % n    # Calcula la columna actual a partir de pos

    # Si la casilla ya está ocupada (por si algún día pre-rellenas algo), pasar a la siguiente
    if tablero[fila][columna] != 0:
        return backtracking(tablero, n, pos + 1, suma_magica)

    # Probar con números del 1 al n^2
    for num in range(1, n * n + 1):
        # Si el número es válido según todas las restricciones
        if valida(tablero, fila, columna, num, n, suma_magica):
            tablero[fila][columna] = num  # Coloca el número en la casilla

            # Llamada recursiva para la siguiente casilla
            if backtracking(tablero, n, pos + 1, suma_magica):
                return True  # Si se encontró solución, se propaga hacia arriba

            # Si no funciona, deshace el cambio (retroceso)
            tablero[fila][columna] = 0

    # Si no se puede colocar ningún número válido aquí, devolvemos False
    return False


# Función para imprimir el tablero
def imprimir_tablero(tablero):
    for fila in tablero:
        print(*fila)  # Imprime cada fila separando los elementos por espacios


# Función principal para generar el tablero y ejecutar backtracking
def main():
    n = 3  # Tamaño del cuadrado mágico (puedes cambiar este valor, por ejemplo 3 o 4)
    tablero = [[0] * n for _ in range(n)]  # Inicializa un tablero vacío con ceros
    suma_magica = n * (n * n + 1) // 2     # Fórmula de la suma mágica: n * (n^2 + 1) / 2

    # Llama a la función de backtracking comenzando desde la posición 0
    if backtracking(tablero, n, 0, suma_magica):
        print("¡Se encontró un cuadrado mágico!")
        imprimir_tablero(tablero)  # Imprime el tablero mágico
    else:
        print("No se encontró un cuadrado mágico.")

# Llamada a la función principal
main()

