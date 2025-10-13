import os 

def crear_archivo(nombre):
    with open(nombre,"w") as f:
        pass
    print("Archivo: "+ nombre + " creado")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
    else:
        print("Archivo: " + nombre + "no existe")
def escribir_archivo(nombre,contenido):
    with open(nombre,"w") as f:
        f.write(contenido)
    print("contenido escrito en :" + nombre + "(modo write)")

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, "r") as f:
            contenido = f.read()
            print("Contenido en: "+ nombre+ ": "+contenido)
    else:
        print("Archivo: " + nombre + "no existe")

def agregar_archivo(nombre,contenido):
    with open(nombre,"a") as f:
        f.write(contenido)
    print("contenido escrito en :" + nombre+"(modo append)")

def menu():
    print("---------------menu---------------")
    print("Escriba:")
    print("0) salir")
    print("1) crear archivo")
    print("2) escribir archivo")
    print("3) leer archivo")
    print("4) agregar archivo")
    print("5) eliminar archivo")

eleccion= ""

while eleccion != "0":
    menu()
    eleccion = input(">> ")
    if eleccion == "1":
        nombre = input("Escriba el nombre del archivo: ")
        crear_archivo(nombre)
    elif eleccion == "2":
        nombre = input("Escriba el nombre del archivo: ")
        contenido = input("Escriba el contenido del archivo: ")
        escribir_archivo(nombre,contenido)
    elif eleccion == "3":
        nombre = input("Escriba el nombre del archivo: ")
        leer_archivo(nombre)
    elif eleccion == "4":
        nombre = input("Escriba el nombre del archivo: ")
        contenido = input("Escriba el contenido del archivo: ")
        agregar_archivo(nombre,contenido)
    elif eleccion == "5":
        nombre = input("Escriba el nombre del archivo: ")
        eliminar_archivo(nombre)

