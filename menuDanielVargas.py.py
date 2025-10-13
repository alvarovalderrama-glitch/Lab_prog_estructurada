import os  
def crear_archivo(nombre):
    with open(nombre,'w') as f:
        pass
    print("Archivo" + nombre +" creado.")     
def eliminar_archivo(nombre):
    if os.path.exists(nombre):
        os.remove(nombre)
        print("Archivo " + nombre + " eliminado.")
    else:
        print("Archivo "+ nombre +" no existe.")      
def escribir_archivo(nombre,contenido):
    with open(nombre,'w') as f:
        f.write(contenido)
    print("Contenido escrito en " + nombre + " (modo write).") 
def leer_archivo(nombre):
    if os.path.exists(nombre):
        with open(nombre,'r') as f:
            contenido=f.read()
        print("Contenido de " + nombre + ":" + contenido)
    else:
        print("El archivo " + nombre + " no existe.")         
def agregar_archivo(nombre,contenido):
    with open(nombre,'a') as f:
        f.write(contenido)
    print("Contenido agregado en " + nombre + " (modo append).")

# El código está representado fielmente a como está en la evaluación.     
   
   
#-----------------------------------------------------------------------------------------------------------------------------   
 
 
# Inicio del programa real y el código creado para ejecutar las funciones.   

print('\n---------------------------------------------------------------')
print('                   MENÚ - GESTOR DE ARCHIVOS')
accion='10'
 
while accion!='6':
    print('---------------------------------------------------------------\n')
    print('Ingresa una opción:')
    print('1 = Crear archivo\n2 = Eliminar archivo\n3 = Escribir archivo (modo w)\n4 = Leer archivo (modo r)\n5 = Agregar archivo (modo a)\n6 = Salir')
    accion=input('> ')
    if accion=='1' or accion=='crear' or accion=='Crear':
        nombre=input('\nNombre del archivo a crear (agregar ".txt" al final): ')
        crear_archivo(nombre)
    elif accion=='2' or accion=='eliminar' or accion=='Eliminar':
        nombre=input('\nNombre del archivo a eliminar (agregar ".txt" al final): ')
        eliminar_archivo(nombre) 
    elif accion=='3' or accion=='escribir' or accion=='Escribir':
        nombre=input('\nNombre del archivo para escribir (se eliminará el contenido anterior): ')
        contenido=input('Escriba el contenido: ')
        escribir_archivo(nombre,contenido)
    elif accion=='4' or accion=='leer' or accion=='Leer':
        nombre=input('\nNombre del archivo para leer: ')
        leer_archivo(nombre)
    elif accion=='5' or accion=='agregar' or accion=='Agregar':
        nombre=input('\nNombre del archivo para agregar contenido: ')
        contenido=input('Escriba el contenido: ')
        agregar_archivo(nombre,contenido)
    elif accion=='6' or accion=='salir' or accion=='Salir':
        break
    else:
        print('\n---------------------------------------------------------------')
        print('OPCIÓN INVÁLIDA. La entrada "'+accion+'" no es una opción.')

print('\n---------------------------------------------------------------')
print('                      GESTIÓN FINALIZADA')
print('---------------------------------------------------------------\n')