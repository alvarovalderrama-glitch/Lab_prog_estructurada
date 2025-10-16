import random
def generar_numero_secreto(longitud=5):
    digitos=list(range(10))
    numero_secreto=random.sample(digitos, longitud)
    return[str(d) for d in numero_secreto] #Convierte a string

def obtener_intento(longitud=5):
    while True:
        intento=input(f"Ingresa tu supocision de {longitud} digitos:")
        if len(intento) != longitud or not intento.isdigit() or len(set(intento)) != longitud:
            print(f"¡Entrada invalida, debes ingresar {longitud} digitos unicos!")
        else:
            return list(intento)
        
def calcular_toques_famas(numero_secreto, intento):
    toques=0
    famas=0
    for i in range(len(numero_secreto)):
        if intento[i]==numero_secreto[i]:
            famas+=1
        elif intento[i] in numero_secreto:
            toques+=1
    return toques, famas

numero_secreto=generar_numero_secreto()
intentos_maximos=30 #Se puede cambiar para ajuste personal
intentos_realizados=0
print("Bienvenido a toque y Fama")
print("Adivina el numero secreto de 5 digitos unicos")
while intentos_realizados<intentos_maximos:
    intento=obtener_intento()
    intentos_realizados+=1
    toques, famas = calcular_toques_famas(numero_secreto, intento)

    print(f"Toques: {toques}, Famas: {famas}")

    if famas == 5:
        print(f"¡Felicidades! ¡Advinaste el numero secreto en {intentos_realizados} intentos!")
if famas !=5:
    print(f"¡Oh no! Te quedaste sin intentos. El numero secreto era: {''.join(numero_secreto)}")