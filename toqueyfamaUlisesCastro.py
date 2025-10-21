import random

print("ADIVINA EL NÚMERO, tienes 5 intentos")

#Generación del Numero Secreto
random1 = str(random.randint(0, 9)) 

while True:
    random2 = str(random.randint(0, 9))
    if random2 != random1:
        break

while True:
    random3 = str(random.randint(0, 9))
    if random3 != random1 and random3 != random2:
        break

while True:
    random4 = str(random.randint(0, 9))
    if random4 != random1 and random4 != random2 and random4 != random3:
        break

numero_secreto = random1 + random2 + random3 + random4

intentos = 5
famas = 0
toques = 0

#donde juegas

while (famas != 4) and (intentos>0):
    
    toques = 0
    famas = 0
    tirada = input("Ingrese su número de 4 dígitos: ")
    tirada1 = tirada[0]
    tirada2 = tirada[1]
    tirada3 = tirada[2]
    tirada4 = tirada[3]
    
   #calculo de cuantas famas hay en el intento
    
    if tirada1 == random1:
        famas = famas +1
    if tirada2 == random2:
        famas = famas +1
    if tirada3 == random3:
        famas = famas +1
    if tirada4 == random4:
        famas = famas +1
        
    #Cálculo de cuantos toques hay en el invento
    if tirada1 in numero_secreto:
        if tirada1 != random1:
            toques = toques + 1
    if tirada2 in numero_secreto:
        if tirada2 != random2:
            toques = toques + 1
    if tirada3 in numero_secreto:
        if tirada3 != random3:
            toques = toques + 1
    if tirada4 in numero_secreto:
        if tirada4 != random4:
            toques = toques + 1
    print(f"Resultado: {famas} Famas, {toques} Toques")
    
    if famas == 4:
        print("¡Fama, Ganaste!")
        
    intentos = intentos - 1
    if intentos == 0 and famas != 4:
        print("No te quedan más intentos.")
        print(f"El número secreto era: {numero_secreto}")