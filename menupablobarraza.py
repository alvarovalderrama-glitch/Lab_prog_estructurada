import os

#crear archivo
def crear_archivo(nombre):
    with open(nombre,"w") as f:
        pass
    print("Archivo" + nombre + "creado")

#eliminar archivo
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo" + nombre + "eliminado.")
    else:
        print("Archivo" + nombre + "no existe.")

#escribir archivo
def escribir_archivo(nombre,contenido):
    with open (nombre, "w") as f:
        f.write(contenido)
    print("Contenido escrito en" + nombre + "(modo write).")

#leer archivo
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre,"r") as f:
            contenido = f.read()
        print("Contenido de " + nombre + ":" + contenido)
    else:
        print("El archivo " + nombre + "no existe.")

#agregar archivo
def agregar_archivo(nombre,contenido):
        with open(nombre,"a") as f:
            f.write(contenido)
        print("Contenido agregado en" + nombre + "(modo append).")

#menu para crear archivo,eliminar archivo, escribir archivo(w), leer archivo(modo r), agregar archivo(modo a), Salir

while True:
    print("1.-Crear archivo")
    print("2.-eliminar archivo")
    print("3.-Escribir archivo")
    print("4.-Leer archivo")
    print("5.-Agregar archivo")
    print("6.-Salir archivo")

    opcion = input("Select an option(1-6):")

    if opcion == "1":
        createfile = input("nombre archivo: ")
        print("Archivo creado: ",createfile)
    elif opcion == "2":
        deletefile = input("nombre archivo: ")
        print("Archivo eliminado: ",deletefile)
    elif opcion == "3":
        writefile = input("nombre archivo: ")
        print("Archivo escrito: ",writefile)
    elif opcion == "4":
        readfile = input("nombre archivo: ")
        print("Archivo leido: ",readfile)
    elif opcion == "5":
        appendfile = input("nombre archivo: ")
        print("Archivo agregado: ", appendfile)
    elif opcion == "6":
        print("Saliendo...")
        break
    else:
        print ("error, seleccione un numero propuesto")    