def mm(A,B):
    BT = list(zip(*B)) 
    # Primero se aplica un asterisco a B dentro de la función zip() para poder separar cada lista de B y dejar cada una como
    # un argumento para zip(). Después, la propia función zip() mezcla las posiciones de ambas listas para crear tuplas, cada 
    # una con elementos que compartían la misma posición. Por último, la función list() ordena las tuplas en una lista.
    
    C = [] # Se define C como una lista vacía, almacenando cada fila resultante.
    for fila in A: # "fila" recorrerá cada elemento de A y tomará la lista de esa posición para poder operar más adelante. 
        nueva_fila = [] # Se define una nueva fila resultante para C, de momento vacía. En total se repite 2 veces.
        for col in BT: # "col" recorre las filas de BT pero siendo realmente las columnas de B, que es [(7,9,11),(8,10,12)].
            valor = sum(x * y for x, y in zip(fila,col)) 
            # zip() mezclará las listas de A y B para formar tuplas sueltas, es decir, que no estarán organizadas en una lista.
            # Se crearán tuplas de la forma (x,y), y es por eso que aparecen las variables "x" y "y". Repetirá esta acción
            # hasta 3 veces, porque se forman 3 tuplas. Luego de operar 3 veces con cada tupla, se suma el resultado de cada 
            # multiplicación, dando la variable "valor",
            nueva_fila.append(valor) 
            # "valor" (siendo un número) se asigna como un elemento de una nueva lista para "nueva_fila". Cómo inicialmente 
            # estaba vacía, ahora es cuando por fin tienen un elemento. Esto se repetirá hasta dos veces, que sería la cantidad 
            # de filas que tienen "BT". Cuando se haya repetido por 2da vez, es cuando termina este ciclo "for".
        C.append(nueva_fila)
        # "nueva_fila" debería ser una fila que es representada por una lista, en este caso siendo [58,64], que luego es añadida
        # como un elemento de la lista C, algo como [[58,64]] (una lista dentro de una lista). Ahora el ciclo "for" se repetirá
        # trabajando con la 2da fila de A.
    return C
    # Saca el resultado de C fuera de la función para que pueda usarse sin problemas. 

# Ejemplo
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]

for fila in mm(A, B):
    print(fila)
# Como arriba se usó "return C" y se quiere imprimir cada fila de la matriz resultante, cada vez que termine la función "mm", 
# "fila" tomará la primera iteración, siendo [58,64], y luego tomará la 2da iteración, ahora siendo [139,154].