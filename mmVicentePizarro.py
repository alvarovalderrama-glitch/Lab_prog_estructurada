def mm(A,B):                        # se define la funcion mm (matriz)
    BT=list(zip(*B))              # se crea una lista de la matriz B traspuesta

    C=[]                            # se crea la variable C                  
    for fila in A:
        nueva_fila=[]               # se crea la variable nueva_lista
        for col in BT:
            valor=sum(x*y for x,y in zip(fila,col)) # se hace multiplican las filas por las columnas y luego se suman
            nueva_fila.append(valor)   # se agrega el valor de la suma de las multiplicaciones a la lista
        
        C.append(nueva_fila)      # se agrega la fila antes creada a una matriz
    return C                      # devuelve la variable C

A= [1,2,3],[4,5,6]
B= [[7,8],[9,10],[11,12]]

for fila in mm(A,B):     
    print(fila)      # se imprime el resultado de la multiplicacion  de matrices
