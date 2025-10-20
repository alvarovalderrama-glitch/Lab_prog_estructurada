print ("Hola,juguemos al toque y fama")
import random 
a= random.randint(0,9) #numero aleatorio de 4 digitos
b= random.randint(0,9)
c= random.randint(0,9)
d= random.randint(0,9)
n=0
def separacion(): #funcion para separar los digitos
        n=int(input("ingresa un numero: ")) #ingreso de numero
        aux=n
        z=aux%10
        aux=(aux-z)//10
        y=aux%10
        aux=(aux-y)//10
        x=aux%10
        aux=(aux-x)//10
        w=aux
        return n,w,x,y,z
def escribe(w,x,y,z): #funcion para mostrar los digitos separados
         print(f"tu numero ingresado es:{w,x,y,z}")
while a==b or a==c or a==d or b==c or b==d or c==d:
    a= random.randint(0,9)
    b= random.randint(0,9)
    c= random.randint(0,9)
    d= random.randint(0,9)
print ("ingrese un número de 4 digitos")
intentos=5
fama=0
toque=0
aux=0
while intentos>0: #bucle principal de intentos
    intentos-=1
    fama=0
    toque=0
    n,w,x,y,z = separacion()
    escribe(w,x,y,z) #llamada a la funcion escribe
    while w==x or w==y or w==z or x==z or y==z or n>9999 or n<0: #verificacion de digitos iguales
        if  w==x or w==y or w==z or x==z or y==z:
           print ("digitos iguales, ingrese otro numero.")
           n= int(input("ingrese un número de 4 digitos:"))
           n,w,x,y,z=separacion()
           escribe(w,x,y,z)
        elif n>9999:
            print("numero mayor que 9999, ingresa otro numero: ")
            n,w,x,y,z=separacion()
            escribe(w,x,y,z)
        elif n<0:
             print("numero menor que 0, ingresa otro numero: ")
             n,w,x,y,z=separacion()
             escribe(w,x,y,z)
    if a==w:  #verificacion de toque y fama
         fama+=1 #contador de fama
    elif a==x or a==y or a==z:
         toque+=1
    if b==x:
          fama+=1
    elif b==w or b==y or b==z:
         toque+=1
    if c==y:
         fama+=1
    elif c==w or c==x or c==z:
         toque+=1
    if d==z:
         fama+=1
    elif d==w or d==x or d==y:
         toque+=1
    print(f"tienes {toque} numero/s bueno/s, pero en la posición equivocada y tienes {fama} numero/s bueno/s y en la posición correcta. \n\n")
    if fama==4: #verificacion de victoria
         intentos=0
    else:  #verificacion de intentos restantes
         print(f"te quedan {intentos} intentos restantes. \n\n" )
         print ("ingresa otro numero de 4 digitos")
if fama==4:  #mensaje de victoria o derrota
     print("felicidades,ganaste. ")
     print(f"el numero era {a,b,c,d}")
else: #mensaje de derrota
     print(f"perdiste, el numero era {a,b,c,d}")
            
        
        
            





