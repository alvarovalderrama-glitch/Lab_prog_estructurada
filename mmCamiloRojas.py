
# Multiplicación de matrices A x B
def mm(A, B): # Función para multiplicar dos matrices
    BT = list(zip(*B))  # Transpone la matriz B (convierte columnas en filas)

    C = []  # Matriz resultante

    for fila in A:  # Recorre cada fila de A
        nueva_fila = [] # Nueva fila para la matriz resultante
        for col in BT:  # Recorre cada columna de B (como fila de BT)
            valor = sum(x * y for x, y in zip(fila, col))  # Producto punto
            nueva_fila.append(valor) # Agrega el valor a la nueva fila
        C.append(nueva_fila)  # Agrega la nueva fila a la matriz resultante

    return C # Devuelve la matriz resultante

# Matriz A (2x3)
A = [[1, 2, 3],
     [4, 5, 6]]

# Matriz B (3x2)
B = [[7, 8],
     [9, 10],
     [11, 12]]

# Imprimir el resultado
for fila in mm(A, B):
    print(fila)
