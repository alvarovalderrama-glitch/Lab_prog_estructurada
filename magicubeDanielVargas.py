def movimiento(actual_x,actual_y):
    nueva_x=actual_x+1
    if nueva_x<medida and actual_y<medida: # Si X e Y siguen en el tablero se avanza a la casilla de la derecha.
        nueva_y=actual_y
        return nueva_x,nueva_y
    elif nueva_x==medida and actual_y==medida-1: # Si está al final del tablero, se corrigen para que queden dentro.
        nueva_x=medida-1
        nueva_y=medida-1
        return nueva_x,nueva_y
    elif nueva_x==medida and actual_y<medida: # Si X está afuera del tablero e Y sigue dentro, se avanza a la siguiente fila.
        nueva_x=0
        nueva_y=actual_y+1
        return nueva_x,nueva_y
    
def final_del_tablero(medida,actual_x,actual_y):
    if actual_x==actual_y==medida-1: # Se comprueba que las coordenadas actuales estén al final del tablero.
        return True
    else:
        return False
    
def cuadrado_magico():
    sumas_filas=[]
    sumas_columnas=[]
    
    diagonal1=[]
    diagonal2=[]
    sumas_diagonales=[]
    
    for fila in tablero: # Se guardan las sumas de todas las filas.
        suma_f=sum(fila)
        sumas_filas.append(suma_f)

    tablero_columnas=list(zip(*tablero))
    for columna in tablero_columnas: # Se guardan las sumas de todas las columnas.
        suma_c=sum(columna)
        sumas_columnas.append(suma_c)
    
    for i in range(medida): # Se guarda la suma de la diagonal 1.
        diagonal1.append(tablero[i][i])
    sumas_diagonales.append(sum(diagonal1))
        
    for i in range(medida): # Se guarda la suma de la diagonal 2.
        diagonal2.append(tablero[i][medida-1-i])
    sumas_diagonales.append(sum(diagonal2))   
    
    # Se comparan todas las sumas de filas, columnas y diagonales.
    for i in sumas_filas:
        for j in sumas_columnas:
            for k in sumas_diagonales:
                if i==j==k:
                    es_magico=1
                else:
                    return False
    if es_magico==1:
        return True 
    
def retroceder(nueva_x,nueva_y):
    actual_x=nueva_x-1
    if actual_x<0: # Si X está afuera del tablero, se corrige y se retrocede a la fila anterior.
        actual_x=medida-1
        actual_y=nueva_y-1
        return actual_x,actual_y
    else:
        actual_y=nueva_y # Si X está adentro, los valores de X y Y se mantienen.
        return actual_x,actual_y
    
def mostrar_tablero(tablero):
    print('')
    for fila1 in range(medida):
        for columna1 in range(medida):
            print(f'{tablero[fila1][columna1]:2}',end=' |') # Cada casilla del tablero ocupa dos espacios y termina con ' |' 
        print('')
        lineas='-'*(medida*4) # Linea que se dibuja entre las filas
        print(lineas)

def siguiente_opcion(numero_actual,nueva_x,nueva_y):
    hay_repeticion=0
    while numero_actual<=medida**2: # Se suma 1 hasta que el número no esté repetido o esté fuera del rango.
        numero_actual=numero_actual+1
        for i in range(medida):
            for j in range(medida):
                if tablero[i][j]==numero_actual:
                    hay_repeticion=1
        if hay_repeticion==0:
            break
        else:
            hay_repeticion=0
    return numero_actual 

def encontrando_cuadrado(medida,tablero):
    solucion=False
    actual_x=0
    actual_y=0
    numero_actual=1
    tablero[actual_y][actual_x]=numero_actual # La primera casilla empieza con 1.
    
    while not solucion and actual_y>=0: # Hasta que haya una solución o la coordenada Y se vuelva negativa por el backtracking.
        nueva_x,nueva_y=movimiento(actual_x,actual_y) # Entrega las coordenadas de la siguiente posición.
        tablero[nueva_y][nueva_x]=0 # Se coloca un 0 para empezar.
        numero_actual=tablero[nueva_y][nueva_x]
        numero_actual=siguiente_opcion(numero_actual,nueva_x,nueva_y) # Se suman 1 al numero anterior hasta llegar a un número no repetido.
        tablero[nueva_y][nueva_x]=numero_actual

        if final_del_tablero(medida,nueva_x,nueva_y): # Comprueba que sea el final.
            if mostrar_pasos==1:
                mostrar_tablero(tablero)
                input('TABLERO ACTUAL')
            
            if cuadrado_magico(): # Comprueba que sea un cuadrado mágico.
                return True    
                
            else:
                tablero[nueva_y][nueva_x]=0 # Se borra la última casilla por un 0.
                hay_repeticion=1
                
                while hay_repeticion==1: # Ciclo de backtracking
                    actual_x,actual_y=retroceder(nueva_x,nueva_y)
                    numero_actual=tablero[actual_y][actual_x] # Entrega el número de la casilla anterior.
                    if mostrar_pasos==1:
                        print('\n====================================================================================================================\nAún no es mágico.')
                        mostrar_tablero(tablero)
                        print(f'Retrocedemos a las coordenadas ({actual_x},{actual_y}).')
                        input(f'El número en esas coordenadas debería ser {numero_actual}.')
                    
                    repite=0
                    while numero_actual<=medida**2: # Se prueba con el siguiente número hasta salirse del rango.
                        numero_actual=numero_actual+1
                        for i in range(medida):
                            for j in range(medida):
                                if tablero[i][j]==numero_actual: # Compara todas las casillas con el número actual
                                    repite=1
                        if mostrar_pasos==1:
                            mostrar_tablero(tablero)
                            print(f'Ver si el {numero_actual} ya estaba en el tablero.')
                        if repite==0: # Si el número no está repetido.
                            if mostrar_pasos==1:
                                input('No está, se puede remplazar.')
                            break
                        else: # Si se encontró un número repetido y vuelve a ejecutarse el ciclo while.
                            repite=0
                            if mostrar_pasos==1:
                                input('Sí está, entonces se prueba el siguiente número.')
                                
                    if numero_actual<=medida**2:
                        tablero[actual_y][actual_x]=numero_actual # Si el número es válido, se registra en la tabla.
                        if mostrar_pasos==1:
                            mostrar_tablero(tablero)
                            print(f'El número {numero_actual} está en la posición ({actual_x},{actual_y}).')
                            print(f'Ahora partimos en ({actual_x},{actual_y}).')
                        hay_repeticion=0 # Variable para terminar el backtracking
                        numero_actual=0
                        
                    else: 
                        tablero[actual_y][actual_x]=0 # Si el número está fuera del rango se remplaza la casilla con un 0.
                        if mostrar_pasos==1:
                            input(f'Pero el numero {numero_actual} es mayor que {medida**2}.')
                            mostrar_tablero(tablero)
                            input(f'Entonces en la casilla ({actual_x},{actual_y}) se pone un 0.')
                        nueva_x=actual_x
                        nueva_y=actual_y
                if mostrar_pasos==1:        
                    input('\nSe termina el backtracking y se vuelven a poner valores.\n')  
                    print('====================================================================================================================')  
                
        else:
            actual_x=nueva_x
            actual_y=nueva_y
        
        
#------------------------------------------------------------------------------------------------------------------------------


print('\n====================================================================================================================')
print('''El programa consiste en encontrar un cuadrado mágico usando backtracking. Debido al algoritmo usado, encontrar
la solución puede tardar horas, por lo que no es capaz de mostrar un resultado en un tiempo razonable.''')

while True:
    try:
        medida=int(input('\nIngrese la medida del cuadrado > '))
        if medida<2:
            print('\nNo es un número válido.')
        else:
            break
    except ValueError:
        print('\nNo es una entrada válida.')
      
        
print('\n¿Mostrar el paso a paso o la solución directa?\n1 = PASO A PASO\n2 = SOLO SOLUCIÓN ') 
accion=input('> ')
while accion!='1' and accion!='2':
      print('\nIngresa una opción válida.')
      accion=input('> ')      
if accion=='1':
    mostrar_pasos=1
else:
    mostrar_pasos=0 

tablero=[[0 for _ in range(medida)] for _ in range(medida)]

if mostrar_pasos==0 and medida>2:
    print('\nSe está encontrando una solución...')

if encontrando_cuadrado(medida,tablero):
    mostrar_tablero(tablero)
    print('\n====================================================================================================================')
    print('Se encontró un cuadrado mágico.\n')
else:
    if mostrar_pasos==0:
        print('\n====================================================================================================================')
    print('No se encontró un cuadrado mágico.\n')