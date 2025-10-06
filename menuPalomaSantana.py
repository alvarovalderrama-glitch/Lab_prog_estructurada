import os
def crear_archivo(nombre):
    with open(nombre,'w') as f:
        pass
    print("Archivo"+nombre+"creado.")
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo"+nombre+"eliminado.")
    else:
        print("Archivo"+nombre+"no existe.")
def escribir_archivo(nombre,contenido):
    with open(nombre,'w') as f:
        f.write(contenido)
    print("Contenido escrito en"+nombre+"(modo write).")
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre,'r') as f:
            contenido=f.read()
        print("Contenido de"+nombre+":"+contenido)
    else:
        print("El archivo"+nombre+"no existe.")
def agregar_archivo(nombre,contenido):
    with open(nombre,'a') as f:
        f.write(contenido)
    print("Contenido agregado en"+nombre+"(modo append).")

while True:
    print("\n---MENÚ---")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir archivo")
    print("4. Leer archivo")
    print("5. Agregar archivo")
    print("6. Salir")

    opcion=input("Seleccione una opcion (1-6):")   

    if opcion=='1':
        nombre=input("ingrese el nombre del archivo:")+'.txt'
        crear_archivo(nombre)
    elif opcion=='2':
        nombre=input("ingrese el nombre del archivo:")+'.txt'
        eliminar_archivo(nombre)
    elif opcion=='3':
        nombre=input("ingrese el nombre del archivo:")+'.txt'
        contenido=input("ingrese el contenido a escribir:")
        escribir_archivo(nombre,contenido)
    elif opcion=='4':
        nombre=input("ingrese el nombre del archivo:")+'.txt'
        leer_archivo(nombre)
    elif opcion=='5':
        nombre=input("ingrese el nombre del archivo:")+'.txt'
        contenido=input("ingrese el contenido a agregar:")+'.txt'
        agregar_archivo(nombre,contenido)
    elif opcion=='6':
        print("Saliendo del programa...")
        break
    else:
        print("opcion no valida.") 