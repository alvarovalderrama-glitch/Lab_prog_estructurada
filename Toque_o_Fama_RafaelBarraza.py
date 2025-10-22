import random                               #Importamos el modulo random,que contiene funciones para generar números aleatorios.Lo necesitamos para crear el numero secreto del juego.

# Generar 4 números aleatorios distintos 

numeros_disponibles = list(range(10))       #Creamos la variable numeros_disponibles, la cual tendra una lista generada por los numeros 0,1,2,3,4,5,6,7,8,9
random.shuffle(numeros_disponibles)         # Mezcla de manera aleatoria los elementos de la lista.
a, b, c, d = numeros_disponibles[:4]        # Tomamos los 4 primeros numeros de la lissta luego de mezclarse

print('Bienvenido a Toque y Fama ')                         #Da la bienvenida al jugaddor y muestra las instrucciones al jugador.
print("Adivina los 4 números secretos (0-9), todos distintos.")
print("Ingresa los 4 números juntos, por ejemplo: 3951")

fama = 0            #Cuenta cuantos digitos acerto el jugador en la posicion correcta
intentos = 0        #Lleva el número de intentos realizados.
max_intentos = 4    #Define el límite máximo de intentos (en este caso, 4).

# Bucle principal 
while fama != 4 and intentos < max_intentos:     #Mientras que fama sea distinto de 4 y los intentos sean menos que el maximo de los intentos, cuando una de estas dos condiciones deja de cumplirse, el bucle termina (o ganó, o se le acabaron los intentos).

    # Pedir al jugador un número de 4 dígitos 

    while True:                                  #Iniciamos un ciclo que se repetira infinitamente pidiendole un numero de 4 digitos al jugador y esto no dejara de repetirse hasat que se ingrese un numero valido ahi se produce un break y se sale del while
       
        entrada = input(f"\nIntento {intentos+1}/{max_intentos} - Ingresa tus 4 números: ")     #Le permite ingresar los 4 numeros al jugador, ademas le muestra la cantidad de intentos que le quedan 
        
        if len(entrada) != 4 or not entrada.isdigit():                                          #Comprueba que la entrada tenga exactamente 4 digitos, y que lo ingresado sean solo numeros y no letras o simbolos.
            print("Debes ingresar exactamente 4 dígitos numéricos. Intenta de nuevo.")

        elif len(set(entrada)) != 4:                                                            #Con set(entrada) convierte la cadena en un conjunto y elimina los elementos repetidos, luego ve si la entrada contiene exactamente los 4 digitos.
            print("No puedes repetir dígitos. Intenta de nuevo.")

        else:
            break                                                                               #Si pasa las validaciones, sale del bucle while True y continúa el juego.

    # Convertir cada dígito en variables individuales 

    w, x, y, z = int(entrada[0]), int(entrada[1]), int(entrada[2]), int(entrada[3])             #Separa el numero del jugador en 4 variables, la entrada[0] es el prier digito y asi sucesivamente,luego se convierten en enteros (int) para poder compararlos con los números secretos a, b, c, d.

    intentos += 1                                                                               #Se suma un intento, y se reinician los contadores de toques y famas para este turno.
    fama = 0
    toque = 0

    #  Comparar posición por posición
    if w == a: fama += 1
    if x == b: fama += 1
    if y == c: fama += 1
    if z == d: fama += 1

    # Toques: número correcto pero posición incorrecta

    if w != a and w in [b, c, d]: toque += 1        #Verificamos que no sea una fama y que el número exista en el resto del número secreto, pero en otra posición.
    if x != b and x in [a, c, d]: toque += 1
    if y != c and y in [a, b, d]: toque += 1
    if z != d and z in [a, b, c]: toque += 1

    print(f" Toques: {toque} | Famas: {fama}")      #Muestra al jugador los resultados de su intento

# Mensaje final 
if fama == 4:                                       #Verifica si fama es igual a 4

    print(f"\n ¡Ganaste! Los números secretos eran: {a}{b}{c}{d}")    #Muestra un mensaje de victoria con los numeros secretos  
    print(f"Lo lograste en {intentos} intentos.")                     #Tambien muestra en cuantos intentos logro acertar.    
else:
    print(f"\n Se acabaron los intentos. Los números secretos eran: {a}{b}{c}{d}")   #Se muestra el mensaje de derrota debido a que no encontro las 4 famas y, ya no se cumple una de las condiciones#
                                                                                     #la cual era que intentos tenia que ser menor que el maximo de intentos.
