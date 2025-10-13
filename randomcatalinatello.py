import random   #importa el modulo random para generar nums aleatorios
random_number = random.randint(1, 6) #genera un num entero aleatorio entre 1 y 6
def get_random_dice_roll(): #define la funcion llamada get_random_dice_roll
    return random_number #devuelve el numero aleatorio guardado
# Imprime el mismo número aleatorio en cuatro veces
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
