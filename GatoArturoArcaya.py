tablero = [[" " for _ in range(3)] for _ in range(3)] # genera una lista vacia de 3 x 3


def imprimir_tablero(tablero):   #crea las separaciones para asi poder juigar gato
    for i in range(3):
        print(" | ".join(tablero[i]))   #inserta un "separador" para poder genrar un tablero en la columna
        if i < 2:
            print("-----------")  #la misma funsion pero separando fila

def verificar_ganador(tablero, jugador):
    for i in range(3):
        if all([celda == jugador for celda in tablero[i]]): return True  #revisa todas las filas i viendo si perneceten al mismo jugador
        if all([tablero[j][i] == jugador for j in range(3)]): return True #hace lo mismo que la linea 12 pero verificando columna 
    if all([tablero[i][i] == jugador for i in range(3)]): return True  #digonal de izquierda a derecha
    if all([tablero[i][2 - i] == jugador for i in range(3)]): return True #diagonal de derecha a izquierda
    return False

jugador = "X" 
movimientos = 0
empate= False

while movimientos < 9 and not empate:    #los movimientos no pueden sobrepasar a 9
    imprimir_tablero(tablero)
    print(f"Turno del jugador {jugador}")    #da los turnos
    try:  #sigue con lineas de codigo aun que este falle
        fila = int(input("Ingresa la fila (0, 1, 2): "))  #convierte en numero entero el ingreso del usuario
        col = int(input("Ingresa la columna (0, 1, 2): "))
        if tablero[fila][col] == " ":   #verifica si el lugar elegido del jugador esta vacio
            tablero[fila][col] = jugador  #ingresa la ficha del jugador actual
            movimientos += 1   #suma movimiento 
            if verificar_ganador(tablero, jugador): #verifica ganador
                print(f"¡Jugador {jugador} ha ganado!")
                empate = True
                break
            jugador = "O" if jugador == "X" else "X" #cambia de jugador
        else:
            print("Esa casilla ya está ocupada. Intenta otra vez.")
    except (ValueError, IndexError): #try no falla siempre y cuando los fallos esten dentro de expect
        print("Entrada inválida. Usa números del 0 al 2.")
    
if not empate:    #si empate se vuelve falso entra
    imprimir_tablero(tablero)
    print("¡Empate!")