import random

def generar_numero_aleatorio():
    #Genera un numero de 4 digitos sin repetir
    digitos = list(range(10))
    random.shuffle(digitos)
    return ''.join(str(d) for d in digitos[:4])

def validar_intento(intento):
    #Valida que el intento sea un número de 4 dígitos sin repetir
    if len(intento) != 4:
        return False
    if not intento.isdigit():
        return False
    if len(set(intento)) != 4:  # Verifica que no haya digitos repetidos
        return False
    return True

def calcular_toques_y_famas(aleatorio, intento):
    #Calcula toques y famas entre el numero aleatorio y el intento
    toques = 0
    famas = 0
    
    for i in range(4):
        if intento[i] == aleatorio[i]:
            famas += 1
        elif intento[i] in aleatorio:
            toques += 1
    
    return toques, famas

def iniciar_toque_y_fama():
   #Esquema del juego
    print("=== Toque Y Fama ===")
    print("Adivina el numero de 4 digitos (sin repetir)")
    print("Toques: digito correcto en posicion incorrecta")
    print("Famas: digito correcto en posicion correcta")
    print("Cuando obtengas 4 famas ganas")
    print("-" * 40)
    
    # Genera numero aleatrio
    aleatorio = generar_numero_aleatorio()
    intentos = 0
    
    while True:
        # el jugador coloca su intento 
        intento = input("\n Ingresa tu intento de 4 digitos: ")
        
        # Validar el intento
        if not validar_intento(intento):
            print("Error: Elija un numero de 4 dígitos sin digitos repetidos")
        else: continue
        '''rendirse = input('¿Se quiere rendir? Si=1 No=2')
        if rendirse == 1:
            print('Buen intento')
        else: continue'''            
        
        intentos += 1
        
        # calcula toques y famas
        toques, famas = calcular_toques_y_famas(aleatorio, intento)
        
        # muestra el resultado
        print(f"Intento #{intentos}: {intento} -> {toques} Toques, {famas} Famas")
        
        # verificar si el jugador gano
        if famas == 4:
            print(f"\n Adivinaste el numero {aleatorio} en {intentos} intentos")
            break

# Iniciar el juego
    iniciar_toque_y_fama()