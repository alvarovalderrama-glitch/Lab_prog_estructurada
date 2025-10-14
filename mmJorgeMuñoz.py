def mm(A, B):
    BT = list(zip(*B))  
    # (*B) desempaqueta la matriz B, pasando sus 3 filas como argumentos individuales de zip(): [7, 8], [9, 10], [11, 12]
    # zip(...) agrupa los elementos de igual posicion y los forma en tuplas: (7, 9, 11), (8, 10 ,12)
    # list(...) convierte el zip(...) en una lista: [(7, 9, 11), (8, 10, 12)]
    """
    BT = [(7, 9, 11),
         (8, 10, 12)]
    """
    # por lo tanto BT es la transpuesta de B, dado que cada columna de B ahora es una fila de BT
    
    C = []  # crea una nueva lista vacía y la asigna a la variable C
    for fila in A:  # este for recorre cada fila de A: [1, 2, 3], [4, 5, 6]
        nueva_fila = []  # crea una lista vacía donde se agregarán los valores obtenidos a continuación
        for col in BT:  # recorre las filas de BT (columnas de B): (7, 9, 11), (8, 10, 12)
            valor = sum(x * y for x, y in zip(fila, col))
            # zip(fila, col) genera pares de elementos: (1, 7), (2, 9), (3, 11)
            # (x * y for x, y in zip(...)) recorre zip(...), donde (x) es el valor de la fila de A e (y) es el valor de la fila de BT. luego multiplica (x * y). ejemplo: 1 * 7
            # sum(...) suma cada producto de (x * y) y asigna el resultado final a la variable valor

            nueva_fila.append(valor)  # agrega valor a la lista nueva_fila. ejemplo: valor == 58   =>   nueva_fila == [58]
        C.append(nueva_fila)  # despues de recorrer cada columna de B, agrega nueva_fila a la lista C
    return C  # devuelve la lista C: [[58, 64], [139, 154]]


# Ejemplo
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]


for fila in mm(A, B):  # recorre cada elemento de C para que se imprima en el formato de una matriz:    [58, 64]
    print(fila)  # imprime el elemento actual de C: primero [58, 64] y luego [139, 154]                 [139, 154]