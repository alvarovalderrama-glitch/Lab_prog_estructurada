import random

# Se define cada espacio de "casilla" como un espacio vacío, la partida indica el turno en que van y de momento no hay ganador.
casilla=[' ',' ',' ',' ',' ',' ',' ',' ',' ']           
partida=0  
ganador=False

def tablero():
    print(f'| {casilla[0]} | {casilla[1]} | {casilla[2]} |')
    print(f'| {casilla[3]} | {casilla[4]} | {casilla[5]} |')
    print(f'| {casilla[6]} | {casilla[7]} | {casilla[8]} |')

def quien_parte(turno):
     if turno==1:
         print('\n--------------------------------------------------------------------------------') 
         print('Empiezas TÚ')
         print('--------------------------------------------------------------------------------\n')
     elif turno==2:
         print('\n--------------------------------------------------------------------------------')
         print('Empieza la MÁQUINA')
         print('--------------------------------------------------------------------------------\n')

def ficha(ficha_jugador):
    if ficha_jugador==1:
        print('\n--------------------------------------------------------------------------------')
        print('Tu ficha será X')
        print('La máquina será O')
        print('--------------------------------------------------------------------------------\n')
    elif ficha_jugador==2:
        print('\n--------------------------------------------------------------------------------')
        print('Tu ficha será O')
        print('La máquina será X')
        print('--------------------------------------------------------------------------------\n')

def preparando_la_partida():
    
    global ficha_jugador,turno,entrada1,entrada2
    
    print('\n--------------------------------------------------------------------------------')
    print('                               JUEGO DEL GATO')
    print('--------------------------------------------------------------------------------')
    print('Así es cómo se verá el tablero durante la partida:\n')
    tablero()
    print('\n--------------------------------------------------------------------------------')
    
    # Se comprueba que la entrada de la ficha sea válida
    while True: 
        print('Elige tu ficha:\n1 = X\n2 = O')
        entrada1=input('> ')
        if entrada1.isdigit():
            ficha_jugador=int(entrada1)
            if ficha_jugador==1 or ficha_jugador==2:
                break
        print('\n--------------------------------------------------------------------------------')
        print('No es una opción válida')
        print('--------------------------------------------------------------------------------')
        
    ficha(ficha_jugador)
    
    # Comprueba esta entrada también
    while True: 
        print('¿Quién parte?:\n1 = TÚ\n2 = MÁQUINA')
        entrada2=input('> ')
        if entrada2.isdigit():
            turno=int(entrada2)
            if turno==1 or turno==2:
                break
        print('\n--------------------------------------------------------------------------------')
        print('No es una opción válida')
        print('--------------------------------------------------------------------------------')
        
    quien_parte(turno)
    
    # Nuevamente se muestra el tablero vacío solo para el jugador (la máquina no necesita este proceso)
    if turno==1:
        tablero()
        
def jugada(casilla,posicion,ficha_jugador):
    global partida
    global turno
    # Comprueba que en la casilla de la posición ingresada por el jugador esté vacía para colocar una ficha
    if turno==1 and ficha_jugador==1:
        if casilla[posicion]==' ':
            casilla[posicion]='X'
            partida=partida+1
            turno=turno+1
        else:
            print('\n--------------------------------------------------------------------------------')
            print('Casilla ocupada.')
            print('--------------------------------------------------------------------------------\n')
    elif turno==1 and ficha_jugador==2:
        if casilla[posicion]==' ':
            casilla[posicion]='O'
            partida=partida+1
            turno=turno+1
        else:
            print('\n--------------------------------------------------------------------------------')
            print('Casilla ocupada.')
            print('--------------------------------------------------------------------------------\n')
    # Se revisa que el turno de la máquina sea válido (depende del número aleatorio)
    elif turno==2 and ficha_jugador==1:
        if casilla[posicion]==' ':
            casilla[posicion]='O'
            print('\n--------------------------------------------------------------------------------')
            print(f'La máquina a puesto su ficha en la casilla {posicion+1}\n')
            tablero()
            partida=partida+1
            turno=turno-1
    elif turno==2 and ficha_jugador==2:
        if casilla[posicion]==' ':
            casilla[posicion]='X'
            print('\n--------------------------------------------------------------------------------')
            print(f'La máquina a puesto su ficha en la casilla {posicion+1}\n')
            tablero()
            partida=partida+1
            turno=turno-1
            
def hay_ganador(casilla):
    global ganador
    # Se comprueban todas las combinaciones
    if ((casilla[0]==casilla[1]==casilla[2]!=' ') or (casilla[3]==casilla[4]==casilla[5]!=' ') or (casilla[6]==casilla[7]==casilla[8]!=' ') or (casilla[0]==casilla[4]==casilla[8]!=' ') or (casilla[6]==casilla[4]==casilla[2]!=' ') or (casilla[0]==casilla[3]==casilla[6]!=' ') or (casilla[1]==casilla[4]==casilla[7]!=' ') or (casilla[2]==casilla[5]==casilla[8]!=' ')):
        ganador=True
    else:
        ganador=False
            
def decidir_ganador():
    if partida==9 and ganador==True: # Primero comprueba que haya un ganador en el último turno
        if turno==2: 
            print('')
            tablero()
            print('\n--------------------------------------------------------------------------------')
            print('                                  ¡GANASTE!')
            print('--------------------------------------------------------------------------------\n')
        else:
            print('\n--------------------------------------------------------------------------------')
            print('                               GANÓ LA MÁQUINA')
            print('--------------------------------------------------------------------------------\n')
    elif partida<9 and ganador==True: # Luego comprueba que haya un ganador en cualquier turno (excepto el último)
        if turno==2:
            print('')
            tablero()
            print('\n--------------------------------------------------------------------------------')
            print('                                  ¡GANASTE!')
            print('--------------------------------------------------------------------------------\n')
        else:
            print('\n--------------------------------------------------------------------------------')
            print('                               GANÓ LA MÁQUINA')
            print('--------------------------------------------------------------------------------\n')
    elif partida==9 and ganador==False: # Será un empate cuando la partida sea 9 y no haya ganador
        if turno==2: # Muestra el tablero final si el último turno es del jugador (para corregir un error visual)  
            print('')
            tablero()
        print('\n--------------------------------------------------------------------------------')
        print('                                   EMPATE')
        print('--------------------------------------------------------------------------------\n')

#================================================ De aquí parte el programa ===================================================

preparando_la_partida()
# La partida sigue hasta que el número de la partida sea menor que 9 y no haya un ganador
while partida<9 and ganador!=True: 
    # Turno del juegador
    if turno==1:
        while True: # Se comprueba que la entrada sea un dígito, para después transformarla en entero y usarla
            print('\nElige la casilla (del 1 al 9):')
            entrada3=input('> ')
            if entrada3.isdigit():
                posicion=int(entrada3)
                if posicion in range(1,10): # Revisa que el número esté entre el 1 y el 9
                    break
            print('\n--------------------------------------------------------------------------------')
            print('No es una opción válida')
            print('--------------------------------------------------------------------------------')
        posicion=posicion-1
        jugada(casilla,posicion,ficha_jugador)
        hay_ganador(casilla)
    # Turno de la máquina
    else:
        posicion=random.randrange(9)
        jugada(casilla,posicion,ficha_jugador)
        hay_ganador(casilla)
decidir_ganador()