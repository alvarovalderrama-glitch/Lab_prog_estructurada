import os

def crear_archivo(nombre):
    if not nombre.endswith('.txt'):
         nombre += '.txt'
    with open(nombre, 'w') as f:
        pass
    print('Archivo' + nombre + 'Ha sido creado.')

def eliminar_archivo(nombre):
    if not nombre.endswith('.txt'):
        nombre+='.txt'
    if os.path.exists(nombre):
        os.remove(nombre)
        print('Archivo' + nombre + 'Ha sido eliminado.')
    else:
        print('Archivo' + nombre + 'No existe.')

def escribir_archivo(nombre):
    if not nombre.endswith('.txt'):
        nombre+='.txt'
    with open(nombre, 'w') as f:
        f.write(contenido)
    print('Contenido escrito en ' + nombre + '(modo write).')

def leer_archivo(nombre):
    if not nombre.endswith('.txt'):
        nombre+='.txt'
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print('Contenido de ' + nombre + ':')
        print(contenido)
    else:
        print('El archivo ' + nombre + 'no existe.')
def agregar_archivo(nombre, contenido):
    if not nombre.endswith('.txt'):
        nombre+='.txt'
    with open(nombre, 'a') as f:
        f.write(contenido)
    print('Contenido agregado en ' + nombre + ' (modo append).')


# Seleccion de Opciones
while True:
    print('--- MENÚ PRINCIPAL ---')
    print("1. Crear archivo")
    print("2. Eliminar archivo")
    print("3. Escribir archivo (modo w)")
    print("4. Leer archivo (modo r)")
    print("5. Agregar archivo (modo a)")
    print("6. Salir")

    opcion = input("Seleccione una opción del 1-6 ")

    if opcion == '1':
        nombre = input("Ingrese el nombre del archivo: ")
        crear_archivo(nombre)

    elif opcion == '2':
        nombre = input("Ingrese el nombre del archivo a eliminar: ")
        eliminar_archivo(nombre)

    elif opcion == '3':
        nombre = input("Ingrese el nombre del archivo: ")
        contenido = input("Ingrese el contenido: ")
        escribir_archivo(nombre, contenido)

    elif opcion == '4':
        nombre = input("Ingrese el nombre del archivo a leer: ")
        leer_archivo(nombre)

    elif opcion == '5':
        nombre = input("Ingrese el nombre del archivo: ")
        contenido = input("Ingrese el texto a agregar: ")
        agregar_archivo(nombre, contenido)

    elif opcion == '6':
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intente nuevamente.")
