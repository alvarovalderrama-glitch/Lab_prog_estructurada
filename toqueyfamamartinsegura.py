import random
numeros = {}
def numeros_aleatorios():
    posicion=0
    while len(numeros.keys()) != 4:
        nuevo_numero = random.randint(0,9)
        if not (nuevo_numero in numeros.keys()): 
            numeros[nuevo_numero] = posicion
            posicion +=1

def movimiento():
    mov = input("Ingrese 4 numeros distintos:\n>> ")
    
    while len(mov) != 4 or not(mov.isdigit()) or len(set(mov)) != len(mov):
        mov = input("Ingrese numeros validos:\n>> ")

    toques_famas(mov)

def toques_famas(mov):
    global famas
    global toques 
    toques = 0
    famas = 0
    nums = list(numeros.keys())
    for i in range(4):
        if nums[i] == int(mov[i]):
            famas +=1
        elif int(mov[i]) in nums:
            toques +=1

    if famas == 4:
        print("Ganaste")
        exit()



numeros_aleatorios()



for intentos in range(4,0,-1):
    print(f"Intento N°{intentos}")
    movimiento()    
    print(f"Toques:{toques}     Famas:{famas}")
    print("---------------------------------------------------------------")


print("Perdiste")
