import os # importar archivos del sistema


def crear_archivo(nombre):  #definir crear_archivo con variable nombre
    with open(nombre,'w') as f: #crear archivo con variable nombre en modo w como f e imprimir archivo nombre creado
        pass
    print("archivo " + nombre +" creado")

def eliminar_archivo(nombre): #definir eliminar_archivo con variable nombre y si existe, remover el archivo nombre e imprimir archivo nombre eliminado, sino imprimir archivo nombre no existe
    if os.path.exists(nombre):
        os.remove(nombre)
        print("archivo " + nombre +" eliminado")
    else:
        print("archivo "+ nombre + "no existe")

def escribir_archivo(nombre, contenido): #definir escribir_archivo con variable nombre, contenido
    with open(nombre, 'w') as f: #con archivo nombre abierto en modo w como f, escribir f en contenido e imprimir contenido escrinto en nombre modo write
        f.write(contenido)
    print("contenido escrito en "+ nombre +"(modo write).")

def leer_archivo(nombre):  #definir leer_archivo con variable nombre
    if os.path.exists(nombre):  # si existe el archivo nombre, abrir archivo nombre en modo r como f y contenido seria igual a leer f
        with open(nombre, 'r') as f:  #imprimir contenido de nombre mas contenido, sino, contenido de nombre no existe
            contenido = f.read()
        print("contenido de "+ nombre + ":"+ contenido)
    else:
        print("el archivo " + nombre + "no existe")

def agregar_archivo(nombre, contenido): #definir agregar_archivo con variable nombre y contenido
    with open(nombre, 'a') as f:    #con archivo nombre abierto en modo a como f, escribir en f contenido e imprimir contenido agregado en nombre modo append
        f.write(contenido)
    print("contenido agregado en " + nombre + "(modo append)")

while True: #definir bucle como verdadero, imprimir menu  con opciones de 1 al 6
    print("\n---menu---")
    print("1. crear archivo")
    print("2. eliminar archivo")
    print("3. escribir en archivo")
    print("4. leer archivo")
    print("5. agregar en archivo")
    print("6. salir")
    
    opcion= input('selecciona una opcion (1-6): ') #usar variable opcion igual a agregar un contenido mas imprimir selecciona una opcion de 1-6

    if opcion=='1':  #si opcion escogida es igual a 1, ingresar nombre del archivo y crearlo, cambiando la variable nombre al contenido ingresado
        nombre = input("ingresa el nombre del archivo: ")
        crear_archivo(nombre)
    elif opcion=='2': #si opcion escogida es igual a 2, escribir el nombre del archivo y llamar a la funcion eliminar_archivo(nombre)
        nombre = input("escribe el nombre del archivo que quieras borrar: ")
        eliminar_archivo(nombre)
    elif opcion== '3':  #si opcion escogida es 3, ingresar el nombre de archivo que se quiera escribir, escribir contenido y llamar funcion escribir_archivo
        nombre= input("ingresa nombre del archivo que quieras escribir: ")
        contenido= str(input(">"))
        escribir_archivo(nombre, contenido)
    elif opcion== '4':# si opcion escogida es 4, ingresar nombre de archivo a leer y llamar funcion leer_archivo
        nombre= input("escribe el nombre del archivo que quieras leer: ")
        leer_archivo(nombre)
    elif opcion== '5':# si opcion escogida es 5, ingresar nombre de archivo, escribir en archivo y llamar a la funcion agregar_archivo
        nombre= input("ingresa el nombre del archivo que quieras agregar:")
        contenido= str(input(">"))
        agregar_archivo(nombre, contenido)
    elif opcion == '6': # si opcion escogida es 6, imprimir saliendo del programa y romper el bucle while
        print('saliendo del programa...')
        break
    else: #si la opcion escogida es invalida, imprimir digito no valido, ingrese otro valido
        print("digito no valido, ingrese otro valido")

