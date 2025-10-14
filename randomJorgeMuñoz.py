import random
def codigo_original():

    ### CÓDIGO ORIGINAL ###
    random_number = random.randint(1, 6)  # Asignación fuera de la funcion get_random_dice_roll()

    def get_random_dice_roll():
        return random_number

    print(get_random_dice_roll())
    print(get_random_dice_roll())
    print(get_random_dice_roll())
    print(get_random_dice_roll())
    # Para que el código funcione correctamente, sería necesario asginar el valor random_number cada vez que se llama a la función
    # En este caso la variable se asigna una sola vez y no vuelve a cambiarse porque la asginación está fuera de la función
    # La funcion get_random_dice_roll() siempre devuelve el mismo resultado

def codigo_corregido():

    ### CÓDIGO CORREGIDO ###
    def get_random_dice_roll():
        random_number = random.randint(1, 6)  # Si la variable random_number se asigna cada vez que se ejecuta la funcion,
        return random_number  # El valor de random_number se generará aleatoriamente cada vez que se llame a get_random_dice_roll()
    
    print(get_random_dice_roll())
    print(get_random_dice_roll())
    print(get_random_dice_roll())
    print(get_random_dice_roll())
    # Valores aleatorios por cada llamada a la función

def menu_opcion():
    while True:
        print ("""\n
-----------------------------------------------------------------------------

1. Ejecutar codigo original
2. Ejecutar codigo corregido

(Cualquier opcion distinta de 1 o 2 cerrará el programa)
-----------------------------------------------------------------------------\n
""")
        opcion = input("Introduzca una opción:\n>")
        if opcion == "1":
            print("\n----------CÓDIGO ORIGINAL----------\n")
            codigo_original()
        elif opcion == "2":
            print("\n----------CÓDIGO CORREGIDO----------\n")
            codigo_corregido()
        else:
            print("Programa cerrado")
            break

menu_opcion()