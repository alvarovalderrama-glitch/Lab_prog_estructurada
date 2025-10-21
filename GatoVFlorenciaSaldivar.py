import random   #importamos el modulo random
c1=1    #Le asignamos un numero a cada casilla
c2=2
c3=3
c4=4
c5=5
c6=6
c7=7
c8=8
c9=9
def mostrar_tablero():  #Creamos la variable para crear el tablero
    print()
    print(c1, "|", c2, "|", c3)
    print("--+--+--")
    print(c4, "|", c5, "|", c6)
    print("--+--+--")
    print(c7, "|", c8, "|", c9)
    print()

def hay_ganador():  #creamos la funcipn para comprobar si hay ganador, comparando las filas, columnas y diagonales
    if c1==c2==c3 or c4==c5==c6 or c7==c8==c9:
        return True
    if c1 == c4 == c7 or c2 == c5 == c8 or c3 == c6 == c9:
        return True
    if c1 == c5 == c9 or c3 == c5 == c7:
        return True
    return False
turnos=0
mostrar_tablero()
while True: #bucle que se repite hasta que alguien gane o empaten
    cas=input("tu turno (x), elige una casilla del 1-9: ")  #pedimos que se escoja una casilla
    if cas not in ["1","2","3","4","5","6","7","8","9"]:    #En caso de que no sean estos numeros
        print("Debes ingresar un numero del 1 al 9")    #Le pide ingresar un numero del uno al nueve
        continue
    if cas == "1" and c1 not in ["X","O"]: c1 = "X"
    elif cas == "2" and c2 not in ["X","O"]: c2 = "X"
    elif cas == "3" and c3 not in ["X","O"]: c3 = "X"
    elif cas == "4" and c4 not in ["X","O"]: c4 = "X"
    elif cas == "5" and c5 not in ["X","O"]: c5 = "X"
    elif cas == "6" and c6 not in ["X","O"]: c6 = "X"
    elif cas == "7" and c7 not in ["X","O"]: c7 = "X"
    elif cas == "8" and c8 not in ["X","O"]: c8 = "X"
    elif cas == "9" and c9 not in ["X","O"]: c9 = "X"
    else:   #si la casilla ya tiene X u O, no se puede usar
        print("Casilla ocupada")
        continue
    turnos +=1
    mostrar_tablero()   #mostramos como quedo el tablero despues del movimiento 
    if hay_ganador():   #revisamos si el jugador gano esta jugada
        print("Ganaste")
        break
    if turnos == 9: #si ya hay nueve jugadas y nadie gano entonces hay empate
        print("Empate")
        break
    print("Turno de la máquina (O)")    

    while True:     #la maquina elige una casilla libre
        eleccion = str(random.randint(1, 9))    #Para cada posible elección, verifica si está libre y, si lo está, marca con "O" y sale del bucle
        if eleccion == "1" and c1 not in ["X","O"]:
            c1 = "O"; break
        elif eleccion == "2" and c2 not in ["X","O"]:
            c2 = "O"; break
        elif eleccion == "3" and c3 not in ["X","O"]:
            c3 = "O"; break
        elif eleccion == "4" and c4 not in ["X","O"]:
            c4 = "O"; break
        elif eleccion == "5" and c5 not in ["X","O"]:
            c5 = "O"; break
        elif eleccion == "6" and c6 not in ["X","O"]:
            c6 = "O"; break
        elif eleccion == "7" and c7 not in ["X","O"]:
            c7 = "O"; break
        elif eleccion == "8" and c8 not in ["X","O"]:
            c8 = "O"; break
        elif eleccion == "9" and c9 not in ["X","O"]:
            c9 = "O"; break

    turnos += 1 #Contamos la jugada de la maquina
    mostrar_tablero()   #volvemos a mostrar el tablero

    if hay_ganador():   #revisamos si la maquina gano
        print("La maquina gano")
        break
    if turnos == 9: #Si se lleno el tablero tras la jugada de la maquina, tambien es empate
        print("Empate")
        break