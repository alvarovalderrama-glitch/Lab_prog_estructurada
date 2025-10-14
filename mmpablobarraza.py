def mm(A,B):   # se crea la funcion mm
    BT = list(zip(*B)) #Esto intercambia las filas por columnas de B. por ejemplo convierte B (3x2) en BT (2x3).

    C = []
    for fila in A: # Esto recorre cada fila de la matriz A. primera iteración → fila = [1, 2, 3] segunda iteración → fila = [4, 5, 6]
        nueva_fila = [] # crea una lista vacia en nueva_fila
        for col in BT: # primera iteración → col = (7, 9, 11) segunda iteración → col = (8, 10, 12) (2ª columna de B)
            valor = sum(x * y for x,y in zip(fila,col)) # Esto multiplica elemento a elemento los valores de fila y col y los suma. se guarda en nueva_fila
            nueva_fila.append(valor) # Para la primera fila de A → obtiene [58, 64] Para la segunda fila de A → obtiene [139, 154]
        C.append(nueva_fila)
    return C

# Ejemplo

A = [[1,2,3],  # se da el valor a A
     [4,5,6]]

B = [[7,8],    # se da el valor de B
     [9,10],
     [11,12]]

for fila in mm(A,B): # se llama a la funcion y el for imprime cada fila 
    print(fila) # se imprime fila y da resultado C = [[58, 64],[139, 154]]
