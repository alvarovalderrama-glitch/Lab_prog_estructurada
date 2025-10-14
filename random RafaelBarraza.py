import random   ##Importamos la librería estandar random, que contiene funciones para trabajar con números aleatorios(entre otras cosas)#

random_number = random.randint(1,6)  #Generamos un número aleatorio entre 1 y 6, lo guardamos en la variable random_number#
def get_random_dice_roll():               #Definimos la función get_random_dice_roll, que servirá para obtener un valor.#
    #Returns a random integer from 1 to 6  (Regresa un número aleatorio de 1 a 6)#
    return random_number             #Devuelve el número guardado en random_number#
                   
print(get_random_dice_roll())                
print(get_random_dice_roll())       #Como la función devuelve siempre la misma variable, todos los prints muestran el mismo número.#
print(get_random_dice_roll())          
print(get_random_dice_roll())


'''
#Una forma de hacer que nos entregue un número random cuatro veces es: #

import random   #Importamos la librería estandar random, que contiene funciones para trabajar con números aleatorios(entre otras cosas)#

def get_random_dice_roll():          #Definimos una función llamada get_random_dice_roll.#
    return random.randint(1,6)       #Dentro de la función, se devuelve el resultado de random.randint(1,6),#
                                     #genera un entero aleatorio entre 1 y 6 incluyendo ambos extremos 

for _ in range(4):                   #Iniciamos un bucle que se repite 4 veces, que produce valores 0,1,2,3, pero como no necesitamos ese contador se usa la convencion _ para indicar "variable ignorada"
    print(get_random_dice_roll())    #En cada iteración del for se llama a get_random_dice-rol, con eso ejecutamos random.randint(1,6) y devuelve un numero que luego se muestra en la consola.
    '''