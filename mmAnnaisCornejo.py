#Define una función que recibe dos matrices A y B.
def mm(A, B):
    BT = list(zip(*B))
    #Traspone la matriz B, convierte sus columnas en filas.

    C = [] #Crea una lista vacía, para guardar la matriz resultante.
    
    for fila in A: #Recorre cada fila de matriz A
        nueva_fila = [] #Crea una lista vacía para la nueva fila de la matriz C (Resultante)
        for col in BT: #Recorre cada columna de matriz B (ahora son filas en BT)
            valor = sum(x * y for x, y in zip(fila,col)) #Calcula el producto entre fila A y columna B
            nueva_fila.append(valor) #Agrega el resultado a la nueva fila
        C.append(nueva_fila) #Agrega la nueva fila a la matriz C (Resultante)
    return C #Retorna a la matriz resultante.

#Ejemplo
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

for fila in mm(A, B):
    print(fila)
