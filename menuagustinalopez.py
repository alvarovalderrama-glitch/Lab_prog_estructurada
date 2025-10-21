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
        print("El archivo " + nombre + " no existe.")
def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write)")
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de " + nombre + ":"+contenido)
    else:
        print("El archivo " + nombre + " no existe.")
def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado a " + nombre + " (modo append)")

def menu():
    while True:
        print("--- MENÚ DE GESTIÓN DE ARCHIVOS ---")
        print("1. Crear un nuevo archivo")
        print("2. Eliminar un archivo")
        print("3. Escribir un archivo (w)")
        print("4. Leer un archivo (r)")
        print("5. Agregar a un archivo (a)")
        print("6. Salir")
        opcion=input("Seleccione una opción (1-6):")
        if opcion=="1":
            nombre=input("Ingrese el nombre del nuevo archivo: ")
            crear_archivo(nombre)    
        elif opcion=="2":
            nombre=input("Ingrese el nombre del archivo que desea eliminar: ")
            eliminar_archivo(nombre)  
        elif opcion=="3":
            nombre=input("Ingrese el nombre del archivo: ")
            contenido=input("Ingrese texto: ")
            escribir_archivo(nombre, contenido)
        elif opcion=="4":
            nombre=input("Ingrese el nombre del archivo a leer: ")
            leer_archivo(nombre)
        elif opcion=="5":
            nombre=input("Ingrese el nombre del archivo: ")
            contenido=input("Ingrese el contenido que desea agregar: ")
            agregar_archivo(nombre, contenido)
        elif opcion=="6":
            print("¡Muchas gracias por usar el Menú de gestion de archivos!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida (1-6).")
if __name__=="__main__":
    menu()