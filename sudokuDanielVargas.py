tablero_sudoku=[
    [0,0,9,0,0,0,4,0,0],
    [1,7,0,0,0,0,0,0,0],
    [6,0,0,0,0,0,0,1,0],
    [0,0,0,0,6,0,0,7,0],
    [0,0,2,5,0,0,8,0,4],
    [0,0,0,2,0,0,1,0,0],
    [0,4,0,6,7,8,0,0,9],
    [0,0,0,0,0,0,0,0,8],
    [5,3,0,0,4,0,0,0,0]
]


def mostrar_tablero(tablero_sudoku):
    print('\n-------------------------------')
    for fila in range(9):
        for columna in range(9):
            if columna==0: # Las casillas de la 1ra columna tendrán una línea a su izquierda
                print(f'| {tablero_sudoku[fila][columna]:1}',end='  ')
            elif columna==2 or columna==5 or columna==8: # Las columnas 3, 6 y 9 tendrán una línea divisora vertical
                print(f'{tablero_sudoku[fila][columna]:1}',end=' | ')
            else: # Solo se imprime la casilla sin niguna línea
                print(f'{tablero_sudoku[fila][columna]:1}',end='  ')
        print('')
        if fila==2 or fila==5 or fila==8: # Luego de la fila 3, 6 y 9 se imprime una línea divisora hoeizontal
            print('-------------------------------')


def validar_posicion(tablero_sudoku,x,y,numero):
    fila=tablero_sudoku[x]
    
    columna=[]
    for filas in tablero_sudoku: # Recorre el tablero completo y solo se adjunta la posición "y" de cada fila
        columna.append(filas[y])
        
    cuadrado=[]
    # Da las coordenadas de la esquina superior izquierda un cuadrado en específico
    cuadrado_x=(x//3)*3
    cuadrado_y=(y//3)*3
    
    # Se recorre el cuadrado elegido
    for i in range(3):
        for j in range(3):
            cuadrado.append(tablero_sudoku[cuadrado_x+i][cuadrado_y+j]) # Se construye el cuadrado 3x3

    # Se recorre "fila", "columna" y "cuadrado" para comprobar que no se encuentre "numero"
    if (numero not in fila) and (numero not in columna) and (numero not in cuadrado):
        return True
    else:
        return False


def resolver_sudoku(tablero_sudoku):
    
    # Se revisa cada casilla
    for x in range(9):
        for y in range(9):
            
            if tablero_sudoku[x][y]==0: # Comprueba que esté vacía
                for numero in range(1,10): # Prueba del número 1 hasta el 9
                    if validar_posicion(tablero_sudoku,x,y,numero): # Si no es válido, prueba el siguiente número
                        tablero_sudoku[x][y]=numero
                        if resolver_sudoku(tablero_sudoku):
                            return True
                        tablero_sudoku[x][y]=0
                        
                return False 
    return True # Cuando las llamadas de "resolver_sudoku" son True y "for" termina, la función devuelve True (hay solución)                   
                    
        
        
        
#=============================================================================================================================        

print('\n====================================================================================================================')
print('Este es el tablero a resolver:')     
mostrar_tablero(tablero_sudoku)
input('\nSi es así, presiona Enter para continuar')

print('\nEncontrando la solución. Espere unos segundos...')

if resolver_sudoku(tablero_sudoku):
    print('\n====================================================================================================================')
    print('\nHay solución:')
    mostrar_tablero(tablero_sudoku)
    print('\nFIN DEL PROGRAMA\n')
    print('====================================================================================================================\n')
else:
    print('\n====================================================================================================================')
    print('\nEste tablero no tiene solución')