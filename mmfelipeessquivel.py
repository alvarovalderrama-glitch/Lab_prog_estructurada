def mm(A, B): #define la funcion mm que recibe dos matrices A y B
    BT = list(zip(*B)) #transpone la matriz B

    C = [] #crea una nueva matriz C vacia
    for fila in A: #recorre cada fila de la matriz A
        nueva_fila = [] #crea una nueva fila vacia
        for col in BT: #recorre cada columna de la matriz transpuesta B
            valor = sum(x * y for x, y in zip(fila, col)) # calcula el producto punto entre la fila de A y la columna de B
            nueva_fila.append(valor) # agrega el valor calculado a la nueva fila
        C.append(nueva_fila) # agrega la nueva fila a la matriz C
    return C #retorna la matriz C



# Ejemplo
A = [[1, 2, 3],  #define la matriz A
   [4, 5, 6]]

B = [[7, 8],  #define la matriz B
   [9, 10],
   [11, 12]]

for fila in mm(A, B): #imprime cada fila de la matriz resultante
    print(fila) #imprime cada fila de la matriz resultante