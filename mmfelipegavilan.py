#Se define una funcion para multiplicar matrices
def mm(A,B):
#Se traspone la matriz B
    BT = list(zip(*B))
#Matriz C
    C = []
    #Recorre las filas de A
    for fila in A:
        nueva_fila = []
        #Recorre las columnas de B
        for col in BT:
            #Se multiplican y suman los valores de la fila y columna
            valor = sum(x *y for x, y in zip(fila, col))
            nueva_fila.append(valor)
            #El resultado se agrega a la matriz C
        C.append(nueva_fila)
    return C

#Ejemplo #Depende el resultado de lo escrito
A = [[1,2,3,],[3,5,6]] 
B = [[7,8],[9,10],[11,12]]

#Muestra la Matriz 
for fila in mm(A,B):
    print(fila)