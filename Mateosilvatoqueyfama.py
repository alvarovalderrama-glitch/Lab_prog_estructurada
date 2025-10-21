# Toque y Fama
# Juego tipo "Bulls and Cows": Fama = dígito correcto y en posición; Toque = dígito correcto en otra posición.

import random                                                     # Librería aleatoria

def numero_secreto():                                             # Crea 4 dígitos únicos
    digitos = list("0123456789")                                  # Lista de 0..9
    random.shuffle(digitos)                                       # Mezcla
    if digitos[0] == "0":                                         # Evita comenzar con 0
        digitos[0], digitos[1] = digitos[1], digitos[0]           # Intercambia
    return "".join(digitos[:4])                                   # Toma 4

def evaluar(secreto, intento):                                    # Cuenta toques/famas
    fama = sum(a==b for a,b in zip(secreto, intento))             # Coincidencias exactas
    toque = sum(c in secreto for c in intento) - fama             # En cualquier lugar menos famas
    return toque, fama                                            # Devuelve tupla

sec = numero_secreto()                                            # Genera secreto
# print(sec)  # (Descomenta para depurar)
print("Adivina el número de 4 dígitos distintos. ¡Suerte!")       # Mensaje inicial
intentos = 0                                                      # Contador

while True:                                                       # Bucle principal
    cad = input("Tu intento: ").strip()                           # Lee intento
    if len(cad)==4 and cad.isdigit() and len(set(cad))==4:        # Valida formato
        intentos += 1                                             # Suma intento
        t,f = evaluar(sec, cad)                                   # Evalúa
        print(f"Toques: {t} | Famas: {f}")                        # Muestra
        if f == 4:                                                # ¿Acertó todo?
            print(f"¡Ganaste en {intentos} intentos!"); break     # Fin
    else:
        print("Debe ser de 4 dígitos distintos, sin repetir.")
