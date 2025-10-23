import os

def crear_archivo (nombre):
    with open(nombre, "w") as f:
        pass
    print ("Archivo "+nombre+" creado.")

def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado.")
    else:
        print("Archivo "+ nombre +" no existe.")
def escribir_archivo(nombre, contenido):
    with open(nombre, 'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).")
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre, 'r') as f:
            contenido = f.read()
        print("Contenido de " + nombre + ":" + contenido)
    else:
        print("El archivo " + nombre + " no existe.")
def agregar_archivo(nombre, contenido):
    with open(nombre, 'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")

print ("----")
print ("MENU")
print ("----")
print ("1. Crear Archivo")
print ("2. Eliminar Archivo")
print ("3. Escribir Archivo")
print ("4. Leer Archivo")
print ("5. Agregar Archivo")
print ("6. Eliminar Archivo")
numero = int(input("Seleccione un número: "))

if numero==1:
    crear_archivo("TestNidiaRivera.txt")
else:
    if numero==2:
        eliminar_archivo("TestNidiaRivera.txt")
    else:
        if numero==3:
            contenido = input ("Ingrese contenido a escribir:")
            escribir_archivo("TestNidiaRivera.txt", contenido)
        else:
            if numero==4:
                leer_archivo("TestNidiaRivera.txt")
            else:
                if numero==5:
                    agregar_archivo("TestNidiaRivera.txt")
                else:
                    exit
