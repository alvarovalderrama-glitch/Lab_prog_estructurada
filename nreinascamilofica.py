def es_seguro(tablero, fila, col, n):
    # Verificar columna 
    for i in range(fila):
        if tablero[i] == col:
            return False

    # Verificar diagonal izquierda 
    i = fila - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if tablero[i] == j:
            return False
        i -= 1
        j -= 1

    # Verificar diagonal derecha 
    i = fila - 1
    j = col + 1
    while i >= 0 and j < n:
        if tablero[i] == j:
            return False
        i -= 1
        j += 1

    return True


def resolver_n_reinas(tablero, fila, n, soluciones):
 
    if fila == n:
        soluciones.append(tablero[:])  # Guardar copia de la solución
        return

    # Intentar poner la reina en cada columna de la fila actual
    for col in range(n):
        if es_seguro(tablero, fila, col, n):
            tablero[fila] = col
            resolver_n_reinas(tablero, fila + 1, n, soluciones) #aqui ocurre lo llamado funcion recursiva
           


def n_reinas(n):
    tablero = [-1] * n  # tablero[i] = columna donde se ubica la reina en la fila i
    soluciones = []
    resolver_n_reinas(tablero, 0, n, soluciones)
    return soluciones




n = 4
sol = n_reinas(n)

print(f"Total soluciones para {n} reinas:", len(sol))
for s in sol:
    print(s)
