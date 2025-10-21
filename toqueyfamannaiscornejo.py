import random

def analizar(guess, numero_secreto):
    toques = len(set(guess) & set(numero_secreto))
    famas = sum([1 if guess[i] == numero_secreto[i] else 0 for i in range(len(guess))])
    return toques, famas

def main():
    max_intentos = 3
    largo = 0
    while largo < 1 or largo > 10:
        largo = int(input("Elige el largo del número: "))

    digitos = list("0123456789")
    while True:
        random.shuffle(digitos)
        numero_secreto = digitos[:largo]
        # print(numero_secreto
        for intento in range(max_intentos):
            guess = list(input(f"Intento {intento + 1}: ")[:largo])
            toques, famas = analizar(guess, numero_secreto)
            if guess == numero_secreto:
                print(f"¡Felicitaciones! Has acertado en {intento + 1} intentos")
                break
            else:
                print(f"Toques {toques} - Famas {famas}: ")
        else:
            print(f"No acertaste. El número era {''.join(numero_secreto)}.")
        opcion = input("¿Deseas jugar nuevamente (S/N)? ").lower().strip()
        if opcion not in ["s", "si"]:
            break

if __name__ == "__main__":
    main()