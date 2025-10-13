import random                               # Importa el módulo "random" para generar números aleatorios
random_number = random.randint(1, 6)        # Genera un número aleatorio entre 1 y 6 una sola vez

def get_random_dice_roll():                 # Define una función que simula tirar un dado
    # Returns a random integer from 1 to 6  # (comentario explicativo en inglés)
    return random_number                    # Devuelve el mismo número aleatorio generado antes

print(get_random_dice_roll())               # Imprime el número aleatorio (será siempre el mismo)
print(get_random_dice_roll())               # Imprime el mismo número otra vez
print(get_random_dice_roll())               # Igual
print(get_random_dice_roll())               # Igual
