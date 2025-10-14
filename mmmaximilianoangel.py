def mm(A, B): # Define una función con el nombre "mm" y le asigna los parametros (A, B), que en este caso son 2 matrices.
    BT = list(zip(*B)) # Crea la variable "BT" a la que se asigna "list(zip(*B))", esto último hace que la matriz B se transponga (Convierte filas en columnas)
                       # y hace que cada columna sea una tupla (por lo que los elementos de BT serán tuplas).

    C = [] # Variable "C" que inicialmente esta vacía, pero será la matriz resultante. 
    for fila in A: # Ciclo repetitivo "for" que recorre cada fila de la matriz A.
        nueva_fila = [] # Crea una lista vacía que almacenará los valores de la nueva fila.
        for col in BT: # Recorre las columnas de la matriz BT.
            # A la variable "valor" se le asigna "sum(x * y for x, y in zip(fila, col))", lo que es el producto punto entre la fila A y la columna B.
            valor = sum(x * y for x, y in zip(fila, col)) 
            nueva_fila.append(valor) # Se le agrega a la variable "nueva_fila" el resultado de "valor".
        C.append(nueva_fila) # Agrega "nueva_fila" (Ya contiene "valor") a la variable "C".
    return C # Da como resultado la variable "C", que será una matriz.

# Ejemplo

while True:
    # Se imprime un menú para seleccionar el tamaño de las matrices.
    print("""
|=================Tamaño de matrices=================|
    1.- Matriz A = 2x3 y Matriz B = 3x2 (Original)
    2.- Matriz A = 2x3 y Matriz B = 4x2
    3.- Salir.
|====================================================|
 """)
    seleccion = input("Ingrese la opción que desea usar: \n> ") # Se crea la variable "seleccion" que será un "input" que se le leerá como una cadena de texto (string).
    if seleccion == "1": # Condicional "if" que ejucatará lo que esta a continuación si la variable "seleccion" es igual a "1". 
        A = [[1, 2 ,3], # Matriz A de 2x3
            [4, 5 ,6]]

        B =  [[7, 8], # Matriz B de 3x2
            [9, 10], 
            [11, 12]]
        
        print("Matrices (2x3) y (3x2)")
        for fila in mm(A, B): # Imprime cada fila resultante de la multiplicación de A y B
            print(fila)


    elif seleccion == "2": # Condicional "elif" que ejucatará lo que esta a continuación si la variable "seleccion" es igual a "2".
        A = [[1, 2 ,3], # Matriz A de 2x3
            [4, 5 ,6]]

        B =  [[7, 8], # Matriz B de 4x2
            [9, 10], 
            [11, 12],
            [13, 14]]

        print("Matrices (2x3) y (4x2)")
        for fila in mm(A, B): # Imprime cada fila resultante de la multiplicación de A y B
            print(fila)


    elif seleccion == "3": # Condicional "elif" que ejucatará lo que esta a continuación si la variable "seleccion" es igual a "3".
        break # Rompe / Termina el ciclo "while"
    else: # Si no se cumple ninguna condición anterior se ejecuta lo siguiente.
        print("Opción invalida.") # Imprime el mensaje "Opción invalida."

# La multiplicación de matrices de dimensiones diferentes no es posible, como es el caso de la opción 2, por lo que pese a que nos dará un resultado, este no será correcto, ya que matematicamente no es posible realizar esa operación.
# Zip realiza un truncamiento es por eso que se obtendrá un resultado

# Imprime cada fila resultante de la multiplicación de A y B
#for fila in mm(A, B):
#    print(fila)

