import os
def crear_archivo(nombre): #función para crear archivos
    with open(nombre, 'w') as f: #with open permite abrir y cerrar el archivo
        pass
    print("Archivo" + nombre +" creado.")


def eliminar_archivo(nombre): #función para eliminar archivos
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado.")
    else:
        print("Archivo "+ nombre +" no existe.")



def escribir_archivo(nombre, contenido): #función para escribir en el archivos
    with open(nombre, 'w') as f:
        f.write(contenido)
        print("Contenido escrito en " + nombre + " (modo write).")


def leer_archivo(nombre): #función para leer el contenido alojado en el archivos
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
            print("Contenido de " + nombre + ":" + contenido)
    else:
        print("El archivo " + nombre + " no existe.")



def agregar_archivo(nombre, contenido): #función para agregar contenido en el archivos
    with open(nombre, 'a') as f:
        f.write(contenido)
        print("Contenido agregado en " + nombre + " (modo append).")


def menu(): #función para navegar a través de las distintas funciones del archivos
    while True:
        print("\n--- MENÚ DE ARCHIVOS ---")
        print("1. crear archivo")
        print("2. eliminar archivo")
        print("3. escribir en archivo (sobrescribir)")
        print("4. leer archivo")
        print("5. agregar a archivo")
        print("6. salir")

        opcion = input("selecciona una opción (1-6): ")

        if opcion == '1':
            nombre = input("nombre del archivo a crear: ")
            crear_archivo(nombre)

        elif opcion == '2':
            nombre = input("nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)

        elif opcion == '3':
            nombre = input("nombre del archivo a escribir: ")
            contenido = input("contenido a escribir: ")
            escribir_archivo(nombre, contenido)

        elif opcion == '4':
            nombre = input("nombre del archivo a leer: ")
            leer_archivo(nombre)

        elif opcion == '5':
            nombre = input("nombre del archivo a agregar contenido: ")
            contenido = input("contenido a agregar: ")
            agregar_archivo(nombre, contenido)

        elif opcion == '6':
            print("saliendo del programa...")
            break

        else:
            print("opción inválida. Intenta nuevamente.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()