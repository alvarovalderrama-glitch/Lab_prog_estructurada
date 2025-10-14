import random  # Importa la librería random
random_number = random.randint(1, 6) # Se genera un valor random

def get_random_dice_roll(): # Retorna el valor (entero desde 1 a 6)
    return random_number    # generado al inicio

print(get_random_dice_roll()) # El llamado de esta función siempre
print(get_random_dice_roll()) # retorna el valor de random_number
print(get_random_dice_roll())
print(get_random_dice_roll())