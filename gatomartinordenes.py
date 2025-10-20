Tablero = [' '] * 9 
Jugador = 'X'

#genera el tablero del gato
def mostrar_tablero():
    print(f"\n{Tablero[0]} | {Tablero[1]} | {Tablero[2]}")
    print('---------')
    print(f"{Tablero[3]} | {Tablero[4]} | {Tablero[5]}")
    print('---------')
    print(f"{Tablero[6]} | {Tablero[7]} | {Tablero[8]}\n")

#ayuda a definir el ganador del juego en base a las combinaciones
def hay_ganador():
    Combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for c in Combinaciones:
        if Tablero[c[0]] == Tablero[c[1]] == Tablero[c[2]] != ' ':
            return True
    return False


for turno in range(9): #
    mostrar_tablero()
    print(f"Turno de {Jugador}")

    try:
        pos = int(input("Elige una posición (0-8): "))
    except ValueError:
        print('ingrese un numero que sea valido en el tablero (0-8)')
        continue

    if pos < 0 or pos > 8:
        print('posicion no valida, elija un numero valido (0-8)')
        continue

    if Tablero[pos] == ' ':
        Tablero[pos] = Jugador
    else:
        print("Esa posición ya está ocupada.")
        continue

    if hay_ganador():
        mostrar_tablero()
        print(f"¡Gana {Jugador}!")
        break #termina el programa al finalizar el juego

    Jugador = 'O' if Jugador == 'X' else 'X'
else:
    mostrar_tablero()
    print("¡Empate!")