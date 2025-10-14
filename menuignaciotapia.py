import os

#funcion que permite mostrar menu
def mostrar_menu():
     print("\n--- menu de archivos ---")
     print('1.  crear archivo')
     print('2.  eliminar archivo')
     print('3.  escribir archivo')
     print('4   leer archivo')
     print('5   agregar archivo')
     print('6   salir')
     print('----------------------------')


#bucle principal

def iniciar_menu(nombre, contenido):
     while True:
          mostrar_menu()
          opcion = input('seleccione una opcion (1-6) >')


          if opcion == '1':
               nombre=crear_archivo
               crear_archivo(nombre) # el usuario presiona 1 ---> llama a la funcion crear archivo
          elif opcion =='2':
               nombre=eliminar_archivo
               eliminar_archivo(nombre)
          elif opcion =='3':
               nombre=escribir_archivo 
               contenido=escribir_archivo
               escribir_archivo(nombre,contenido)
          elif opcion =='4':
               nombre=leer_archivo
               leer_archivo(nombre)
          elif opcion == '5':
               nombre=agregar_archivo
               contenido=agregar_archivo
               agregar_archivo (nombre,contenido)
          elif opcion =='6':
            print('saliendo del programa, hasta luego!')
            break
          else:
               print ('opcion no valida porfavor introduzca un numero')
        

#definicion de funciones que el programa usara



def crear_archivo(nombre):  
    nombre = input ( "Nombre del archivo a crear: ")                            
    with open (nombre,'w') as f:
        pass
    print ("archivo " + nombre + " creado")

def eliminar_archivo(nombre):
    nombre = input ('Nombre el archivo a eliminar:')
    if os.path.exists(nombre):
            os.remove(nombre)
            print("archivo " +nombre+ " eliminado.")
    else:
            print("archivo " +nombre+ " no existe.")

def escribir_archivo(nombre,contenido):
    nombre=input("ingresa nombre: ")
    contenido=input("\n------------------\nContenido para agregar al archivo: ")
    with open(nombre,'w')as f:
         f.write(contenido)
         print('contenido escrito en'+nombre+'(modo write).')

def leer_archivo(nombre):
     nombre = input ('Nombre del archivo a leer:')
     if os.path.exists(nombre):
          with open(nombre,'r')as f:
               contenido=f.read
               print ('contenido de' +nombre+ ':'+ str(contenido))
     else:
            print('el archivo' +nombre+' no existe.')
          
def agregar_archivo(nombre,contenido):
     nombre= input ('Nombre del archivo a agregar:')
     contenido= input('Introduzca el contenido que desea poner en el archivo:')
     with open(nombre,'a')as f:
          f.write (contenido)
          print ('contenido agregado en ' + nombre + ' (modo append).')

nombre=iniciar_menu
contenido=iniciar_menu
iniciar_menu(nombre, contenido)     




         
 