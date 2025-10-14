import os

def crear_archivo(nombre):
    nombre = str(nombre + '.txt') #Convierte el archivo en .txt para ser leido normalmente en la computadora
    with open(nombre, 'w') as f: 
        pass 
    print("Archivo " + nombre +" creado.")
    
def eliminar_archivo(nombre):
    nombre = str(nombre + '.txt') #Agrega .txt al nombre, para que detecte correctamente el archivo
    if os.path.exists(nombre): 
        os.remove(nombre) 
        print("Archivo " + nombre + " eliminado.") 
    else: 
        print("Archivo "+ nombre +" no existe.")
        
def escribir_archivo(nombre, contenido):
    nombre = str(nombre + '.txt') #Agrega .txt al nombre, para que detecte correctamente el archivo
    with open(nombre, 'w') as f: 
        f.write(contenido) 
    print("Contenido escrito en " + nombre + " (modo write).")
    
def leer_archivo(nombre):
    nombre = str(nombre + '.txt') #Agrega .txt al nombre, para que detecte correctamente el archivo
    if os.path.exists(nombre): 
        with open(nombre, 'r') as f: 
            contenido = f.read() 
        print("Contenido de " + nombre + ": " + contenido) 
    else: 
        print("El archivo " + nombre + " no existe.")
        
def agregar_archivo(nombre, contenido):
    nombre = str(nombre + '.txt') #Agrega .txt al nombre, para que detecte correctamente el archivo
    with open(nombre, 'a') as f: 
        f.write(contenido) 
    print("Contenido agregado en " + nombre + " (modo append).")
    
def interactuar_menu():
    print("\n    --- Menu ---")
    print("1.- Crear archivo")
    print("2.- Eliminar archivo")
    print("3.- Escribir archivo")
    print("4.- Leer archivo")
    print("5.- Agregar archivo")
    print("6.- Salir")
    
    opcion = input("Selecciona una opción (1-6): ")
    
    if opcion == '1':
        nombre = input("Ingresa el nombre del archivo: ")
        crear_archivo(nombre)
    elif opcion == '2':
        nombre = input("Ingresa el nombre del archivo a borrar: ")
        eliminar_archivo(nombre)
    elif opcion == '3':
        nombre = input ("Ingresa el nombre del archivo que quieres escribir: ")
        contenido = input("Ingresa lo que quieras escribir: ")
        escribir_archivo(nombre, contenido)
    elif opcion == '4':
        nombre = input("Ingresa el nombre del archivo que quieras leer: ")
        leer_archivo(nombre)
    elif opcion == '5':
        nombre = input("Ingresa el nombre del archivo la que quieres agregar información: ")
        contenido = input("Ingresa lo que quieras agregar: ")
        agregar_archivo(nombre, contenido)
    elif opcion == '6':
        print("\nAdios")
        exit()
    else:
        print("\nIngresa un número valido")
            
while True:
    interactuar_menu()