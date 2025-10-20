import random

def generar_numeros():
    # genera el numero sin que se repita algun numero
    a = random.randint(0, 9)
    b = random.randint(0, 9)
    while b == a:
        b = random.randint(0, 9)

    c = random.randint(0, 9)
    while c == a or c == b:
        c = random.randint(0, 9)

    d = random.randint(0, 9)
    while d == a or d == b or d == c:
        d = random.randint(0, 9)

    return a, b, c, d


def evaluar_intento(a, b, c, d, numero_jugador):
    # separa los numeros escritos por el jugador y los compara con el numeros generados
    w = int(numero_jugador[0])
    x = int(numero_jugador[1])
    y = int(numero_jugador[2])
    z = int(numero_jugador[3])

    fama = 0
    toque = 0

    if a == w:
        fama += 1
    elif a in [x, y, z]:
        toque += 1

    if b == x:
        fama += 1
    elif b in [w, y, z]:
        toque += 1

    if c == y:
        fama += 1
    elif c in [w, x, z]:
        toque += 1

    if d == z:
        fama += 1
    elif d in [w, x, y]:
        toque += 1

    return fama, toque


# JUEGO EN SI

print("Toque y Fama")

a, b, c, d = generar_numeros() # le da valor a 'a,b,c,d'

intentos = 5

while intentos != 0:
    print(f"{intentos} intentos")
    numero_jugador = input(f"Escribe un numero: ")

    if len(numero_jugador) != 4:
        print("Intenta nuevamente.")
        continue

    fama, toque = evaluar_intento(a, b, c, d, numero_jugador)
    print(f"Famas: {fama} | Toques: {toque}")
    intentos -= 1

    if fama == 4:
        print(f"Ganaste. El número era {a}{b}{c}{d}")
        break

print(f"Perdiste. El número era {a}{b}{c}{d}")