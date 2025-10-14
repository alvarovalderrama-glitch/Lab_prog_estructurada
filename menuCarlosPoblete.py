import os

def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print("Archivo " + nombre + " creado.")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado.")
    else:
        print("Archivo " + nombre + " no existe.")

def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).")

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de " + nombre + ": " + contenido)
    else:
        print("El archivo " + nombre + " no existe.")

def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")

menu = True

while menu == True:
    print("Menú:")
    print("1. Crear Archivo")
    print("2. Eliminar Archivo")
    print("3. Escribir Archivo")
    print("4. Leer Archivo")
    print("5. Agregar Archivo")
    print("6. Salir")

    opcion = int(input('Eliga una opcion: '))
    
    if opcion == 1:
        nombre = input('Nombre del archivo que deseas crear: ')
        crear_archivo(nombre)
    elif opcion == 2:
        nombre = input('Nombre del archivo que deseas eleminar: ')
        eliminar_archivo(nombre)
    elif opcion == 3:
        nombre = input('Nombre del archivo donde quiere escribir(se borrara todo lo escrito anteriormente): ')
        contenido = input('Que deseas escribir en el archivo: ')
        escribir_archivo(nombre, contenido)
    elif opcion == 4:
        nombre = input('Nombre del archivo que deseas leer: ')
        leer_archivo(nombre)
    elif opcion == 5:
        nombre = input('En que archivo desea agregar contenido: ')
        contenido = input('Que deseas agregar en el archivo: ')
        agregar_archivo(nombre, contenido)
    elif opcion == 6:
        print('Programa apagado.')
        menu = False
    else:
        print('Opcion no valida, intente nuevamente.')
