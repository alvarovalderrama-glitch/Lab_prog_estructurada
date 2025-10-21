A=['1','2','3'] #Fila1
B=['4','5','6'] #Fila2
C=['7','8','9'] #Fila3

#Función para mostrar el tablero (las 3 filas)
def mostrar_tablero():
    print(A)
    print(B)
    print(C)
#variables vacías para luego darles otro dato
jugador=0
computadora=0
seleccion=input('Escoge O o X : ')

#Condicionales por elección del jugador al ser O o X
if seleccion == 'O' or seleccion == 'o' or seleccion==0:
    print('Bien, escogiste ser O.')
    jugador='O'
    computadora='X'
    print('Tu contrincante será X.')
elif seleccion=='X' or seleccion=='x':
    print('Genial, escogiste ser X.')
    jugador='X'
    computadora='O'
    print('Tu contrincante será O.')
else:
    print('Intenta de nuevo.')

#Diccionario para las filas
posiciones = {1:(A, 0), 2:(A, 1), 3:(A, 2),
              4:(B, 0), 5:(B, 1), 6:(B, 2),
              7:(C, 0), 8:(C, 1), 9:(C, 2)}

def verificar_ganador():
    #Verificar filas
    if A[0] == A[1] == A[2]: return A[0]
    if B[0] == B[1] == B[2]: return B[0]
    if C[0] == C[1] == C[2]: return C[0]
    
    #Verificar columnas
    if A[0] == B[0] == C[0]: return A[0]
    if A[1] == B[1] == C[1]: return A[1]
    if A[2] == B[2] == C[2]: return A[2]

    if A[0] == B[1] == C[2]: return A[0]
    if A[2] == B[1] == C[0]: return A[2]
    
    return None

def verificar_empate():
    for fila in [A, B, C]:
        for celda in fila:
            if celda in ['1','2','3','4','5','6','7','8','9']:
                return False
    return True

mostrar_tablero()

juego_activo = True
turno_jugador = True

while juego_activo:
    if turno_jugador:
        #Turno del jugador
        try:
            turno = int(input('Bien, ahora escoge la posición de tu movimiento (1-9): '))
            if turno in posiciones:
                fila, idx = posiciones[turno]
                #Verificar que la posición esté disponible
                if fila[idx] in ['1','2','3','4','5','6','7','8','9']:
                    fila[idx] = jugador
                    mostrar_tablero()
                    
                    #Verificar si el jugador ganó
                    ganador = verificar_ganador()
                    if ganador == jugador:
                        print('¡Felicidades! ¡Has ganado!')
                        juego_activo = False
                        continue
                    #Verificar si hay empate
                    elif verificar_empate():
                        print('¡Es un empate!')
                        juego_activo = False
                        continue
                    
                    print('Bien, ahora es turno de tu contrincante.')
                    turno_jugador = False
                else:
                    print('Esa posición ya está ocupada. Elige otra.')
            else:
                print('Por favor, ingresa un número entre 1 y 9.')
        except ValueError:
            print('Por favor, ingresa un número válido.')
    
    else:
        #Turno de la computadora
        import random
        def turno_computadora():
            posiciones_libres = []
            for a in range(1,10):
                fila, idx = posiciones[a]
                if fila[idx] in ['1','2','3','4','5','6','7','8','9']:
                   posiciones_libres.append(a)

            if posiciones_libres:
                eleccion = random.choice(posiciones_libres)
                fila, idx = posiciones[eleccion]
                fila[idx] = computadora
                print(f'La computadora jugó en la posición {eleccion}')
                mostrar_tablero()
                
                #Verifica si la computadora ganó
                ganador = verificar_ganador()
                if ganador == computadora:
                    print('¡La computadora ha ganado!')
                    return False
                #Verifica si hay empate
                elif verificar_empate():
                    print('¡Es un empate!')
                    return False
                return True
            return False
        
        #Llama a la función y maneja el resultado
        if turno_computadora():
            turno_jugador = True
        else:
            juego_activo = False
