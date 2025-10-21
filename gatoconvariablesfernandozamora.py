tablero = [" "] * 9 #crea una lista vacia de 9 espacios
jugador_actual = "X" #el primer jugador es "X"
juego_activo = True #variable para saber si el juego continua

def imprimir_tablero(): #funcion para dibujar el tablero de la pantalla
    print(f" {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} ")

def revisar_ganador(): #funcion para saber si alguien gano
#todas las combinaciones ganadoras
    lineas = [ 
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for l in lineas: #revisa cada linea
        if tablero[l[0]] == tablero[l[1]] == tablero[l[2]] and tablero[l[0]] != " ":
            return True #hay un ganador
    return False #no hay ganador

while juego_activo: #bucle principal del juego
    imprimir_tablero()
    print(f"Turno del jugador: {jugador_actual}")
    
    try: #pide al usuario que mueva
        movimiento = int(input("Elige una casilla (1-9): ")) - 1
    except ValueError:
        print("Error: Ingresa un número.")
        continue #vuelve a pedir

    if 0 <= movimiento <= 8 and tablero[movimiento] == " ": #revisa si el movimiento es valido
        #pone la X o 0 en el tablero
        tablero[movimiento] = jugador_actual
        
        if revisar_ganador(): #revisa si gano
            imprimir_tablero()
            print(f"¡Jugador {jugador_actual} ha ganado!")
            juego_activo = False #termina el juego
        elif " " not in tablero: #revisa si hay empate
            imprimir_tablero()
            print("¡Es un empate!")
            juego_activo = False #termina el juego
        else: #el movimiento no es valido
            if jugador_actual == "X":
                jugador_actual = "O"
            else:
                jugador_actual = "X" 
    else:
        print("Movimiento inválido o casilla ocupada.") #el movimiento no fue valido.