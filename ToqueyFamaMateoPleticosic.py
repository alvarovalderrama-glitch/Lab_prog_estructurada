import random

# Módulo: Número Secreto
def numero_aleatorio():
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)
    while a == b or a == c or a == d or b == c or b == d or c == d:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
    return f"{a}{b}{c}{d}"

# Módulo: Jugada Válida
def es_jugada_valida(jugada):
    if len(jugada) != 4:
        print("Error: El número debe tener 4 dígitos.")
        return False
    
    if not jugada.isdigit():
        print("Error: Debes ingresar solo números.")
        return False
        
    if len(set(jugada)) < 4:
        print("Error: Los dígitos no deben repetirse.")
        return False
    
    return True

# Módulo: Calcular resultado
def calcular_resultado(secreto, numero_ingresado):
    famas = 0
    toques = 0
    
    # 1) Famas
    for i in range(4):
        if numero_ingresado[i] == secreto[i]:
            famas += 1
            
    # 2) Aciertos totales
    aciertos_totales = 0
    for digito_jugador in numero_ingresado:
        if digito_jugador in secreto:
            aciertos_totales += 1
            
    # 3) Toques
    toques = aciertos_totales - famas
    
    print(f"Resultado: {famas} Fama(s) y {toques} Toque(s).")
    return famas

# ----------------- Programa principal -----------------
secreto = numero_aleatorio()
intentos = 0
gano = False
print("¡Bienvenido a Toque y Fama! Tienes 10 intentos para adivinar el número de 4 dígitos.")


while gano == False:
    intentos = intentos + 1
    if intentos >10:
        print("Has perdido" )
        break
    
    numero_ingresado = input(f"Intento {intentos}: Ingresa un número de 4 dígitos: ")
    
    if not es_jugada_valida(numero_ingresado):
        continue
    
    famas_obtenidas = calcular_resultado(secreto, numero_ingresado)

    if famas_obtenidas == 4:
        print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
        gano = True
