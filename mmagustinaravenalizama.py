def mm(A,B): #definir mm en parametro A,B
    BT = list(zip(*B)) #BT es igual a la lista zip en b pero traspuesta

    C = []   #definir C como resultado de la multiplicacion
    for fila in A:  #definir fila A y columna BT
        nueva_fila =[]
        for col in BT:
            valor = sum(x * y for x,y in zip(fila,col))  #definir valor como suma de la multiplicacion de x por y en combinacion horizontal de fila y columna
            nueva_fila.append(valor)  #se le agrega a nueva_fila la variable valor y la variable c se le agrega la variable nueva fila
        C.append(nueva_fila)
    return C  #devuelve el valor en C


#ejemplo
A = [[1,2,3],
     [4,5,6]]

B= [[7,8],
    [9,10],
    [11,12]]

#para la funcion mm, imprime el resultado del ejemplo
for fila in mm(A,B):
    print(fila)