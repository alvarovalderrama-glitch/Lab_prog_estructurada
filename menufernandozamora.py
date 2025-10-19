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

#Menu Principaaaaal--------------------

def mostrar_menu():
    print("MENU PARA GESTIONAR ARCHIVOOS :)")
    print("1. CREAR ARCHIVO")
    print("2. ELIMINAR ARCHIVO")
    print("3. ESCRIBIR ARCHIVO O SOBREESCRIBIR ")
    print("4. LEER ARCHIVO")
    print("5. AGREGAR ARCHIVO")
    print("6. SALIR")

while True:
    mostrar_menu()
    opcion = input("seleccione una opcion: ")
    
    if opcion == "1":
        nombre_archivo = input("Ingrese el nombre del archivo el cual quiere crear :)")
        crear_archivo(nombre_archivo)
    elif opcion == "2":
        nombre_archivo = input("Igrese el nombre del archivo que desea eliminar :)")
        eliminar_archivo(nombre_archivo)
    elif opcion == "3":
        nombre_archivo = input("Ingrese el nombre del archivo que desea modificar :)")
        escribir_archivo(nombre_archivo)
    elif opcion == "4":
        nombre_archivo = input("Ingrese el nombre el archivo que desea leer")
        leer_archivo(nombre_archivo)
    elif opcion == "5":
        nombre_archivo = input("Ingrese el nombre del archivo que desea agregar contenido")
        agregar_archivo(nombre_archivo)
    elif opcion == "6":
        nombre_archivo = input("Saliendo del programa!!")
    else:
        print("Opcion no disponible, porfavor volver a intentar :)")