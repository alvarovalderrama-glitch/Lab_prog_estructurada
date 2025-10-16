def imprimir_tablero(tablero):
    print("\n")
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 5)
    print("\n")

def verificar_ganador(tablero, jugador):
    # Verifica filas, columnas y diagonales
    for i in range(3):
        if all([celda == jugador for celda in tablero[i]]):  # Filas
            return True
        if all([tablero[j][i] == jugador for j in range(3)]):  # Columnas
            return True
    # Diagonales
    if all([tablero[i][i] == jugador for i in range(3)]):
        return True
    if all([tablero[i][2 - i] == jugador for i in range(3)]):
        return True
    return False

def tablero_lleno(tablero):
    return all([celda != " " for fila in tablero for celda in fila])

def jugar():
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X"

    while True:
        imprimir_tablero(tablero)
        print(f"Turno de {turno}")
        try:
            fila = int(input("Ingresa fila (0, 1, 2): "))
            col = int(input("Ingresa columna (0, 1, 2): "))
        except ValueError:
            print("Entrada inválida. Usa solo números.")
            continue

        if 0 <= fila <= 2 and 0 <= col <= 2:
            if tablero[fila][col] == " ":
                tablero[fila][col] = turno
                if verificar_ganador(tablero, turno):
                    imprimir_tablero(tablero)
                    print(f"¡El jugador {turno} gana!")
                    break
                elif tablero_lleno(tablero):
                    imprimir_tablero(tablero)
                    print("¡Empate!")
                    break
                turno = "O" if turno == "X" else "X"
            else:
                print("Esa casilla ya está ocupada. Intenta otra.")
        else:
            print("Posición fuera de rango. Usa 0, 1 o 2.")

if __name__ == "__main__":
    jugar()