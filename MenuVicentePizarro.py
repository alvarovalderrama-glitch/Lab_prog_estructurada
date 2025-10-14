import os
def crear_archivo(nombre):
    with open(nombre,"w") as f:
        pass
    print("Archivo " + nombre + " creado")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " Eliminado.")
    else :
        print("Archivo " + nombre + " no existe.")
    
def escribir_archivo(nombre,contenido):
    with open( nombre,"w")as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).")

def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open( nombre, "r")as f:
            contenido = f.read()
        print("contenido de " + nombre + ": " + contenido)
    else:
        print("el archivo " + nombre + " no existe.")

def agregar_archivo(nombre,contenido):
    with open( nombre,"a")as f:
        f.write( contenido )
    print("contenido agregado en " + nombre + " (modo append).")

#-------------------------------------------------------------------------------------------------------------------------

while True:
    print("-----Menu-----")
    print("1. crear archivo")
    print("2. eliminar archivo")
    print("3. escribir archivo (modo w)")
    print("4. leer archivo (modo r)")
    print("5. agregar archivo (modo a)")
    print("6. salir")
    break

print("Elige una opcion desde 1 a 6 ")
opcion= input()

if opcion == "1":
    crear_archivo(input("introduzca el nombre de su archivo: "))
 
elif opcion == "2":
    eliminar_archivo(input("introduzca el nombre del archivo que quiere eliminar: "))
    
elif opcion == "3":
    escribir_archivo(input("introduzca el nombre del archivo en el que escribira: "),input("escribiendo: "))

elif opcion == "4":
    leer_archivo(input("introduzca el nombre del archivo que leera: "))

elif opcion == "5":
    agregar_archivo(input("introduzca el nombre del archivo que quiere agregar texto: "),input("agregando: "))

elif opcion == "6":
    print("saliendo del archivo...")
    
else:
    print("numero fuera de las opciones, porfavor elija denuevo")
