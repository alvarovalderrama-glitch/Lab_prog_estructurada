
def imprimir_tablero(tablero):
    # Imprime el tablero en formato de matriz
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f'{tablero[i][j]:2}', end=" ")
        print("")
    print("")

def cuadrado_magico(tablero):
    # Calcula el valor que deberían tener todas las filas, columnas y diagonales
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

    # Si todo coincide, es un cuadrado mágico válido
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

    # # Revisar que el número no se haya usado antes
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if tablero[i][j] == candidato:
                return False

    return True

def siguiente_posicion(i, j):
    # Avanza a la siguiente casilla del tablero (recorrido por filas)
    j += 1
    if j == tamaño_tablero:
        j = 0
        i += 1
    return i, j

def posicion_anterior(i, j):
    # Retrocede a la casilla anterior
    j -= 1
    if j < 0:
        j = tamaño_tablero - 1
        i -= 1
    return i, j

def encontrar_solucion(tablero):
    
    i, j = 0, 0         # Comenzamos en la casilla (0,0) con el primer número posible
    candidato = 1
    terminado = False

    while not terminado:

        # # Probar todos los números posibles
        while candidato <= tamaño_tablero * tamaño_tablero:

            # Si el número se puede colocar aquí:
            if valida(tablero, candidato, i, j):
                tablero[i][j] = candidato  # colocarlo

                # Si el tablero está lleno, verificar cuadrado mágico
                if final(tablero):
                    if cuadrado_magico(tablero):
                        # Si lo es, ya terminamos
                        terminado = True
                        return True
                    else:
                        # # Si no lo es, se limpia la casilla y probar otro número
                        tablero[i][j] = 0
                        candidato += 1
                        continue

                # Si no está lleno, avanzamos a la siguiente posición
                i, j = siguiente_posicion(i, j)
                candidato = 1   # reiniciar candidato en la nueva casilla
                break  # salir para intentar en la nueva posición

            else:
                candidato += 1 # Probar siguiente número

        else:  
            # Si no quedan candidatos válidos, retrocedemos una casilla
            if i == 0 and j == 0:
                return False  # no existe solución

            # volver atrás
            i, j = posicion_anterior(i, j)
            candidato = tablero[i][j] + 1   # probar siguiente número ahí
            tablero[i][j] = 0   # limpiar casilla para deshacer paso del backtracking

# Programa principal

tamaño_tablero = 3     
tablero =[[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]

print("Buscando solución...")

# Ejecutar la búsqueda
if encontrar_solucion(tablero):
    print("\nSolución encontrada:")
    imprimir_tablero(tablero)
else:
    print("No existe una solucíon") 