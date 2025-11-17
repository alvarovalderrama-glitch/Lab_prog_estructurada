def resolver_cuadrado_magico(n):
    cuadrado = [[0 for _ in range(n)] for _ in range(n)]
    numeros_usados = [False] * (n*n + 1)
    suma_magica = n * (n*n + 1) // 2
    
    def es_seguro(fila, col, num):
        # Comprobar si el número ya está usado
        if numeros_usados[num]:
            return False

        # Comprobar sumas parciales de fila y columna
        cuadrado[fila][col] = num
        
        # Comprobar suma de fila
        suma_fila = sum(cuadrado[fila][:col+1])
        if col == n - 1 and suma_fila != suma_magica:
            cuadrado[fila][col] = 0
            return False
        if suma_fila > suma_magica:
            cuadrado[fila][col] = 0
            return False

        # Comprobar suma de columna
        suma_col = sum(cuadrado[i][col] for i in range(fila+1))
        if fila == n - 1 and suma_col != suma_magica:
            cuadrado[fila][col] = 0
            return False
        if suma_col > suma_magica:
            cuadrado[fila][col] = 0
            return False

        # Comprobar suma de diagonales solo si están completas
        if fila == n - 1 and col == n - 1:
            suma_diag1 = sum(cuadrado[i][i] for i in range(n))
            if suma_diag1 != suma_magica:
                cuadrado[fila][col] = 0
                return False
        
        if fila == n - 1 and col == 0:
             suma_diag2 = sum(cuadrado[i][n - 1 - i] for i in range(n))
             if suma_diag2 != suma_magica:
                cuadrado[fila][col] = 0
                return False

        return True

    def encontrar_celda_vacia():
        for r in range(n):
            for c in range(n):
                if cuadrado[r][c] == 0:
                    return r, c
        return -1, -1
    
    def backtrack():
        fila, col = encontrar_celda_vacia()
        
        if fila == -1: 
            return True

        for num in range(1, n*n + 1):
            if es_seguro(fila, col, num):
                numeros_usados[num] = True
                cuadrado[fila][col] = num

                if backtrack():
                    return True

                cuadrado[fila][col] = 0
                numeros_usados[num] = False
        
        return False 
    if backtrack():
        return cuadrado
    else:
        return None

def imprimir_cuadrado(cuadrado):
    if not cuadrado:
        print("No se encontró solución")
    else:
        for fila in cuadrado:
            print(" ".join(str(num) for num in fila))

# Ejemplo de uso para un cuadrado de 3x3
n = 4
resultado = resolver_cuadrado_magico(n)
imprimir_cuadrado(resultado)