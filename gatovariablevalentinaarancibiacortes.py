# ==========================
#  JUEGO DEL GATO (JUGADOR vs jugador 2) con variables
# ==========================

''' Variables de juego '''
victoria = False # Variable tipo Booleana (Bool) -> Verdadero (True) o Falso (False)
jugador = "X"


''' Variables para coordenadas '''

a1 = ' '
a2 = ' '
a3 = ' '

b1 = ' '
b2 = ' '
b3 = ' '

c1 = ' '
c2 = ' '
c3 = ' '



'''             MAIN.        '''
# Muestra por primera vez tablero

print("\n\n\n\n\n")
print(f" {a1} | {a2} | {a3} ")
print("---+---+---")
print(f" {b1} | {b2} | {b3} ")
print("---+---+---")
print(f" {c1} | {c2} | {c3} ")


while not victoria:
    
    ''' input de usuario mediante terminal para posicion '''

    fila = int(input("Ingresar fila (1-3): "))
    col = int(input("Ingresar columna (1-3): "))



    ''' Verifica si se puede poner una ficha en esa posicion ''' 

    if fila == 1 and col == 1 and a1 == ' ':
        a1 = jugador
    elif fila == 1 and col == 2 and a2 == ' ':
        a2 = jugador
    elif fila == 1 and col == 3 and a3 == ' ':
        a3 = jugador
    
    elif fila == 2 and col == 1 and b1 == ' ':
        b1 = jugador
    elif fila == 2 and col == 2 and b2 == ' ':
        b2 = jugador
    elif fila == 2 and col == 3 and b3 == ' ':
        b3 = jugador

    elif fila == 3 and col == 1 and c1 == ' ':
        c1 = jugador
    elif fila == 3 and col == 2 and c2 == ' ':
        c2 = jugador
    elif fila == 3 and col == 3 and c3 == ' ':
        c3 = jugador

    else:
        print("\n>>>No se puede colocar la ficha en esa posicion !!")

    
    '''    COMPROBAR SI EXISTE VICTORIA.    '''

    # Comprueba horizontal

    if a1 == jugador and a2 == jugador and a3 == jugador:
        victoria = True # Variable Booleana (Verdadero o Falso)
        print("VICTORIA !!!\n\n")
    
    if b1 == jugador and b2 == jugador and b3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")
    
    if c1 == jugador and c2 == jugador and c3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")
    
    # Comprobar vertical

    if a1 == jugador and b1 == jugador and c1 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    if a2 == jugador and b2 == jugador and c2 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    if a3 == jugador and b3 == jugador and c3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    # Comprobar diagonales

    if a1 == jugador and b2 == jugador and c3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")
    
    if a3 == jugador and b2 == jugador and c1 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")


    '''     IMPRIME TABLERO.   '''

    print("")
    print(f" {a1} | {a2} | {a3} ")
    print("---+---+---")
    print(f" {b1} | {b2} | {b3} ")
    print("---+---+---")
    print(f" {c1} | {c2} | {c3} ")    


    ''' Cambia por cada turno la ficha que se juega '''
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"