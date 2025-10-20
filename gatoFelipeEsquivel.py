print ("juega al gato ") 
x= "___" #variable casilla vacia
a1=x                             #variables de las casillas
a2=x
a3=x
b1=x
b2=x
b3=x
c1=x
c2=x
c3=x
import random #importar libreria random
inicio= random.randint(0,1)     #variable para decidir quien empieza
turnos=9 #variable turnos
ocupado=1 #variable casilla ocupada
ganador=0 #variable ganador
while turnos!=0 and ganador==0: #bucle del juego
    if inicio==0: #si inicio es 0 empieza el jugador
        print ("turno del jugador, tu simbolo es X") 
        ocupado=1 
        while ocupado==1: #bucle para verificar si la casilla está ocupada
            print(f"{a1}|{a2}|{a3}\n{b1}|{b2}|{b3}\n{c1}|{c2}|{c3}") #print del tablero
            print (" Ingrese una casilla del 1 al 9") 
            casilla= input ("ingrese una casilla:") #ingreso de casilla
            if casilla=="1" and a1==x: # verificacion de casilla ocupada
                a1=" x " # marcar casilla
                ocupado=0 #casilla no ocupada
            elif casilla=="2" and a2==x: 
                a2=" x " 
                ocupado=0
            elif casilla=="3" and a3==x: 
                a3=" x " 
                ocupado=0 
            elif casilla=="4" and b1==x: 
                b1=" x "  
                ocupado=0 
            elif casilla=="5" and b2==x: 
                b2=" x " 
                ocupado=0 
            elif casilla=="6" and b3==x: 
                b3=" x " 
                ocupado=0 
            elif casilla=="7" and c1==x: 
                c1=" x " 
                ocupado=0 
            elif casilla=="8" and c2==x: 
                c2=" x " 
                ocupado=0 
            elif casilla=="9" and c3==x: 
                c3=" x " 
                ocupado=0 
            else: 
                print ("esta casilla está ocupada")# mensaje casilla ocupada
        inicio=1 #cambiar turno
        turnos=turnos-1 
        print(f"quedan {turnos} turnos restantes (fue tu turno)") #print turnos restantes
    else:
        print("turno de la computadora") #turno de la computadora
        ocupado=1 #variable casilla ocupada
        while ocupado==1: #bucle para verificar si la casilla está ocupada
            casilla= str(random.randint(1,9)) #seleccion aleatoria de casilla
            if casilla=="1" and a1==x: # verificacion de casilla ocupada
                a1=" O " # marcar casilla
                ocupado=0 #casilla no ocupada
            elif casilla=="2" and a2==x: 
                a2=" O " 
                ocupado=0 
            elif casilla=="3" and a3==x:
                a3=" O " 
                ocupado=0  
            elif casilla=="4" and b1==x: 
                b1=" O " 
                ocupado=0 
            elif casilla=="5" and b2==x: 
                b2=" O " 
                ocupado=0 
            elif casilla=="6" and b3==x: 
                b3=" O " 
                ocupado=0 
            elif casilla=="7" and c1==x: 
                c1=" O " 
                ocupado=0 
            elif casilla=="8" and c2==x: 
                c2=" O " 
                ocupado=0 
            elif casilla=="9" and c3==x: 
                c3=" O " 
                ocupado=0 
            else:
                ocupado=1 #casilla ocupada
        turnos-=1 #disminuir turnos
        inicio=0 #cambiar turno
        print(f"quedan {turnos} turnos restantes (fue turno de la computadora)") #print turnos restantes
    if a1==a2 and a2==a3 and a1!="___" or b1==b2 and b2==b3 and b1!="___" or c1==c2 and c2==c3 and c1!="___" or a1==b1 and b1==c1 and a1!="___" or a2==b2 and b2==c2 and a2!="___" or a3==b3 and b3==c3 and a3!="___" or a1==b2 and b2==c3 and a1!="___" or a3==b2 and b2==c1 and a3!="___":
        ganador=1 #definir ganador
        print(f"{a1}|{a2}|{a3}\n{b1}|{b2}|{b3}\n{c1}|{c2}|{c3}") #print del tablero final
        if inicio==1: #si inicio es 1 gana el jugador
            print("ganaste")
        else: 
            print("perdiste") #si no gana la computadora
        break
    if ganador==0: #si no hay ganador y se acaban los turnos
        if turnos==0:
            print("empate") #mensaje de empate

        
       
        

    
    
    

                
            
        

            
                                         
                                                
                                                    

           

