import random
#Funcion creada para generar el numero secreto a adivinar
def numero_secreto():        
    #Asegurarnos que el primer numero no sea 0
    numero_inicial = random.sample('123456789', 1) [0]    
    #Asegurarnos que no se repitan con el numero inicial
    numeros_aparte = random.sample('0123456789'.replace(numero_inicial, ""), 3) 
    #Nos aseguramos de juntar los elementos
    return numero_inicial + ''.join(numeros_aparte)

#Definimos una funcion para el intento del jugador
def pedir_intentos(): 
    while True:
        intento = input("Ingresa tu intento (4 dígitos): ").strip()
        #Nos aseguramos que el conjunto sea solo de 4 digitos
        if len(intento) != 4 or not intento.isdigit():
            print("Debe ingresar exactamente 4 digitos (0-9). ")
            continue
        #Nos aseguramos que el conjunto no comienze con un 0
        if intento[0] == '0':
            print("El conjunto a ingresar no puede comenzar con un 0.")
            continue
        #Verificamos que no posea digitos repetidos
        if len(set(intento)) != 4:
            print("No se permiten dígitos repetidos.")
            continue
        #Luego de todas las verificaciones, devolvemos el intento valido:)
        return intento
    
#Creamos una funcion para comparar nuestro numero generado y el intento del jugador
def toqueyfama(numero_secreto, intento):
    fama = 0
    toque = 0
#Creamos un bucle para contar las posiciones exactas(famas)
    for i in range(4):
        if numero_secreto[i] == intento[i]:
            fama = fama + 1 
#Creamos otro bucle para contar los digitos acertados (toques)
    for i in range(4):
        if intento[i] in numero_secreto:
            if numero_secreto[i] != intento[i]:
                toque = toque + 1
    return fama, toque

#Definimos una funcion para implementar un bucle principal 
def jugar():
    secreto = numero_secreto()
    intentos = 0

    print("-----Toque y Fama-----")
    while True:
        intento_usuario = pedir_intentos()
        intentos += 1

        famas, toques = toqueyfama(secreto, intento_usuario)

        print(f"Intento #{intentos}: {famas} famas, {toques} toques")

        if famas == 4:
            print(f"¡Felicidades! Adivinaste el número {secreto} en {intentos} intentos")
            break

jugar()