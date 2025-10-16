#importa la variable random
import random

#
def analizar(guess, numero_secreto):
    toques = len(set(guess) & set(numero_secreto))
    famas = sum([1 if guess[i] == numero_secreto[i] else 0 for i in range(len(guess))])
    return toques, famas

#Se define el ciclo principal

def main():
    max_intentos = 3                                        #cantidad de intentos para adivinar el numero
    largo = 0                                               #permite escoger 
    while largo < 1 or largo > 10:                          #establece que solo podemos escoger hasta el numero 9
        largo = int(input("Elige el largo del número: "))

    digitos = list("0123456789")                            #establecemos la lista disponibles
    while True:
        random.shuffle(digitos)                             #se "randomizan" los numeros
        numero_secreto = digitos[:largo]
        # print(numero_secreto
        for intento in range(max_intentos): 
            guess = list(input(f"Intento {intento + 1}: ")[:largo])
            toques, famas = analizar(guess, numero_secreto)
            if guess == numero_secreto:                     #si es que adivinamos el numero, eel juego termina
                print(f"¡Felicitaciones! Has acertado en {intento + 1} intentos") 
                break
            else:                                           #si es que no acertamos:
                print(f"Toques {toques} - Famas {famas}: ") #nos muestra cuanto toques tenemos y cuantas famas tenemos:
        else:                                               #si es que nos quedamos sin intentos:
            print(f"No acertastes. El número era {''.join(numero_secreto)}.") #se acaba el juego y se nos muestra cual era el numero secreto
        opcion = input("¿Deseas jugar nuevamente (S/N)? ").lower().strip()    #se nos da la opcion de jugar de nuevo o no
        if opcion not in ["s", "si" , "S"]:
            break

if __name__ == "__main__":
    main()

                 
        

    
                 
              