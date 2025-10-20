import random

def generar_numero():
    digitos = random.sample(range(10), 4)
    return ''.join(map(str, digitos))

def obtener_intento():
    while True:
        intento = input("Ingresa un número de 4 dígitos únicos: ")
        if len(intento) == 4 and intento.isdigit():
            if len(set(intento)) == 4:
                return intento
        print("Número inválido. Ingresa 4 dígitos únicos.")

def obtener_pistas(secreto, intento):
    famas = sum(s == i for s, i in zip(secreto, intento))
    toques = 0
    for i, digito in enumerate(intento):
        if digito in secreto and secreto[i] != digito:
            toques += 1
    return toques, famas

def juego_tyf():
    secreto = generar_numero()
    intentos = 0
    max_intentos = 10
    
    print("¡Bienvenido al juego de Toque y Fama!")
    print("- Tienes que adivinar un número de 4 dígitos (No repetidos).")
    print("- Famas: dígitos correctos en la posición correcta.")
    print("- Toques: dígitos correctos en una posición incorrecta.")
    print(f"- Tienes {max_intentos} intentos máximo.")
    
    while intentos < max_intentos:
        intento = obtener_intento()
        intentos += 1
        
        toques, famas = obtener_pistas(secreto, intento)
        
        if famas == 4:
            print(f"¡Felicidades! Adivinaste el número {secreto} en {intentos} intentos.")
            break
        
        print(f"Toques: {toques} - Famas: {famas}")
        print(f"{max_intentos-intentos} intentos restantes.\n")
    else:
        print(f"¡Perdiste! El número era {secreto}.")

juego_tyf()