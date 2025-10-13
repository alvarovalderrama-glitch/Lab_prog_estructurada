def mm(A, B):                           # función que multiplica la matriz A por la matriz B
    BT = list(zip(*B))                  # transponer B (cada tupla en BT es una columna de B)

    C = []                              # inicializar la matriz resultado vacía
    for fila in A:                      # para cada fila de A
        nueva_fila = []                 # crear la lista que contendrá la fila resultante
        for col in BT:                  # para cada columna de B (usando BT)
            valor = sum(x * y for x, y in zip(fila, col))  # producto punto fila·columna
            nueva_fila.append(valor)    # añadir el valor calculado a la nueva fila
        C.append(nueva_fila)            # añadir la nueva fila a la matriz resultado
    return C                            # devolver la matriz resultado


# Ejemplo de uso:
A = [[1, 2, 3],                         # matriz A (2x3)
     [4, 5, 6]]

B = [[7, 8],                            # matriz B (3x2)
     [9, 10],
     [11, 12]]

for fila in mm(A, B):                   # llamar mm(A, B) e imprimir cada fila del resultado
    print(fila)                         # imprime: [58, 64] y luego [139, 154]

        