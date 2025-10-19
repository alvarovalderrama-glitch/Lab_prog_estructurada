import random
tablero = [[0 for _ in range(3)] for _ in range(3)]
def mostrar_tablero(tablero):
    for i in range(3):
        for j in range(3):
            print(tablero[i][j], end = " ")
        print("")
    print("")
def jmarcar_posicion(tablero):
    while True:
        fila=int(input("Ingrese la fila (0-2): "))
        columna=int(input("Ingrese la columna (0-2): "))
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = "X"
            return True
        else:
            print("Posición ya ocupada. Intente de nuevo.")
            continue
def Mmarcar_posicion(tablero):
    while True:
        Mfila=random.randint(0,2)
        Mcolumna=random.randint(0,2)
        if tablero[Mfila][Mcolumna] == 0:
            tablero[Mfila][Mcolumna] = "O"
            break
        else:
            continue
def verificar_ganador(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != 0:
            return tablero[i][0]
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != 0:
            return tablero[0][i]
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != 0:
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != 0:
        return tablero[0][2]
    return False
ganador = False
jugadas = 0
while ganador is False:
    mostrar_tablero(tablero)
    jmarcar_posicion(tablero)
    jugadas += 1
    ganador = verificar_ganador(tablero)
    if ganador:
        mostrar_tablero(tablero)
        print(f"¡El ganador es: {ganador}!")
        break
    if jugadas == 9 and not ganador:
        mostrar_tablero(tablero)
        print("¡El juego es un empate!")
        break
    Mmarcar_posicion(tablero)
    jugadas += 1
    ganador = verificar_ganador(tablero)
    if ganador:
        mostrar_tablero(tablero)
        print(f"¡El ganador es: {ganador}!")


