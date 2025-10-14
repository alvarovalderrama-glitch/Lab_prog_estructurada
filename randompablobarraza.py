import random # importa random que contiene funciones para generar números aleatorios
 
random_number = random.randint(1, 6) # genera un numero aleatorio entre 1 y 6 y lo guarda en la variable random_number

def get_random_dice_roll(): # crea la funcion get_random_dice_roll+
    #Returns a random integer from 1 to 6 
    return random_number # retorna el random_number al valor de la funcion

print(get_random_dice_roll()) # imprime 4 veces el valor que se le asigno a get_random_dice_roll
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())