### Toque y Fama ###
import random


def generar_numeros():
    valor_incognito = random.sample(range(10), 4)  # random.sample genera una lista de numeros (entre 0 y 9 ,  4 veces), sin repetirlos entre si
    if valor_incognito[0] == 0:
        # si el primer número es un 0, lo cambia con el segundo, que siempre va a ser uno distinto
        valor_incognito[0], valor_incognito[1] = valor_incognito[1], valor_incognito[0]
    return valor_incognito



def adivinar_numeros():
    while True:
        try:  # hace posible el uso de except, evitando que el programa no funcione por un error
            # verifica que guess sea un número
            guess = abs(int(input("Ingrese un número entero de 4 dígitos NO REPETIDOS ENTRE SÍ:\n>")))  # si no es un numero la funcion int(...) genera un ValueError

        except ValueError:  # la excepción hace que el programa no se detenga con el error y reinicia el ciclo
            input("Error: Asegurese de ingresar un NÚMERO ENTERO (presione enter para continuar)\n")
            continue

        if len(set(str(guess))) != 4 or len(str(guess)) != 4:  # verifica que el número sea de 4 DÍGITOS DISTINTOS (gracias a set(...))
            input("Error: El número debe ser de 4 dígitos NO REPETIDOS (presione enter para continuar)\n")
            continue
        
        lista_guess = list(str(guess))  # guarda cada dígito del número en una lista (en formato string). ej: ["1", "2", "3", "4"]
        return lista_guess
    


def coincidencias(valor_incognito, lista_guess, toque, fama, lista_coincidencias):
    for i in range(4):
        if int(lista_guess[i]) == valor_incognito[i]:  # si el número coincide en la misma casilla, entonces es una fama
            fama += 1
            lista_coincidencias[i] = "F"
        elif int(lista_guess[i]) in valor_incognito:  # si el número no está en la misma casilla pero sí dentro de la lista, entonces es un toque
            toque += 1
            lista_coincidencias[i] = "T"

    
    return toque, fama, lista_coincidencias



def ganar(fama, ganador):
    if fama == 4:  # si hay cuatro famas significa que el jugador ganó
        ganador = True
    return ganador



def main():
    intentos = 0
    ganador = False
    valor_incognito = generar_numeros()

    while intentos < 5 and ganador == False:  # el programa continúa hasta que se acaben los intentos o hasta que el jugador gane
        print(f"Intentos restantes: {5 - intentos}\n")
        lista_guess = adivinar_numeros()
        toque = 0
        fama = 0
        intentos += 1
        lista_coincidencias = ["X", "X", "X", "X"]
        
        # comparar guess con valor_incognito y devolver toques y famas
        toque, fama, lista_coincidencias = coincidencias(valor_incognito, lista_guess, toque, fama, lista_coincidencias)

        print(f"Números ingresados: \n{lista_guess}\n")
        print(f"Cantidad de coincidencias (T = toque, F = fama, X = sin coincidencias): \n{lista_coincidencias}\n")
        print(f"Toques: {toque}   Famas: {fama}\n")
        ganador = ganar(fama, ganador)

    if ganador == True:
        print("Felicidades, has ganado!")
    else:
        print("Intentos agotados, has perdido.")


main()