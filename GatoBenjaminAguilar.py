import random

tablero = [" " for _ in range(9)]
jugador = "X"
maquina = "O"
juego_activo = True
ganador = None

def mostrar_tablero():
    print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]} ")
    print("---+---+---")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]} ")
    print("---+---+---")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]} \n")

def verificar_ganador():
    global ganador, juego_activo
    combinaciones = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combinaciones:
        a, b, c = combo
        if tablero[a] == tablero[b] == tablero[c] and tablero[a] != " ":
            ganador = tablero[a]
            juego_activo = False
            return
    if " " not in tablero:
        ganador = "Empate"
        juego_activo = False

print("Bienvenido al Juego del Gato (Jugador vs Máquina)")
print("Posiciones del tablero (usa números del 1 al 9):")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

while juego_activo:
    mostrar_tablero()
    posicion = input("Elige una posición (1-9): ")
    if posicion.isdigit():
        posicion = int(posicion) - 1
        if 0 <= posicion <= 8 and tablero[posicion] == " ":
            tablero[posicion] = jugador
            verificar_ganador()
            if juego_activo:
                posiciones_disponibles = [i for i in range(9) if tablero[i] == " "]
                if posiciones_disponibles:
                    eleccion = random.choice(posiciones_disponibles)
                    tablero[eleccion] = maquina
                    verificar_ganador()
        else:
            print("Posición inválida o ya ocupada. Intenta de nuevo.")
    else:
        print("Ingresa un número válido.")

mostrar_tablero()
if ganador == "Empate":
    print("El juego terminó en empate.")
else:
    if ganador == jugador:
        print("Ganaste.")
    else:
        print("La máquina ganó.")
