import random  # Importa el módulo random, usado para generar números aleatorios

# Pide el tamaño del tablero cuadrado (n x n)
MAX = int(input("Ingrese el número de fila y columnas que desea (Será un tablero cuadrado, tendrá la misma cantida de filas y de columnas):  \n> "))

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

def backtrack_recursivo(tablero, x, y, contador):
    if final(x, y):
        sol_tupla = tuple(tuple(fila) for fila in tablero) # Convertimos el tablero en tuplas, para poder usar el set y evitar soluciones duplicadas
        if sol_tupla not in soluciones_unicas: # Ve si la solución no se repite, en caso de que sea una nueva la guarda
            soluciones_unicas.add(sol_tupla)
            todas_soluciones.append(([fila[:] for fila in tablero], contador))

        # En caso de que el usuario seleccione la opción 1 o 2, para que solo muestre 1 sola solución
        if seleccion in ("1", "2"):
            return True
        
        # Para que cuando la opción elegida sea "3" se busquen las diferentes soluciones hasta encontrar la más corta
        else:
            return False


    # Probar las 4 direcciones posibles (1 a 4)
    for candidato in range(1, 5):

        if valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)

            # Marcar casilla
            tablero[nx][ny] = contador + 1

            if seleccion == "1":
                mostrar_tablero(tablero)

            # Recursión
            if backtrack_recursivo(tablero, nx, ny, contador + 1):
                return True

            # Retroceso (backtracking)
            tablero[nx][ny] = 0

    return False

def solucion(tablero):
    todas_soluciones.clear()
    soluciones_unicas.clear()

    tablero[0][0] = 1
    return backtrack_recursivo(tablero, 0, 0, 1)

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
        rx = random.randint(0, (MAX-1))  # Genera coordenada aleatoria en x
        ry = random.randint(0, (MAX-1))  # Genera coordenada aleatoria en y

        # Evita poner obstáculos en la casilla inicial y final
        if ((rx, ry) not in [(0, 0), ((MAX-1), (MAX-1))]) and tablero[rx][ry] == 0:
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
        # Genera un nuevo tablero con nuevos obstaculos
        tablero.clear()
        tablero_original = [[0 for _ in range(MAX)] for _ in range(MAX)] 
        colocar_obstaculo(tablero_original) 

    elif seleccion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Error, opción invalida.")