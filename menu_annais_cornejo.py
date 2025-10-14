import os
def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print('El archivo ' + nombre + ' fue creado.')

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print('El archivo ' + nombre + ' fue eliminado.')
    else:
        print('El archivo ' + nombre + ' no existe.')

def escribir_archivo(nombre, contenido):
    with open(nombre,'w') as f:
        f.write(contenido)
    print('Contenido escrito en ' + nombre + ' (modo write).')

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print('Contenido de ' + nombre + ':' + contenido)
    else:
        print('El archivo' + nombre + 'no existe.')

def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print('Contenido agregado en' + nombre + '(modo append).')

while True:
    print('-------Menú-------')
    print('1. Crear archivo.')
    print('2. Eliminar archivo.')
    print('3. Escribir archivo.')
    print('4. Leer archivo.')
    print('5. Agregar archivo.')
    print('6. Salir.')

    seleccion=int(input('Seleccione la opción que desea ejecutar (1-6): '))

    if seleccion == 1:
        nombre=input('Ingrese el nombre del archivo a crear (+.txt): ')
        crear_archivo(nombre)
    elif seleccion == 2:
        nombre=input('Ingrese nombre del archivo a eliminar (+.txt): ')
        eliminar_archivo(nombre)
    elif seleccion == 3:
        nombre=input('Ingrese nombre del archivo a escribir (+.txt): ')
        contenido=input('Ingresa lo que desea escribir: ')
        escribir_archivo(nombre,contenido)
    elif seleccion == 4:
        nombre=input('Ingrese nombre del archivo a leer (+.txt): ')
        leer_archivo(nombre)
    elif seleccion == 5:
        nombre=input('Ingrese nombre del archivo que desea agregar (+.txt): ')
        contenido=input('Ingrese lo que desea agregar al archivo: ')
        agregar_archivo(nombre,contenido)
    elif seleccion == 6:
        break
    else: 
        print('Opción invalida, intente de nuevo')