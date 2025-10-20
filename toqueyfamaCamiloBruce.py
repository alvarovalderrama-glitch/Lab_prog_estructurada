import random 
#Toque digito correcto, pos incorrecta; Fama digito correcto, pos correcta.
#Variables globales.
intentos=5
secreto=0
fama=0
toque=0

#---------------------------------------------------------------

def digitos(): #Se encarga de generar el numero secreto, este debe tener 4 digitos.
    A=random.randint(1,9) # Rango del 1 al 9, asi se "genera" un numero mayor a 1000
    B=random.randint(0,9)
    while A==B: #El juego requiere que todos los digitos sean diferentes, aca se revisa que A y B no sean iguales.
        B=random.randint(0,9)
    C=random.randint(0,9)
    while B==C or A==C: # Aca se hace lo mismo de recien, verifica que C no sea igual que A y B.
        C=random.randint(0,9)
    D=random.randint(0,9)
    while A==D or B==D or C==D:
        D=random.randint(0,9) # Lo mismo que antes.
    secreto=[A,B,C,D] # Convierte los numeros en una lista.
    return secreto

#---------------------------------------------------------------

def valida_intento(usuario_resp): #Valida los intentos que ingrese el usuario.
    if len(usuario_resp)!=4: # Verifica que la respuesta dada por el usuario tenga 4 digitos.
        print('El numero tiene que tener 4 digitos, intentalo de nuevo.')
        return False
    if not usuario_resp.isdigit(): #Verifica que el usuario haya ingresado digitos.
        print('Solo se permiten digitos, intentalo de nuevo.')
        return False
    if len(set(usuario_resp))!=4: #Verifica que todos los digitos sean diferentes.
        print('Todos los digitos deben ser diferentes, intentalo de nuevo')
        return False
    return True

#---------------------------------------------------------------

def tyf(secreto, intento): # Calcula los toques y las famas.
    fama=0
    toque=0
    intento_lista=[int(digito) for digito in intento] # Convierte el intento en una lista.
    
    for i in range(4):
        if secreto[i] == intento_lista[i]: #Compara digito por digito, posicion por posicion
            fama = fama+1 # Si dos digitos son iguales y estan en la misma posicion, se suma una fama.

    for i in range(4):
        if intento_lista[i] in secreto and intento_lista[i] != secreto[i]: # Verifica que el digito esté en el numero secreto, pero no en la misma pos
            toque = toque+1 # Si se cumple esto, se suma un toque

    return toque, fama

#---------------------------------------------------------------

def juego():
    global intentos, secreto, fama, toque
    secreto=digitos()

    while intentos>0: #Mientras que los intentos sean mayor a 0, se realiza lo siguiente.
        print(f"Te quedan {intentos} intentos restantes.")

        while True: # Se repite hasta que el jugador ingrese un numero valido.
            usuario_resp = input('Ingresa el numero de 4 digitos: ')
            if valida_intento(usuario_resp):
               break
        
        toque, fama = tyf(secreto, usuario_resp) #Calcula los toques y las famas, se los muestra al jugador.
        print(f"Resultado: {toque} Toques, {fama} Famas")

        if fama==4: #Si se logran 4 famas (es decir, todos los digitos ingresados estan en su respectiva posicion)
            print('¡Has adivinado el numero!') # Se le avisa al jugador que ganó, además se le muestra el numero secreto
            print(f"El numero era {secreto}")
            return True
    
        intentos=intentos-1 #Se restan los intentos, empezando desde el 5.

    print('No has logrado adivinar el numero.') # Cuando los intentos llegan a 0 y el jugador no adivina, se le notifica que perdio.
    print(f"El numero era {secreto}") # Además se le muestra el numero.

#---------------------------------------------------------------

juego()
