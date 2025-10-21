
tablero = {
    "a1": " ", "a2": " ", "a3": " ",
    "b1": " ", "b2": " ", "b3": " ",
    "c1": " ", "c2": " ", "c3": " "
}

#  Función para mostrar el tablero
def mostrar_tablero():
    print("   1   2   3")
    print(f"a  {tablero['a1']} | {tablero['a2']} | {tablero['a3']}")
    print("  ---+---+---")
    print(f"b  {tablero['b1']} | {tablero['b2']} | {tablero['b3']}")
    print("  ---+---+---")
    print(f"c  {tablero['c1']} | {tablero['c2']} | {tablero['c3']}")
    print()

#  Función para revisar si alguien ganó
def ganador():
    # Filas
    if (tablero["a1"] == tablero["a2"] == tablero["a3"] != " " or
        tablero["b1"] == tablero["b2"] == tablero["b3"] != " " or
        tablero["c1"] == tablero["c2"] == tablero["c3"] != " "):
        return True
    # Columnas
    if (tablero["a1"] == tablero["b1"] == tablero["c1"] != " " or
        tablero["a2"] == tablero["b2"] == tablero["c2"] != " " or
        tablero["a3"] == tablero["b3"] == tablero["c3"] != " "):
        return True
    # Diagonales
    if (tablero["a1"] == tablero["b2"] == tablero["c3"] != " " or
        tablero["a3"] == tablero["b2"] == tablero["c1"] != " "):
        return True
    return False

# : Máquina juega en la primera casilla vacía
def jugada_maquina():
    for casilla in tablero:
        if tablero[casilla] == " ":
            return casilla
    return None

#  Inicio del juego
print("Bienvenido al Gato :3")
print("Tú eres 'X' y la máquina es 'O'\n")

turno = "X"

# Bucle del juego
for i in range(9):
    mostrar_tablero()

    if turno == "X":
        jugada = input("Elige una casilla (ejemplo a1, b2, c3): ").lower()

        if jugada not in tablero:
            print("Casilla inválida. Intenta otra.\n")
            continue

        if tablero[jugada] != " ":
            print("Esa casilla ya está ocupada.\n")
            continue

        tablero[jugada] = "X"

    else:  # Turno de la máquina
        jugada = jugada_maquina()
        if jugada is None:
            break
        print("La máquina juega en:", jugada)
        tablero[jugada] = "O"

    # Verificar ganador
    if ganador():
        mostrar_tablero()
        if turno == "X":
            print("¡Ganaste! wowowow")
        else:
            print("La máquina ganó beep-boop ksks")
        break

    # Cambiar turno
    turno = "O" if turno == "X" else "X"

else:
    mostrar_tablero()

    print("Empate. ¡Nadie ganó!")
