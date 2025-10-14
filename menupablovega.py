import os

#Funciones del punto anterior
def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print("Archivo " + nombre + " creado.")
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado.")
    else:
        print("El archivo " + nombre + " no existe.")
def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).")
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de " + nombre + ":")
        print(contenido)
    else:
        print("El archivo " + nombre + " no existe.")
def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")

#Menú principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir archivo (modo w)")
    print("4. Leer archivo (modo r)")
    print("5. Agregar archivo (modo a)")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del archivo (ej: texto.txt): ")
        crear_archivo(nombre)

    elif opcion == "2":
        nombre = input("Nombre del archivo a eliminar: ")
        eliminar_archivo(nombre)

    elif opcion == "3":
        nombre = input("Nombre del archivo: ")
        contenido = input("Contenido a escribir: ")
        escribir_archivo(nombre, contenido)

    elif opcion == "4":
        nombre = input("Nombre del archivo a leer: ")
        leer_archivo(nombre)

    elif opcion == "5":
        nombre = input("Nombre del archivo: ")
        contenido = input("Contenido a agregar: ")
        agregar_archivo(nombre, contenido)

    elif opcion == "6":
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intente nuevamente.")