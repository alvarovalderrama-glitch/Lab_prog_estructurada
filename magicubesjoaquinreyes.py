def imprimir_tablero(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero)):
            print(tablero[i][j], end = " ") 
        print(" ")
    print(" ")


def es_magico(tablero, suma_magica):
    n = len(tablero)

    # Filas
    for fila in tablero:
        if sum(fila) != suma_magica:
            return False

    # Columnas
    for c in range(n):
        if sum(tablero[f][c] for f in range(n)) != suma_magica:
            return False

    # Diagonales
    if sum(tablero[i][i] for i in range(n)) != suma_magica:
        return False

    if sum(tablero[i][n - 1 - i] for i in range(n)) != suma_magica:
        return False

    return True


def suma_parcial_valida(tablero, fila, col, suma_magica):
    n = len(tablero)

    # comprobar fila
    if all(tablero[fila][c] != 0 for c in range(n)):
        if sum(tablero[fila]) != suma_magica:
            return False
    else:
        if sum(x for x in tablero[fila] if x != 0) > suma_magica:
            return False

    # comprobar columna
    columna = [tablero[r][col] for r in range(n)]
    if all(columna[r] != 0 for r in range(n)):
        if sum(columna) != suma_magica:
            return False
    else:
        if sum(x for x in columna if x != 0) > suma_magica:
            return False

    # diagonal principal
    if fila == col:
        diag1 = [tablero[i][i] for i in range(n)]
        if all(diag1[i] != 0 for i in range(n)):
            if sum(diag1) != suma_magica:
                return False
        else:
            if sum(x for x in diag1 if x != 0) > suma_magica:
                return False

    # diagonal secundaria
    if fila + col == n - 1:
        diag2 = [tablero[i][n - 1 - i] for i in range(n)]
        if all(diag2[i] != 0 for i in range(n)):
            if sum(diag2) != suma_magica:
                return False
        else:
            if sum(x for x in diag2 if x != 0) > suma_magica:
                return False

    return True


def resolver_cuadrado_magico(n):
    tablero = [[0] * n for _ in range(n)]
    usados = set()
    suma_magica = n * (n*n + 1) // 2
    encontrado=0

    def backtracking(pos):
        nonlocal encontrado
        if pos == n*n:
            if pos==n*n:
                return [fila[:] for fila in tablero]
            
            else:
                return None
            

        fila = pos // n
        col = pos % n

        for num in range(1, n*n + 1):
            if num not in usados:
                tablero[fila][col] = num
                usados.add(num)

                if suma_parcial_valida(tablero, fila, col, suma_magica):
                    resultado=backtracking(pos + 1)
                    if resultado:
                        return resultado

                tablero[fila][col] = 0
                usados.remove(num)
        return None
    solucion=backtracking(0)
    return solucion
n = int(input("Ingresa el tamaño del tablero: "))
solucion = resolver_cuadrado_magico(n)

if solucion:
    imprimir_tablero(solucion)
else:
    print("No hay solución para un tablero de tamaño", n)



