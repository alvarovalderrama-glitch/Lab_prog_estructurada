def mm(A, B):

    BT = list(zip(*B))   # Transpone la matriz B (convierte filas en columnas)

    C = []
    for fila in A:                  # Recorre cada fila de A
        nueva_fila = []
        for col in BT:               # Recorre cada columna de B transpuesta
            valor = sum(x * y for x, y in zip(fila, col))  # Calcula el producto punto
            nueva_fila.append(valor)
        C.append(nueva_fila)
    return C

# Ejemplo de multiplicación de matrices
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

for fila in mm(A, B):
    print(fila)

# Este programa multiplica dos matrices (A de 2x3 y B de 3x2) 
# y devuelve la matriz resultante C de tamaño 2x2.
