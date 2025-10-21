# Gestor de archivos
# Menú simple: crear, escribir, leer, agregar y eliminar archivos de texto.

import os                                                         # Para operaciones de archivos

def crear(nombre):                                                # Crea archivo vacío
    open(nombre, "w", encoding="utf-8").close()                   # Crea y cierra
    print("Creado.")

def escribir(nombre):                                             # Sobrescribe contenido
    texto = input("Contenido (sobrescribe):\n")                   # Pide texto
    with open(nombre, "w", encoding="utf-8") as f:                # Abre en escritura
        f.write(texto)                                            # Escribe
    print("Guardado.")

def agregar(nombre):                                              # Agrega al final
    texto = input("Contenido a agregar:\n")                       # Pide texto
    with open(nombre, "a", encoding="utf-8") as f:                # Abre en append
        f.write(texto + "\n")                                     # Añade con salto
    print("Agregado.")

def leer(nombre):                                                 # Muestra contenido
    if not os.path.exists(nombre):                                # Verifica existencia
        print("No existe."); return                               # Informa
    with open(nombre, "r", encoding="utf-8") as f:                # Abre lectura
        print("\n--- CONTENIDO ---")                              # Cabecera
        print(f.read())                                           # Imprime todo
        print("------------------")                               # Pie

def eliminar(nombre):                                             # Borra archivo
    if os.path.exists(nombre):                                    # Si existe
        os.remove(nombre)                                         # Elimina
        print("Eliminado.")                                       # Mensaje
    else:
        print("No existe.")                                       # Mensaje

while True:                                                       # Bucle menú
    print("\n1) Crear  2) Escribir  3) Agregar  4) Leer  5) Eliminar  6) Salir") # Opciones
    op = input("Opción: ").strip()                                # Lee opción
    if op == "6": break                                           # Salir
    nombre = input("Nombre de archivo (ej: notas.txt): ").strip() # Pide nombre
    if op == "1": crear(nombre)                                   # Ejecuta crear
    elif op == "2": escribir(nombre)                              # Ejecuta escribir
    elif op == "3": agregar(nombre)                               # Ejecuta agregar
    elif op == "4": leer(nombre)                                  # Ejecuta leer
    elif op == "5": eliminar(nombre)                              # Ejecuta eliminar
    else: print("Opción inválida.")                               # Error
