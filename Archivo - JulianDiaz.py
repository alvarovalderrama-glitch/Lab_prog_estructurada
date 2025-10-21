
import os

def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print(f"Archivo '{nombre}' creado.")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print(f"Archivo '{nombre}' eliminado.")
    else:
        print(f"El archivo '{nombre}' no existe.")

def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print(f"Contenido escrito en '{nombre}' (modo w).")

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print(f"Contenido de '{nombre}':\n{contenido}")
    else:
        print(f"El archivo '{nombre}' no existe.")

def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print(f"Contenido agregado en '{nombre}' (modo a).")


if __name__ == "__main__":
    ejecutando = True
    while ejecutando:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear archivo")
        print("2. Eliminar archivo")
        print("3. Escribir archivo (modo w)")
        print("4. Leer archivo (modo r)")
        print("5. Agregar archivo (modo a)")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del archivo (ej: test.txt): ")
            crear_archivo(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Escriba el contenido: ")
            escribir_archivo(nombre, contenido)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del archivo a leer: ")
            leer_archivo(nombre)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del archivo: ")
            contenido = input("Escriba el contenido a agregar: ")
            agregar_archivo(nombre, contenido)
        elif opcion == "6":
            print("Saliendo del programa...")
            ejecutando = False
        else:
            print("Opción inválida. Intente de nuevo.")
