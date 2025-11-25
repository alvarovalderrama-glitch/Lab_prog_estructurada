import random
import copy

"""
Juego de Sudoku (9x9) en consola.

Flujo:
1. Se genera un tablero completo válido.
2. Se borran casillas según la dificultad (fácil / medio / difícil).
3. El usuario juega ingresando: fila columna valor  (por ejemplo: 1 3 9)
4. Comandos especiales:
   - 'resolver'  -> muestra la solución
   - 'salir'     -> termina el juego
"""

# ---------------- FUNCIONES BÁSICAS DE SUDOKU ---------------- #

def imprimir_tablero(tablero):
    """Muestra el tablero de forma bonita en consola."""
    print("    1 2 3   4 5 6   7 8 9")
    print("  +-------+-------+-------+")
    for i, fila in enumerate(tablero):
        fila_str = f"{i+1} | "
        for j, val in enumerate(fila):
            if val == 0:
                fila_str += ". "
            else:
                fila_str += str(val) + " "
            if (j + 1) % 3 == 0 and j < 8:
                fila_str += "| "
        fila_str += "|"
        print(fila_str)
        if (i + 1) % 3 == 0:
            print("  +-------+-------+-------+")


def es_valido(tablero, fila, col, num):
    """Revisa si puedo poner 'num' en la posición (fila, col)."""
    # Revisar fila
    for j in range(9):
        if tablero[fila][j] == num:
            return False

    # Revisar columna
    for i in range(9):
        if tablero[i][col] == num:
            return False

    # Revisar subcuadrante 3x3
    inicio_fila = (fila // 3) * 3
    inicio_col = (col // 3) * 3
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_col, inicio_col + 3):
            if tablero[i][j] == num:
                return False

    return True


def buscar_vacio(tablero):
    """Devuelve (fila, col) del primer espacio vacío (0). Si no hay, None."""
    for i in range(9):
        for j in range(9):
            if tablero[i][j] == 0:
                return i, j
    return None


def resolver_sudoku(tablero):
    """
    Resuelve el tablero por backtracking.
    Devuelve True si encontró solución; modifica el tablero original.
    """
    vacio = buscar_vacio(tablero)
    if not vacio:
        return True  # ya no hay huecos

    fila, col = vacio

    numeros = list(range(1, 10))
    random.shuffle(numeros)  # para que no sea siempre igual el patrón

    for num in numeros:
        if es_valido(tablero, fila, col, num):
            tablero[fila][col] = num
            if resolver_sudoku(tablero):
                return True
            tablero[fila][col] = 0  # retroceder

    return False


# ---------------- GENERACIÓN DEL JUEGO ---------------- #

def generar_tablero_completo():
    """Genera un tablero de Sudoku completo y válido."""
    tablero = [[0 for _ in range(9)] for _ in range(9)]
    resolver_sudoku(tablero)
    return tablero


def crear_puzzle(dificultad="medio"):
    """
    Crea un puzzle a partir de un tablero completo.
    No garantiza unicidad de solución (pero sirve como juego básico).
    dificultad: 'facil', 'medio', 'dificil'
    """
    tablero_completo = generar_tablero_completo()
    puzzle = copy.deepcopy(tablero_completo)

    # Elegimos cuántas pistas dejar según la dificultad
    if dificultad == "facil":
        pistas = random.randint(36, 45)   # más números visibles
    elif dificultad == "dificil":
        pistas = random.randint(24, 30)   # menos números visibles
    else:  # medio
        pistas = random.randint(30, 35)

    # Partimos con todo lleno (81) y vamos borrando
    casillas_a_borrar = 81 - pistas

    posiciones = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(posiciones)

    borradas = 0
    for (i, j) in posiciones:
        if borradas >= casillas_a_borrar:
            break
        if puzzle[i][j] != 0:
            puzzle[i][j] = 0
            borradas += 1

    return puzzle, tablero_completo


# ---------------- LOOP DEL JUEGO ---------------- #

def pedir_dificultad():
    print("Elige dificultad: (f)ácil, (m)edio, (d)ifícil")
    while True:
        op = input("> ").strip().lower()
        if op in ("f", "facil", "fácil"):
            return "facil"
        if op in ("m", "medio"):
            return "medio"
        if op in ("d", "dificil", "difícil"):
            return "dificil"
        print("Opción no válida. Intenta de nuevo.")


def esta_completo(tablero):
    """True si no hay ceros en el tablero."""
    for fila in tablero:
        if 0 in fila:
            return False
    return True


def jugar_sudoku():
    print("===== SUDOKU =====")
    dificultad = pedir_dificultad()
    puzzle, solucion = crear_puzzle(dificultad)

    # Tablero que el usuario va modificando
    tablero_jugador = copy.deepcopy(puzzle)

    while True:
        imprimir_tablero(tablero_jugador)

        if esta_completo(tablero_jugador):
            if tablero_jugador == solucion:
                print("🎉 ¡Felicidades! ¡Has resuelto el Sudoku correctamente!")
            else:
                print("El tablero está lleno, pero hay errores.")
                print("Puedes seguir corrigiendo o escribir 'resolver' para ver la solución.")
            # permitimos seguir o salir
        print("Escribe: fila columna valor (ej: 1 3 9)")
        print("Comandos: 'resolver' para ver la solución, 'salir' para terminar.")
        entrada = input("> ").strip().lower()

        if entrada == "salir":
            print("Gracias por jugar. ¡Hasta luego!")
            break

        if entrada == "resolver":
            print("Esta es una solución posible:")
            imprimir_tablero(solucion)
            print("Fin del juego.")
            break

        partes = entrada.split()
        if len(partes) != 3:
            print("Entrada inválida. Debes escribir: fila columna valor (ej: 1 3 9)")
            continue

        try:
            fila = int(partes[0]) - 1  # el usuario usa 1..9
            col = int(partes[1]) - 1
            valor = int(partes[2])
        except ValueError:
            print("Debes ingresar números enteros (1..9).")
            continue

        if not (0 <= fila < 9 and 0 <= col < 9 and 1 <= valor <= 9):
            print("Fila, columna o valor fuera de rango (debe ser 1..9).")
            continue

        # No permitir cambiar las pistas originales
        if puzzle[fila][col] != 0:
            print("Esa casilla es una pista del puzzle y no se puede cambiar.")
            continue

        # Verificamos si es un movimiento válido (con respecto a las reglas)
        if es_valido(tablero_jugador, fila, col, valor):
            tablero_jugador[fila][col] = valor
        else:
            print("Movimiento inválido según las reglas del Sudoku.")

# Ejecutar el juego si se corre este archivo directamente
if __name__ == "__main__":
    jugar_sudoku()
