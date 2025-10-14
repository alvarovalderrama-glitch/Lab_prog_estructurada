def mm(A,B):           #Definimos una función que tiene el nombre de mm (de "multiplicación de matrices"), se le pasan como parametros 2 matrices una A y B#
    BT = list (zip(*B))  #Esto crea una versión traspuesta de B, es decir cambia filas por columnas.#

    C=[]               #Creamos una lista vacía C, que será la matriz resultado.#
    for fila in A:       #Recorremos cada fila de A 
        nueva_fila= []   #Creamos una lista vacía donde iremos guardando los valores de una nueva fila del ressultado.#
        for col in BT:    #Recorremos cada columna de B, que ahora esta en BT
            valor= sum(x*y for x, y in zip(fila,col))    #Aqui hacemos el producto punto entre una fila de A y una columna de B.
            nueva_fila.append(valor)   #Agregamos el valor de cada suma a la lista nueva_fila.#
        C.append(nueva_fila)    #Cuando terminamos con todas las columnas, agregamos la fila completa a C.#
    return C    #Devolvemos la Matriz Resultado.

#Ejemplo
A =[[1,2,3],                  #Estas son las matrices que nos dan para ejecutar el código.
   [4,5,6]]

B =[[7,8],
    [9,10],
    [11,12]]

for fila in mm(A,B):      #Llama a mm(A,B), itera las filas devueltas y las imprime una por una.#
    print(fila)      