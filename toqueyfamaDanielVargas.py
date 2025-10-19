import random

#============================= Se definen las siguientes variables y funciones para el programa ===============================

aprobado1=0
aprobado2=0
toque=0
fama=0
intentos=10  

def generador_del_numero(aprobado1):
    global x,y,z,w
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=random.randint(0,9)
    w=random.randint(0,9)
    while aprobado1==0:
        if w!=x and w!=y and w!=z: # Con cada "if" se van comparando los números para que no se repitan entre sí
            if z!=x and z!=y:
                if y!=x:
                    aprobado1=1
                else:
                    y=random.randint(0,9)
            else:
                z=random.randint(0,9)
        else:
            w=random.randint(0,9)
    global numero_generado
    numero_generado=list(str(x)+str(y)+str(z)+str(w))

def comprobacion_entero():
    while True:
        no_se_puede_seguir=0
        try: # Es un ciclo que sigue hasta que el dato ingresado sea un número entero
            print('=================================================================================')
            numero_string=input('Ingrese el número: ')
            numero_entero=int(numero_string)
            break
        except ValueError:
            print('\n|!| LA ENTRADA NO ES VÁLIDA')
    return numero_entero,numero_string,no_se_puede_seguir

def comprobacion_signo_longitud_repeticion(numero_entero,numero_string,no_se_puede_seguir):
    global aprobado2
    aprobado2=0
    if numero_entero>=0: # Verifica que sea positivo
        if len(numero_string)==4: # Verifica que tenga cuatro dígitos
            global numero_listado
            numero_listado=list(numero_string) # Los números se guardan en una lista para analizar cada número por separado
            for posicion_iteracion_1, numero_1 in enumerate(numero_listado): # Se verifica que los números no se repitan
                for posicion_iteracion_2, numero_2 in enumerate(numero_listado):
                    if numero_1==numero_2:
                        if posicion_iteracion_1==posicion_iteracion_2:
                            pass
                        else:
                            no_se_puede_seguir=1
                            break
            if no_se_puede_seguir==1:
                print('\n|!| LA ENTRADA NO ES VÁLIDA')
            else:
                aprobado2=1
        else:
            print('\n|!| LA ENTRADA NO ES VÁLIDA')      
    else:
        print('\n|!| LA ENTRADA NO ES VÁLIDA')

def comparacion_de_numeros():
    global fama,toque
    for pos1,num1 in enumerate(numero_generado): # Se comparar las posiciones y números de "numero_generado" y "numero_listado"
        for pos2,num2 in enumerate(numero_listado):
            if num1==num2 and pos1==pos2:
                fama=fama+1
            elif num1==num2:
                toque=toque+1
            else:
                pass

def hay_ganador(x,y,z,w):
    if fama==4:
        print('                         -------------------------')
        print('                         |      ¡HAS GANADO!     |')
        print('                         -------------------------\n')
    else:
        print('=================================================================================')
        print('\n                                   PERDISTE')
        print('                                  ----------')
        print('                              El número era:',str(x)+str(y)+str(z)+str(w),'\n')
        
#================================================ De aquí parte el programa ===================================================

print('\n=================================================================================')
print('Bienvenido al juego de "Toque y Fama". Deberás adivinar cuatro números aleatrios')
print('distintos entre sí. La cantidad de intentos se presenta a continuación:\n')
generador_del_numero(aprobado1) # Se genera el número para adivinar
while fama!=4 and intentos!=0: # La partida entra en bucle usando todas las funciones hasta que fama=4 o los intentos se acaben.
    print('                         -------------------------')
    print('                         | Intentos restantes:',intentos,'|')
    print('                         -------------------------\n')
    toque=0
    fama=0
    while aprobado2==0: # Bucle que revisa la entrada hasta que sea válida
        numero_entero,numero_string,no_se_puede_seguir=comprobacion_entero()
        comprobacion_signo_longitud_repeticion(numero_entero,numero_string,no_se_puede_seguir)
    comparacion_de_numeros()
    # Termina la revisión y va con los resultados. Las variable "aprobado2" sirve para que la partida entre de nuevo en bucle
    aprobado2=0
    intentos=intentos-1
    print('=================================================================================')
    print(f'\n                        |  TOQUE: {toque}   |   FAMA: {fama}  |\n')
hay_ganador(x,y,z,w)