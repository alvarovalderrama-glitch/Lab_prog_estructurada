
import os

def crear_archivo(nombre):     

    with open(nombre, 'w') as f:         
        pass 
    print("Archivo " + nombre +" creado.")

def eliminar_archivo(nombre):  

    if os.path.exists(nombre): 
        os.remove(nombre) 
        print("Archivo " + nombre + " eliminado.")  

    else: 
        print("Archivo "+ nombre +" no existe.") 

def escribir_archivo(nombre, contenido):  

    with open(nombre, 'w') as f:         
        f.write(contenido) 
    print("Contenido escrito en " + nombre + " (modo write).") 

def leer_archivo(nombre):  

    if os.path.exists(nombre):         
        with open(nombre, 'r') as f:             
            contenido = f.read() 
        print("Contenido de " + nombre + ":" + contenido)     

    else: 
        print("El archivo " + nombre + " no existe.") 

def agregar_archivo(nombre, contenido):     
    with open(nombre, 'a') as f:         
        f.write(contenido) 
    print("Contenido agregado en " + nombre + " (modo append).")

def existe_archivo(nombre):

    if os.path.exists(nombre):
        return True
    
    else:
        return False


flag = False
while flag != True:

    print(" ")
    print("------------ MENÚ ------------")
    print("")
    print("(1) Crear archivo (Ejemplo: test.txt)")
    print("(2) Eliminar archivo")
    print("(3) Escribir archivo (modo w))")
    print("(4) Leer archivo")
    print("(5) Agregar archivo (modo a)")
    print("(6) Salir")
    print(" ")

    opcion = int(input("Eliga una opción: "))
    while opcion < 1 or opcion >= 7:
        opcion = int(input("Ingrese una opcion válida: "))

    if opcion == 1:
        nombre_arch = input("Ingrese el nombre del archivo que desee crear:")
        crear_archivo(nombre_arch)

    if opcion == 2:
        nombre_arch = input("Ingrese el nombre del archivo que desee eliminar: ")
        eliminar_archivo(nombre_arch)

    if opcion == 3:
        nombre_arch = input("Ingrese el archivo en el que desee escribir: ")
        flag1 = existe_archivo(nombre_arch)
    
    if opcion == 4:
        nombre_arch = input("Ingrese el nombre del archivo que el programa desee que lee: ")
        leer_archivo(nombre_arch)

    if opcion == 5:
        nombre_arch = input("Ingrese el nombre del archivo en el que desee agregar algun contenido: ")
        flag1 = existe_archivo(nombre_arch)

        if flag1 == True:
            contenido = input("Ingrese el contenido que desee escribir en el archivo: ")
            agregar_archivo(nombre_arch, contenido)
        
        else:
            print("El archivo " + nombre_arch + " no existe.")
                              
    if opcion == 6: 
        flag = True
        print("Cerrando programa...")
