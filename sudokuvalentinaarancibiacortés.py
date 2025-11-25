import random

# Tamaño del tablero (9x9), típico de un Sudoku
MAX = 9

# Creamos un tablero vacío lleno con espacios
tablero = [[" " for _ in range(MAX)] for _ in range(MAX)]

# -----------------------------------------------------------
# Función que imprime el tablero de forma ordenada en consola
# -----------------------------------------------------------
def mostrar_tablero(tablero):
    print("\n" + "-" * (MAX * 5 + 1))
    for fila in tablero:
        for celda in fila:
            # Se imprime cada celda con un borde | y espacio
            print(f"| {celda:2}", end=" ")
        print("|")
        print("-" * (MAX * 5 + 1))
    print("")

# ---------------------------------------------------------------
# Función que verifica si es válido colocar un número en una celda
# ---------------------------------------------------------------
def es_valido(tablero, fila, col, num):

    # 1️⃣ Revisar si el número ya está en la misma fila
    if num in tablero[fila]:
        return False

    # 2️⃣ Revisar la columna
    for i in range(9):
        if tablero[i][col] == num:
            return False

    # 3️⃣ Revisar el subcuadrante 3x3
    inicio_fila = (fila // 3) * 3     # fila inicial del bloque
    inicio_col = (col // 3) * 3       # columna inicial del bloque
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False

    return True  # Si pasa las 3 pruebas es válido

# ------------------------------------------------------------
# Algoritmo BACKTRACKING para resolver completamente el sudoku
# ------------------------------------------------------------
def resolver(tablero):
    for i in range(9):         # recorremos filas
        for j in range(9):     # recorremos columnas

            # Si encontramos una casilla vacía
            if tablero[i][j] == " ":
                
                # Lista de números 1 a 9 mezclados al azar
                numeros = list(range(1, 10))
                random.shuffle(numeros)

                # Probar cada número posible
                for num in numeros:
                    if es_valido(tablero, i, j, num):

                        # Colocamos el número tentativamente
                        tablero[i][j] = num

                        # Llamada recursiva
                        if resolver(tablero):
                            return True

                        # Si no funciona, deshacemos y probamos otro
                        tablero[i][j] = " "

                # Si ningún número sirve, retrocedemos
                return False

    # Si no quedan espacios vacíos, el sudoku está resuelto
    return True

# ----------------------------------------------------------
# Función que borra una cantidad de casillas al azar del tablero
# ----------------------------------------------------------
def borrar_casillas(tablero, cantidad):
    # Lista de todas las posiciones del tablero
    celdas = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(celdas)

    # Borrar las primeras 'cantidad' posiciones aleatorias
    for k in range(cantidad):
        fila, col = celdas[k]
        tablero[fila][col] = " "

#️⃣ Primero resolvemos el tablero completo
resolver(tablero)

#️⃣ Borramos 60 casillas para generar un sudoku incompleto
borrar_casillas(tablero, 60)
print("Tablero sin resolver:")
mostrar_tablero(tablero)

#️⃣ Intentamos resolver el tablero incompleto nuevamente
resolver(tablero)
print("Tablero resuelto:")
mostrar_tablero(tablero)
import random

# Tamaño del tablero (9x9), típico de un Sudoku
MAX = 9

# Creamos un tablero vacío lleno con espacios
tablero = [[" " for _ in range(MAX)] for _ in range(MAX)]

# -----------------------------------------------------------
# Función que imprime el tablero de forma ordenada en consola
# -----------------------------------------------------------
def mostrar_tablero(tablero):
    print("\n" + "-" * (MAX * 5 + 1))
    for fila in tablero:
        for celda in fila:
            # Se imprime cada celda con un borde | y espacio
            print(f"| {celda:2}", end=" ")
        print("|")
        print("-" * (MAX * 5 + 1))
    print("")

# ---------------------------------------------------------------
# Función que verifica si es válido colocar un número en una celda
# ---------------------------------------------------------------
def es_valido(tablero, fila, col, num):

    # 1️⃣ Revisar si el número ya está en la misma fila
    if num in tablero[fila]:
        return False

    # 2️⃣ Revisar la columna
    for i in range(9):
        if tablero[i][col] == num:
            return False

    # 3️⃣ Revisar el subcuadrante 3x3
    inicio_fila = (fila // 3) * 3     # fila inicial del bloque
    inicio_col = (col // 3) * 3       # columna inicial del bloque
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False

    return True  # Si pasa las 3 pruebas es válido

# ------------------------------------------------------------
# Algoritmo BACKTRACKING para resolver completamente el sudoku
# ------------------------------------------------------------
def resolver(tablero):
    for i in range(9):         # recorremos filas
        for j in range(9):     # recorremos columnas

            # Si encontramos una casilla vacía
            if tablero[i][j] == " ":
                
                # Lista de números 1 a 9 mezclados al azar
                numeros = list(range(1, 10))
                random.shuffle(numeros)

                # Probar cada número posible
                for num in numeros:
                    if es_valido(tablero, i, j, num):

                        # Colocamos el número tentativamente
                        tablero[i][j] = num

                        # Llamada recursiva
                        if resolver(tablero):
                            return True

                        # Si no funciona, deshacemos y probamos otro
                        tablero[i][j] = " "

                # Si ningún número sirve, retrocedemos
                return False

    # Si no quedan espacios vacíos, el sudoku está resuelto
    return True

# ----------------------------------------------------------
# Función que borra una cantidad de casillas al azar del tablero
# ----------------------------------------------------------
def borrar_casillas(tablero, cantidad):
    # Lista de todas las posiciones del tablero
    celdas = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(celdas)

    # Borrar las primeras 'cantidad' posiciones aleatorias
    for k in range(cantidad):
        fila, col = celdas[k]
        tablero[fila][col] = " "

#️⃣ Primero resolvemos el tablero completo
resolver(tablero)

#️⃣ Borramos 60 casillas para generar un sudoku incompleto
borrar_casillas(tablero, 60)
print("Tablero sin resolver:")
mostrar_tablero(tablero)

#️⃣ Intentamos resolver el tablero incompleto nuevamente
resolver(tablero)
print("Tablero resuelto:")
mostrar_tablero(tablero)
