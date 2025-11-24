tablero = [
    ['#','#','#','#'],
    ['#','#','#','#'],
    ['#','#','#','#'],
    ['#','#','#','#']
    ]



    
    
def colocar_reina(x,y,tablero):
    
    for i in range(len(tablero)):
       while 'R' in tablero[x]:
            x += 1
   
   
       if tablero[x][y] == '#' and 'R' not in tablero[x]:
            tablero[x][y] = 'R'
            y += 1
            
    
    
    

colocar_reina(0,0,tablero)

def imprimir_tablero(tablero):
    for fila in tablero:
        print(' '.join(fila))
    print()
    
imprimir_tablero(tablero)

