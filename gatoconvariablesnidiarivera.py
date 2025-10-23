# JUEGO: EL GATO (versión con variables individuales)
import random
import os

# Función para mostrar el tablero con variables individuales
def mostrar_tablero(a1, a2, a3, b1, b2, b3, c1, c2, c3):
    print("")
    print(f"{a1} | {a2} | {a3}")
    print("--+---+--")
    print(f"{b1} | {b2} | {b3}")
    print("--+---+--")
    print(f"{c1} | {c2} | {c3}")
    print("")

# Función para verificar si hay un ganador
def hay_ganador(a1, a2, a3, b1, b2, b3, c1, c2, c3, ficha):
    return (
        (a1 == a2 == a3 == ficha) or
        (b1 == b2 == b3 == ficha) or
        (c1 == c2 == c3 == ficha) or
        (a1 == b1 == c1 == ficha) or
        (a2 == b2 == c2 == ficha) or
        (a3 == b3 == c3 == ficha) or
        (a1 == b2 == c3 == ficha) or
        (a3 == b2 == c1 == ficha)
    )

# Función principal del juego
def jugar_gato():
    os.system("cls")

    print("===============================")
    print("         JUEGO: EL GATO         ")
    print("===============================")
    print("Reglas: Logra tres en línea para ganar.\n")

    # Declaración de variables para cada casilla
    a1 = a2 = a3 = b1 = b2 = b3 = c1 = c2 = c3 = " "

    jugador = input("Elige tu ficha (X u O): ").upper()
    while jugador not in ["X", "O"]:
        jugador = input("Opción no válida. Elige X u O: ").upper()

    bot = "O" if jugador == "X" else "X"
    turno = random.choice(["Jugador", "Bot"])
    print("\nComienza:", turno)

    jugadas = 0

    while True:
        mostrar_tablero(a1, a2, a3, b1, b2, b3, c1, c2, c3)

        if turno == "Jugador":
            pos = input("Elige una posición (ej: a1, b2, c3): ").lower()

            if pos not in ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]:
                print("Posición inválida.")
                continue

            # Usamos un diccionario para manejar las variables
            posiciones = {
                "a1": a1, "a2": a2, "a3": a3,
                "b1": b1, "b2": b2, "b3": b3,
                "c1": c1, "c2": c2, "c3": c3
            }

            if posiciones[pos] != " ":
                print("Esa posición ya está ocupada.")
                continue

            posiciones[pos] = jugador
            jugadas += 1

        else:
            posiciones = {
                "a1": a1, "a2": a2, "a3": a3,
                "b1": b1, "b2": b2, "b3": b3,
                "c1": c1, "c2": c2, "c3": c3
            }
            vacias = [p for p, v in posiciones.items() if v == " "]
            if not vacias:
                mostrar_tablero(**posiciones)
                print("¡Empate!")
                break

            pos_bot = random.choice(vacias)
            print(f"El bot jugó en {pos_bot.upper()}")
            posiciones[pos_bot] = bot
            jugadas += 1

        # Actualizamos las variables desde el diccionario
        a1, a2, a3 = posiciones["a1"], posiciones["a2"], posiciones["a3"]
        b1, b2, b3 = posiciones["b1"], posiciones["b2"], posiciones["b3"]
        c1, c2, c3 = posiciones["c1"], posiciones["c2"], posiciones["c3"]

        # Verificar ganador después de cada turno
        if hay_ganador(a1, a2, a3, b1, b2, b3, c1, c2, c3, jugador):
            mostrar_tablero(a1, a2, a3, b1, b2, b3, c1, c2, c3)
            print("¡Felicidades! Ganaste")
            break

        if hay_ganador(a1, a2, a3, b1, b2, b3, c1, c2, c3, bot):
            mostrar_tablero(a1, a2, a3, b1, b2, b3, c1, c2, c3)
            print("Perdiste. El bot ganó.")
            break

        if jugadas == 9:
            mostrar_tablero(a1, a2, a3, b1, b2, b3, c1, c2, c3)
            print("¡Empate!")
            break

        turno = "Bot" if turno == "Jugador" else "Jugador"


# Ejecutar el juego
jugar_gato()
