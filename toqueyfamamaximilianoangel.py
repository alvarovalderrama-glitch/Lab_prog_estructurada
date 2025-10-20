import random # Importa la libreria random.

print("Hola, juguemos al Toque y Fama") # Imprime el mensaje "Hola, juguemos al Toque y Fama".

secreto = random.sample(range(10), 4) # Genera un número de 4 dígitos sin repetición.

# Se define una función con el nombre "comprobacion".
def comprobacion():
    # Se usa un ciclo "while", donde se pide ingresar un número de 4 dígitos sin repetidos (n), posterior a eso verifica que verdaderamente no sean 4 dígitos,
    # usando "len(n) != 4", también se usa "not n.isdigit()" para comprobar que es un número el ingresado, si no se cumple lo anterior se volverá a pedir otro
    # número, después se convierte lo ingresado en una lista hecha con enteros (digitos), siguiente a esto se verifica que no sean repetidos con "len(set(digitos)) < 4".
    # Si todo lo anterior se cumple, entonces nos regresa la variable "digitos".
    while True:
        n = input("Ingresa un número de 4 dígitos (sin repetir): \n> ")
        if not n.isdigit() or len(n) != 4:
            print("Debe ser un número de 4 dígitos.\n")
            continue
        digitos = [int(x) for x in n]
        if len(set(digitos)) < 4:
            print("No repitas dígitos, inténtalo de nuevo.\n")
            continue
        return digitos

# Se define una función con el nombre "mostrar_numero" y toma como parametro "lista".
def mostrar_numero(lista):
    print(f"Tu número ingresado es: {tuple(lista)}\n") # Imprime "Tu número ingresado es: (La lista de números que se ingresaron)."

intentos = int(input("Ingresa el número de intentos que deseas: \n> ")) # Se crea la variable "intentos" y se le pide ingresar cuantos desea para jugar.
# Imprime el mensaje "Tienes (La cantidad de intentos que se ingreso) intentos para adivinar el número secreto."
print(f"Tienes {intentos} intentos para adivinar el número secreto.\n") 

while intentos > 0: # Ciclo "while" que se repetira mientras "intentos" sea mayor a 0.
    intento = comprobacion() # A la variable "intento" se le asigna el resultado de la función "comprobacion"
    mostrar_numero(intento) # Se llama la función "mostrar_numero" con el parametro "intento"

    fama = sum(intento[i] == secreto[i] for i in range(4)) # Verifica que los números esten en la posición correcta y la cantidad de correctos los asigna a "fama".
    # Verifica que se encuentren los números y se le resta "fama" para que solo nos de los que estan en una posición equivocada, donde se asigna a la variable "toque".
    toque = sum(d in secreto for d in intento) - fama 

    print(f"Tienes {toque} número(s) bueno(s) en posición equivocada y {fama} en posición correcta.\n") # Se imprime el mensaje en su interior donde se dice la cantidad de "toque" y de "fama".

    # Si la cantidad de "fama" es igual a 4 se imprime el mensaje "¡Felicidades, ganaste!" y muestra el número "secreto".
    if fama == 4:
        print("¡Felicidades, ganaste!")
        print(f"El número era {secreto}.")
        break
    # Si no se cumplio lo anterior se le resta 1 a los intentos y te dice los restantes, pero si la cantidad de "intentos" es igual a 0 imprime "Perdiste, el número era (El número secreto)".
    else:
        intentos -= 1
        if intentos > 0:
            print(f"Te quedan {intentos} intento(s) restantes.\n")
        else:
            print(f"Perdiste, el número era {tuple(secreto)}.")