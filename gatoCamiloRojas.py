import random  # Importa la librería random para tener funciones de aleatoriedad

# Tablero Mostrar
def mostrar_tablero(tablero): # Función que muestra tablero
    for fila in tablero:  # Recorre cada fila del tablero
        print(" | ".join(fila))  # Imprime la fila separada por barras verticales
        print("-" * 9)  # Imprime la fila separada por barras horizontales

# Victoria
def verificar_victoria(tablero, jugador): # Función que verifica si un jugador ganó
    for i in range(3):  # Recorre índices 0 a 2 (3 filas y 3 columnas)
        if all(c == jugador for c in tablero[i]):  # Verifica si toda la fila i es del jugador
            return True
        if all(tablero[j][i] == jugador for j in range(3)):  # Verifica si toda la columna i es del jugador
            return True
    # Verifica la diagonal principal (de arriba izquierda a abajo derecha)
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    # Verifica la diagonal secundaria (de arriba derecha a abajo izquierda)
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    return False  # Si no hay ninguna combinación ganadora

# Tablero lleno
def tablero_lleno(tablero): # Función que verifica si ya no quedan espacios vacíos en el tablero
    return all(c != " " for fila in tablero for c in fila)  # Return True si todas las casillas están ocupadas

# Tablero casillas libres
def obtener_casillas_libres(tablero): # Función que devuelve una lista con todas las posiciones vacías del tablero
    libres = []  # Lista vacía donde se guardarán las casillas disponibles
    for i in range(3):  # Recorre las filas
        for j in range(3):  # Recorre las columnas
            if tablero[i][j] == " ":  # Si la casilla está vacía
                libres.append((i, j))  # Agrega la posición (i, j) a la lista
    return libres  # Devuelve la lista con las casillas disponibles

# IA movimiento (de forma aleatoria)
def movimiento_ia(tablero, ficha_ia): # Función que hace que la IA juegue automáticamente (elige una casilla libre al azar)
    casillas = obtener_casillas_libres(tablero)  # Obtiene las casillas vacías disponibles
    if casillas:  # Si hay alguna casilla vacía
        i, j = random.choice(casillas)  # Elige una posición aleatoria de la lista
        tablero[i][j] = ficha_ia  # Coloca la ficha de la IA en esa posición
        print(f"La IA juega en fila {i+1}, columna {j+1}")  # Muestra al jugador dónde jugó la IA


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------

# Crea el tablero como una matriz 3x3 llena de espacios en blanco
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Pide al jugador elegir si quiere jugar con "X" o "O"
while True:
    jugador = input("Elige tu ficha (X/O): ").upper()  # Solicita al jugador su ficha y la convierte en mayúscula
    if jugador in ["X", "O"]:  # Verifica que la ficha sea válida
        break  # Sale del bucle si la ficha es válida
    print("Entrada inválida. Escribe X o O.")  # Mensaje de error si la entrada no es válida

# La IA usa la ficha opuesta a la que eligió el jugador
ia = "O" if jugador == "X" else "X"

print("\nComienza el juego:")  # Mensaje de inicio
mostrar_tablero(tablero)  # Muestra el tablero vacío

turno = "jugador"  # Variable para alternar el turno; empieza el jugador

# Bucle principal del juego (sigue hasta que alguien gane o haya empate)
while True:
    if turno == "jugador":  # Si es el turno del jugador
        print("\nTu turno:")  # Mensaje de turno

        # Bucle para validar la entrada del jugador
        while True:
            try:
                fila = int(input("Fila (1-3): ")) - 1  # Solicita fila, resta 1 para usar índices 0-2
                col = int(input("Columna (1-3): ")) - 1  # Solicita columna, también resta 1
                if 0 <= fila <= 2 and 0 <= col <= 2:  # Verifica que estén dentro del rango válido
                    if tablero[fila][col] == " ":  # Verifica que la casilla esté vacía
                        tablero[fila][col] = jugador  # Coloca la ficha del jugador
                        break  # Sale del bucle interno si la jugada es válida
                    else:
                        print("Esa casilla ya está ocupada.")  # Mensaje si la casilla no está libre
                else:
                    print("Debes ingresar números del 1 al 3.")  # Si está fuera de rango
            except ValueError:  # Si el usuario ingresa texto o algo no convertible a int
                print("Entrada inválida. Escribe números del 1 al 3.")

        mostrar_tablero(tablero)  # Muestra el tablero después de la jugada

        if verificar_victoria(tablero, jugador):  # Verifica si el jugador ganó
            print("¡Ganaste!")  # Muestra mensaje de victoria
            break  # Termina el juego

        elif tablero_lleno(tablero):  # Verifica si se llenó el tablero
            print("¡Empate!")  # Muestra mensaje de empate
            break  # Termina el juego

        turno = "ia"  # Cambia el turno a la IA

    else:
        print("\nTurno de la IA:")  # Mensaje para indicar turno de la IA
        movimiento_ia(tablero, ia)  # Llama a la función que hace jugar a la IA
        mostrar_tablero(tablero)  # Muestra el tablero después de la jugada de la IA

        if verificar_victoria(tablero, ia):  # Verifica si la IA ganó
            print("¡La IA gana!")  # Muestra mensaje de derrota
            break  # Termina el juego

        elif tablero_lleno(tablero):  # Verifica si hay empate
            print("¡Empate!")  # Muestra mensaje de empate
            break  # Termina el juego

        turno = "jugador"  # Cambia el turno al jugador


# -----------------------------
# Fin del programa
# -----------------------------

### Planificación Camilo Rojas: 
# El jugador elige su ficha (X u O).
# Crear el tablero vacío (3x3).
# El juego alterna turnos entre el jugador y la IA.
# En el turno del jugador, se le pide que ingrese fila y columna.
# Se valida que la entrada sea correcta y la casilla esté libre en entradas del 1 al 3.
# La ficha del jugador se coloca en la casilla elegida.
# El juego muestra el tablero después de cada jugada.
# La IA elige una casilla libre al azar para su jugada.
# El juego verifica después de cada jugada si alguien ha ganado o si hay empate.
# El juego continúa hasta que alguien gane o haya empate.
### Fin planificación Camilo Rojas