
def crear_tablero():
    
    # Crea un tablero vacío de 3x3
    tablero = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(" ")
        tablero.append(fila)
    return tablero

def mostrar_tablero(tablero):
    
    # Muestra el tablero actual
    for i in range(3):
        print(f"{i} {tablero[i][0]} | {tablero[i][1]} | {tablero[i][2]}")
        if i < 2:
            print("  --+---+--")

def verificar_ganador(tablero, jugador):
   
    # Verificar filas
    for fila in tablero:
        ganador_fila = True
        for celda in fila:
            if celda != jugador:
                ganador_fila = False
                break
        if ganador_fila:
            return True
    
    # Verificar columnas
    for col in range(3):
        ganador_columna = True
        for fila in range(3):
            if tablero[fila][col] != jugador:
                ganador_columna = False
                break
        if ganador_columna:
            return True
    
    # Verificar diagonal principal
    ganador_diagonal1 = True
    for i in range(3):
        if tablero[i][i] != jugador:
            ganador_diagonal1 = False
            break
    if ganador_diagonal1:
        return True
    
    # Verificar diagonal secundaria
    ganador_diagonal2 = True
    for i in range(3):
        if tablero[i][2-i] != jugador:
            ganador_diagonal2 = False
            break
    if ganador_diagonal2:
        return True
    
    return False

def tablero_lleno(tablero):
   
    # Verifica si el tablero está lleno (empate)
    for fila in tablero:
        if " " in fila:
            return False
    return True

def movimiento_valido(tablero, fila, col):
    
    #Verifica si el movimiento es válido
    if (0 <= fila < 3) and (0 <= col < 3) and (tablero[fila][col] == " "):
        return True
    else:
        return False

def obtener_movimiento(tablero, jugador_actual):
   
    #Obtiene un movimiento válido del jugador
    movimiento_obtenido = False
    fila = -1
    col = -1
    
    while not movimiento_obtenido:
            
        entrada = input("Ingresa tu movimiento (fila columna): ").split()
        if len(entrada) != 2:
            print("Error: Debes ingresar exactamente 2 números")
            continue
            
        fila = int(entrada[0])
        col = int(entrada[1])
            
        if movimiento_valido(tablero, fila, col):
            movimiento_obtenido = True
        else:
            print("Movimiento inválido. Intenta de nuevo.")

    return fila, col

def jugar_partida():
    
    # Juega una partida completa de Gato
    tablero = crear_tablero()
    jugador_actual = "X"
    juego_terminado = False
    ganador = ""
    
    print("¡Bienvenido al juego Gato!")

    while not juego_terminado:
        mostrar_tablero(tablero)
        print(f"\nTurno del jugador {jugador_actual}")
        
        # Obtener movimiento del jugador
        fila, col = obtener_movimiento(tablero, jugador_actual)
        
        # Realizar el movimiento
        tablero[fila][col] = jugador_actual
        
        # Verificar si hay ganador
        if verificar_ganador(tablero, jugador_actual):
            juego_terminado = True
            ganador = jugador_actual
        # Verificar empate
        elif tablero_lleno(tablero):
            juego_terminado = True
            ganador = "Empate"
        else:
            # Cambiar jugador
             if jugador_actual == "X":
                jugador_actual = "O"
             
             else:
                 jugador_actual = "X"
    
    # Mostrar resultado final
    mostrar_tablero(tablero)
    if ganador == "Empate":
        print("\n¡Empate! El juego ha terminado.")
    else:
        print(f"\n¡Felicidades! Jugador {ganador} ha ganado!")
    
    return ganador

# Programa principal
jugar_partida()
print("\n¡Gracias por jugar!")