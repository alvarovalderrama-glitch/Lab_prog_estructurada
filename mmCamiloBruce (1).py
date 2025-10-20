def mm(A, B):
    BT = list(zip(*B)) # Transpone la matriz B

    C=[]  # Crea una nueva matriz vacia
    for fila in A:
        nf=[] 
        for col in BT:
            valor = sum(x*y for x, y in zip(fila,col)) #Multiplica las filas y columnas, despues las suma.
            nf.append(valor) 
        C.append(nf) # Ingresa los resultados a la matriz vacia
    return C # Entrega la matriz C con los resultados

# Ejemplo
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6],
     [7, 8]]

for fila in mm(A, B):
    print(fila)