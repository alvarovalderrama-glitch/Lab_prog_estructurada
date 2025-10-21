### Gato con arreglos ###
import random


def elegir_ficha():
    while True:
        fichaj = input("Elige una ficha (O, X): \n>")
        fichaj = fichaj.upper()
        if fichaj in ("O", "X"):
            break
        else:
            print("\nEntrada inválida.\n\n")

    # devuelve la ficha de la máquina
    if fichaj == "O":
        ficham = "X"
    else:
        ficham = "O"
    return fichaj, ficham



def elegir_turno():
    # pregunta quién inicia el juego
    if input("Quien juega primero? (ingresar algo inválido => empieza la maquina)\n1. Jugador \n2. Maquina\n>") == "1":
        inicio = 0  # jugador
    else:
        inicio = 1  # máquina
    return inicio


def crear_tablero():
    # crea y devuelve un tablero vacío
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    return tablero


def mostrar_tablero(tablero):
    # imprime el tablero en pantalla
    for i in range(3):
        print(" | ".join(f"{tablero[i][j]:3}" for j in range(3)))
        if i < 2:
            print("---------------")


def posiciones():
    # asigna números del 1 al 9 a coordenadas del tablero en un diccionario pos{}
    pos = {
        "1": (0, 0), "2": (0, 1), "3": (0, 2),
        "4": (1, 0), "5": (1, 1), "6": (1, 2),
        "7": (2, 0), "8": (2, 1), "9": (2, 2)
        }
    return pos


def ganar(tablero):
    # comprueba si hay un ganador
    lineas = [
        [tablero[0][0], tablero[0][1], tablero[0][2]],  # fila 1
        [tablero[1][0], tablero[1][1], tablero[1][2]],  # fila 2
        [tablero[2][0], tablero[2][1], tablero[2][2]],  # fila 3
        [tablero[0][0], tablero[1][0], tablero[2][0]],  # columna 1
        [tablero[0][1], tablero[1][1], tablero[2][1]],  # columna 2
        [tablero[0][2], tablero[1][2], tablero[2][2]],  # columna 3
        [tablero[0][0], tablero[1][1], tablero[2][2]],  # diagonal \
        [tablero[0][2], tablero[1][1], tablero[2][0]]   # diagonal /
    ]
    for linea in lineas:
        if linea[0] == linea[1] == linea[2] != " ":
            return True
    return False


def turno_jugador(tablero, fichaj):
    # pide al jugador colocar su ficha
    while True:
        mostrar_tablero(tablero)
        casilla = input("Ingrese la casilla que desea jugar (1 a 9): \n> ")
        pos = posiciones()

        if casilla in pos:
            fila, col = pos[casilla]
            if tablero[fila][col] == " ":
                tablero[fila][col] = fichaj
                break
            else:
                print("\nCasilla ocupada. Inténtelo de nuevo.\n")
        else:
            print("\nNúmero inválido. Inténtelo de nuevo.\n")


def turno_maquina(tablero, ficham):
    # la máquina elige una casilla al azar
    print("Turno de la máquina...\n")
    pos = posiciones()
    while True:
        casilla = str(random.randint(1, 9))
        fila, col = pos[casilla]
        if tablero[fila][col] == " ":
            tablero[fila][col] = ficham
            break


def main():
    # programa principal
    fichaj, ficham = elegir_ficha()
    turno = elegir_turno()
    tablero = crear_tablero()
    turnos = 9
    ganador = False

    while turnos > 0 and not ganador:
        if turno == 0:
            turno_jugador(tablero, fichaj)
            turno = 1
        else:
            turno_maquina(tablero, ficham)
            turno = 0

        turnos -= 1
        ganador = ganar(tablero)
        print(f"\nQuedan {turnos} turnos restantes.\n")

    mostrar_tablero(tablero)

    if ganador:
        if turno == 1:
            print("Felicidades. Has ganado!.\n")
        else:
            print("Ha ganado la máquina.\n")
    else:
        print("La partida ha terminado en empate.\n")


# ejecutar el juego
main()