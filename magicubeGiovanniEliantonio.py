
def cuadrado_magico(tablero):
    # Calcula la suma objetivo ("valor mágico") usando la primera fila
    valor_suma = 0
    for i in  range(tamaño_tablero):
        valor_suma += tablero[0][i] # suma la primera fila
    
    # Verifica todas las filas
    for i in range(tamaño_tablero):
        suma = 0
        for j in range(tamaño_tablero):
            suma += tablero[i][j]
        
        if suma != valor_suma: 
            return False
    
    # Verifica todas las columnas    
    for j in range(tamaño_tablero):
        suma = 0
        for i in range(tamaño_tablero):
            suma += tablero[i][j]

        if suma != valor_suma:
            return False
    
    # Verifica diagonal principal
    i = 0; j = 0; suma = 0
    while (i < tamaño_tablero) and (j < tamaño_tablero):

        suma += tablero[i][j]
        i += 1; j += 1

    if suma != valor_suma:
        return False

    # Verifica diagonal secundaria
    i = 0; j = tamaño_tablero - 1; suma = 0
    while (i < tamaño_tablero) and (j >= 0):

        suma += tablero[i][j]
        i += 1; j -= 1

    # Si todas las verificaciones son correctas entonces es cuadrado mágico
    if suma != valor_suma:
        return False
    else:
        return True

def final(tablero):
    # Verifica si el tablero está lleno (sin ceros)
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if tablero[i][j] == 0:
                return False
            
    return True

def valida(tablero, candidato, i, j):
    # No se permite escribir sobre una casilla que ya tiene valor
    if tablero[i][j] != 0:
        return False

    """ Revisa que el número no se haya usado antes
    El uso de x,y evita sobrescribir en i,j """
    for x in range(tamaño_tablero):
        for y in range(tamaño_tablero):
            if tablero[x][y] == candidato:
                return False

    return True

def encontrar_solucion(tablero, pos):
    
    # Si se llenaron todas las casillas, se comprueba si es cuadrado mágico
    if pos == tamaño_tablero * tamaño_tablero:
        return cuadrado_magico(tablero)

    # Convertir "pos" a coordenadas (i,j), ej: pos 4: i = (4 // 3), j = (4 % 3) entones i = 1 y j = 0
    # i: fila actual, j: columna actual
    i = pos // tamaño_tablero
    j = pos % tamaño_tablero

    # Probar todos los números posibles en la casilla actual
    for candidato in range(1, tamaño_tablero * tamaño_tablero + 1):

        if valida(tablero, candidato, i, j):
            tablero[i][j] = candidato  # colocar candidato

            # Llamada recursiva para avanzar a la siguiente casilla
            if encontrar_solucion(tablero, pos + 1):  # recursión a siguiente casilla
                return True

            # Si falló, retirar número
            tablero[i][j] = 0

    # Si ningún número funcionó, no hay solución
    return False

def mostrar_tablero(tablero):
    """ Imprime el tablero en pantalla """
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f'{tablero[i][j]:2}', end=" ")
        print("")
    print("")

# Programa principal

tamaño_tablero = 3
# Crea un tablero vacío 
tablero =[[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]

print("Buscando solución...")

# Ejecutar la búsqueda
if encontrar_solucion(tablero, 0):
    print("\nSolución encontrada:")
    mostrar_tablero(tablero)
else:
    print("No existe una solucíon") 
