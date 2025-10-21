import random
c1="1"
c2="2"
c3="3"
c4="4"
c5="5"
c6="6"
c7="7"
c8="8"
c9="9"
def tablero():
    print(f"{c1} | {c2} | {c3} ")
    print("---------")
    print(f"{c4} | {c5} | {c6} ")
    print("---------")
    print(f"{c7} | {c8} | {c9} ")
def jugador():
    posicion=input("Escriba su movimiento:")
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    if posicion=="1" and c1=="1":
        c1="X"
    elif posicion=="2" and c2=="2":
        c2="X"
    elif posicion=="3" and c3=="3":
        c3="X"
    elif posicion=="4" and c4=="4":
        c4="X"
    elif posicion=="5" and c5=="5":
        c5="X"
    elif posicion=="6" and c6=="6":
        c6="X"
    elif posicion=="7" and c7=="7":
        c7="X"
    elif posicion=="8" and c8=="8":
        c8="X"
    elif posicion=="9" and c9=="9":
        c9="X"
    else:
        print("Movimiento invalido")
        jugador()
def bot():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    posicion=random.randint(1,9)
    if posicion==1 and c1=="1":
        c1="O"
    elif posicion==2 and c2=="2":
        c2="O"
    elif posicion==3 and c3=="3":
        c3="O"
    elif posicion==4 and c4=="4":
        c4="O"
    elif posicion==5 and c5=="5":
        c5="O"
    elif posicion==6 and c6=="6":
        c6="O"
    elif posicion==7 and c7=="7":
        c7="O"
    elif posicion==8 and c8=="8":
        c8="O"
    elif posicion==9 and c9=="9":
        c9="O"
    else:
        bot()
def verificar_ganador():
    if (c1==c2==c3=="X" or c4==c5==c6=="X" or c7==c8==c9=="X" or c1==c4==c7=="X" or c2==c5==c8=="X" or c3==c6==c9=="X" or c1==c5==c9=="X" or c3==c5==c7=="X"):
        print("Felicidades, has ganado!")
        return True
    elif (c1==c2==c3=="O" or c4==c5==c6=="O" or c7==c8==c9=="O" or c1==c4==c7=="O" or c2==c5==c8=="O" or c3==c6==c9=="O" or c1==c5==c9=="O" or c3==c5==c7=="O"):
        print("Has perdido contra el bot.")
        return True
    else:
        return False
def verificar_empate(jugadas):
    if jugadas>=9:
        print("El juego ha terminado en empate.")
        return True
    else:
        return False
ganador=False
empate=False
jugadas=0
while True:
    tablero()
    jugador()
    jugadas+=1
    ganador=verificar_ganador()
    empate=verificar_empate(jugadas)
    if ganador==True and empate==False:
        tablero()
        break
    elif empate==True and ganador==False:
        tablero()
        break
    bot()
    jugadas+=1
    ganador=verificar_ganador()
    empate=verificar_empate(jugadas)
    if ganador==True and empate==False:
        tablero()
        break
    elif empate==True and ganador==False:
        tablero()
        break


