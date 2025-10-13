import os

#---------------------------------------

def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print('Archivo '+nombre+' creado.')

#---------------------------------------

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print('Archivo '+nombre+' eliminado.')
    else:
        print('Archivo '+nombre+' no existe.')

#---------------------------------------

def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print('Contenido escrito en '+nombre+' (modo write).')

#---------------------------------------

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print('Contenido de '+nombre+': '+contenido)
    else:
        print('El archivo '+nombre+' no existe.')

#---------------------------------------

def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print('Contenido agregado en '+nombre+' (modo append).')

#---------------------------------------

while True:
    print("\n--- Menu---")
    print('1. Crear archivo.')
    print('2. Eliminar archivo.')
    print('3. Escribir archivo.')
    print('4. Leer archivo.')
    print('5. Agregar archivo.')
    print('6. Salir del programa')

    opcion=int(input('Selecciona una opción (1-6): '))

    if opcion==1:
        crear_archivo(input('Ingrese el nombre: ')+'.txt')
    elif opcion==2:
        eliminar_archivo(input('Ingrese el nombre del archivo:')+'.txt')
    elif opcion==3:
       nombre=input('Ingrese el nombre del archivo: ')+'.txt'
       contenido=input('Ingresa el texto a escribir: ')
       escribir_archivo(nombre,contenido)
    elif opcion==4:
        nombre=input('Ingrese nombre del archivo a leer: ')+'.txt'
        leer_archivo(nombre)
    elif opcion==5:
        nombre=input('Ingrese nombre del archivo: ')+'.txt'
        contenido=input('Ingrese lo que quiere agregar al archivo: ')
        agregar_archivo(nombre,contenido)
    elif opcion==6:
        break
    else:
        print('\nOpción inválida, intenta de nuevo.')
