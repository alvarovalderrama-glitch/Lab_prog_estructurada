import os
def crear_archivo(nombre):
    with open(nombre,'w') as f:
        pass
    print("Archivo " + nombre + " Creado")
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado")
    else:
        print("Archivo " + nombre + " no existe")
def escribir_archivo(nombre,contenido):
    with open(nombre,'w') as f:
        f.write(contenido)
        print("contenido escrito en " + nombre + " (modo write)")
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre,'r') as f:
            contenido= f.read()
            print("Lo que está escrito en " + nombre + ":" + contenido)
    else:
        print("El archivo " + nombre + " no existe")
def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
        print('Contenido agregado en ' + nombre + " (modo append)")

while True:
    print("------ menu ------")
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir archivo")
    print("4. Leer archivo")
    print("5. Agregar texto")
    print("6. Salir")
    
    opcion= input('Selecciona una opción \n')
    if opcion == '1':
        nombre=input('ingresa del nombre del archivo que desea crear \n')
        crear_archivo(nombre)
    elif opcion == "2":
        nombre=input('ingrese el nombre del archivo que desea eliminar \n')
        eliminar_archivo(nombre)
    elif opcion == "3":
        nombre=input('nombre del archivo en el que desea escribir \n')
        contenido=input('Escriba lo que desea agregar \n')
        escribir_archivo(nombre, contenido)
    elif opcion == '4':
        nombre=input('archivo que desea leer \n')
        leer_archivo(nombre)
    elif opcion == "5":
        nombre=input('nombre del archivo en el que desea agregar texto \n')
        contenido=input('Escriba lo que desea agregar \n')
        agregar_archivo(nombre, contenido)
    elif opcion == '6':
        print('Saliendo del programa...')
        break
