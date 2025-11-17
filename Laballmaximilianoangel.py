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
    
    # Si la celda está vacía, la posición es válida
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
    while candidato <= 4:  # ← quitamos "and not hay_solucion" para que explore todas
        # Verifica si el movimiento actual es válido
        if (valida(tablero, candidato, x, y)):
            nx, ny = siguiente_posicion(candidato, x, y)  # Calcula la nueva posición
            tablero[nx][ny] = contador + 1  # Marca el número siguiente

            # Si se llegó a la posición final, se guarda la solución
            if (final(nx, ny)):
                # Convierte el tablero a tupla para poder usarlo en un set
                sol_tupla = tuple(tuple(fila) for fila in tablero)

                # Si la solución no está registrada, se agrega
                if sol_tupla not in soluciones_unicas:
                    todas_soluciones.append(([fila[:] for fila in tablero], contador + 1))
                    soluciones_unicas.add(sol_tupla)
                    hay_solucion = True  # Marca que se encontró al menos una

                # Después de guardar, desmarcamos la casilla y seguimos buscando
                tablero[nx][ny] = 0
                candidato += 1
                continue

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

tablero = [[0 for _ in range(MAX)] for _ in range(MAX)] # Creación del tablero

colocar_obstaculo(tablero)  # Solo una vez al inicio

while True:
    print("""
|==========Traza del movimiento==========|
    1.- Todas las soluciones.
    2.- Otro tablero.
    3.- Salir.
|========================================|
 """)
    
    print("|==========Tablero generado==========|\n")
    mostrar_tablero(tablero)
    print("|====================================|")

    seleccion = input("Ingrese la opción que desea usar:  \n> ")

    if seleccion == "1": 
        todas_soluciones.clear()  # Limpia la lista de soluciones previas
        soluciones_unicas.clear()  # Limpia el conjunto de soluciones únicas (para evitar duplicados)

        solucion(tablero)  # Llama a la función que busca todas las soluciones posibles en el tablero actual

        # Si se encontraron soluciones, entra en este bloque
        if todas_soluciones:
            # Se crea el archivo donde se guardarán todas las soluciones encontradas
            with open("Soluciones posibles (Laberinto).txt", "w") as f: 
                # Recorre todas las soluciones con un índice (i) que empieza en 1
                for i, sol in enumerate(todas_soluciones, 1):
                    # Escribe el encabezado de cada solución (por ejemplo: "Solución N°1")
                    f.write(f"Solución N°{i}: \n")

                    # Recorre cada fila del tablero y la escribe en el archivo
                    # Si hay una casilla con 'X', la mantiene; de lo contrario, escribe su número alineado
                    for fila in sol[0]:
                        f.write(" ".join(f"{'X' if n=='X' else n:>3}" for n in fila) + "\n")

                    # Agrega una línea en blanco entre cada solución para mayor claridad
                    f.write("\n")

            # Imprime un mensaje informando cuántas soluciones se encontraron y dónde se guardaron
            print(f"\nSe encontraron {len(todas_soluciones)} soluciones y se almacenaron en [Soluciones posibles (Laberinto).txt].\n")

        else:
            # Si no se encontró ninguna solución, muestra este mensaje
            print("\nNo hay soluciones posibles.\n")

    elif seleccion == "2":
        tablero.clear()
        tablero_original = [[0 for _ in range(MAX)] for _ in range(MAX)] 
        colocar_obstaculo(tablero_original) 

    elif seleccion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Error, opción invalida.")

