# ---- Define la función mm para los parametros A y B ----

def mm(A, B): # Multiplicación de matrices
    BT = list(zip(*B)) # zip empareja en tuplas los elementos
                       # (en la misma iteración) de la lista B
    C = []
    for fila in A:
        nueva_fila = []
        for col in BT:  # Recorremos cada columna de la matriz B
            valor = sum(x * y for x, y in zip(fila, col))
            nueva_fila.append(valor) # Agregamos el valor calculado a la fila del resultado
        C.append(nueva_fila) # Una vez terminada la fila, la agregamos a la matriz resultado
    return C

A = [[1, 2, 3],[4, 5, 6]]

B = [[7, 8], [9, 10], [11, 12]]

for fila in mm(A, B):
    print(fila)