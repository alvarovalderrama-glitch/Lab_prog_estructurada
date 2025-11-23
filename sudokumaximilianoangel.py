###============Sudoku============###

import random

# Tamaño del tablero Sudoku (9x9)
n = 9

# Se crea el tablero inicial lleno de ceros
tablero = [[0 for _ in range(n)] for _ in range(n)]

# Función para imprimir el tablero en consola
def crear_tablero():
    # Recorre filas del tablero
    for i in range(n):
        # Recorre columnas del tablero
        for j in range(n):
            # Imprime cada número con formato de ancho fijo
            print(f"{tablero[i][j]:3}", end = " ")
        # Salto de línea al finalizar cada fila
        print("")
    # Salto extra para separar visualmente tableros
    print("")

# Algoritmo de backtracking para generar el Sudoku completo
def back_recursivo(fila, colum):
    # Caso base: si se llegó al final de las filas, el tablero está completo
    if fila == n:
        return True
    
    # Si se terminó la fila actual, se pasa a la siguiente
    if colum == n:
        return back_recursivo(fila + 1, 0)
    
    # Si la casilla ya tiene un número, se avanza a la siguiente columna
    if tablero[fila][colum] != 0:
        return back_recursivo(fila, colum + 1)
    
    # Se prueban los números del 1 al 9 en orden aleatorio
    for num in random.sample(range(1, 10), 9):
        # Se valida si el número puede colocarse
        if valido(fila, colum, num) == True:
            # Se asigna el número a la casilla
            tablero[fila][colum] = num

            # Llamada recursiva para continuar llenando el tablero
            if back_recursivo(fila, colum + 1) == True:
                return True
            
            # Si no funciona, se deshace el cambio (backtracking)
            tablero[fila][colum] = 0

    # Si ningún número funciona, se retorna False
    return False

# Función que valida si un número puede ir en la posición indicada
def valido(fila, colum, num):

    # Comprobar filas #
    # Verifica que el número no se repita en la misma fila
    for i in range(n):
        if tablero[fila][i] == num:
            return False
        
    # Comprobar columnas #
    # Verifica que el número no se repita en la misma columna
    for i in range(n):
        if tablero[i][colum] == num:
            return False
        
    # Se calcula la esquina superior izquierda del subcuadro 3x3
    inicial_fila = (fila // 3)*3
    inicial_colum = (colum // 3)*3

    # Se revisa el subcuadro 3x3 correspondiente
    for i in range(inicial_fila, inicial_fila + 3):
        for j in range(inicial_colum, inicial_colum + 3):
            if tablero[i][j] == num:
                return False
    
    # Si pasa todas las validaciones, el número es válido
    return True


# Función para mostrar el tablero formateado
def mostrar_tablero():
    # Recorre cada fila del tablero
    for fila in tablero:
        # Recorre cada valor de la fila
        for valor in fila:
            # Imprime el número separado por espacios
            print(valor, end=" ")
        print()
    # Salto para separar tableros
    print()

### Main ###

# Se genera un tablero completo válido usando backtracking
back_recursivo(0, 0)

# Guardar solución
# Se hace una copia profunda del tablero completo
solucion = [fila[:] for fila in tablero]

# Quitar algunos números para que no quede lleno
# Esto genera el tablero inicial del Sudoku (con espacios vacíos)
for i in range(9):
    for j in range(9):
        # Probabilidad del 50% de borrar cada número
        if random.random() < 0.5:  # 50% de probabilidad de borrar
            tablero[i][j] = 0

# Se muestra el tablero incompleto (para resolver)
print("Tablero inicial:\n")
mostrar_tablero()

# Restaurar solución
# Se vuelve a cargar el tablero completo
# para mostrar la solución final
tablero = solucion

print("Tablero solucionado:\n")
mostrar_tablero()
