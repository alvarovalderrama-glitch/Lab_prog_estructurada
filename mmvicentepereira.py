def mm(A, B): #se define una funcion, de 2 paramatros, que son matrices
    BT=list(zip(*B)) #transpone la matriz B, conviertiendo las filas en columnas
    C=[] #Aqui se almacena la matriz resultante
    for fila in A: # para cada fila de a 
        nueva_fila= [] #aqui se guarda las filas nuevas de C
        for col in BT: #para cada columna de matriz BT
        
            valor = sum(x * y for x, y in zip(fila,col))
            nueva_fila.append(valor) #agregar el valor a la nueva fila
        C.append(nueva_fila) #agregar nueva fila a C
    return C #devolver C 

#Ejemplo
A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]
for fila in mm(A,B): #imprimir cada fila del resultado
    print(fila)