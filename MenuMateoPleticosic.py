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
        print("Contenido de " + nombre + ":")
        print(contenido)
    else:
        print("El archivo " + nombre + " no existe.")

def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")

def menu():
    while True:
        print("1.Crear archivo ")
        print("2.Eliminar archivo")
        print("3.Escribir ")
        print("4.Leer archivo: ")
        print("5.Agregar ")
        print("6.Salir ")
        
        opcion = input("Elija una opcion: ")

        if opcion == '6':
            print("Saliendo del programa...")
            return

        nombre = input("Ingresa el nombre del archivo: ")

        if opcion == '1':
            crear_archivo(nombre)
        elif opcion == '2':
            eliminar_archivo(nombre)
        elif opcion == '3':
            contenido = input("Escribe el contenido del archivo:\n")
            escribir_archivo(nombre, contenido)
        elif opcion == '4':
            leer_archivo(nombre)
        elif opcion == '5':
            contenido = input("Escribe el texto que deseas agregar:\n")
            agregar_archivo(nombre, contenido)
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
