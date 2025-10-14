
import os

# 1. Crear un archivo vacío
def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print("Archivo " + nombre + " creado correctamente.")


# 2. Eliminar un archivo existente
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado correctamente.")
    else:
        print("El archivo " + nombre + " no existe.")


# 3. Escribir contenido (modo write: reemplaza todo el contenido)
def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).")


# 4. Leer contenido (modo read)
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("\n--- Contenido de " + nombre + " ---")
        print(contenido)
        print("----------------------------\n")
    else:
        print("El archivo " + nombre + " no existe.")


# 5. Agregar contenido (modo append: agrega al final del archivo)
def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")


# ------------------ MENÚ PRINCIPAL ------------------
def menu():
    while True:
        print("\n===== MENÚ DE ARCHIVOS =====")
        print("1. Crear archivo (modo w)")
        print("2. Eliminar archivo")
        print("3. Escribir archivo (modo w)")
        print("4. Leer archivo (modo r)")
        print("5. Agregar archivo (modo a)")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            nombre = input("Ingrese el nombre del archivo: ")
            crear_archivo(nombre)

        elif opcion == '2':
            nombre = input("Ingrese el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)

        elif opcion == '3':
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Ingrese el contenido: ")
            escribir_archivo(nombre, contenido)

        elif opcion == '4':
            nombre = input("Ingrese el nombre del archivo a leer: ")
            leer_archivo(nombre)

        elif opcion == '5':
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Ingrese el contenido a agregar: ")
            agregar_archivo(nombre, contenido)

        elif opcion == '6':
            print("Saliendo del programa...!Adiós!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

# Ejecutar el menú
menu()
