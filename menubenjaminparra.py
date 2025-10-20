import os

def crear_archivo(nombre): 
    with open(nombre, 'w') as f: 
        pass 
    print("Archivo" + nombre +" creado.") 

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
while True:
    print("Menu de manejo de archivos:")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir en archivo")
    print("4. Leer archivo")
    print("5. Agregar a archivo")
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