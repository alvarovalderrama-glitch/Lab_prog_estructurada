
tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#para saber de quien es el turno
jugador_actual = 'X'
#para contar movimientos y saber si hay empate
intentos = 0
#variable para saber si el juego termino
ganador = False
print('Jugador X contra Jugador O')
print('elige el numero de la casilla donde quieres jugar')

#ciclo principal del juego
while ganador == False:
    
   #tablero
    print("[ " + tablero[0] + " ] [ " + tablero[1] + " ] [ " + tablero[2] + " ]")
    print("[ " + tablero[3] + " ] [ " + tablero[4] + " ] [ " + tablero[5] + " ]")
    print("[ " + tablero[6] + " ] [ " + tablero[7] + " ] [ " + tablero[8] + " ]")

    print("turno del jugador: " + jugador_actual)
    
    posicion = int(input('elige un numero del 1 al 9 '))

    indice = posicion - 1

    tablero[indice] = jugador_actual
    
    # sumamos un intento para saber si hay empate
    intentos = intentos + 1

    # se revisa si alguien gano
    
    # se revisa por filas horizontales
    if (tablero[0] == jugador_actual and tablero[1] == jugador_actual and tablero[2] == jugador_actual):
        ganador = True
    elif (tablero[3] == jugador_actual and tablero[4] == jugador_actual and tablero[5] == jugador_actual):
        ganador = True
    elif (tablero[6] == jugador_actual and tablero[7] == jugador_actual and tablero[8] == jugador_actual):
        ganador = True
        
    # se revisa por filas verticales
    elif (tablero[0] == jugador_actual and tablero[3] == jugador_actual and tablero[6] == jugador_actual):
        ganador = True
    elif (tablero[1] == jugador_actual and tablero[4] == jugador_actual and tablero[7] == jugador_actual):
        ganador = True
    elif (tablero[2] == jugador_actual and tablero[5] == jugador_actual and tablero[8] == jugador_actual):
        ganador = True
        
    # revisar filas diagonales
    elif (tablero[0] == jugador_actual and tablero[4] == jugador_actual and tablero[8] == jugador_actual):
        ganador = True
    elif (tablero[2] == jugador_actual and tablero[4] == jugador_actual and tablero[6] == jugador_actual):
        ganador = True

    # si hay ganador se sale del bucle principal
    if ganador == True:
        print('felicidades ' + jugador_actual + ' ganaste')
        break
        
    # si hay empoate se termina el bucle principal
    if intentos == 9:
        print("empate")
        break 

    # cambios de turnos
    if jugador_actual == 'X':
        jugador_actual = 'O'
    else:
        jugador_actual = 'X'


print("[ " + tablero[0] + " ] [ " + tablero[1] + " ] [ " + tablero[2] + " ]")
print("[ " + tablero[3] + " ] [ " + tablero[4] + " ] [ " + tablero[5] + " ]")
print("[ " + tablero[6] + " ] [ " + tablero[7] + " ] [ " + tablero[8] + " ]")