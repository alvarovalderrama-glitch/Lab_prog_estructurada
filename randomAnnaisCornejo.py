import random 
#Importa el módulo random que tiene funciones para generar números aleatorios
random_number = random.randint(1, 6)
#Genera un número aleatorio entre 1 y 6, guardándolo en la variable random_number

def get_random_dice_roll():
    #Define una función que simula tirar un dado
    return random_number
    #Devuelve el valor de la variable random_number (Siempre devuelve el mismo n° que se generó)

print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
print(get_random_dice_roll())
#Llama a la función 4 veces y imprime el resultado (El mismo número 4 veces)
