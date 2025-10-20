import random

    # Generador de numero aleatorio
    
digitos = list(range(10)) # Crea los números del 0 al 9
random.shuffle(digitos) # Cambia el orden
secreto = str(digitos[0]) + str(digitos[1]) + str(digitos[2]) + str(digitos[3]) #Toma los primeros 4

print(" Juego Toque Y Fama ")
print("Debes adivinar un número de 4 dígitos diferentes.")
print(secreto)

intentos = 0  # Variable que cuenta cuantos intentos se han hecho
famas = 0 # Inicializar la fama en 0

    # Bucle principal
    
while famas != 4:  # El juego se repite hasta que no se tengan 4 famas
    adivinar = input("Ingresa tu intento (4 dígitos): ")
    intentos += 1 # Cada vez que se entra en el bucle se suma un intento
    famas = 0 # Se reinician los contadores para este nuevo intento  
    toques = 0

    # Contador famas y toques
    
    for i in range(4):  # Recorre las posiciones de los numeros
        if adivinar[i] == secreto[i]: # Si el numero intentado esta en la misma posicion de secreto se suma 1 fama
            famas += 1
        elif adivinar[i] in secreto: # Si el intento esta en el numero secreto se suma 1 toque
            toques += 1

    print("Intento", intentos, " Famas:", famas, " Toques:", toques) # Imprime el numero de intento, las famas y los toques

print("¡Felicitaciones! Adivinaste el número secreto:", secreto)
print("Usaste", intentos, "intentos.")
