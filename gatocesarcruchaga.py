# Usamos una lista para representar el tablero ( 0 al 8)
# Inicialmente use numeros para que los jugadores puedan jugar la posicion que quieran
tablero = [str(i+1) for i in range(9)] 

def dibujar_tablero(tablero):
    """Imprime el tablero en formato 3x3 para que se vea bien."""
    print('\n')
    #Esto para que la lineas se impriman en el tablero
    print(f' {tablero[0]} | {tablero[1]} | {tablero[2]}')
    print('---|---|---')
    print(f' {tablero[3]} | {tablero[4]} | {tablero[5]}')
    print('---|---|---')
    print(f' {tablero[6]} | {tablero[7]} | {tablero[8]}')
    print('\n')

def chequear_ganador(tablero, jugador):
    """Revisa si el jugador ('X' u 'O') ha ganado comparando las 8 combinaciones."""
    # Lista con las 8 combinaciones ganadoras  
    combinaciones = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Filas (Horizontal)
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Columnas (Vertical)
        [0, 4, 8], [2, 4, 6]             # Diagonales
    ]
    
    # Usamos 'for' para recorrer todas las combinaciones 
    for combo in combinaciones:
        # Sentencia 'if': Si las tres casillas tienen el mismo símbolo (el del jugador) 
        if tablero[combo[0]] == tablero[combo[1]] == tablero[combo[2]] == jugador:
            return True # Devuelve True 
    return False

def chequear_empate(tablero):
    """Revisa si ya no quedan casillas vacías ('1' a '9')."""
    # Usamos 'for' para recorrer el tablero y 'if' para ver si encuentra un número (casilla sin jugar)
    for simbolo in tablero:
        if simbolo.isdigit(): # El símbolo es un número si la casilla no se ha jugado
            return False
    return True # Si no encuentra ningún número, es empate

def jugar_gato():
    """Función principal del juego El Gato."""
    jugador_actual = 'X'
    juego_activo = True
    
    # Bucle 'while' principal que mantiene el juego activo 
    while juego_activo:
        dibujar_tablero(tablero)
        
        # Bucle 'while' interno para la jugada y validarla
        while True:
            try:
                # Usamos input() para pedir la posición, y lo convertimos a int
                posicion = int(input(f"Turno de {jugador_actual}. Elige una casilla (1-9): ")) - 1
            except ValueError:
                print("Por favor, ingresa un número válido (entero).")
                continue # Vuelve a pedir la jugada 
            
            # Chequeo de jugada válida: Rango de 0 a 8 Y que la casilla no esté jugada
            # Usamos sentencias 'if/else' 
            if 0 <= posicion <= 8 and tablero[posicion].isdigit(): 
                break # Jugada válida, salimos del while interno
            else:
                print("Jugada inválida. Esa casilla ya está ocupada o no existe. Intenta de nuevo.")

        # Actualizamos el tablero con el símbolo del jugador
        tablero[posicion] = jugador_actual
        
        # revision de condiciones
        if chequear_ganador(tablero, jugador_actual):
            dibujar_tablero(tablero)
            print(f"¡El jugador {jugador_actual} ha ganado! ¡Felicidades!")
            juego_activo = False
        elif chequear_empate(tablero):
            dibujar_tablero(tablero)
            print("¡Es un EMPATE! El tablero está lleno.")
            juego_activo = False
        else:
            # Si el juego sigue, alternamos el turno
            jugador_actual = 'O' if jugador_actual == 'X' else 'X'

if __name__ == "__main__":
    jugar_gato()