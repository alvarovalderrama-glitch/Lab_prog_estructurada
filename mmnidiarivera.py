#Define una función llamada mm que multiplica dos matrices A y B
def mm(A, B):
    #Transpone la matriz B para facilitar el acceso por columnas
    #zip(*B) agrupa los elementos por columnas 
    BT = list(zip(*B)) 
    #Lista donde se almacenará la matriz resultado
    C = []
    #Recorre cada fila de la matriz A
    for fila in A: 
        #Lista para almacenar los valores de la nueva fila de la matriz resultado
        nueva_fila = [] 
        
        #Recorre cada columna de la matriz B transpuesta 
        for col in BT: 
            #Calcula el producto punto entre la fila de A y la columna de B
            valor = sum(x * y for x, y in zip(fila, col)) 
            #Agrega el resultado a la nueva fila
            nueva_fila.append(valor) 

        #Agrega la fila completa a la matriz resultado
        C.append(nueva_fila)

#Devuelve la matriz resultante   
    return C 
# Matriz A (2 filas x 3 columnas)
A = [[1, 2, 3], 
     [4, 5, 6]] 
#Matriz B (3 filas x 2 columnas)
B = [[7, 8],    
     [9, 10],   
     [11, 12]]  
#Imprime cada fila de la matriz resultante de A * B
for fila in mm(A, B): 
    print(fila) 

