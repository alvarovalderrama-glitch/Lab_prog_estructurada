from os import system
from random import randint
opciones =[str(i) for i in range(1,10)]
opciones_bot = opciones.copy()
ganador ="_"
def gato():
    for i in range(-1,6,3):
        print(f"{opciones[i+1]} | {opciones[i+2]} | {opciones[i+3]}")
        print("--|---|--")
	
def gano():
    global ganador
    for i in [jugador,bot1]:
        if (opciones [0] == opciones[1] == opciones[2] == i or opciones [3] ==opciones[4] == opciones[5] == i or opciones [6] == opciones[7] ==opciones[8] == i or opciones [0] == opciones[3] == opciones[6] == i or opciones [1] == opciones[4] == opciones[7] == i or opciones [2] ==opciones[5] == opciones[8] == i or opciones [0] == opciones[4] ==opciones[8] == i or  opciones [2] == opciones[4] == opciones[6] == i):
            if (i == "X" and jugador == "X") or (i == "O" and jugador == "O"):
                
                ganador = "ganaste"
                return True
            elif (i == "X" and jugador == "O") or (i == "O" and jugador == "X"):
                ganador = "perdiste"
                return True
    return False


def eleccion():
    boole =True
    while boole:
        des = input("Escriba su movimiento")
        if des.isdigit() and 0<=int(des)-1<= len(opciones) and not opciones[int(des)-1].isalpha():
            opciones_bot.remove(opciones[int(des)-1])
            opciones[int(des)-1] =	jugador 
            boole = False
        else:
            print("El movimiento es invalido")

def bot():
    if len(opciones_bot) != 0:
        
        eleccion =	randint(0,len(opciones_bot)-1)
        op = opciones.index(opciones_bot[eleccion])
        opciones[op] = bot1	    	
        del opciones_bot[eleccion]

jugador = input("(1. Para jugar con las x)  (2. para jugar con las O)\n")

if jugador == "1" or jugador != "2":
    jugador = "X"
    bot1 = "O"
else:
    jugador = "O"
    bot1 = "X"

for i in range(1,11):
    system("clear")
    gato()
    if not gano():
        if i%2!=0:
            print("Turno Jugador:")
            eleccion()
        else: bot()	
    else:
        print(ganador)
        exit()
print("Empate")
