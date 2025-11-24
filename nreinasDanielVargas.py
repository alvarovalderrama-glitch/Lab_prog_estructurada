def mostrar_tablero(tablero):
    print('')
    for fila1 in range(medida):
        for columna1 in range(medida):
            print(f'{tablero[fila1][columna1]:2}',end=' |')
        print('')
        lineas='-'*(medida*4)
        print(lineas)

def tapar_casillas(actual_x,actual_y):
    tapar_x=0
    tapar_y=0
    
    # Tapa la fila
    for _ in range(medida):
        if tablero[actual_y][tapar_x]==0:
            tablero[actual_y][tapar_x]=' \033[31m\u25FC\033[0m' # Color rojo -> \033[31m + \u25FC + \033[0m
            tapar_x=tapar_x+1
        else:
            tapar_x=tapar_x+1
    
    # Tapa la columna      
    for _ in range(medida):
        if tablero[tapar_y][actual_x]==0:
            tablero[tapar_y][actual_x]=' \033[31m\u25FC\033[0m'
            tapar_y=tapar_y+1
        else:
            tapar_y=tapar_y+1
   
    # Tapa la diagonal superior derecha
    tapar_x=actual_x
    tapar_y=actual_y
    while tapar_x<medida-1 and tapar_y>0:
        tablero[tapar_y-1][tapar_x+1]=' \033[31m\u25FC\033[0m'
        tapar_x+=1
        tapar_y-=1
        
    # Tapa la diagonal inferior derecha
    tapar_x=actual_x
    tapar_y=actual_y
    while tapar_x<medida-1 and tapar_y<medida-1:
        tablero[tapar_y+1][tapar_x+1]=' \033[31m\u25FC\033[0m'
        tapar_x+=1
        tapar_y+=1
  

  
def avanzar(actual_x):
    nueva_x=actual_x+1
    opciones=[]
    for nueva_y in range(medida):
        if tablero[nueva_y][nueva_x]==0:
            opciones.append((nueva_y,nueva_x)) # Se guardan tuplas (y,x) de las coordenadas desocupadas 
    return opciones 
          
def final(reina_actual):
    if reina_actual==medida:
        return True
     
# Función con backtracking recursivo
def encontrando_reina(reina_actual, actual_x, actual_y):
    tapar_casillas(actual_x, actual_y)
    if mostrar_pasos==1:
        mostrar_tablero(tablero)
        input(f'El número {reina_actual} se coloca en ({actual_x},{actual_y}), tapando los espacios')
        print('====================================================================================================================\n')
    if final(reina_actual):
        return True
    
    opciones=avanzar(actual_x) 
    
    for nueva_y,nueva_x in opciones: # Recorre los distintos espacios disponibles en el tablero hasta que uno sirva. Si "opciones" está vacía "for" no se ejecuta
        
        tablero_anterior=[fila[:] for fila in tablero] # "fila[:]" hace una copia independiente de cada fila del tablero para guardarlo

        nueva_reina=reina_actual+1 
        tablero[nueva_y][nueva_x]=nueva_reina # Se coloca la siguiente reina

        if encontrando_reina(nueva_reina,nueva_x,nueva_y): # La función se llama a sí misma hasta encontrar una solución
            return True 
        tablero[:]=tablero_anterior  # El tablero se remplaza con el contenido del tablero anterior. Cada "tablero anterior" es independiente en cada llamada
        if mostrar_pasos==1:
            mostrar_tablero(tablero)
            input(f'Volvemos al tablero anterior.')
            print('====================================================================================================================\n')
    if mostrar_pasos==1:
        print(f'No quedan opciones para poner el {reina_actual+1}')
    return False
    
def solucion():
    opciones=[(0,primera_y) for primera_y in range(medida)]  # Guarda en tuplas todas las coordenadas de la columna 1, en donde está la reina N°1
    for _,primera_y in opciones: # La coordenada X siempre será 0 y la coordenada Y irá aumentando
        for i in range(medida): # Limpia el tablero cada vez que se inicia con la reina N°1
            for j in range(medida):
                tablero[i][j] = 0

        reina_actual=1
        tablero[primera_y][0]=reina_actual

        if encontrando_reina(reina_actual,0,primera_y): # Si devuelve False, la reina N°1 avanza a la siguiente fila
            return True 
    return False  
        
#==============================================================================================================================

while True:
    try:
        medida=int(input('\nIngrese la medida del tablero > '))
        if medida<2:
            print('\nNo es un número válido.')
        else:
            break
    except ValueError:
        print('\nNo es una entrada válida.')
        
tablero=[[0 for _ in range(medida)] for _ in range(medida)]
mostrar_tablero(tablero)

print('\n¿Mostrar el paso a paso o la solución directa?\n1 = PASO A PASO\n2 = SOLO SOLUCIÓN ') 
accion=input('> ')
while accion!='1' and accion!='2':
      print('\nIngresa una opción válida.')
      accion=input('> ')      
if accion=='1':
    mostrar_pasos=1
else:
    mostrar_pasos=0 

if solucion():
    print('\nSE ENCONTRÓ UN TABLERO')
    mostrar_tablero(tablero)
    print('')
else:
    print('\n\n====================================================================================================================')
    print('No hay solución para ese tablero')
    print('====================================================================================================================\n')