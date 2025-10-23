#Importa la libreria 'random' para poder generar números aleatorios
import random    

#Genera un número aleatorio entre 1 y 6 y lo guarda en la variable 'random_number'
random_number = random.randint(1, 6) 

#Define una función que devuelve el número aleatorio generado 
def get_random_dice_roll(): 
   
#Devuelve el mismo número cada vez que se llama (en este caso 4 veces)  
    return random_number 

#Imprime el valor que devuelve la función, el mismo valor cada vez que se llama.
print(get_random_dice_roll()) 
print(get_random_dice_roll()) 
print(get_random_dice_roll()) 
print(get_random_dice_roll()) 

