import random

# Juego "toque y fama" desarrollado en Python.

digitos_lista = []  # Lista donde se almacenaran los digitos del numero a adivinar.

# El ciclo for genera 4 digitos entre 0 y 9 sin repetirlos.
for i in range(0,4):
    while True:
        if i == 0:
            digito = random.randint(1,9)   # El primer digito no puede ser 0, por lo que en la primera iteración el rango es de 1 a 9.
        else:
            digito = random.randint(0,9)
        if str(digito) not in digitos_lista:    # Se verifica que el digito no esté en digitos_lista para agregarlo.
            digitos_lista.append(str(digito))    # Se agregan como str para facilitar la comparación.
            break

# Esta función verifica que el numero ingresado por el usuario sea valido.
def verificar():
    while True:
        try:
            variable = int(input('Ingrese un entero de cuatro cifras sin repetirlas:'))
            if variable not in range(1000,10000):  # Filtrar los numero que no tengan 4 cifras.
                print('El numero no tiene cuatro cifras.')
            elif len(set(list(str(variable)))) == 4:  # Verificar que las cifras no se repitan.
                return(variable)  # Retorna la variable.
            else:
                print('El numero tiene cifras repetidas.')
        except ValueError:  # Se imprime un mensaje si el tipo de dato ingreso no es int.
            print('Dato no valido.')

#Iniciar juego

print('\n TOQUE Y FAMA: JUEGO \n')

intentos = 7  # Numero de intentos.
FAMA = ''
while  intentos > 0 and FAMA != 4:  # El juego termina si se acaban los intentos o si adivinas el numero.
    FAMA = 0
    TOQUES = 0
    print(f'Tienes {intentos} intentos.')
    numero_pl = verificar()
    for digito in list(str(numero_pl)):   # Ciclo for que busca toques y famas en numero_pl.
        if digito == (digitos_lista[list(str(numero_pl)).index(digito)]):  # Verifica que el respectivo digito y el elemento con la misma indexación en digitos_lista sean iguales para sumar una fama.
            FAMA += 1
        else:
            if digito in digitos_lista:  # Verifica que el digito pertenezca a digitos_lista para sumar un toque.
                TOQUES += 1
    print(f'N° Toques: {TOQUES}      N° Famas: {FAMA} \n ')  # Muestra el numero de famas y toques que tuvo el candidato numero_pl
    intentos = intentos - 1  # Se resta un intento en cada iteración.

# Ganas al adivinar el numero y obtener las cuatro famas; 
# De lo contrario, el numero de intentos llego a cero y significa que perdiste.

if FAMA == 4:
    print('Ganaste!')
else:
    print('Te quedaste sin intentos. Has perdido. \n')
    numero_adivinar = int(''.join(digitos_lista)) # Se concadenan los digitos y se convierten en int para mostrarlo.
    print(f'El numero a adivinar era {numero_adivinar}.')