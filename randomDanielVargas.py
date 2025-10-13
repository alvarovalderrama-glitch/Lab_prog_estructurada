import random
random_number=random.randint(1,6)

def get_random_dice_roll():
    return random_number
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

# El código de arriba es el presentado en la evaluación.

'''====================================================================================================================
Lo que hace la función ".randint()" es devolver un número entero entre el 1 y el 6 (que son los parámetros que están 
puestos), pero el detalle es que solo se ejecutó una sola vez, haciendo que no se obtengan nuevos números, y es por eso
que al momento de imprimirlo cuatro veces aparece el mismo. Una forma de arreglarlo es crear un ciclo "for" que se 
repita hasta cuatro veces, en donde se ejecute la función ".randint()" y luego "print()", todo dentro de "for", para 
poder mostrar cada resultado en iteración. Si "print()" es colocado fuera de "for", entonces imprimirá una sola vez el 
último número que se generó, ocasionando otro tipo de problema.
========================================================================================================================'''

# Este sería un código para que los números varíen correctamente:

print('====================\n VERSIÓN ARREGLADA:\n====================')
for i in range(4):
    numero_aleatorio=random.randint(1,6)
    print(numero_aleatorio)