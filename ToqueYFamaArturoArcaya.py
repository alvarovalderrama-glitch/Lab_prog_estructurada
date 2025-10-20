import random

def numero_secreto(largo):
    digitos = list("0123456789")   #separa cada numero en una lista
    random.shuffle(digitos)        #desordena los numeros de la lista
    return digitos[:largo]         #solo escoge el largo de la lista segun la cantida de digitos a divinar en este caso los primeros 4

def verificar_toque_fama(secreto, intento):
    fama = 0
    toque = 0
    for i in range(len(secreto)):    #va por cada numero de la lista segun el tamaño de esta
        if intento[i] == secreto[i]: #compara el primer numero de la lista del jugador con la que se esta adivinando
            fama += 1                
        elif intento[i] in secreto:  #pregunta si algun numero del jugador esta en la lista 
            toque += 1
    return toque, fama

def jugar():
    print("Bienvenido al juego Toque y Fama")
    largo = 4                              #el largo de la lista, en este caso 4
    secreto = numero_secreto(largo)        #al numero secreto se le da el largo para asi poder tener mas o menos digitos a adivinar
    intentos = 0                           #variable

    while True:
        jugador = input(f"\nIntento #{intentos + 1} - Ingresa {largo} dígitos únicos: ")#se le suma a la variable 1 para asi tener una cuenta de la cantidad de intentos que lleva el jugador 
        if len(jugador) != largo or len(set(jugador)) != largo or not jugador.isdigit(): #toma la cantidad de digitos del jugador y lo compara con el del numero a adivinar, set utilizado para eliminar numeros repetidos, y por ultimo descartar que la entrada no tenga algo que no sea digito
            print("Entrada inválida. Asegúrate de ingresar dígitos únicos.")
            continue

        intento = list(jugador)   #mete en una lista los digitos
        intentos += 1
        toque, fama = verificar_toque_fama(secreto, intento) #llama la funsion y le da el numero secreto y el del jugador para asi empezar compararlos
        print(f"Toques: {toque} | Famas: {fama}")

        if fama == largo:
            print(f"\nAdivinaste el número secreto {''.join(secreto)} en {intentos} intentos.") #se ingresa el valor del numero secreto y la cantidad de intentos
            break

jugar()
