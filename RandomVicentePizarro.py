import random
random_number = random.randint(1,6)  # se define una variable establecida con la funcion de manera aleatoria, esta funcion se ejecuta solo 1 vez cuando se inicia el codigo

def get_random_dice_roll():       # se define una funcion que devuelve la variable anterior
    return random_number

print(get_random_dice_roll())  #se imprime 5 veces la funcion antes definida y no cambia su valor debido a que se asigna una sola vez al inicio del codigo
print(get_random_dice_roll())   
print(get_random_dice_roll())  
print(get_random_dice_roll())  
