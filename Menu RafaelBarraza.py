import os

def main():
    while True:
        imprimir_menu()

        accion = input("\nElige una accion: ")

        if accion == "1":
            nombre = input("Ingresa el nombre del archivo: ")
            crear_archivo(nombre)

        if accion == "2":
            nombre = input("Ingresa el nombre del archivo a eliminar: ")
            eliminar_archivo(nombre)

        if accion == "3":
            nombre = input("Ingresa el nombre del archivo: ")
            contenido = input("Ingresa el contenido: ")
            escribir_archivo(nombre, contenido)

        if accion == "4":
            nombre = input("Ingresa el nombre del archivo a leer: ")
            leer_archivo(nombre)  

        if accion == "5":
            nombre = input("Ingresa el nombre del archivo: ")
            contenido = input("Ingresa el contenido a agregar: ")
            agregar_archivo(nombre, contenido)

        if accion == "6":    
            break
        
    print("\n\n---------------------\nFIN DE PROGRAMA\n---------------------\n")  


def crear_archivo(nombre):
    with open(nombre,'w') as f:
        pass
    print('Archivo'' '+nombre+'Creado')



def eliminar_archivo(nombre):
 if os.path.exists(nombre):
        os.remove(nombre)
        print('Archivo'+nombre+'eliminado')
 else:
        print('Archivo'+nombre+'no existe')



def escribir_archivo(nombre,contenido):
     with open(nombre,'w') as f:
          f.write('\n'(contenido))
     print('Contenido escrito en'+nombre+'(modo write).')



def leer_archivo(nombre):
     if os.path.exists(nombre):
          with open(nombre,'r') as f:
               contenido= f.read()
          print ('Contenido de'+nombre+':'+ '\n'(contenido))
     else:
          print('El arcrchivo' + nombre + 'no existe.')



def agregar_archivo(nombre, contenido):
     with open(nombre,'a') as f:
          f.write(contenido)
     print('Contenido agregado en ' + nombre + '(modo append).') 


def imprimir_menu():
    print("\n\n\n\n\n===========================================")
    print("\t MANEJO DE ARCHIVOS.")
    print()
    print("1. Crear    \t archivo")
    print("2. Eliminar \t archivo")
    print("3. Escribir \t archivo")
    print("4. Leer     \t archivo")
    print("5. Agregar  \t archivo")
    print('6. Salir\n'           )


if __name__ == "__main__":
    main()
