import os

#---Funciones principales----

def crear_archivo(nombre):
#---Crea un archivo---
    with open(nombre, 'w') as f:
        pass
    print("Archivo" + nombre + "creado.")

def eliminar_archivo(nombre):
#---Elimina un archivo existente---
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo" + nombre + "eliminado.")
    else:
        print("Archivo" + nombre + "no existe.")

def escribir_archivo(nombre, contenido):
#---Escribe contenido en el archivo---
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en" + nombre + "(modo write).")

def leer_archivo(nombre):
#---Lee y muestra el contenido de un archivo---
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de" + nombre + ":" + contenido)
    else:
        print("El archivo" + nombre + "no existe.")

def agregar_archivo(nombre, contenido):
#---Agrega contenido al final de un archivo---
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en" + nombre + "(modo append).")

                              # ---Función del menu---

#Funcion que muestra el menu principal
def mostrar_menu():
    while True:
        print("\n------ Menú ------")
        print("1. Crear archivo")
        print("2. Eliminar archivo")
        print("3. Escribir archivo")
        print("4. Leer archivo")
        print("5. Agregar archivo")
        print("6. Salir")

        opcion = input("Selecciona una opción (1-6): ")

        if opcion == '1':
            nombre_archivo = input("Ingrese el nombre del archivo a crear: ")
            crear_archivo(nombre_archivo)
        
        elif opcion == '2':
            nombre_archivo = input("Ingrese el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre_archivo)
        
        elif opcion == '3':
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            texto = input("Ingrese el contenido a escribir: ")
            escribir_archivo(nombre_archivo, texto)
        
        elif opcion == '4':
            nombre_archivo = input("Ingrese el nombre del archivo a leer: ")
            leer_archivo(nombre_archivo)
        
        elif opcion == '5':
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            texto = input("Ingrese el contenido a agregar: ")
            agregar_archivo(nombre_archivo, texto)
        
        elif opcion == '6':
            print("Saliendo del programa con éxito.")
            break
        
        else:
            print("Opción no válida. Intenta de nuevo.")

# --- Ejecución del programa ---
if __name__ == "__main__":
    mostrar_menu()
