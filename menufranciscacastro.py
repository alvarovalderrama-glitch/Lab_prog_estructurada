import os  #importa libreria "os" al codigo 

def crear_archivo(nombre):                        #crea funcion "crear archivo" con parametro nombre
    with open(nombre, 'w') as f:                  #abre el archivo en modo escritura hace llamar la funcion f
        pass                                      #pasar
    print("Archivo " + nombre +" creado.")        #imprime la confirmacion de que el archivo ha sido creado

def eliminar_archivo(nombre):                     # define la función eliminar_archivo con parámetro 'nombre'
    if os.path.exists(nombre):                    #comprueba si un archivo con ese nombre existe en el sistema 
        os.remove(nombre)                         # si existe, lo elimina
        print("Archivo " + nombre +" eliminado.") # imprime confirmación de eliminación
    else:                                         # si no existe...
        print("Archivo "+ nombre +" no existe.")  # ...imprime que no se encontró el archivo                

def escribir_archivo(nombre, contenido):          # define función para escribir (sobrescribir) contenido en un archivo
    with open(nombre, 'w') as f:                  # abre el archivo en modo escritura ('w'), que borra el contenido previo
        f.write(contenido)                        # escribe la cadena 'contenido' dentro del archivo  
    print("Contenido escrito en " + nombre +" (modo write).") # confirma que se escribió el contenido

def leer_archivo(nombre):                         # define función para leer y mostrar el contenido de un archivo
    if os.path.exists(nombre):                    # comprueba si el archivo existe
        with open(nombre, 'r') as f:              # abre el archivo en modo lectura ('r') (read)
            contenido = f.read()                  # lee todo el contenido y lo guarda en la variable 'contenido'
        print("Contenido de " + nombre +":" + contenido) # imprime el nombre del archivo y su contenido
    else:                                         # si no existe el archivo...
        print("El archivo " + nombre +" no existe.") # ...informa que no existe

def agregar_archivo(nombre, contenido):           # define función para agregar (append) contenido al final del archivo
    with open(nombre, 'a') as f:                  # abre el archivo en modo 'a' (append): añade sin sobrescribir
        f.write(contenido)                        # escribe/añade la cadena 'contenido' al final del archivo
    print("Contenido agregado en " + nombre +" (modo append).") # confirma que se agregó el contenido


# Menú principal
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Crear archivo")
        print("2. Eliminar archivo")
        print("3. Escribir archivo (modo w)")
        print("4. Leer archivo (modo r)")
        print("5. Agregar archivo (modo a)")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del archivo: ")
            crear_archivo(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del archivo: ")
            eliminar_archivo(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Ingrese el contenido a escribir: ")
            escribir_archivo(nombre, contenido)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del archivo: ")
            leer_archivo(nombre)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Ingrese el contenido a agregar: ")
            agregar_archivo(nombre, contenido)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

# Llamada al menú
menu()
