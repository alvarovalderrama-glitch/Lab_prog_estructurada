sudoku= [              # Sudoku a resolver
[5,0,0,6,2,7,9,4,8],
[0,0,0,0,0,0,0,0,0],
[0,2,0,5,9,4,6,0,0],
[0,0,6,1,0,0,0,0,0],
[0,1,8,0,0,9,0,5,4],
[7,0,0,0,0,0,1,0,9],
[9,6,2,4,0,0,0,8,7],
[3,7,4,9,8,0,0,1,0],
[0,0,5,0,3,6,0,0,2],
]

def mostrar_tablero(sudoku): # Funcion para mostrar el tablero de sudoku
    for i in range(9): # Recorre cada fila del 0 al 8
        if i == 3 or i == 6: # Cada 3 filas...
            print('|-------+-------+-------|') #... Pone un separador
        for j in range(9): # Recorre cada columna
            if j%3==0: # Cada 3 columnas...
                print('| ', end='') # ... Pone un separador
            if sudoku[i][j]: # Si la casilla tiene un numero distinto al 0
                print(str(sudoku[i][j])+' ', end='') # Se muestra ese numero
            else: # Si tiene un 0
                print('. ', end='') # Entonces se reemplaza por un punto.
        print('|') # Cierra el tablero

def validar(sudoku, n, i, j): # Funcion para validar numeros
    fila = sudoku [i]
    col = [f[j] for f in sudoku]
    bloque = [sudoku[a][b] 
            for a in range(9) # Recorre todas las filas
            for b in range(9) # Recorre todas las columnas
            if i//3 == a//3 
            and j//3 == b//3]
    
    if n not in fila and n not in col and n not in bloque: # Si n no esta en la fila, en la columna, y en el bloque
        return True # Se devuelve True
    else: # Si no
        return False # Se devuelve False
     

def solucion(sudoku):
    for i in range(9): # Recorre todas las filas
        for j in range(9): # Recorre todas las columnas
            if sudoku[i][j] == 0: # Si hay un 0 en el tablero
                for n in range(1,10): # Se prueban numeros del 1 al 9
                    if validar(sudoku, n, i, j): # Si el numero es valido
                        sudoku[i][j] = n # Se reemplaza en la casilla actual.
                        if solucion(sudoku): # Se llama recursivamente a la funcion solucion
                            return True # Se retorna True si se encuentra sol.
                        sudoku[i][j]=0 # Si no, la casilla se vacia
                return False # Si ningun numero funciono, se retorna False
    return True # Si no hay casillas vacias, se retorna True

if solucion(sudoku): # Si se encuentra solución
    print('Se ha encontrado solución: \n') # Se notifica que se encontró...
    mostrar_tablero(sudoku) # Y se muestra la solución
else: # Si no se encuentra solución
    print('No se ha encontrado solución') # Se notifica que no se encontró