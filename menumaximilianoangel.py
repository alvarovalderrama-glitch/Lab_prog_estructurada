import os
# Creación de archivo
def crear_archivo(nombre): 
    with open(nombre, 'w') as f: 
        pass 
    print("Archivo" + nombre +" creado.") 

# Eliminar un archivo
def eliminar_archivo(nombre): 
    if os.path.exists(nombre): 
        os.remove(nombre) 
        print("Archivo " + nombre + " eliminado.") 
    else: 
        print("Archivo "+ nombre +" no existe.") 

# Escribir un archivo
def escribir_archivo(nombre, contenido): 
    with open(nombre, 'w') as f: 
        f.write(contenido) 
    print("Contenido escrito en " + nombre + " (modo write).") 
 
# Leer un archivo
def leer_archivo(nombre): 
    if os.path.exists(nombre): 
        with open(nombre, 'r') as f: 
            contenido = f.read() 
        print("Contenido de " + nombre + ":" + contenido) 
    else: 
        print("El archivo " + nombre + " no existe.") 

# Agregar contenido a un archivo
def agregar_archivo(nombre, contenido): 
    with open(nombre, 'a') as f: 
        f.write(contenido) 
    print("Contenido agregado en " + nombre + " (modo append).") 

### MAIN ###
while True:
    print("""
|==========Acciones de archivo==========|
    1.- Crear archivo (p.ej. test.txt)
    2.- Eliminar archivo
    3.- Escribir archivo (modo w)
    4.- Leer archivo (modo r)
    5.- Agregar archivo (modo a) 
    6.- Salir 
|=======================================|
 """)
    seleccion = input("Ingrese el número de la acción que desea: \n> ")
    if seleccion == "1":
        nombre = input("Ingrese el nombre del archivo que desea crear (Agregar .txt): \n> ")
        crear_archivo(nombre)
    elif seleccion == "2":
        nombre = input("Ingrese el nombre del archivo que desea eliminar (Agregar .txt): \n> ")
        eliminar_archivo(nombre)
    elif seleccion == "3":
        nombre = input("Ingrese el nombre del archivo que desea escribir/sobreescribir (Agregar .txt): \n> ")
        if os.path.exists(nombre):
            contenido = input("\nIngrese el texto que desea escribir en el archivo: \n> ")
            escribir_archivo(nombre, contenido)
        else: 
            print("Archivo "+ nombre +" no existe.")             
    elif seleccion == "4":
        nombre = input("Ingrese el nombre del archivo que desea leer (Agregar .txt): \n> ")
        leer_archivo(nombre)
    elif seleccion == "5":
        nombre = input("Ingrese el nombre del archivo al que desea agregar un contenido (Agregar .txt): \n> ")
        contenido = input("\nIngrese el texto que desea agregar en el archivo: \n> ")
        agregar_archivo(nombre, contenido)
    elif seleccion == "6":
        print("Saliendo del programa... ")
        break
    else:
        print("Error, opción invalida. ") 

