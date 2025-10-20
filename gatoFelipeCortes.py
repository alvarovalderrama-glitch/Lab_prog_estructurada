import random

def imprimir_tablero(tablero):
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}\n ")

def verificar_ganador(tablero, jugador):
    lineas_ganadoras = [ # Arreglos con las lineas ganadoras
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columnas
        [0, 4, 8], [2, 4, 6]              # Diagonales
    ]
    for linea in lineas_ganadoras:
        if tablero[linea[0]] == tablero[linea[1]] == tablero[linea[2]] == jugador:
            return True
    return False

def elegir_simbolo(): # El jugador elige su simbolo
    while True:
        eleccion = input("¿Quieres ser 'X' o 'O'? ").upper() # Pregunta y convierte el simbolo en mayuscula
        if eleccion in ['X', 'O']:
            return eleccion
        else:
            print("Elige 'X' o 'O'")

def obtener_movimiento_jugador(tablero, jugador):
    while True:
        try:
            movimiento = int(input("Elige una casilla (1-9): ")) - 1 # Pide el numero de la casilla y le resta 1 para acomodarlo con la casilla real dentro del codigo
            if movimiento >= 0 and movimiento <= 8 and tablero[movimiento] == " ":
                return movimiento
            elif movimiento >= 0 and movimiento <= 8 and tablero[movimiento] != " ":
                print("Casilla ocupada.")
            else:
                print("Casilla no válida.")
        except ValueError:
            print("Ingresa un número válido.")

def obtener_movimiento_bot(tablero, bot):
    casillas_disponibles = [i for i, x in enumerate(tablero) if x == " "] # Busca por las casillas disponibles
    return random.choice(casillas_disponibles) # Escoge una casilla aleatoria

def juego_terminado(tablero):
    return verificar_ganador(tablero, "X") or verificar_ganador(tablero, "O") or " " not in tablero

def juego_gato():
    tablero = [" "] * 9
    
    print("¡Bienvenido al Juego del Gato!")
    
    jugador = elegir_simbolo()
    bot = "O" if jugador == "X" else "X" # Alterna el simbolo del bot
    
    print(f"Tú eres: {jugador}")
    print(f"El bot es: {bot}")
    
    print("Posiciones:")
    print("\n 1 | 2 | 3 ")
    print(" 4 | 5 | 6 ")
    print(" 7 | 8 | 9 \n")

    jugador_actual = "X"
    
    while not juego_terminado(tablero):
        if jugador_actual == jugador:
            movimiento = obtener_movimiento_jugador(tablero, jugador)
            tablero[movimiento] = jugador
            if verificar_ganador(tablero, jugador):
                imprimir_tablero(tablero)
                print("¡Has ganado!")
                return
        else:
            movimiento = obtener_movimiento_bot(tablero, bot)
            tablero[movimiento] = bot
            print(f"El bot eligió la casilla {movimiento + 1}")
            if verificar_ganador(tablero, bot):
                imprimir_tablero(tablero)
                print("¡El bot ganó!")
                return
        
        imprimir_tablero(tablero)
        jugador_actual = "X" if jugador_actual == "O" else "O" # Alterna el turno

    imprimir_tablero(tablero)
    print("¡Es un empate!")

juego_gato()