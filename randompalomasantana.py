# genera un nuevo núemro aleatorio solo una vez al inicio del programa.
import random
random_number=random.randint(1,6)

def get_random_dice_roll():
    # Returns a random integer from 1 to 6
    # siepre de vuelve el mismo número porque se usa la variable random_number que se genera una sola vez.
    return random_number

#simula el lanzamiento de un dado (mostrará el mismo número siempre).
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())