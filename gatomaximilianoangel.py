### Gato con arreglos ###
import random  # Para la selección aleatoria de turnos y casillas

print("Juguemos al gato.\n")  # Muestra mensaje inicial al jugador

x = " "  # Representa casillas vacías
tablero = [[x, x, x],      # Crea el tablero 3x3 vacío
           [x, x, x],
           [x, x, x]]

# Pide al jugador elegir su ficha
while True:
    fichaj = input("Elige tu ficha X o O: \n> ").upper()  # Convierte a mayúscula
    if fichaj in ("X", "O"):  # Comprueba si es válida
        break
    else:
        print("Elección inválida.\n")  # Mensaje de error

# Asigna la ficha de la máquina según la del jugador
if fichaj == "X":
    ficham = "O"
else:
    ficham = "X"

inicio = random.randint(0,1)  # Quién inicia: 0 jugador, 1 máquina
turnos = 9  # Total de turnos
ganador = 0  # Controla si hay un ganador

# Función para mostrar el tablero actual
def mostrar_tablero():
    print(f"""  {tablero[0][0]}  |  {tablero[0][1]}  |  {tablero[0][2]}  
-----------------
  {tablero[1][0]}  |  {tablero[1][1]}  |  {tablero[1][2]}  
-----------------
  {tablero[2][0]}  |  {tablero[2][1]}  |  {tablero[2][2]}  """)

# Función que devuelve las coordenadas de cada casilla
def posiciones():
    return {
        "1": (0,0), "2": (0,1), "3": (0,2),
        "4": (1,0), "5": (1,1), "6": (1,2),
        "7": (2,0), "8": (2,1), "9": (2,2)
    }

# Ciclo principal del juego
while turnos != 0 and ganador == 0:

    if inicio == 0:  # Turno del jugador
        ocupado = 1
        while ocupado == 1:
            mostrar_tablero()  # Muestra tablero
            casilla = input("Ingrese la casilla (Del 1 al 9) que desea usar: \n> ")
            pos = posiciones()  # Obtiene coordenadas de las casillas

            # Si la casilla elegida existe y está vacía, se coloca la ficha
            if casilla in posiciones():
                fila, col = pos[casilla]
                if tablero[fila][col] == x:
                    tablero[fila][col] = fichaj
                    ocupado = 0  # Casilla ocupada, termina bucle
                else:
                    print("\nLa casilla seleccionada está ocupada.\n")
            else:
                print("\nNúmero inválido.\n")

        inicio = 1  # Cambia turno a la máquina
        turnos -= 1  # Resta un turno
        print(f"\nQuedan {turnos} turnos restantes (Fue tu turno).\n")

    else:  # Turno de la computadora
        print("Turno de la computadora.\n")
        ocupado = 1
        while ocupado == 1:
            casilla = str(random.randint(1,9))  # Casilla aleatoria
            pos = posiciones()
            fila, col = pos[casilla]

            if tablero[fila][col] == x:  # Si está libre, coloca ficha
                tablero[fila][col] = ficham
                ocupado = 0  # Casilla ocupada, termina bucle

        turnos -= 1  # Resta un turno
        inicio = 0  # Cambia turno al jugador
        print(f"\nQuedan {turnos} turnos restantes (Fue turno de la computadora).\n")

    # Comprueba si hay un ganador (todas las filas, columnas y diagonales)
    lineas = [
        [tablero[0][0], tablero[0][1], tablero[0][2]],  # Fila 1
        [tablero[1][0], tablero[1][1], tablero[1][2]],  # Fila 2
        [tablero[2][0], tablero[2][1], tablero[2][2]],  # Fila 3
        [tablero[0][0], tablero[1][0], tablero[2][0]],  # Columna 1
        [tablero[0][1], tablero[1][1], tablero[2][1]],  # Columna 2
        [tablero[0][2], tablero[1][2], tablero[2][2]],  # Columna 3
        [tablero[0][0], tablero[1][1], tablero[2][2]],  # Diagonal \
        [tablero[0][2], tablero[1][1], tablero[2][0]]   # Diagonal /
    ]
    for linea in lineas:
        if linea[0] == linea[1] == linea[2] != x:  # Si hay tres iguales y no vacíos
            ganador = 1  # Se marca ganador
            mostrar_tablero()  # Muestra tablero final

# Mensaje final según quién ganó
if ganador == 1:
    if inicio == 1:
        print("Ganó el jugador. Felicidades.\n")
    else:
        print("Ganó la máquina. Suerte para la próxima.\n")
else:
    print("Uy, un empate.\n")
