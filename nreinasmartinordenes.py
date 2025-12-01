def reinas_valid(fila, col, reinas):
    for r in range(fila):
        if col == reinas[r]:
            return False
        
        if abs(col - reinas[r]) == abs(fila - r):
            return False
    return True

def casilla(fila, col):
    letra = chr(ord('A') + col) # reemplaza los numeros de las columnas con las letras del ajedrez
    número = fila + 1
    return f'{letra}{número}'

def p_reinas(fila, reinas, n):
    if fila == n:
        solucion = [casilla(i, reinas[i]) for i in range(n)]
        print(solucion)
        return 1
    
    sol_total = 0
    for col in range(n):
        if reinas_valid(fila, col, reinas):
            reinas[fila] = col
            sol_total += p_reinas(fila + 1, reinas, n)

    return sol_total

def n_reinas(n):
    reinas = [-1] * n
    return p_reinas(0, reinas, n)

n = int(input('elija un numero para el tamaño del tablero: '))
print("soluciones totales:", n_reinas(n))