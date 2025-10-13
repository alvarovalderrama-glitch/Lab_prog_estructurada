import os
#Crea archivo vacío.
def crear_archivo(nombre):
    with open(nombre, 'w') as f:
         pass
    print("Archivo" + nombre +" creado.")
#Elimina archivo.
def eliminar_archivo(nombre):
     if os.path.exists(nombre):
          os.remove(nombre)
          print("Archivo " + nombre + " eliminado.")
     else:
          print("Archivo "+ nombre +" no existe.")
#Escribe archivo.
def escribir_archivo(nombre, contenido):
     with open(nombre, 'w') as f:
          f.write(contenido)
      print("Contenido escrito en " + nombre + " (modo write).")
#Leer archivo
def leer_archivo(nombre):
     if os.path.exists(nombre):
          with open(nombre, 'r') as f:
               contenido = f.read()
            print("Contenido de " + nombre + ":" + contenido)
     else:
          print("El archivo " + nombre + " no existe.")
#Agregar archivo
def agregar_archivo(nombre, contenido):
     with open(nombre, 'a') as f:
          f.write(contenido)
        print("Contenido agregado en " + nombre + " (modo append).")