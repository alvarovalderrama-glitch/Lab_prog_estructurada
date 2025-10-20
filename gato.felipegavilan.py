import random

tablero = {'c1':' ', 'c2':' ', 'c3':' ', 'c4':' ', 'c5':' ', 'c6':' ', 'c7':' ', 'c8':' ', 'c9':' '}
ganador = False

def imprimir_tablero():
    print(f' {tablero["c1"]} | {tablero["c2"]} | {tablero["c3"]} ')
    print('---+---+---')
    print(f' {tablero["c4"]} | {tablero["c5"]} | {tablero["c6"]} ')
    print('---+---+---')
    print(f' {tablero["c7"]} | {tablero["c8"]} | {tablero["c9"]} ')

jugador = input('Elija ficha X - O: ').upper()
while jugador not in ('X', 'O'):
    jugador = input('Seleccione entre las opciones dadas, X - O: ').upper()

if jugador == 'X':
    maquina = 'O'
else:
    maquina = 'X'

def combinaciones_ganadoras():
    jugadas_ganadoras = [
        ['c1', 'c2', 'c3'],  # Horizontal superior
        ['c4', 'c5', 'c6'],  # Horizontal medio
        ['c7', 'c8', 'c9'],  # Horizontal inferior
        ['c1', 'c4', 'c7'],  # Vertical izquierda
        ['c2', 'c5', 'c8'],  # Vertical medio
        ['c3', 'c6', 'c9'],  # Vertical derecha
        ['c1', 'c5', 'c9'],  # Diagonal \
        ['c3', 'c5', 'c7']   # Diagonal /
    ]
    return jugadas_ganadoras

def verificar_ganador(ficha):
    combinaciones = combinaciones_ganadoras()
    for combo in combinaciones:
        if tablero[combo[0]] == ficha and tablero[combo[1]] == ficha and tablero[combo[2]] == ficha:
            return True
    return False

def verificar_empate():
    return ' ' not in tablero.values()

def jugada_maquina():
    casillas_vacias = [clave for clave, valor in tablero.items() if valor == ' ']
    if casillas_vacias:
        return random.choice(casillas_vacias)
    return None

def jugar():
    global ganador
    turno_jugador = True  # True para jugador, False para máquina
    
    print("\n¡Comienza el juego!")
    imprimir_tablero()
    
    while not ganador and not verificar_empate():
        if turno_jugador:
            # Turno del jugador
            casilla = input(f'\nTu turno ({jugador}). Elige una casilla (c1-c9): ')
            while casilla not in tablero or tablero[casilla] != ' ':
                casilla = input('Casilla inválida o ocupada. Elige otra (c1-c9): ')
            
            tablero[casilla] = jugador
            imprimir_tablero()
            
            if verificar_ganador(jugador):
                print('\n¡Felicidades! ¡Has ganado!')
                ganador = True
                break
                
        else:
            # Turno de la máquina
            print('\nTurno de la máquina...')
            casilla = jugada_maquina()
            if casilla:
                tablero[casilla] = maquina
                imprimir_tablero()
                
                if verificar_ganador(maquina):
                    print('\n¡La máquina ha ganado!')
                    ganador = True
                    break
        
        turno_jugador = not turno_jugador
        
        if verificar_empate() and not ganador:
            print('\n¡Empate!')
            break
jugar()