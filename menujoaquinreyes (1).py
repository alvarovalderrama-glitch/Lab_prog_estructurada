import os
def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print("Archivo" + nombre + "creado.")
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo" + nombre + "eliminado.")
    else:
        print("El archivo" + nombre + "no existe.")
def escribir_archivo(nombre,contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito" + nombre + "(modo write).")
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de" + nombre + ":" + contenido)
    else:
        print("El archivo" + nombre + "no existe.")
def agregar_archivo(nombre,contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en" + nombre + "(modo append).")
while True:
    print("\nMenu de opciones:")
    print("1. Crear archivo")
    print("2. Eliminar archivo")    
    print("3. Escribir archivo (modo w)")
    print("4. Leer archivo (modo r)")
    print("5. Agregar archivo (modo a)")
    print("6. Salir")
    opcion = input("Seleccione una opcion (1-6): ")
    if opcion == '1':
        nombre = input("Ingrese el nombre del archivo a crear: ")
        crear_archivo(nombre)
    elif opcion == '2':
        nombre = input("Ingrese el nombre del archivo a eliminar: ")
        eliminar_archivo(nombre)
    elif opcion == '3':
        nombre = input("Ingrese el nombre del archivo a escribir: ")
        contenido = input("Ingrese el contenido a escribir: ")
        escribir_archivo(nombre, contenido)
    elif opcion == '4':
        nombre = input("Ingrese el nombre del archivo a leer: ")
        leer_archivo(nombre)
    elif opcion == '5':
        nombre = input("Ingrese el nombre del archivo a agregar contenido: ")
        contenido = input("Ingrese el contenido a agregar: ")
        agregar_archivo(nombre, contenido)
    elif opcion == '6':
        print("Saliendo del programa.")
        break
    else:
        print("Opcion no valida. Intente de nuevo.")