import os                                                                           #Importa el modulo de os 
def crear_archivo(nombre):                                                          #Define una función que tiene como nombre crear archivo
    with open(nombre, 'w') as f:                                                    #Abre y crea un archivo con el nombre indicado
        pass                                                                        #Es una instruccion que no ejecuta nada
    print("Archivo" + nombre +" creado.")                                           #Imprime el nombre del archivo creado
def eliminar_archivo(nombre):                                                       #Define una función para eliminar un archivo
    if os.path.exists(nombre):                                                      #Verifica que el archivo exista
        os.remove(nombre)                                                           #Elimina el archivo
        print("Archivo " + nombre + " eliminado.")                                  #Imprime que el archivo fue eliminado
    else:                                                                           #Si el archivo no existe
        print("Archivo "+ nombre +" no existe.")                                    #Se muestra que el archivo con el nombre ingresado no existe
def escribir_archivo(nombre, contenido):                                            #Define una función para escribir en el archivo
    with open(nombre, 'w') as f:                                                    #Abre el archivo que se nombro, y se pone en modo write
        f.write(contenido)                                                          #Escribe dentro del archivo el contenido
        print("Contenido escrito en " + nombre + " (modo write).")                  #Imprime que se le escribió el nuevo contenido al archivo
def leer_archivo(nombre):                                                           #Define una funcion para leer el archivo
    if os.path.exists(nombre):                                                      #Verifica que el archivo exista
        with open(nombre, 'r') as f:                                                #Abre el archivo y lo lee
            contenido = f.read()                                                    #El contenido pasa a ser lo que leyo
            print("Contenido de " + nombre + ":" + contenido)                       #Se imprime el contenido del archivo
    else:                                                                           #Si el archivo no existe
            print("El archivo " + nombre + " no existe.")                           #Se imprime que el archivo no existe
def agregar_archivo(nombre, contenido):                                             #Define la funcion de agregar texto 
    with open(nombre, 'a') as f:                                                    #Abre el archivo que se escogio en modo append
        f.write(contenido)                                                          #Agrega al archivo el contenidp sin borrar lo anterior
        print("Contenido agregado en " + nombre + " (modo append).")                #Se imprime en nombre del contenido y el contenido agregado
while True:                                                                         #Comienza un bucle para que se ejecute el menú y sus opciones
    print("----Menú de archivos----")                                               #Muestra el menú de archivos
    print("1.- Crear archivos")                                                     #Muestra la opcion de crear el archivo
    print("2.- Eliminar archivo")                                                   #Muestra la opcion de eliminar el archivo
    print("3.- Escribir archivo")                                                   #Muestra la opcion de escribir contenido nuevo (eliminando lo anterior)
    print("4.- Leer archivo")                                                       #Muestra la opcion de leer el archivo
    print("5.- Agregar contenido")                                                  #Muestra la opcion de agregar contenido al final del archivo
    print("6.- Salir")                                                              #Muestra la opcion de salir del menú
    opcion= input("Seleccione una opcion ")                                         #Hace escoger entre las opciones
    if opcion=="1":                                                                 #Si se tomo la opcion 1:
        nombre=input("Ingresa el nombre del archivo: ")                             #Pide el nombre del archivo
        crear_archivo(nombre)                                                       #Se crea el archivo
    elif opcion=="2":                                                               #Si se escoge la opcion dos
        nombre=input("Ingresa el nombre del archivo que deseas eliminar: ")         #Pide el nombre del archivo que quieras eliminar
        eliminar_archivo(nombre)                                                    #Elimina el archivo
    elif opcion=="3":                                                               #Si se escoge la opcion 3
        nombre=input("Ingresa el nombre del archivo: ")                             #Se pide el nombre del archivo
        contenido=input("Ingresa el contenido del archivo: ")                       #Se pide que es lo que se quiere escribir
        escribir_archivo(nombre, contenido)                                         #Se escribe en el archivo
    elif opcion=="4":                                                               #Si se escoge la opcion 4
        nombre=input("Ingresa el nombre del archivo que quieras leer: ")            #Se pide el nombre del archivo que se desea leer
        leer_archivo(nombre)                                                        #Se lee el archivo
    elif opcion=="5":                                                               #Si se escoge la opcion 5
        nombre=input("Ingresa el nombre del archivo al que le quieras agregar: ")   #Se pide el nombre de el archivo al que le quieras añadir contenido
        contenido=input("Agregar cotenido: ")                                       #Se pide el contenido que se quiere agregar
        agregar_archivo(nombre, contenido)                                          #Se agrega el archivo
    elif opcion=="6":                                                               #Si se escoge la opcion 6
        print("Saliendo")                                                           #Se imprime que esta saliendo
        break                                                                       #Se rompe el ciclo
    else:                                                                           #Si no es ninguna de estas opciones 
        print("Opcion invalida")                                                    #Se imprime opcion invalida


