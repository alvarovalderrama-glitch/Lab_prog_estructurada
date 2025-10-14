import random

random_number = random.randint(1, 6)

def get_random_dice_roll():
    return random_number

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())

# Este programa define un número aleatorio solo una vez (random_number) 
# y cada llamada a la función devuelve siempre ese mismo valor.
