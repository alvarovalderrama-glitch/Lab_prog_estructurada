import random #importa "random" para elegir numeros al azar

secreto = random.sample("0123456789", 4) #de random importa sample para elegir numeros al azar, elige 4 numeros del 0 al 9  y los guarda el lista
intentos = 0 #contador de intentos
juego_activo = True #variable para mantener el juego corriendo

print("Adivina el número secreto de 4 cifras (no se repiten).")

#bucle principal del juego
while juego_activo:
    intento = input("Ingresa tu número: ") #pide al usuario que ingrese un numero
    
    if len(intento) != 4: #valida que el numero tenga 4 cifras
        print("Debe ser de 4 cifras.")
        continue #vuelve al inicio del bucle
#resetea los contadores de toque y fama
    famas = 0
    toques = 0
    intentos = intentos + 1 #suma un intento

    for i in range(4): #revisa cada numero del intento (del 0 al 3)
        if intento[i] == secreto[i]: #si el numero y la posicion son correctos
            famas = famas + 1
        elif intento[i] in secreto: #si el numero es correcto pero esta en otra posicion
            toques = toques + 1

    print(f"--- Resultado: {famas} Famas, {toques} Toques ---") #muestra el resultado del turno
#revisa si el jugador gano
    if famas == 4:
        print(f"¡Ganaste! Adivinaste en {intentos} intentos.") #muestra el numero secreto
        print(f"El número era: {''.join(secreto)}")
        juego_activo = False #termina el juego
