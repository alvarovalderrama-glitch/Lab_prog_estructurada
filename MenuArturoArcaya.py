#tarea 10

import os
def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print("Archivo" + nombre +" creado.")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print('archivo ' + nombre + ' eliminado')

def escribir_archivo(nombre, contenido):
    with open(nombre , 'w') as f:
        f.write(contenido)
    print('contenido escrito en ' + nombre + ' (modo write).')

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido=f.read()
        print('contenido de ' + nombre + ':' + contenido)
    else:
        print('contenido agregado en ' + nombre + 'no existe.')

def agregar_archivo(nombre, contenido):
    with open (nombre, 'a') as f:
        f.write(contenido)
    print('contenido agregado en ' + nombre)

#menu


while True:
    print(' ')
    print('----------------------------------------------------------------------------------------')
    print(' ')
    print('Que desea hacer')
    print(' ')
    print('1.- Crear archivo')
    print('2.- Eliminar archivo')
    print('3.- Escribir en el archivo')
    print('4.- Leer archivo')
    print('5.- Agregar archivo')
    print('6.- Cerrar programa')
    opcion=input('>')
    
    if opcion == '1':
        crear_archivo(input('nombre del archivo a crear: '))
    elif opcion == '2':
        eliminar_archivo(input('nombre del archivo que desea eliminar: '))
    elif opcion == '3':
        escribir_archivo(input('nombre del archivo donde desea escribir: ') , input('Escriba lo que desea que este dentro de su archivo: '))
    elif opcion == '4':
        leer_archivo(input('nombre del archivo que desea leer: '))
    elif opcion == '5':
        agregar_archivo(input('En que archivo desea escribir: ') , input('Escriba lo que desea añadir al archivo: '))
    elif opcion == '6':
        break
    else: 
        print('opcion invalida')

