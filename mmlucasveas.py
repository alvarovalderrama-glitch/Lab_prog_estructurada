def mm(A, B):
    BT = list(zip(*B)) # Transponer B

    C = [] 
    for fila in A: # Iterar sobre filas de A
        nueva_fila = []
        for col in BT: # Iterar sobre filas de B transpuesta (columnas de B)
            valor = sum(x * y for x, y in zip(fila, col)) # Producto punto
            nueva_fila.append(valor) 
        C.append(nueva_fila) 
    return C 

#Ejemplo 

A = [[1, 2, 3], #matriz 2x3
     [4, 5, 6]]
B = [[7, 8],  #matriz 3x2 y 4x2
     [9, 10],
     [11, 12],
     [13, 14]]


for fila in mm(A, B):
    print(fila)
