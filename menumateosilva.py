import os

def crear_archivo(nombre):
    with open(nombre, 'w') as f:
        pass
    print("Archivo " + nombre + " creado.")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado.")
    else:
        print("Archivo " + nombre + " no existe.")

def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).")

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de " + nombre + ":\n" + contenido)
    else:
        print("El archivo " + nombre + " no existe.")

def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")

def menu():
    while True:
        print("\n=== Menú Archivos ===")
        print("1) Crear archivo (w)")
        print("2) Eliminar archivo")
        print("3) Escribir archivo (w)")
        print("4) Leer archivo (r)")
        print("5) Agregar archivo (a)")
        print("6) Salir")
        op = input("Elige una opción [1-6]: ").strip()

        if op == "1":
            nombre = input("Nombre del archivo (p.ej. test.txt): ").strip()
            crear_archivo(nombre)
        elif op == "2":
            nombre = input("Nombre del archivo a eliminar: ").strip()
            eliminar_archivo(nombre)
        elif op == "3":
            nombre = input("Nombre del archivo a escribir (se sobreescribe): ").strip()
            contenido = input("Contenido: ")
            escribir_archivo(nombre, contenido)
        elif op == "4":
            nombre = input("Nombre del archivo a leer: ").strip()
            leer_archivo(nombre)
        elif op == "5":
            nombre = input("Nombre del archivo para agregar contenido: ").strip()
            contenido = input("Contenido a agregar: ")
            agregar_archivo(nombre, contenido)
        elif op == "6":
            print("Saliendo…")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

if __name__ == "__main__":
    menu()
