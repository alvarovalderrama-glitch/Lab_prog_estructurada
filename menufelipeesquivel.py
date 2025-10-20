import os       #importa la libreria os para manejar archivos

def crear_archivo(nombre):     #crea una funcion para crear el archivo
    with open(nombre, 'w') as f:            #abre el archivo en modo write (w)
        pass                                    # solo crea el archivo sin escribir nada
    print("Archivo " + nombre + " creado.")   #imprime un mensaje de que el archivo fue creado

def eliminar_archivo(nombre):    #crea una funcion para eliminar el archivo
    if os.path.exists(nombre):    #verifica el path del archivo 
        os.remove(nombre)            #elimina el archivo 
        print("Archivo " + nombre + " eliminado.")     #imprime un mensaje de confirmacion de que fue eliminado
    else:                         #si no existe el archivo...
        print("Archivo "+ nombre +" no existe.")     #imprime un mensaje de que no existe el archivo

def escribir_archivo(nombre, contenido):      #crea una funcion para escribir en el archivo 
    with open(nombre, 'w') as f:       # abre el archivo en modo write (w)
        f.write(contenido)          # escribe el contenido en el archivo 
    print("Contenido escrito en " + nombre + " (modo write).")  #imrime un mensaje de confirmacion de que se escribio el contenido

def leer_archivo(nombre):          #crea una función para leer el archivo 
    if os.path.exists(nombre):   #verifica si el archivo existe 
        with open(nombre, 'r') as f:   #abre el archivo en modo read (r) 
            contenido = f.read()    #lee el contenido del archivo
        print("Contenido de " + nombre + ":" + contenido)  #imprime el contenido del archivo 
    else:                  #si el archivo no existe...
        print("El archivo " + nombre + " no existe.")  #imprime un mensaje de que no existe el archivo 

def agregar_archivo(nombre, contenido):  # crea una funcion para agregar contenido al archivo
    with open(nombre, 'a') as f:         #abre el archivo en modo append (a)
        f.write(contenido)          #agrega el contenido al final del archivo 
    print("Contenido agregado en " + nombre + " (modo append).")       #imprime un mensaje de confirmacion de que se agrego el contenido


# Ejemplo:


while True:
    print("Menu de manejo de archivos:")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir en archivo")
    print("4. Leer archivo")
    print("5. Agregar a archivo ")
    print("6. Salir")



    opcion = input("Elige una opción (1-6): \n")

    if opcion == "1":
        nombre = input("Ingrese el nombre del archivo a crear: \n")
        crear_archivo(nombre)
    elif opcion == "2":
        nombre = input("Ingrese el nombre del archivo a eliminar: \n")
        eliminar_archivo(nombre)
    elif opcion == "3":
        nombre = input("Ingrese el nombre del archivo a escribir: \n")
        contenido = input("Ingrese el contenido a escribir: \n")
        escribir_archivo(nombre, contenido)
    elif opcion == "4":
        nombre = input("Ingrese el nombre del archivo a leer: \n")
        leer_archivo(nombre)
    elif opcion == "5":
        nombre = input("Ingrese el nombre del archivo a agregar: \n")
        contenido = input("Ingrese el contenido a agregar: \n")
        agregar_archivo(nombre, contenido)
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print("Opción no válida.")
        