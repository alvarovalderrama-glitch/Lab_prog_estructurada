import random 

# 1. FUNCIÓN PARA DIBUJAR EL TABLERO
def dibujar_tablero(tablero):
    """Muestra el tablero 3x3 en la consola."""
    print(' ' + tablero[0] + ' | ' + tablero[1] + ' | ' + tablero[2]) 
    print('---+---+---')
    print(' ' + tablero[3] + ' | ' + tablero[4] + ' | ' + tablero[5])
    print('---+---+---')
    print(' ' + tablero[6] + ' | ' + tablero[7] + ' | ' + tablero[8])

# 2. FUNCIÓN PARA VERIFICAR SI HAY UN GANADOR
def verificar_ganador(tablero, jugador):
    """Comprueba si el jugador actual ha ganado."""
    return (
        # 3 Filas horizontales
        (tablero[0] == jugador and tablero[1] == jugador and tablero[2] == jugador) or
        (tablero[3] == jugador and tablero[4] == jugador and tablero[5] == jugador) or
        (tablero[6] == jugador and tablero[7] == jugador and tablero[80] == jugador) or
        # 3 Columnas verticales
        (tablero[0] == jugador and tablero[3] == jugador and tablero[6] == jugador) or
        (tablero[1] == jugador and tablero[4] == jugador and tablero[7] == jugador) or
        (tablero[2] == jugador and tablero[5] == jugador and tablero[8] == jugador) or
        # 2 Diagonales
        (tablero[0] == jugador and tablero[4] == jugador and tablero[8] == jugador) or
        (tablero[2] == jugador and tablero[4] == jugador and tablero[6] == jugador)
    )

# 3. FUNCIÓN PARA VERIFICAR EMPATE
def verificar_empate(tablero):
    """Comprueba si todas las posiciones están ocupadas."""
    for elemento in tablero:
        if elemento.isdigit(): 
            return False  # Hay al menos una posición libre, no hay empate.
    return True # No quedan posiciones libres y no hubo ganador.

# Modulo Movimiento maquina
def movimiento_Maquina(tablero):
    posiciones_libres = []
    
    
    for i in range(len(tablero)):
        #si es un digito va a estar disponible
        if tablero[i].isdigit(): 
            posiciones_libres.append(i) # Guardamos el índice (0-8) en la lista de opciones.

    if posiciones_libres:
        # random.choice() elige un elemento aleatorio de la lista [no en fuentes, pero es la función estándar del módulo random]
        indice_real = random.choice(posiciones_libres)
        return indice_real
    else:
        # Si no hay posiciones libres, devuelve None.
        return None

# -------------------Programa----Principal-----------------------
def juego_principal():
    tablero = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    jugador_actual = 'X' 

    # Bucle principal: 
    while True: 
        
        # LÓGICA DEL JUGADOR 
        if jugador_actual == 'X':
            dibujar_tablero(tablero)
            movimiento = input(f"Turno de {jugador_actual}. Ingresa una posición (1-9): ").strip()
            
            #Movimiento Valido
            if not movimiento.isdigit(): #Es para ver si la entrada es un digito 
                print("¡Error! Debes ingresar un número del 1 al 9.")
                continue 
            
            posicion_elegida = int(movimiento) # Convertimos la cadena a entero [31].
            indice_real = posicion_elegida - 1 # Calculamos el índice de la lista (0-8).

            if not (0 <= indice_real <= 8): # Si no esta dentro del tablero 
                print("¡Error! La posición debe estar entre 1 y 9.")
                continue

            # 2. Validación de posición ocupada
            if tablero[indice_real] == 'X' or tablero[indice_real] == 'O':
                print(f"La posición {posicion_elegida} ya está ocupada.")
                continue
            
        #Juego de la maquina
        else: # Si jugador_actual es 'O'
            print("\nTurno de la Maquina (O)...")
            indice_real = movimiento_Maquina(tablero) #Tiene que escoger un casillero libre 
            
        
            #Informa donde puso la ficha la maquina 
            posicion_elegida = indice_real + 1
            print(f"La Maquina eligió la posición {posicion_elegida}")
            
        
        # 6. ACTUALIZAR EL TABLERO
        tablero[indice_real] = jugador_actual

        # 7. VERIFICAR VICTORIA
        if verificar_ganador(tablero, jugador_actual):
            dibujar_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado!")
            break

        # 8. VERIFICAR EMPATE
        if verificar_empate(tablero):
            dibujar_tablero(tablero)
            print("¡Es un empate!")
            break 

        #Turnos 
        if jugador_actual == 'X':
            jugador_actual = 'O'
        else:
            jugador_actual = 'X'

# Ejecutamos el juego si el programa se inicia directamente
if __name__ == "__main__":
    juego_principal()