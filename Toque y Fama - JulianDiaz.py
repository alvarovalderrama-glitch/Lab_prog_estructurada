import random

# Genera 4 dígitos únicos
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

print("Número secreto generado. ¡Intenta adivinarlo!")

famas = 0
intentos = 0
# print(a,b,c,d)  # Línea de prueba para ver el número secreto

# Bucle principal del juego
while famas != 4 and intentos < 4:
    intento = int(input("Ingresa un número de 4 dígitos distintos: "))
    intentos += 1

    # Separa el número ingresado en 4 dígitos
    d1 = intento // 1000
    d2 = (intento // 100) % 10
    d3 = (intento // 10) % 10
    d4 = intento % 10

    # Valida que no se repitan
    if d1 == d2 or d1 == d3 or d1 == d4 or d2 == d3 or d2 == d4 or d3 == d4:
        print("Número inválido")
        intentos -= 1
    else:
        famas = 0
        toques = 0

        # Verifica coincidencias exactas (famas) o parciales (toques)
        if d1 == a: famas += 1
        elif d1 in [b, c, d]: toques += 1

        if d2 == b: famas += 1
        elif d2 in [a, c, d]: toques += 1

        if d3 == c: famas += 1
        elif d3 in [a, b, d]: toques += 1

        if d4 == d: famas += 1
        elif d4 in [a, b, c]: toques += 1

        print("Intento", intentos, "- Famas:", famas, "Toques:", toques)

# Resultado final
if famas == 4:
    print("¡Ganaste en", intentos, "intentos! El número era:", a, b, c, d)
else:
    print("Se acabaron los intentos. El número era:", a, b, c, d)
