import random

def comparar(a, b, c, d, x, y, z, w):
    toques = 0
    famas = 0
    
    if a == x:
        famas += 1
    elif a == y or a == z or a == w:
        toques += 1
    if b == y:
        famas += 1
    elif b == x or b == z or b == w:
        toques +=1
    if c == z:
        famas +=1
    elif c == x or c == y or c == w:
        toques +=1
    if d == w:
        famas +=1
    elif d == x or d == y or d == z:
        toques += 1
    
    return toques, famas
    

def generar_numeros():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    while a == b:
        b = random.randint(0,9)
    c = random.randint(0, 9)
    while a == c or b == c:
        c = random.randint(0, 9)
    d = random.randint(0, 9)
    while a== d or b == d or c == d:
        d = random.randint(0, 9)
        
    return a, b, c, d


    

def toque_y_fama():
    print("Bienvenido al juego de toque y fama")
    a, b, c, d = generar_numeros()
    intentos = 0
    ganador = 0
    max_intentos = 5
    
    while intentos < max_intentos and ganador == 0:
        intento_usuario = input("ingrese un número de 4 digitos: ")
        if len(intento_usuario) != 4: #inicio de busqueda de errores
            print("error: debes ingresar un número de 4 digitos.")
            continue
        if not intento_usuario.isdigit():
            print("debes ingresar digitos del 0 al 9")
            continue
        if len(set(intento_usuario)) != 4:
            print("error: los digitos no deben repetirse entre si.")
            continue #fin de busqueda de errores
        
        digitos = [int(ch) for ch in intento_usuario] 
        
        x, y, z, w = digitos[0], digitos[1], digitos[2], digitos[3]
        
        toques, famas = comparar(a, b, c, d, x, y, z, w)
        
        print(f"famas: {famas} | toques: {toques}")
        
        if famas == 4:
            ganador = 1
            print("\n adivinaste el número")
            break
        else:
            intentos = intentos + 1
    if ganador == 0:
        print("\n Perdiste. El número era: {}{}{}{}". format(a, b, c, d))
        return
    
    

    
toque_y_fama()