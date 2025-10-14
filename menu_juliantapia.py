import os 
 
def crear_archivo(nombre):  
    with open(nombre, 'w') as f:  
        pass  
    print("Archivo " + nombre +" creado.")  
 
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
        print("Contenido de " + nombre + ": " + contenido)  
    else:  
        print("El archivo " + nombre + " no existe.") 
 
def agregar_archivo(nombre, contenido):  
    with open(nombre, 'a') as f:  
        f.write(contenido)  
    print("Contenido agregado en " + nombre + " (modo append).")  
 
def menu_interactivo(): 
    print('--- MENU ---') 
    print('1. Crear archivo (p.ej. test.txt) \n2. Eliminar archivo \n3. Escribir archivo (modo w) \n4. Leer archivo (modo r) \n5. Agregar archivo (modo a) \n6. Salir \n') 
    print('Elija una opción:') 
    while True: 
        try: 
            opcion = int(input('>')) 
            if opcion not in [1,2,3,4,5,6]: 
                print('Opcion fuera de rango.') 
            else:break 
        except ValueError: 
            print('Dato no valido') 
    if opcion !=6: 
        print('Ingrese el nombre del archivo') 
        nombre_archivo = input('>') 
         
        if opcion in [3,5]: 
            print('Ingrese el contenido que desea agregar') 
            contenido_archivo = input('>') 
         
        if opcion == 1: 
            crear_archivo(nombre_archivo) 
        elif opcion == 2: 
            eliminar_archivo(nombre_archivo) 
        elif opcion == 3: 
            escribir_archivo(nombre_archivo, contenido_archivo) 
        elif opcion == 4: 
            leer_archivo(nombre_archivo) 
        elif opcion == 5: 
            agregar_archivo(nombre_archivo, contenido_archivo) 
        print() 
         
    else: 
        print('Adios.') 
        return(False) 
     
ejecutar=True 
while ejecutar!=False: 
    ejecutar = menu_interactivo()