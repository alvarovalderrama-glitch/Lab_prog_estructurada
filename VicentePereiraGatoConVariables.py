MAX = 3
#funcion para imprimir el tablero
def mostrar_tablero(tablero):
    for i in range(MAX):
        # imprime la fila
        print(tablero[i][0] + " " + tablero[i][1] + " " + tablero[i][2])
    # imprime un espacio vacio
    print("")
#se define una funcion que valida los movimientos
def valida(tablero, fila, col):
    if (fila < 0 or fila >= MAX):
        return False
    if (col < 0 or col >= MAX):
        return False
    #si la casilla no esta vacia, esta ocupada
    if (tablero[fila][col] != ' '):
        return False 
    
    #en caso de todo estar bien, continua....
    return True

# se define una funcion para verificar si hay ganador
def revisar_ganador(tablero, jugador):
    # revisar filas
    for i in range(MAX):
        if (tablero[i][0] == jugador and tablero[i][1] == jugador and tablero[i][2] == jugador):
            return True
    # revisar columnas
    for j in range(MAX):
        if (tablero[0][j] == jugador and tablero[1][j] == jugador and tablero[2][j] == jugador):
            return True

    # revisar la diagonola \
    if (tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador):
        return True
    
    # revisar la diagonal /
    if (tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador):
        return True
    
    #si no hay ganador continua
    return False

# revisa si quedan espacios vacios
def revisar_empate(tablero): #revisar todas las casillas
    for i in range(MAX):
        for j in range(MAX):
            # si encuentra un espacio vacio
            if tablero[i][j] == ' ':
                return False # todavia no es empate
                
    # de no haber encontrado espacios vacios, es empate
    return True

#programa inicial

#tablero
tablero = [[' ' for _ in range(MAX)] for _ in range(MAX)]

# variables del juego
turno_actual = 'X'
juego_terminado = False 

# bucle del juego se repite hasta que acabe
while juego_terminado == False:
    
    # imprime el tableor
    mostrar_tablero(tablero)
    print("es el turno de: " + turno_actual)
    
    # Pedimos la jugada
    jugada_ok = False
    while jugada_ok == False:
        
        # Pedimos fila y columna
        fila = int(input("fila (0, 1 o 2): "))
        col = int(input("columna (0, 1 o 2): "))

        # se comprueba si la jugada es valida
        if valida(tablero, fila, col) == True:
            jugada_ok = True #si valida es verdadero, continua, si no..
        else:
            print("intenta de nuevo")

    # poner X o O en el tablero
    tablero[fila][col] = turno_actual
    
    #  comprobar si hay ganador
    if revisar_ganador(tablero, turno_actual) == True:
        print("gano " + turno_actual)
        juego_terminado = True #Se acaba el juego
    
    # revisar si hay empato
    elif revisar_empate(tablero) == True:
        print("hay empate")
        juego_terminado = True #Se acaba el juego
    
    # si no paso nada, al siguente turno
    else:
        if turno_actual == 'X':
            turno_actual = 'O'
        else:
            turno_actual = 'X'

# muestra tablero final cuando termino el juego 
print('/n juego terminado')
mostrar_tablero(tablero)