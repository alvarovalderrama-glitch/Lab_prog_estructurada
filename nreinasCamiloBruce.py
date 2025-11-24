contador = 0

def validar(tablero, fila, columna, n): # Verifica que es posible poner una reina en la posición.
    
    for j in range(n): # Verifica si hay otra reina en la misma fila
        if tablero[fila][j] == 1:
            return False

    for i in range(n): # Verifica si hay otra reina en la misma col.
        if tablero[i][columna] == 1:
            return False
        
    # Verifica si hay otra reina en la diagonal superior izq.   
    i = fila 
    j = columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1
    
    # Verifica si hay otra reina en la diagonal superior der.   
    i = fila 
    j = columna
    while i >= 0 and j < n:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j += 1
    
    # Verifica si hay otra reina en la diagonal inferior izq.   
    i = fila 
    j = columna
    while i < n and j >= 0:
        if tablero[i][j] == 1:
            return False
        i += 1
        j -= 1
    
    # Verifica si hay otra reina en la diagonal inferior der.  
    i = fila 
    j = columna
    while i < n and j < n:
        if tablero[i][j] == 1:
            return False
        i += 1
        j += 1
    
    return True

def resolver(tablero, fila, n, archivo): # Funcion para resolver.
    global contador

    if fila == n: # Si se llega al final del tablero y se encontro solución
        contador = contador + 1 # Incrementa el numero de soluciones
        archivo.write(f"Solución {contador}\n\n") # Escribe el numero de la sol. en el archivo
        guardar_sol(tablero, archivo) # Guarda el tablero de la sol.
        return 1 # Return 1 para contar la sol.
    
    soluciones = 0 # Contador de soluciones para esta pos.

    for columna in range(n): # Probar todas las columnas de la fila actual
        if validar(tablero, fila, columna, n): # Si es valida la pos. actual...
            tablero[fila][columna] = 1 #...Coloca la reina
            soluciones = soluciones + resolver(tablero, fila + 1, n, archivo) # Llama recursivamente a la funcion y suma los sol. encontradas
            tablero[fila][columna] = 0 # Quita la reina
    
    return soluciones # Retorna la cantidad de soluciones

def guardar_sol(tablero, archivo): # Funcion para guardar la sol.
    for fila in tablero: # Recorre cada fila del tablero
        for celda in fila: # Recorre cada celda de la fila.
            if celda == 1: # Si en la celda hay un 1
                archivo.write("R ") # Lo cambia por una R para denotar que hay una reina en esa pos.
            else: # Si no hay un 1.
                archivo.write(". ") # Entonces lo cambia por un punto
        archivo.write("\n")
    archivo.write("\n")


# Programa principal.
n = int(input("Ingrese el numero de reinas: "))
tablero = [[0 for _ in range(n)] for _ in range(n)]

with open("nreinas.txt", "w") as f:
        total_sol = resolver(tablero, 0, n, f)
        print(f'Se han encontrado {total_sol} solucione(s) y se guardaron en "nreinas.txt"')