from typing import List
"""
while(hay celdas por llenar y no se decide parar):
    probar números posibles
    if(colocación válida):
        avanzar
        if(cuadrado completo):
            guardar solución
            decidir si seguir o no
        else:
            seguir buscando
    else:
        probar otro número
while(no hay más números válidos y no inicio):
    return
"""
def generar_cuadrados_magicos(n: int = 3, solo_una: bool = False) -> List[List[List[int]]]:

    # Constante mágica: suma que deben tener filas, columnas y diagonales
    magic_sum = n * (n**2 + 1) // 2

    # Tablero n x n lleno de ceros (celdas vacías)
    tablero = [[0 for _ in range(n)] for _ in range(n)]

    # Arreglo para saber si un número ya fue usado 
    usado = [False] * (n*n + 1)

    soluciones: List[List[List[int]]] = []

    def es_valido(fila: int, col: int, num: int) -> bool:
        # Para comprobar si se puede poner 'num' en (fila, col) sin romper las sumas.
        if usado[num]:
            return False

        # Colocamos temporalmente
        tablero[fila][col] = num

        # Comprobar FILA 
        suma_fila = sum(tablero[fila])
        # Si la suma parcial ya se pasa de la constante, no sirve
        if suma_fila > magic_sum:
            tablero[fila][col] = 0
            return False
        # Si la fila está completa (sin ceros) debe ser exactamente la constante
        if 0 not in tablero[fila] and suma_fila != magic_sum:
            tablero[fila][col] = 0
            return False

        # Comprobar COLUMNA 
        col_vals = [tablero[i][col] for i in range(n)]
        suma_col = sum(col_vals)
        if suma_col > magic_sum:
            tablero[fila][col] = 0
            return False
        if 0 not in col_vals and suma_col != magic_sum:
            tablero[fila][col] = 0
            return False

        #  Comprobar DIAGONAL PRINCIPAL (si corresponde) 
        if fila == col:
            diag_princ = [tablero[i][i] for i in range(n)]
            suma_diag_p = sum(diag_princ)
            if suma_diag_p > magic_sum:
                tablero[fila][col] = 0
                return False
            if 0 not in diag_princ and suma_diag_p != magic_sum:
                tablero[fila][col] = 0
                return False

        #  Comprobar DIAGONAL SECUNDARIA (si corresponde) 
        if fila + col == n - 1:
            diag_sec = [tablero[i][n-1-i] for i in range(n)]
            suma_diag_s = sum(diag_sec)
            if suma_diag_s > magic_sum:
                tablero[fila][col] = 0
                return False
            if 0 not in diag_sec and suma_diag_s != magic_sum:
                tablero[fila][col] = 0
                return False

        # Si pasamos todos los chequeos, dejamos el número colocado
        return True

    def backtrack(pos: int) -> bool:
        if pos == n * n:
            # Guardar copia de la solución
            sol = [fila[:] for fila in tablero]
            soluciones.append(sol)
            return solo_una

        fila = pos // n
        col = pos % n

        # Intentar colocar todos los números posibles
        for num in range(1, n*n + 1):
            if not usado[num]:
                if es_valido(fila, col, num):
                    usado[num] = True
                    # Avanzar a la siguiente celda
                    if backtrack(pos + 1):
                        return True  # cortar si solo una == True
                    usado[num] = False
                    tablero[fila][col] = 0

        # Si ningún número sirve, se vuelve hacia atrás
        return False

    # Iniciar backtracking desde la primera celda (posición 0)
    backtrack(0)
    return soluciones


def imprimir_cuadrado(cuadrado: List[List[int]]) -> None:
    """Imprime un cuadrado mágico de forma bonita."""
    n = len(cuadrado)
    ancho = len(str(n*n))
    for fila in cuadrado:
        print(" ".join(f"{x:>{ancho}}" for x in fila))
    print()


# Ejemplo de uso 
if __name__ == "__main__":
    n = 3  # cuadrado mágico 3x3
    todas = generar_cuadrados_magicos(n, solo_una=False)

    print(f"Se encontraron {len(todas)} soluciones para n={n}:\n")
    for i, cuad in enumerate(todas, start=1):
        print(f"Solución {i}:")
        imprimir_cuadrado(cuad)
