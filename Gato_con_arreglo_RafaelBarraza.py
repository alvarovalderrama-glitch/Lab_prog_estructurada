                                                                                # Función para mostrar el tablero de juego junto a una referencia de posiciones
def mostrar_tablero(tablero):
                                                                                # Imprime el encabezado del tablero con separación para la referencia
    print("\nTABLERO DE JUEGO" + " " * 15 + "REFERENCIA")
    
                                                                                # Recorre cada fila del tablero con índice i
    for i, fila in enumerate(tablero):
                                                                                # 'real' crea un string de la fila actual separando los elementos con " | "
        real = " | ".join(fila)
                                                                                # 'ref' crea un string con las posiciones de la fila, útil como referencia
        ref = " | ".join([f"{i}.{j}" for j in range(3)])
                                                                                # Imprime la fila real y su referencia, con formato y espacios para alinear
        print(f"{real:<10}" + " " * 15 + f"{ref}")
                                                                                # Línea separadora debajo de cada fila para mayor claridad visual
        print("-" * 10 + "  " * 7 + "-" * 16)
    
                                                                                # Salto de línea final para separar del siguiente contenido
    print("\n")


                                                                                # Función que revisa si un jugador específico ha ganado
def hay_ganador(tablero, jugador):
                                                                                # Revisa si alguna fila está completamente ocupada por el jugador
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True                                                         # Devuelve True si se cumple la condición
    
                                                                                # Revisa si alguna columna está completamente ocupada por el jugador
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True                                                         # Devuelve True si se cumple la condición
    
                                                                                # Revisa la diagonal principal
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    
                                                                                # Revisa la diagonal secundaria
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True
    
                                                                                # Si ninguna condición se cumple, retorna False (no hay ganador)
    return False


                                                                                # Función que verifica si el tablero está completamente lleno
def tablero_lleno(tablero):
                                                                                # Comprueba que todas las casillas de todas las filas no estén vacías
    return all(casilla != " " for fila in tablero for casilla in fila)


                                                                                # Función para que la computadora haga un movimiento
def movimiento_computadora(tablero, simbolo):
                                                                                # Recorre todas las filas y columnas del tablero
    for i in range(3):
        for j in range(3):
                                                                                # Si la casilla está vacía, coloca el símbolo de la computadora
            if tablero[i][j] == " ":
                tablero[i][j] = simbolo
                return                                                          # Sale de la función después de colocar el símbolo


                                                                                # Función principal que controla el flujo del juego
def jugar():
                                                                                # Inicializa un tablero 3x3 con espacios vacíos
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    jugador = "X"                                                               # Símbolo del jugador humano
    computadora = "O"                                                           # Símbolo de la computadora

    turno = "jugador"                                                           # Variable que controla de quién es el turno

                                                                                # Bucle principal del juego, se repite hasta que haya ganador o empate
    while True:
        mostrar_tablero(tablero)                                                # Muestra el estado actual del tablero

        if turno == "jugador":                                                  # Si es el turno del jugador humano
            print("Tu turno (X). Indica fila y columna (0-2).")
            try:
                                                                                # Solicita la fila y columna deseada al usuario
                fila = int(input("Fila: "))
                col = int(input("Columna: "))
            except ValueError:
                                                                                # Si la entrada no es un número, muestra error y vuelve a pedir
                print("Entrada inválida. Intenta de nuevo.")
                continue                                                        # Salta al inicio del bucle

                                                                                # Verifica que la fila y columna estén dentro del rango y que la casilla esté vacía
            if 0 <= fila < 3 and 0 <= col < 3 and tablero[fila][col] == " ":
                tablero[fila][col] = jugador                                    # Coloca el símbolo del jugador

                                                                                # Revisa si el jugador ha ganado
                if hay_ganador(tablero, jugador):
                    mostrar_tablero(tablero)
                    print("¡Ganaste!")
                    break                                                       # Sale del bucle, terminando el juego
                
                turno = "computadora"                                           # Cambia el turno a la computadora
            else:
                                                                                # Mensaje de error si el movimiento no es válido
                print("Movimiento inválido, intenta de nuevo.")
        
        else:                                                                   # Turno de la computadora
            print("Turno de la computadora (O)...")
            movimiento_computadora(tablero, computadora)                        # Hace el movimiento

                                                                                # Revisa si la computadora ha ganado
            if hay_ganador(tablero, computadora):
                mostrar_tablero(tablero)
                print("La computadora ganó.")
                break
            
            turno = "jugador"                                                   # Cambia el turno al jugador

                                                                                # Revisa si el tablero está lleno para declarar empate
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("Empate.")
            break


                                                                                # Punto de entrada del programa
if __name__ == "__main__":
    jugar()                                                                     # Llama a la función que inicia el juego
