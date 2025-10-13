def mm(A,B):
    # Calcula la matriz traspuesta de B y obtiene sus columnas como tuplas.
    BT=list(zip(*B))
    # Se genera una nueva matriz resultante.
    C=[]
    for fila in A:
        nueva_fila=[]
        # Para cada columna traspuesta de B.
        for col in BT:
            # producto punto: empareja elemtos de filas y columnas para multiplicarlos y luego sumarlos.
            valor=sum(x*y for x, y in zip(fila,col))
            nueva_fila.append(valor)
        C.append(nueva_fila)
    return C

# Ejemplo de uso al multiplicar matrices 2x3 3x2.
A=[[1,2,3],
   [4,5,6]]

B=[[7,8],
   [9,10],
   [11,12]]

for fila in mm(A,B):
    print(fila)