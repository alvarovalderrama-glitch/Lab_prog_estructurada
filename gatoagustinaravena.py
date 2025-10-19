


''' Variables de juego '''
victoria = False # Variable tipo Booleana (Bool) -> Verdadero (True) o Falso (False)
jugador = "X"


''' Arreglo para coordenadas '''
tablero = [[' ', ' ', ' '], 
           [' ', ' ', ' '], 
           [' ', ' ', ' ']] # Matriz





'''             MAIN.        '''
# Muestra por primera vez tablero

print("\n\n\n\n\n")
print(f" {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} ")
print("---+---+---")
print(f" {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} ")
print("---+---+---")
print(f" {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} ")


while not victoria:

    ''' input de usuario mediante terminal para posicion '''

    fila = int(input("Ingresar fila (1-3): ")) - 1
    col = int(input("Ingresar columna (1-3): ")) - 1



    ''' Verifica si se puede poner una ficha en esa posicion '''

    # Paso 1: Verifica
    if tablero[fila][col] == ' ':
        # Paso 2: coloca ficha
        tablero[fila][col] = jugador
    else:
        print("\n>>>No se puede colocar la ficha en esa posicion !!")


    


    
    '''    COMPROBAR SI EXISTE VICTORIA.    '''


    # Revisa filas
    for fila  in range(3):
        contador = 0
        for col in range(3):
            if tablero[fila][col] == jugador:
                contador += 1
        if contador == 3:
            victoria = True
            print("\n\nVICTORIA !!!")

    
    # Revisa columnas
    for col  in range(3):
        contador = 0
        for fila in range(3):
            if tablero[fila][col] == jugador:
                contador += 1
        if contador == 3:
            victoria = True
            print("\n\nVICTORIA !!!")
    

    # Revisa diagonales

    # Diagonal 1
    contador = 0
    for i in range(3):
        if tablero[i][i] == jugador:
            contador += 1
    if contador == 3:
        victoria = True
        print("\n\nVICTORIA !!!")

    # Diagonal 2
    contador = 0
    for i in range(3):
        if tablero[i][2-i] == jugador:
            contador += 1
    if contador == 3:
        victoria = True
        print("\n\nVICTORIA !!!")





    print("\n\n")
    print(f" {tablero[0][0]} | {tablero[0][1]} | {tablero[0][2]} ")
    print("---+---+---")
    print(f" {tablero[1][0]} | {tablero[1][1]} | {tablero[1][2]} ")
    print("---+---+---")
    print(f" {tablero[2][0]} | {tablero[2][1]} | {tablero[2][2]} ") 



    ''' Cambia por cada turno la ficha que se juega '''
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

