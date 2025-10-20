import random #importa el modulo random

random_number = random.randint(1, 6)    #genera un numero aleatorio entre 1 y 6

def get_random_dice_roll():
    #returns a random integer from 1 to 6
    return random_number   #retorna el numero aleatorio generado

print(get_random_dice_roll()) #imprime el numero aleatorio x4 
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())