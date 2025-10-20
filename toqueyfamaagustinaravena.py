import random #importar random

digitos = [str(d) for d in random.sample(range(10), 4)]
print(digitos)  #crear numeros aleatorios del 0 al 9




def fama_y_toques(digitos,intento):  #modulo de fama

    famas = 0
    toques = 0
    indice_famas = []

    for i in range(len(digitos)):
        if digitos[i] == intento[i]: #recorre toda la columna del digito creado para verificar si son iguales
            famas +=1
            indice_famas.append(i)
    digitos_restantes = [digitos[i] for i in range(len(digitos)) if i not in indice_famas] #crea un una lista de numeros que no esten en indice famas
    intento_restante = [intento[i] for i in range(len(digitos)) if i not in indice_famas] #crea otra lista de numeros que no son famas en indice famas

    for d in intento_restante:   #para d dentro de la lista intento restante
        if d in digitos_restantes:    #si d esta en digitos restantes, se le suma 1 toque y se borra el numero para q no se repita
            toques += 1
            intento_restante.remove(d)    

            

    return famas, toques


# adivino es igual a falso con 5 intentos
adivino = False
maximo_intentos = 5
intentos = 0

while not adivino and intentos < maximo_intentos: #mientras no adivine y intentos sea menor al maximo el juego continuara
    intento = list(input('>'))
    if len(intento) !=4:
        print("porfavor ingresa 4 digitos")
        continue
    famas, toques = fama_y_toques(digitos,intento)
    adivino = fama_y_toques(digitos,intento)
    if famas == 4:
        print("ganaste")
        adivino = True
    else:
        print("tienes", famas, "famas y", toques, "toques")
        intentos +=1
        print("llevas",intentos, "intentos")
        adivino = False

if not adivino:
    print("perdiste")
    print("el numero escondido era", digitos)
