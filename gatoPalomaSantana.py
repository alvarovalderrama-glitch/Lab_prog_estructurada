#Juego gato para dos jugadores
import random #Importa el módulo random para generar números aleatorios
#Tablero de 9 espacios
tablero=[' ']*9
turno=random.randint(0,1) #0 = Jugador 1 (X), 1 = Jugador 2 (O)
#Combinaciones ganadoras
ganadores=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] #Filas, columnas, diagonales

print("Gato, escoge número del 1 al 9 para jugar")
#Bucle principal, genera máximo 9 movimientos
for movimiento in range(9):
    #Motrar el tablero
    print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}")
    print("----------")
    print(f" {tablero[3]} | {tablero[4]} | {tablero[5]}")
    print("----------")
    print(f" {tablero[6]} | {tablero[7]} | {tablero[8]}")
    #Turno del Jugador 
    Jugador='X' if turno==0 else 'O'
    print(f"\nTurno del Jugador {turno + 1} ({Jugador})")
    #Válida posición
    while True:
        try:
            #Convierte la entrada en número y ajusta e indice (0-8)
            posicion=int(input("Elige una posicion (1-9):"))- 1
            #Verifica si la casilla está libre
            if 0<= posicion <=8 and tablero[posicion]==' ':
                break #Salir de l bucle si este es válido
            print("Posicion inválida u ocupada")
        except: #Lanza error si no se ingresa un número
            print("Ingresa un número del 1 al 9")
    #Realiza el movimiento en el tablero
    tablero[posicion]=Jugador
    
    #Verificación de ganador
    for a,b,c in ganadores:
        #Comprueba línea ganadora
        if tablero[a]==tablero[b]==tablero[c] != ' ':
            print(f"\n¡Jugador {turno + 1} {Jugador} ganó!")
            #Mostrar tablero final
            print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}")
            print("----------")
            print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
            print("----------")
            print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")
            exit()
    #Cambiar turno
    turno= 1 - turno
    

#Si se completa todos los movimientos sin ganador, es empate
print("\n ¡Empate!")
print(f"\n {tablero[0]} | {tablero[1]} | {tablero[2]}")
print("----------")
print(f"{tablero[3]} | {tablero[4]} | {tablero[5]}")
print("----------")
print(f"{tablero[6]} | {tablero[7]} | {tablero[8]}")