def mm(A, B): #define la funcion mm que recibe dos matrices A y B
    BT = list(zip(*B)) # transpone la matriz B (convierte filas en columnas)
    C = []  # Inicializa la matriz resultado C
    for fila in A:       # Recorre cada fila de la matriz A
        nueva_fila = []   # Crea una nueva fila para la matriz resultado
        for col in BT:     # Recorre cada columna de la matriz B transpuesta
            valor = sum(x * y for x, y in zip(fila, col)) # Calcula el producto punto entre la fila y la columna
            nueva_fila.append(valor)   # Agrega el valor calculado a la nueva fila
        C.append(nueva_fila)  # Agrega la nueva fila a la matriz resultado
    return C   # Devuelve la matriz resultado


A = [[1, 2, 3],
     [4, 5, 6]]    # Matriz A (2x3)

B = [[7, 8],
     [9, 10],   # Matriz B (3x2)
     [11, 12]]

for fila in mm(A, B):  # llama a la funcion y recorre cada fila del resultado
    print(fila)   # Imprime el resultado de multiplicar A * B
