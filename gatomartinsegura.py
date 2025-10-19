from random import randint
from os import system
opciones =[str(i) for i in range(1,10)]
opciones_bot = opciones.copy()
ganador ="_"
def tabla():
    #genera la tabla
    for i in range(-1,6,3):
        print(f"{opciones[i+1]} | {opciones[i+2]} | {opciones[i+3]}")
        print("--|---|--")
	
def verificar_si_hubo_ganador():
    for i in [jugador,bot1]:
    
    #verifica si hubo un ganador en la lineas verticales o horizontales
        for j in range(3):
            if all([opciones[f] == i for f in range(j,9,3)]):

                return gano(i)
            if all([opciones[f] == i for f in range((3*(j+1))-3,(3*(j+1)))]):
                return gano(i)
        #ahora revisa las diagonales
        for j in range(2):

            if all([opciones[f] == i for f in range(2*j,9,4-(2*j))][:3]):
                return gano(i)
    return False

#Se evalua el movimiento del jugador
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
#da al ganador 
def gano(i):
    global ganador
    if (i == jugador == "X") or (i == jugador == "O"):
                
        ganador = "ganaste"
    else:        
        ganador = "perdiste"
    return True
def bot():
    if len(opciones_bot) != 0:
        
        eleccion =	randint(0,len(opciones_bot)-1)
        op = opciones.index(opciones_bot[eleccion])
        opciones[op] = bot1	    	
        del opciones_bot[eleccion]

jugador = input("1) Para jugar con las x y 2) para jugar con las O\n")

if jugador == "1" or jugador != "2":
    jugador = "X"
    bot1 = "O"
else:
    jugador = "O"
    bot1 = "X"

for i in range(1,11):
    system("clear")
    tabla()
    if not verificar_si_hubo_ganador():
        if i%2!=0:
            print("Turno Jugador:")
            eleccion()
        else: bot()	
    else:
        print(ganador)
        exit()
print("Empate")
