
from typing import List

def imprimir_tablero(solucion: List[int]) -> None:

    n = len(solucion)
    for fila in range(n):
        linea = ""
        for col in range(n):
            if solucion[fila] == col:
                linea += " Q "
            else:
                linea += " . "
        print(linea)
    print()


def n_reinas_una_solucion(n: int) -> List[int] | None:
   
    # tablero[i] = columna de la reina en la fila i
    tablero = [-1] * n

    # conjuntos para controlar ataques
    columnas = set()          # columnas ocupadas
    diag_principal = set()    # (fila - col) ocupadas
    diag_secundaria = set()   # (fila + col) ocupadas

    def backtrack(fila: int) -> bool:
        # Si ya colocamos reinas en todas las filas -> solución encontrada
        if fila == n:
            return True

        for col in range(n):
            # Comprobar si esta posición está bajo ataque
            if col in columnas:
                continue
            if (fila - col) in diag_principal:
                continue
            if (fila + col) in diag_secundaria:
                continue

            # Colocamos la reina
            tablero[fila] = col
            columnas.add(col)
            diag_principal.add(fila - col)
            diag_secundaria.add(fila + col)

            # Llamada recursiva
            if backtrack(fila + 1):
                return True  # ya encontramos una solución

            # Retroceso (backtracking)
            tablero[fila] = -1
            columnas.remove(col)
            diag_principal.remove(fila - col)
            diag_secundaria.remove(fila + col)

        # Si no se pudo colocar reina en esta fila, no hay solución por este camino
        return False

    if backtrack(0):
        return tablero
    else:
        return None


def n_reinas_todas(n: int) -> List[List[int]]:
   
    tablero = [-1] * n
    columnas = set()
    diag_principal = set()
    diag_secundaria = set()
    soluciones: List[List[int]] = []

    def backtrack(fila: int) -> None:
        if fila == n:
            # Copiamos la solución actual y la guardamos
            soluciones.append(tablero.copy())
            return

        for col in range(n):
            if col in columnas:
                continue
            if (fila - col) in diag_principal:
                continue
            if (fila + col) in diag_secundaria:
                continue

            tablero[fila] = col
            columnas.add(col)
            diag_principal.add(fila - col)
            diag_secundaria.add(fila + col)

            backtrack(fila + 1)

            # Retroceder
            tablero[fila] = -1
            columnas.remove(col)
            diag_principal.remove(fila - col)
            diag_secundaria.remove(fila + col)

    backtrack(0)
    return soluciones


if __name__ == "__main__":
    n = int(input("Ingresa el valor de N: "))

    print("\n--- Una solución ---")
    sol = n_reinas_una_solucion(n)
    if sol is None:
        print("No existe solución para N =", n)
    else:
        print("Representación (fila -> columna):", sol)
        imprimir_tablero(sol)

    print("\n--- Todas las soluciones ---")
    sols = n_reinas_todas(n)
    print(f"Cantidad de soluciones para N = {n}: {len(sols)}")

    # Si quieres, imprime todas (para N pequeño)
    if n <= 6:
        for i, s in enumerate(sols, start=1):
            print(f"Solución {i}: {s}")
            imprimir_tablero(s)
