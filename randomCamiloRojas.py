import random  # Importa el módulo de números aleatorios

def get_random_dice_roll(): # Define la función para obtener un número aleatorio
    random_number = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6
    return random_number  # Devuelve el número generado

# Llamamos a la función tres veces e imprimimos los resultados
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
