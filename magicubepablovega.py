# Cuadrado Mágico con Backtracking

N = 3  # tamaño del cuadrado mágico 3x3
objetivo = 15  # suma mágica para un cuadrado de 3x3
cuadrado = [[0 for _ in range(N)] for _ in range(N)]
usados = set()


def es_valido(fila, col, num):
    if num in usados:
        return False
    
    # Verificar suma parcial de fila
    suma_fila = sum(cuadrado[fila]) + num
    if suma_fila > objetivo:
        return False

    # Verificar suma parcial de columna
    suma_col = sum(cuadrado[i][col] for i in range(N)) + num
    if suma_col > objetivo:
        return False

    return True


def suma_completa():
    # Filas
    for fila in cuadrado:
        if sum(fila) != objetivo:
            return False

    # Columnas
    for col in range(N):
        if sum(cuadrado[f][col] for f in range(N)) != objetivo:
            return False
    
    # Diagonal principal
    if sum(cuadrado[i][i] for i in range(N)) != objetivo:
        return False
    
    # Diagonal inversa
    if sum(cuadrado[i][N - 1 - i] for i in range(N)) != objetivo:
        return False

    return True


def backtracking(fila, col):
    if fila == N:
        return suma_completa()

    sig_fila = fila + (col + 1) // N
    sig_col = (col + 1) % N

    for num in range(1, 10):
        if es_valido(fila, col, num):
            cuadrado[fila][col] = num
            usados.add(num)

            if backtracking(sig_fila, sig_col):
                return True

            cuadrado[fila][col] = 0
            usados.remove(num)

    return False


if backtracking(0, 0):
    print("Cuadrado mágico encontrado:")
    for fila in cuadrado:
        print(fila)
else:
    print("No existe solución.")
