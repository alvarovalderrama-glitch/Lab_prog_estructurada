def mm(A,B):
    BT= list(zip(*B))
    C=[]
    for fila in A:
        nueva_fila= []
        print(BT)
        for col in BT:
            valor = sum(x *y for x, y in zip(fila, col))
            nueva_fila.append(valor)
        C.append(nueva_fila)
    return C
    
A= [[1,2,3],
   [4,5,6]]

B= [[7,8],
   [9,10],
   [11,12]]

for fila in mm(A,B):
    print(fila)