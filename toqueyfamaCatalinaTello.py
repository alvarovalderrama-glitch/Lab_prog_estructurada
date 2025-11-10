import random

def generar():
    d = list('0123456789')
    random.shuffle(d)
    return ''.join(d[:4])

def contar(secret, intento):
    famas = sum(1 for a,b in zip(secret, intento) if a==b)
    toques = sum(1 for c in intento if c in secret) - famas
    return famas, toques

def jugar():
    sec = generar()
    intentos = 0
    while True:
        t = input("Ingrese 4 dígitos: ").strip()
        if len(t)!=4 or not t.isdigit():
            print("Entrada inválida"); continue
        intentos += 1
        f, to = contar(sec, t)
        print(f"Intento {intentos}: Famas={f}, Toques={to}")
        if f==4:
            print("¡Adivinaste en", intentos, "intentos!")
            break

if __name__ == "__main__":
    jugar()
