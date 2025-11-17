import random  # Importa la libreria random, usado para generar números aleatorios

# Pide el tamaño del tablero cuadrado (n x n)
MAX = int(input("Ingrese el número de fila y columnas que desea (Será un tablero cuadrado, tendrá la misma cantida de filas y de columnas):  \n> "))
MAX2 = MAX - 1  # Variable "MAX2" que será la última casilla valida en el tablero

todas_soluciones = []  # Lista para guardar todas las soluciones encontradas (tableros completos)
soluciones_unicas = set()  # Conjunto para evitar duplicar soluciones repetidas

def valida(tablero, candidato, x, y):
    # Listas con desplazamientos en los ejes (derecha, abajo, izquierda, arriba)
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    
    # Calcula nueva posición en base al número candidato (1 a 4)
    nx = x + posx[candidato - 1]
    ny = y + posy[candidato - 1]
    
    # Comprueba que la nueva posición esté dentro de los límites del tablero
    if (nx < 0 or nx >= MAX):
        return False
    if (ny < 0 or ny >= MAX):
        return False
    
    # Si la celda está vacía (0), la posición es válida
    if (tablero[nx][ny] == 0):
        return True
    else:
        return False

def siguiente_posicion(candidato, x, y):
    posx = [0, 1, 0, -1]
    posy = [1, 0, -1, 0]
    nx = x + posx[candidato - 1]  # Calcula desplazamiento en x
    ny = y + posy[candidato - 1]  # Calcula desplazamiento en y
    return nx, ny  # Retorna la nueva posición

def final(nx, ny):
    if (nx == MAX - 1 and ny == MAX - 1):
        return True
    return False

def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if (tablero[i][j] == contador):
                return i, j  # Retorna las coordenadas encontradas

def solucion(tablero):

    candidato = contador = 1
    hay_solucion = False
    x = y = 0

    # Crea un tablero auxiliar para guardar movimientos previos
    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador  # Marca la casilla inicial con 1

    # Bucle de búsqueda de soluciones
    while (candidato <= 4 and not hay_solucion):
        # Verifica si el movimiento actual es válido
        if (valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(candidato, x, y)  # Calcula la nueva posición
            tablero[nx][ny] = contador + 1  # Marca el número siguiente

            # Si se seleccionó la opción "1", muestra el tablero paso a paso
            if seleccion == "1":
                mostrar_tablero(tablero)

            # Si se llegó a la posición final, se guarda la solución
            if (final(nx, ny)):
                # Convierte el tablero a tupla para poder usarlo en un set
                hay_solucion = True
                sol_tupla = tuple(tuple(fila) for fila in tablero)

                # Si la solución no está registrada, se agrega
                if sol_tupla not in soluciones_unicas:
                    todas_soluciones.append(([fila[:] for fila in tablero], contador + 1))
                    soluciones_unicas.add(sol_tupla)

            else:
                # Guarda el movimiento actual en el tablero auxiliar
                tablero_aux[x][y] = candidato
                x = nx  # Actualiza coordenada x
                y = ny  # Actualiza coordenada y
                contador += 1  # Aumenta el contador
                candidato = 1  # Reinicia el candidato
                continue

        else:
            # Si no es válido, prueba el siguiente candidato (otra dirección)
            candidato += 1

        # Si ya se probaron las 4 direcciones posibles
        while candidato > 4:
            # Si se regresa al inicio, termina la búsqueda
            if x == 0 and y == 0:
                return hay_solucion

            tablero[x][y] = 0  # Limpia la celda actual
            contador -= 1  # Retrocede un paso
            nx, ny = buscar_xy(tablero, contador)  # Busca la celda anterior
            candidato = tablero_aux[nx][ny] + 1  # Retoma desde el siguiente candidato
            tablero_aux[nx][ny] = 0  # Limpia el registro auxiliar
            x = nx
            y = ny

            # Muestra el tablero si la opción "1" está activa
            if seleccion == "1":
                mostrar_tablero(tablero)

    return hay_solucion  # Devuelve si se encontró o no una solución

def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            val = str(tablero[i][j])  # Convierte cada valor a string
            print(f"{val:>3}", end=" ")  # Alinea y muestra sin salto de línea
        print("")  # Salto de línea al terminar una fila
    print("")  # Espacio adicional al final

def colocar_obstaculo(tablero):
    # Coloca obstáculos en aproximadamente un tercio de las casillas
    for _ in range((MAX * MAX) // 4):
        rx = random.randint(0, MAX2)  # Genera coordenada aleatoria en x
        ry = random.randint(0, MAX2)  # Genera coordenada aleatoria en y

        # Evita poner obstáculos en la casilla inicial y final
        if (rx, ry) not in [(0, 0), (MAX2, MAX2)]:
            tablero[rx][ry] = "X"  # Marca el obstáculo

### MAIN ###

tablero_original = [[0 for _ in range(MAX)] for _ in range(MAX)] 
colocar_obstaculo(tablero_original) 

while True:
    # Copia limpia del tablero original con los mismos obstáculos
    tablero = [fila[:] for fila in tablero_original] 

    print("""
|==========Traza del movimiento==========|
    1.- Quiero ver la traza.
    2.- Quiero solo la solución.
    3.- Mejor solución.
    4.- Otro tablero.
    5.- Salir.
|========================================|
 """)
    
    print("|==========Tablero generado==========|\n")
    mostrar_tablero(tablero)
    print("|====================================|")

    seleccion = input("Ingrese la opción que desea usar:  \n> ")

    if seleccion == "1":
        mostrar_tablero(tablero)   
        if(solucion(tablero) == True):  # Llama a la función solucion(tablero) y verifica si retornó True
            print("\nHay al menos 1 solución posible. \n")  # Mensaje de éxito si existe solución
            mostrar_tablero(tablero)  # Muestra el tablero solución
        else:
            print("\nNo hay una solución posible. \n")  # Mensaje si no se encontró ninguna solución

    elif seleccion == "2":
        if(solucion(tablero) == True):  # Llama a la función solucion(tablero) y verifica si retornó True
            print("\nHay al menos 1 solución posible. \n")  # Mensaje de éxito si existe solución
            mostrar_tablero(tablero)  # Muestra el tablero solución
        else:
            print("\nNo hay una solución posible. \n")  # Mensaje si no se encontró ninguna solución    

    elif seleccion == "3":  # Si el usuario elige la opción 3 ("Mejor solución")
        todas_soluciones.clear()  # Limpia la lista de soluciones anteriores
        soluciones_unicas.clear()  # Limpia el conjunto que evita duplicados

        solucion(tablero)  # Llama a la función que busca todas las soluciones posibles del tablero

        # Si se encontraron soluciones, entra a este bloque
        if todas_soluciones:
            # Obtiene la mejor solución (la que tiene MENOS movimientos)
            mejor_tablero, menor_movimientos = min(todas_soluciones, key=lambda s: s[1])

            # Muestra en pantalla cuántos movimientos tiene la mejor solución
            print(f"\nLa mejor solución tiene {menor_movimientos} movimientos:\n")

            # Imprime el tablero correspondiente a esa mejor solución
            mostrar_tablero(mejor_tablero)

            # Se crea un archivo de texto para guardar la mejor solución
            with open("Mejor solución (Laberinto).txt", "w") as f:
                # Escribe el encabezado con la cantidad de movimientos
                f.write(f"Mejor solución con {menor_movimientos} movimientos:\n")

                # Recorre cada fila del tablero y la escribe en el archivo
                # Si hay una celda con -1, se reemplaza por 'X' al escribirla
                for fila in mejor_tablero:
                    f.write(" ".join(f"{'X' if n == -1 else n:>3}" for n in fila) + "\n")

            # Mensaje indicando que se guardó correctamente la mejor solución
            print("\nSe guardó la mejor solución en [Mejor solución (Laberinto).txt].\n")

        else:
            # Si no se encontró ninguna solución, muestra este mensaje
            print("\nNo hay soluciones posibles.\n")

    elif seleccion == "4":
        tablero.clear()
        tablero_original = [[0 for _ in range(MAX)] for _ in range(MAX)] 
        colocar_obstaculo(tablero_original) 

    elif seleccion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Error, opción invalida.")



