import random

def mostrar_tablero(tablero):
    for fila in tablero:
        print(fila)
    print()


def hay_ganador(tablero, jugador):
    # revisa cada opcion con la que se pueda ganar
    if tablero[0][0] == tablero[0][1] == tablero[0][2] == jugador:
        return True
    if tablero[1][0] == tablero[1][1] == tablero[1][2] == jugador:
        return True
    if tablero[2][0] == tablero[2][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][0] == tablero[1][0] == tablero[2][0] == jugador:
        return True
    if tablero[0][1] == tablero[1][1] == tablero[2][1] == jugador:
        return True
    if tablero[0][2] == tablero[1][2] == tablero[2][2] == jugador:
        return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False


def tablero_lleno(tablero):
    # recorre el tablero y si no encuentra " " es porque esta lleno y returna True, si no False o sea sigue el juego
    for fila in tablero:
        if " " in fila:
            return False
    return True


tablero = [[" " for i in range(3)] for i in range(3)]


jugador = input("Elige tu símbolo (X/O): ")
while jugador != 'X' and jugador != 'O':
    jugador = input("Por favor, elige X o O: ")
if jugador == 'X':
    maquina = 'O'
else:
    maquina = 'X'


mostrar_tablero(tablero)

# JUEGO EN SI

while True:
    # turno de jugador
    print("Tu turno")
    fila = int(input("Elige fila (0-2): "))
    while fila not in [0,1,2]:
        fila = int(input("Elige fila (0-2): "))
    columna = int(input("Elige columna (0-2): "))
    while columna not in [0,1,2]:
        columna = int(input("Elige columna (0-2): "))
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, elige otra.")
        continue


    mostrar_tablero(tablero)


    if hay_ganador(tablero, jugador):
        print("Gana Jugador")
        break
    if tablero_lleno(tablero):
        print("Empate")
        break
    # turno de maquina
    print("Turno de la máquina")
    jugada_hecha = False
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = maquina
                jugada_hecha = True
                break
        if jugada_hecha:
            break


    mostrar_tablero(tablero)


    if hay_ganador(tablero, maquina):
        print("Gana Maquina")
        break
    if tablero_lleno(tablero):
        print("Empate")
        break