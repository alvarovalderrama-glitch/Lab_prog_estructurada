import random # Importa la libreria que permite generar números aleatorios

def random_repetido(): # Define la función con el nombre "random_repetido".
    random_number = random.randint(1, 6) # A la variable "random_number", el número aleatorio entre 1 y 6 se genera 1 sola vez.

    def get_random_dice_roll(): # Define una función con el nombre "get_random_dice_roll".
        # Returns a random integer from 1 to 6 / Devuelve un número entero aleatorio del 1 al 6.
        return random_number # Nos regresa / da como resultado la variable "random_number".

    # Todas las impresiones serán el mismo número.
    print(get_random_dice_roll()) # Imprime el resultante de la función "get_random_dice_roll()", por lo que sera igual en esta y en las siguientes
    print(get_random_dice_roll()) # ya que no se esta generando otro número aleatorio.
    print(get_random_dice_roll())
    print(get_random_dice_roll())

def random_sin_repetidos(): # Define la función con el nombre "random_sin_repetidos".
        
    print(random.randint(1, 6)) # Genera números aleatorios en cada uno de las impresiones tanto en esta,
    print(random.randint(1, 6)) # esta, 
    print(random.randint(1, 6)) # esta,
    print(random.randint(1, 6)) # y esta.

def random_sin_repetidos2(): # Define la función con el nombre "random_sin_repetidos2".
    
    def get_random_dice_roll(): # Define una función con el nombre "get_random_dice_roll".
        random_number = random.randint(1, 6) # Se le asigna a la varible "random_number" un número aleatorio entre 1 y 6.
        return random_number # Nos regresa / da como resultado la variable "random_number".

    print(get_random_dice_roll()) # Imprime lo resultante de la función "get_random_dice_roll2" dando números aleatorios.
    print(get_random_dice_roll())
    print(get_random_dice_roll())
    print(get_random_dice_roll())

### Main / Menú ###

while True: # Ciclo repetivo "while" con el valor booleano True, para que se repita indefinidamente.
    # Se imprime el menú para poder ver las opciones que se pueden seleccionar.
    print("""
|================Menú de números================|
     1.- Todos los números iguales (Original).
     2.- Todos números aleatorios (Opción 1).
     3.- Todos números aleatorios (Opción 2).
     4.- Salir.
|===============================================|
 """)
    # Se crea la variable "seleccion" en la que se usa un "input(...)", para que el usuario ingrese que opción quiere y que la tome como una cadena de texto (string).
    seleccion = input("Ingrese el número de la acción que desea: \n> ")
    print(" ")
    if seleccion == "1": # Condicional "if" que ejecutará la función "random_repetido" si "seleccion" es igual a "1". 
        random_repetido() # Llama a la función "random_repetido".
    elif seleccion == "2": # Condicional "elif" que ejecutará la función "random_sin_repetidos" si "seleccion" es igual a "2".
        random_sin_repetidos() # Llama a la función "random_sin_repetidos".
    elif seleccion == "3": # Condicional "elif" que ejecutará lo que esta en su interior si "seleccion" es igual a "3"
        random_sin_repetidos2() # Llama a la función "random_sin_repetidos2".
    elif seleccion == "4": # Condicional "elif" que imprimirá un mensaje y hará que termine el ciclo "while", si "seleccion" es igual a "4".
        print("Saliendo del programa...") # Imprime el mensaje "Saliendo del programa...".
        break # Hace que se rompa el ciclo "while".
    else: # Si no se cumple ninguna de las condiciones anteriores ejecutará lo siguiente.
        print("Opción invalida, elige otra.") # Imprime el mensaje "Opción invalida, elige otra."
