import random

tab = [[0 for _ in range(9)] for _ in range(9)]
max_tab = len(tab)
numeros = [1,2,3,4,5,6,7,8,9]


def validacion(tab,num,fila,columna):

    for j in range(max_tab):
        if tab[fila][j] == num:          #revisa fila
            return False
        
    for i in range(max_tab):
        if tab[i][columna] == num:       #revisa columna
            return False
        
    in_fila_bloque = (fila//3)*3      # inicio de filas y columnas, da inicio a cada bloque dando 0, 3 o 6
    in_columna_bloque = (columna//3)*3

    for i in range(in_fila_bloque, in_fila_bloque + 3):         #se suma 3 debido a si es de 0 a 3, de 3 a 6 o de 6 a 9
        for j in range(in_columna_bloque,in_columna_bloque + 3):  #recorre fila y columnas del bloque
            if tab[i][j] == num:          #si el numero ya existe en el bloque
                return False #retornamos falso 
            
    return True


def imprimir_sudoku(tab):
    for i in tab:
        for j in i:
            print(j, end= " ")
        print()

  # crea numeros aleatorios para el sudoku
def randomnum_sudoku(tab):
    maximo = 10
    cantidad = 0
    while cantidad < maximo:
        num = random.choice(numeros) #numero aleatorio de la lista numeros
        numx = random.randint(0,max_tab-1)          #fila aleatoria de numero aleatorio
        numy = random.randint(0,max_tab-1)          #columna aleatoria de numero aleatorio
        if validacion(tab,num,numx,numy) and tab[numx][numy] == 0:               #validamos con la función y si no hay numero...
            tab[numx][numy] = num            #se coloca y se suma 1 a la cantidad
            cantidad += 1

    return tab


def backtracking_sudoku(tab):
    for i in range (max_tab):
       for j in range (max_tab):
           if tab[i][j] == 0:          #busca la primera posicion vacia
               for num in numeros:      #prueba numeros del 1 al 9
                   if validacion (tab,num,i,j):     #valida si se puede colocar el numero
                       tab[i][j] = num          #coloca el numero
                       if backtracking_sudoku(tab):      #llamada recursiva
                           return True
                       tab[i][j] = 0           #si no funciona, retrocede
               return False        #si ningun numero funciona, retorna falso
    return True         #si el tablero esta completo, retorna verdadero





print("Sudoku inicial:")
imprimir_sudoku(randomnum_sudoku(tab))
if backtracking_sudoku(tab):
    print("Sudoku resuelto:")
    imprimir_sudoku(tab)
else:
    print("No se pudo resolver el Sudoku")