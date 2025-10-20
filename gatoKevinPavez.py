#Variables del juego
victoria = False 
jugador = "X"

#Definimos las coordenadas del tablero junto con sus variables (abc) y (123)
a1 = ' ' 
a2 = ' '
a3 = ' '

b1 = ' '
b2 = ' '
b3 = ' '

c1 = ' '
c2 = ' '
c3 = ' '

#Muestra del tablero 

print("\n\n\n\n\n")
print(f" {a1} | {a2} | {a3} ")
print("---+---+---")
print(f" {b1} | {b2} | {b3} ")
print("---+---+---")
print(f" {c1} | {c2} | {c3} ")

while not victoria:

  

   #Creamos un input del usuario para la posicion de columna y fila

    fila = int(input("Ingresar fila (1-3): "))
    col = int(input("Ingresar columna (1-3): "))

    #Verificamos si se puede colocar un signo en la posicion dada

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
        print("\n>>>No se puede colocar la ficha en esa posicion !!")    #Le mostramos al jugador que su ingreso de ficha es invalido


    #        Comprobar si existe victoria en las combinaciones correspondientes y finalizar con un print de victoria

    # Comprobar la fila horizontal

    if a1 == jugador and a2 == jugador and a3 == jugador:
        victoria = True 
        print("VICTORIA !!!\n\n")
    
    if b1 == jugador and b2 == jugador and b3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")
    
    if c1 == jugador and c2 == jugador and c3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")
    
    # Comprobar las columnas verticales

    if a1 == jugador and b1 == jugador and c1 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    if a2 == jugador and b2 == jugador and c2 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    if a3 == jugador and b3 == jugador and c3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    # Comprobar las diagonales

    if a1 == jugador and b2 == jugador and c3 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")
    
    if a3 == jugador and b2 == jugador and c1 == jugador:
        victoria = True
        print("VICTORIA !!!\n\n")

    #         Imprimimos el tablero
    print("")
    print(f" {a1} | {a2} | {a3} ")
    print("---+---+---")
    print(f" {b1} | {b2} | {b3} ")
    print("---+---+---")
    print(f" {c1} | {c2} | {c3} ")    

    #        Cambia por cada turno jugado
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"

