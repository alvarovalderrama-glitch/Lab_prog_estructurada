
def mm(A,B):
    #Se obtienen las 2 columnas de B en 2 listas
    BT = list(zip(*B))
    C = []
    for fila in A:
        nueva_fila = []
        for col in BT:
            #zip agrupa los valores de las filas y las columnas en listas de tamaño 2
            #se pasa por un for de 2 variables para recorrer cada par y multiplicarlos
            # Se suma el resultado de todas las multiplicaciones 
            valor = sum(x*y for x,y in zip(fila,col))
            nueva_fila.append(valor)
        C.append(nueva_fila)
    return C
#Se definen las matrices A y B
A=[[1,2,3],[4,5,6]]

B=[[7,8],[9,10],[11,12]]
#Se llama a la funcion mm y se mandan las matrice A y B
for fila in mm(A,B):
    print(fila)


