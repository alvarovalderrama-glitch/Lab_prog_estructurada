def mostrar_tablero(tablero):
    print("\n")
    print(tablero[0] + "  | " + tablero[1] + " | " + tablero[2])
    print("---+---+---")
    print(tablero[3] + "  | " + tablero[4] + " | " + tablero[5])
    print("---+---+---")
    print(tablero[6] + "  | " + tablero[7] + " | " + tablero[8])
    print("\n")

def ganador(tablero):
    
    if tablero[0] == tablero[1] == tablero[2] != " " or tablero[3] == tablero[4] == tablero[5] != " " or tablero[6] == tablero[7] == tablero[8] != " ":
        ganador = 1
    elif tablero[0] == tablero[3] == tablero[6] != " " or tablero[1] == tablero[4] == tablero[7] != " " or tablero[2] == tablero[5] == tablero[8] != " ":
        ganador = 1
    elif tablero[0] == tablero[4] == tablero[8] != " " or tablero[2] == tablero[4] == tablero[6] != " ":
        ganador = 1
    else:
        ganador = 0
    return ganador
    
    

def gato():
    
    tablero = [" "] *9
    jugador_actual = "X"
    turnos = 0
    
    while True:
        mostrar_tablero(tablero)
        print(f"turno del jugador {jugador_actual}")
        posicion = input("ingrese una casilla de 0-8: ")#posibles errores, no colocar digito, que coloque un digito distinto de 0 a 8, o que la casilla esté ocupada.
        if not posicion.isdigit():
            print("\n\nDEBES INGRESAR UN NUMERO")
            continue
        posicion = int(posicion)
        if posicion < 0 or posicion > 8:
            print("\n\nDEBES INGRESAR UNA CASILLA EXISTENTE")
            continue
        if tablero[posicion] != " ":
            print("\n\nDEBES INGRESAR UNA CASILLA VACIA")
            continue #fin de busqueda de errores
        
        tablero[posicion] = jugador_actual
        
        if ganador(tablero) == 1:
            mostrar_tablero(tablero)
            print(f"\nEL JUGADOR {jugador_actual} HA GANADO")
            break
        mostrar_tablero(tablero)
        if jugador_actual == 'X':
            jugador_actual = 'O'
        else:
            jugador_actual = 'X'
        turnos += 1
        if turnos == 9:
            print("\n ES UN EMPATE")
            break
        
        
gato()