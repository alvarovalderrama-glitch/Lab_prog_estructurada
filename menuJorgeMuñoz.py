import os

def crear_archivo(nombre):
    with open(nombre, "w") as f:
        pass
    print(f"Archivo {nombre} creado.")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print(f"Archivo {nombre} eliminado.")
    else:
        print("Archivo {nombre} no existe.")

def escribir_archivo(nombre, contenido):
    with open(nombre, "w") as f:
        f.write(contenido)
    print(f"Contenido escrito en {nombre} (modo write).")

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, "r") as f:
            contenido = f.read()
        print(f"Contenido de {nombre}: {contenido}")
    else:
        print(f"El archivo {nombre} no existe.")

def agregar_archivo(nombre, contenido):
    with open(nombre, "a") as f:
        f.write(contenido)
    print(f"Contenido agregado en {nombre} (modo append).")





def mostrar_menu():
    while True:
        print("""\n\n
------------------------------- MENU ------------------------------- 
    1. Crear archivo
    2. Eliminar archivo
    3. Escribir archivo (sobreescribe texto previo)
    4. Leer archivo
    5. Agregar al archivo
    6. Salir
--------------------------------------------------------------------""")
        
        opcion = input("Seleccione una opción:\n>")
        if opcion == "1":
            nombre = input("Ingrese el nombre del archivo a crear (agregue .txt al final):\n>")
            crear_archivo(nombre)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del archivo a eliminar (agregue .txt al final):\n>")
            eliminar_archivo(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del archivo a escribir (agregue .txt al final):\n>")
            contenido = input("\nIngrese el contenido a escribir:\n>")
            escribir_archivo(nombre, contenido)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del archivo a leer (agregue .txt al final):\n>")
            leer_archivo(nombre)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del archivo al que desea agregar texto (agregue .txt al final):\n>")
            contenido = input("\nIngrese el contenido a escribir:\n>")
            agregar_archivo(nombre, contenido)
        elif opcion == "6":
            print("Cerrando programa...")
            break
        else:
            print("Valor inválido. Inténtelo nuevamente.")

mostrar_menu()