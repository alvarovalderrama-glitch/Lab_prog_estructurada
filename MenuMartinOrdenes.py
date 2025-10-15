import os
def crear_archivo(Nombre):
    with open(Nombre, 'w') as f:
        pass
    print ("Archivo " + Nombre + " creado")

def Eliminar_Archivo(Nombre):
    if os.path.exists(Nombre):
        os.remove(Nombre)
        print ("Archivo " + Nombre + " ha sido eliminado")
    else:
        print ("Archivo " + Nombre + " no existe")

def Escribir_Archivo (Nombre, Contenido):
    with open(Nombre, 'w') as f:
        f.write(Contenido)
        print ("El Contenido ha sido escrito en " + Nombre + " (modo write)")

def leer_archivo(Nombre):
    if os.path.exists(Nombre):
        with open(Nombre, 'r') as f:
            Contenido = f.read()
        print ("El contenido de " + Nombre + "es: " + Contenido)
    else:
        print ("El archivo " + Nombre + " no existe")

def Agregar_Archivo (Nombre, Contenido):
    with open(Nombre, 'a') as f:
        f.write(Contenido)
        print ("Contenido agregado en " + Nombre + " (modo append)")

while True:
    print ("\n----Menu----")
    print ("1. Crear un archivo")
    print ("2. Eliminar un archivo")
    print ("3. Escribir archivo")
    print ("4. Leer un archivo")
    print ("5. Agregar un archivo")
    print ("6. Salir del menu")

    Opcion = input("Elija una opcion (1-6): ")

    if Opcion == '1' :
        Nombre = input("Ingrese el nombre del nuevo archivo: ")
        crear_archivo(Nombre)
    elif Opcion == '2' :
        Nombre = input("Escriba el nombre del archivo que se va a eliminar: ")
        Eliminar_Archivo(Nombre)
    elif Opcion == '3' :
        Nombre =  input("Ingrese el nombre del archivo: ")
        contenido = input("Escribe el contenido: ")
        Escribir_Archivo(Nombre, contenido)
    elif Opcion == '4' :
        Nombre = input('Ingrese el Nombre del archivo: ')
        leer_archivo(Nombre)
    elif Opcion == '5':
        Nombre = input("Ingrese el nombre del archivo: ")
        contenido = input("Escriba el contenido que va a agregar: ")
        Agregar_Archivo(Nombre, contenido)
    elif Opcion == '6' :
        print("Saliendo del menu...")
        break
    else:
        print("Opcion no valida, por favor intente ingresar otra opcion ")