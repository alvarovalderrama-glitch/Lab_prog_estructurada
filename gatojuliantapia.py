import random

# Juego "Gato" (tres en raya) desarrollado en Python.

fichas_colocadas = [' ' for i in range(0,9)] # Lista donde se guardara la posición de cada ficha O,X colocada. 

indices_disponibles = [i for i in range(0,9)] # Lista donde se almacenan los indices de las posiciones disponibles para colocar fichas.

ficha = ['O','X'] # Lista con los dos tipos de fichas a elegir.

matriz_ganador = [[0 for i in range(0,3)] for j in range(0,8)] # Lista que guardará las ocho combinaciones de tres fichas para para ganar.

# Este for crea todas las combinaciones ganadoras del juego.
for j in range(0,3):
    matriz_ganador[0][j] = j
    matriz_ganador[1][j] = 3 + j
    matriz_ganador[2][j] = 6 + j
    matriz_ganador[3][j] = j*3
    matriz_ganador[4][j] = j*3 + 1
    matriz_ganador[5][j] = j*3 + 2
    matriz_ganador[6][j] = j*4
    matriz_ganador[7][j] = (j+1)*2

# Esta función muestras el tablero con las fichas que se han colocado hasta el momento.
def mostrar_estado_partida(lista):
    print(f'\n {lista[0]} | {lista[1]} | {lista[2]}')
    print(f' {lista[3]} | {lista[4]} | {lista[5]}')
    print(f' {lista[6]} | {lista[7]} | {lista[8]}\n')

# Esta función se encarga de verificar que la posicion que el usuario ingrese no esté ocupada y sea valida.
def poner_ficha():
    while True:
        try:
            posicion_ficha = int(input('Elige un posición disponible del 1 al 9: '))-1 #Se resta uno para que coincida con la indexación de fichas_colocadas
            if not 0<=posicion_ficha<=8: # Filtrar los enteros que no pertenecen al rango del 0 al 8.
                print('Dato fuera de rango')
            elif fichas_colocadas[posicion_ficha] == ' ': # Si la posición que el usuario eligio está "vacia", se valida la posición.
                return(posicion_ficha)
            else:
                print('Posición ocupada.')
        except ValueError:
            print('Dato no valido')

# Esta función actualiza el estado del juego con la ficha jugador o el bot en la posición que ambos determinaron.           
def reemplazar_jugadas_en_listas(posicion_respectiva,ficha_respectiva):
    for lista_ganador in matriz_ganador: #for que recorre cada combinación ganadora
        if posicion_respectiva in lista_ganador: # Verifica si la posición elegida está en la combinación ganadora.
            lista_ganador[lista_ganador.index(posicion_respectiva)] = ficha_respectiva # Se reemplaza esa posicion en la combinación por la ficha correspondiente.
    fichas_colocadas[posicion_respectiva] = ficha_respectiva # Se coloca la ficha en la posición que el jugador o el bot detemino para que ya no se pueda elegir
    indices_disponibles.remove(posicion_respectiva) # Se remueve la posición de la ficha de los indices disponibles.

# Esta función verifica que la elección de la ficha de parte de usuario sea valida.
def elegir_ficha():
    while True:
        try:
            eleccion = int(input('Selecciona tu ficha:\nPulsa 0 para elegir O; Pulsa 1 para elegir X\nElección: '))
            if eleccion in [0,1]:
                return(eleccion)
            else:
                print('Elección no valida.\n')
        except ValueError:
            print('Dato ingresado no valido.')

# Está función verifica que uno los contincantes haya hecho un tres en raya.
def verificar_ganador(ficha_respectica):
    return([ficha_respectica for i in range(0,3)] in matriz_ganador) # Verifica que una de las combinaciones haya sido reemplazada completamente por la ficha respectiva.

# Inicia el juego.

print('Juego del gato en Python.\n')

eleccion = elegir_ficha()
ficha_jugador = ficha[eleccion] # Se define la ficha del jugador.
ficha_bot = ficha[(eleccion+1)%2] # Se define la ficha del bot.

# Se muestra el tablero del "gato" con el numero correspondiente a cada posición como referencia.
print('Posiciones de referencia:\n')
for i in range(0,3):
    print(f'Posición {i*3+1} | Posición {i*3+2} | Posición {i*3+3}')
print()

turno = random.randint(0,1)

# Ejecución de la partida.

while True:
    if ' ' in fichas_colocadas: # Si hay espacio para más fichas, la partida puede avanzar.
        if turno == 0:
            # Definición de la ficha del jugador en ese turno y actualización del estado de la partida
            posicion_jugador = poner_ficha()
            reemplazar_jugadas_en_listas(posicion_jugador,ficha_jugador)
    
            #Si el jugador hizo una combinación ganadora, muestra el estado de la partida y termina el juego.
            if verificar_ganador(ficha_jugador):
                mostrar_estado_partida(fichas_colocadas)
                print('Ganaste!!')
                break
        if turno == 1:
            # Definición de la ficha del bot en ese turno y actualización del estado de la partida
            posicion_bot = indices_disponibles[random.randint(0,len(indices_disponibles)-1)]
            reemplazar_jugadas_en_listas(posicion_bot,ficha_bot)
            
            #Si el bot hizo una combinación ganadora, muestra el estado de la partida y termina el juego.
            if verificar_ganador(ficha_bot):
                mostrar_estado_partida(fichas_colocadas)
                print('Perdiste JAJAJAAJAJA')
                break
            mostrar_estado_partida(fichas_colocadas) # Se muestra el estado de la partido siempre que el bot termine de jugar.  
        turno = (turno+1)%2 # El turno cambia para que juegue el siguiente
    else: # Si ya no hay espacio para más fichas y no se detuvo la ejecución del ciclo while, significa que hubo un empate.
        if turno == 1:
            mostrar_estado_partida(fichas_colocadas)
        print('Empate')
        break
