#Gato Hecho con Variables

import random                                                              #Importamos el modulo random para que la comutadora elija una casilla aleatoria#

#  VARIABLES DE JUEGO 
victoria = False                                                           #Creamos una variable llamada victoria la cual comienza en False debido a que al iniciar el juego no hay ganadores#
tablero = {
    'a1': ' ', 'a2': ' ', 'a3': ' ',
    'b1': ' ', 'b2': ' ', 'b3': ' ',                                       #Creamos un diccionario que contenga como clave 'a1' y valor ' ' #
    'c1': ' ', 'c2': ' ', 'c3': ' '
}

#  ELECCIÓN DE FICHA 
jugador = input("¿Quieres ser X o O?: ").upper()                            #Creamos la variable jugador donde le decimos al jugador que decida con que ficha quiere jugar, con el .upper() nos aseguramos de convertir lo que ingrese a mayusculas#
while jugador not in ['X', 'O']:                                            #Esto se repite mientras que jugador no sea X o O
    jugador = input("Por favor, elige entre X o O: ").upper()               #Pide ingresar una opcion valida entre X o O

if jugador == 'X':                                                          #Aqui dice que si el jugador es igual a X, la computadora utilizara las fichas O
    computadora='O'
else:                                                                       #En caso contrario si el jugador no es igual a la ficha X, la commputadora ocupara la ficha X
    computadora='X'    

#  FUNCIÓN PARA IMPRIMIR TABLERO 
def imprimir_tablero():    
     print("\n    1   2   3")  
     print(f"A   {tablero['a1']} | {tablero['a2']} | {tablero['a3']}")      #f-string(Cadena con formato), permite colocar dentro de una cadena el contenido de variables, escribiendolas entre llaves{}
     print("   ---+---+---")                                                #con tablero accedemos al diccionario que tiene posiciones como 'a1','b2'
     print(f"B   {tablero['b1']} | {tablero['b2']} | {tablero['b3']}")      #y al colocar tablero['a1'] accederiamos al valor guardado en esa clave.
     print("   ---+---+---")
     print(f"C   {tablero['c1']} | {tablero['c2']} | {tablero['c3']}\n")

#  FUNCIÓN PARA COMPROBAR VICTORIA 
def hay_victoria(ficha):
    combinaciones = [                                          #Entregamos las combinaciones ganadoras
        ['a1','a2','a3'], ['b1','b2','b3'], ['c1','c2','c3'],  # horizontales
        ['a1','b1','c1'], ['a2','b2','c2'], ['a3','b3','c3'],  # verticales         
        ['a1','b2','c3'], ['a3','b2','c1']                     # diagonales
    ]
    for combo in combinaciones:                                #Teneos un ciclo for donde creamos una variable temporal llamda combo que es una sub lista de la lista de combinaciones, con ella decimos voy a tomar cada elemento dentro de la lista combinaciones y lo voy a guardar, uno por uno, en una nueva variable temporal llamada combo
        if all(tablero[pos] == ficha for pos in combo):        #Aqui decimos que si todo lo que esta dentro del parentesis es verdadero me retornara verdadero
            return True
    return False                                               #En caso de que no hubiese una de esas combinaciones se nos retornara falso 

#  FUNCIÓN PARA MOVIMIENTO DE LA COMPUTADORA 
def movimiento_computadora():                                                 #Definimos una funcion llamada moviemiento de la computadora
    posiciones_libres = [pos for pos, val in tablero.items() if val == ' ']   #Aqui se crea una lista llamada posiciones_libres, donde toma una clave(pos) y un valor(val) del diccionario
    if posiciones_libres:
        eleccion = random.choice(posiciones_libres)                 #De la lista de psociones libre toma una eleccion al azar ya sea 'a1' o 'c3', dependiendo de cuales tenga el val==' '
        tablero[eleccion] = computadora                             #Coloca en el tablero la elccion random con la ficha que tenga en ese momento la cmputadora
        print(f"La computadora jugó en {eleccion.upper()}.")        #Muestra la eleccion de la computadora, eleccin.upper() es utilizada solo con fines esteticos

#  BUCLE PRINCIPAL
turno_jugador = True                                # Empieza el jugador
imprimir_tablero()                                  #Muestra el tablero en la consola

while not victoria and ' ' in tablero.values():     #Este bucle dice mientras que no hay ganador y en el diccionario hay valores que tengan ' ' se ejecuta el if
    
    if turno_jugador:                               #Esta condicion verifica que sea el turno del jugador
        print("Tu turno.")                          #Muestra que es turno del jugador 
        
        #  VALIDACIÓN DE FILA 
        while True:
            fila = input("Elige fila (A, B, C): ").lower()    #Aqui fila toma valores desde A,B,C, con el .lower() nos sercioramos de que lo que ingrese el jugador se convierta a minusculass esto se hace porque en el diccionario las claves estan definidas de esa manera.
            if fila in ['a','b','c']:                         #Con esto se evita un error de que al colocar por ej: 'a1' en fila y luego apretar enter se marca la casilla de 'a1' con la ficha del jugador, esto resuelve ese problema.
                break
            print("Fila no válida. Elige A, B o C.")
        
        #  VALIDACIÓN DE COLUMNA 
        while True:
            col = input("Elige columna (1-3): ")            #Aqui col solo pide ingresar un numero entre 1 y 3  
            if col in ['1','2','3']:
                break
            print("Columna no válida. Elige 1, 2 o 3.")
        
        posicion = fila + col                               #Posicion se toma de la suma de fila y col, segun los que ingrese el jugador

        if tablero[posicion] == ' ':                        #Verifica que la posicion este vacia.
            tablero[posicion] = jugador                     #Coloca la ficha con la que el jugador juega y la posicon que eligio el jugador.
            if hay_victoria(jugador):                       #Llama a la funcion hay_victoria con el parametro jugador para revissar si el jugador logro una linea de tres.
                imprimir_tablero()                          #Muestra el tablero final
                print("¡Ganaste!")                          #Muestra en la consola ¡"Ganaste"!
                victoria = True                             #El valor de victoria cambia a verdadero para salir del bucle
                break
            turno_jugador = False                           #Cambia el turno para que en la próxima vuelta juegue la computadora.
        else:
            print("Posición ya ocupada. Intenta otra.")     #Si la posición no existe o ya está ocupada, muestra este mensaje y no cambia el turno (para que el jugador intente de nuevo).

    else:                                      
        movimiento_computadora()                            #Llama a la función que hace que la computadora elija su jugada automáticamente
        if hay_victoria(computadora):                       #Comprueba si la computadora formó una línea ganadora.
            imprimir_tablero()
            print("La computadora gana.")                   #Si gana, muestra el tablero, imprime el mensaje y termina el juego.
            victoria = True
            break
        turno_jugador = True                                #Cambia la variable para que el próximo turno sea del jugador otra vez.

    imprimir_tablero()                                      #Al final de cada ronda, se muestra el estado actual del tablero (ya con la nueva jugada hecha).

if not victoria:                                            #Una vez que termina el while, si nadie ganó (victoria sigue siendo False), significa que el tablero está lleno, entonces muestra el mensaje "Empate".
    print("¡Empate!")
