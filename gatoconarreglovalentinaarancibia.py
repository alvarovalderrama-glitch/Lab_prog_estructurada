import random

# ==========================
#  JUEGO DEL GATO (JUGADOR vs MÁQUINA) con arreglos
# ==========================

# -------- FUNCIÓN PARA MOSTRAR TABLERO --------
def mostrar_tablero(tablero):
    print("\n")
    print("   1   2   3")
    for i, fila in enumerate(tablero):
        print(f"{i+1}  {fila[0]} | {fila[1]} | {fila[2]}")
        if i < 2:
            print("  ---+---+---")
    print("\n")


# -------- FUNCIÓN PARA COMPROBAR VICTORIA --------
def comprobar_victoria(tablero, simbolo):
    # Filas
    for fila in tablero:
        if all(celda == simbolo for celda in fila):
            return True
    # Columnas
    for col in range(3):
        if all(tablero[fila][col] == simbolo for fila in range(3)):
            return True
    # Diagonales
    if all(tablero[i][i] == simbolo for i in range(3)):
        return True
    if all(tablero[i][2 - i] == simbolo for i in range(3)):
        return True
    return False


# -------- FUNCIÓN PARA MOVIMIENTO DE MÁQUINA --------
def movimiento_maquina(tablero):
    vacios = [(f, c) for f in range(3) for c in range(3) if tablero[f][c] == ' ']
    if vacios:
        return random.choice(vacios)
    return None


# -------- FUNCIÓN PARA PREGUNTAR SI SE DESEA JUGAR NUEVAMENTE --------
def jugar_nuevamente():
    while True:
        respuesta = input("¿Deseas jugar nuevamente? (si/no): ").strip().lower()
        if respuesta in ["si", "sí", "s"]:
            return True
        elif respuesta in ["no", "n"]:
            print("¡Buen juego! Nos vemos ✌️ 😀 ✌️")
            return False
        else:
            print("responda 'si' o 'no'")


# -------- FUNCIÓN PRINCIPAL DEL JUEGO --------
def jugar():
    jugador = "X"
    maquina = "O"
    victoria = False
    turnos = 0

    # Crear un nuevo tablero
    tablero = [[' ', ' ', ' '],
               [' ', ' ', ' '],
               [' ', ' ', ' ']]

    print("\n=== JUEGO DEL GATO: JUGADOR (X) vs MÁQUINA (O) ===")
    mostrar_tablero(tablero)

    while not victoria and turnos < 9:

        # ---- TURNO DEL JUGADOR ----
        try:
            fila = int(input("Ingresa la fila (1-3): ")) - 1
            col = int(input("Ingresa la columna (1-3): ")) - 1

            # Validación
            if not (0 <= fila <= 2 and 0 <= col <= 2):
                print("❌ Posición fuera del tablero")
                continue
            if tablero[fila][col] != ' ':
                print("❌ Posición ocupada")
                continue

            # Colocar ficha del jugador
            tablero[fila][col] = jugador
            turnos += 1
            mostrar_tablero(tablero)

            # Comprobar victoria del jugador
            if comprobar_victoria(tablero, jugador):
                print("🎉 ¡Ganaste! 🎉")
                victoria = True
                break

            if turnos >= 9:
                break

            # ---- TURNO DE LA MÁQUINA ----
            print("🤖 Turno de la máquina...")
            fila_m, col_m = movimiento_maquina(tablero)
            tablero[fila_m][col_m] = maquina
            turnos += 1
            mostrar_tablero(tablero)

            # Comprobar victoria de la máquina
            if comprobar_victoria(tablero, maquina):
                print("💀 La máquina ha ganado...")
                victoria = True
                break

        except ValueError:
            print("⚠️ Ingresa solo números entre 1 y 3.")

    # ---- EMPATE ----
    if not victoria:
        print("🤝 ¡Empate!")


# -------- BUCLE GENERAL DEL PROGRAMA --------
while True:
    jugar()
    if not jugar_nuevamente():
        break  