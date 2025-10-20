import random

spam = random.randint(1,5)#genera un número entre 1 y 5

print("Número generado: ", spam)#muestra al usuario qué numero se genero entregandole la variable spam
if spam == 1 or spam == 2:#muestra Hola si es 1 o 2, sino muestra Saludos
    print("Hola")
else:
    print("Saludos")
        
    