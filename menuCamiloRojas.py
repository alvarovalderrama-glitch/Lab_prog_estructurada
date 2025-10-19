import os

# Codigo para manejar archivos de texto

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

    #///////////////////////////////////////////////////////////////////////////////////

# Menú principal para interactuar con el usuario

while True:
    # opciones menu
    print("\nSeleccione una opción:")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir contenido")
    print("4. Leer archivo")
    print("5. Agregar contenido")
    print("6. Salir")

    opcion = input("Ingrese una opción (1-6): ") # la persona elige una opcion

# ejecucion de las opciones

# crear el archivo y crea el nombre del archivo
    if opcion == '1':
        nombre = input("Ingrese el nombre del archivo (ej: datos.txt): ")
        crear_archivo(nombre)

# elimina el archivo y pide el nombre del archivo a eliminar

    elif opcion == '2':
        nombre = input("Ingrese el nombre del archivo a eliminar: ")
        eliminar_archivo(nombre)
    
# escribe el archivo y pide el nombre del archivo y el contenido a escribir

    elif opcion == '3':
        nombre = input("Ingrese el nombre del archivo: ")
        contenido = input("Ingrese el contenido a escribir: ")
        escribir_archivo(nombre, contenido)
    
# lee el archivo y pide el nombre del archivo a leer

    elif opcion == '4':
        nombre = input("Ingrese el nombre del archivo a leer: ")
        leer_archivo(nombre)

# agrega contenido al archivo y pide el nombre del archivo y el contenido a agregar

    elif opcion == '5':
        nombre = input("Ingrese el nombre del archivo: ")
        contenido = input("Ingrese el contenido a agregar: ")
        agregar_archivo(nombre, contenido)

# cierra el programa

    elif opcion == '6':
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")