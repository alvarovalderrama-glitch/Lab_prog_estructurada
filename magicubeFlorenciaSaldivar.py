SUMA_MAGICA = 15


def crear_tablero():    # Crea un tablero vacío de 3x3.
    return [    
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def imprimir_tablero(tablero):      # Imprime el tablero de forma legible.
    print("-------------")
    for fila in tablero:        # Itera sobre cada fila del tablero
        print(fila)
    print("-------------\n")


def fila_correcta(tablero, fila):   # Revisa si la fila está completa y si su suma es correcta.
   
    if 0 not in tablero[fila]:  # si no hay ceros, la fila está llena
        return sum(tablero[fila]) == SUMA_MAGICA
    return True  # si no está llena, todavía podría ser válida


def columna_correcta(tablero, col): #  Revisa si la columna está completa y si su suma es correcta.
    columna = [tablero[0][col], tablero[1][col], tablero[2][col]]   # extrae la columna
    if 0 not in columna:
        return sum(columna) == SUMA_MAGICA
    return True


def diagonales_correctas(tablero):  # Revisa si las diagonales están completas y si su suma es correcta.

    diag1 = [tablero[0][0], tablero[1][1], tablero[2][2]]
    diag2 = [tablero[0][2], tablero[1][1], tablero[2][0]]

    if 0 not in diag1 and sum(diag1) != SUMA_MAGICA:    # si la diagonal está llena y no suma 15
        return False

    if 0 not in diag2 and sum(diag2) != SUMA_MAGICA:    # si la diagonal está llena y no suma 15
        return False

    return True


def es_valido(tablero, fila, col):
    return (
        fila_correcta(tablero, fila)
        and columna_correcta(tablero, col)
        and diagonales_correctas(tablero)
    )


def siguiente_posicion(fila, col):
    if col == 2:
        return fila + 1, 0
    return fila, col + 1


def backtracking(tablero, usados, fila, col, soluciones):   # Algoritmo de backtracking para llenar el tablero.
    if fila == 3:
        soluciones.append([fila[:] for fila in tablero])    # guardar solución
        print("Solución encontrada:")   
        imprimir_tablero(tablero)
        return

    # Probar números del 1 al 9
    for numero in range(1, 10):
        if numero in usados:
            continue  # no repetir números

        tablero[fila][col] = numero
        usados.add(numero)

        if es_valido(tablero, fila, col):   # si es válido, continuar
            nf, nc = siguiente_posicion(fila, col)
            backtracking(tablero, usados, nf, nc, soluciones)   # llamada recursiva

        tablero[fila][col] = 0
        usados.remove(numero)


def main():
    tablero = crear_tablero()
    usados = set()     # números usados
    soluciones = []    # lista donde se guardarán las soluciones

    backtracking(tablero, usados, 0, 0, soluciones)

    print("Total de soluciones:", len(soluciones))


if __name__ == "__main__":
    main()
