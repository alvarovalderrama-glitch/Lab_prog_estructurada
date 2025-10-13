import random

 # numero aleatorio del 1-6

def get_random_dice_roll():
    return random.randint(1,6)  # se devuelve el numero aleatorio


print(get_random_dice_roll()) # se llama a la funcion y este regresa el numero aleatorio
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
