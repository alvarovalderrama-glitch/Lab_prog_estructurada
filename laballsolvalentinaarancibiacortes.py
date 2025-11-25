# -----------------------------------------------
# LABERINTO (BACKTRACKING) TODAS LAS SOLUCIONES
# -----------------------------------------------

''' Este código resuelve el problema del laberinto con backtracking
iterativo. Todas las soluciones encontradas se guardan en un archivo txt. '''

# Se pide al usuario las dimensiones del tablero nxn
MAX = int(input("ingrese las dimensiones del tablero: "))

# Movimientos posibles: derecha, abajo, izquierda, arriba
mov_x = [0, 1, 0, -1]
mov_y = [1, 0, -1, 0]

# ---- Muestra el tablero en consola ----
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{c:2}" for c in fila))  # muestra cada celda
    print("")

# ---- Verifica si la celda es válida ----
def es_valida(tablero, x, y):
    # Debe estar dentro del tablero y NO ser obstáculo (-1)
    return 0 <= x < MAX and 0 <= y < MAX and tablero[x][y] != -1

# ---- Coloca obstáculos sin bloquear inicio ni salida ----
def colocar_obstaculos(tablero):
    obstaculos = [(0,3), (1,1), (2,1), (2,2), (2,3)]  # posiciones predeterminadas

    for x, y in obstaculos:
        if 0 <= x < MAX and 0 <= y < MAX:   # dentro del tablero
            # Evita bloquear la casilla inicial (0,0) o la final (MAX-1, MAX-1)
            if (x, y) != (0,0) and (x, y) != (MAX-1, MAX-1):
                tablero[x][y] = -1  # marca como obstáculo

# ---- Encuentra TODOS los caminos válidos mediante backtracking iterativo ----
def encontrar_caminos(tablero):
    soluciones = []   # lista donde se guardarán todos los caminos
    stack = []        # pila para simular la recursión (backtracking iterativo)

    # Tablero auxiliar para marcar pasos visitados
    tablero_aux = [[0]*MAX for _ in range(MAX)]
    tablero_aux[0][0] = 1  # primera celda marcada como visitada

    # La pila guarda: (x, y, lista_camino, tablero_aux, paso_numero)
    stack.append((0, 0, [(0,0)], tablero_aux, 1))

    while stack:
        # Se toma el último estado guardado en la pila
        x, y, camino, aux, paso = stack.pop()

        # Si llegamos a la meta, se guarda el camino
        if x == MAX - 1 and y == MAX - 1:
            soluciones.append(camino.copy())
            continue

        # Probar los 4 movimientos
        for i in range(4):
            nx = x + mov_x[i]
            ny = y + mov_y[i]

            # Si es celda válida y no visitada:
            if es_valida(tablero, nx, ny) and aux[nx][ny] == 0:

                # Copiamos el tablero auxiliar para el nuevo estado
                nuevo_aux = [fila.copy() for fila in aux]
                nuevo_aux[nx][ny] = paso + 1  # marcamos el nuevo paso

                # Copiamos el camino y agregamos la nueva celda
                nuevo_camino = camino + [(nx, ny)]

                # Guardamos el nuevo estado en la pila
                stack.append((nx, ny, nuevo_camino, nuevo_aux, paso + 1))

    return soluciones

# ---- Guarda todas las soluciones en un archivo TXT ----
def guardar_en_txt(soluciones):
    with open("soluciones.txt", "w", encoding="utf-8") as f:
        if not soluciones:
            f.write("No hay caminos válidos.\n")
            return

        for i, camino in enumerate(soluciones, 1):
            f.write(f"Camino {i}:\n")

            # Escribe el recorrido
            f.write(" → ".join(str(p) for p in camino) + "\n")

            # Prepara tablero para mostrar el recorrido numerado
            tablero = [[0]*MAX for _ in range(MAX)]
            colocar_obstaculos(tablero)

            paso = 1
            for (x, y) in camino:
                tablero[x][y] = paso
                paso += 1

            # Escribe el tablero en el archivo
            f.write("Tablero:\n")
            for fila in tablero:
                f.write(" ".join(f"{c:2}" for c in fila) + "\n")
            f.write("\n")

        f.write(f"Total de caminos encontrados: {len(soluciones)}\n")

# ---- Función principal ----
def main():
    # Crear tablero inicial vacío
    tablero = [[0]*MAX for _ in range(MAX)]

    # Colocar obstáculos en el tablero
    colocar_obstaculos(tablero)

    print("tablero con obstáculos:")
    mostrar_tablero(tablero)

    # Buscar todos los caminos posibles
    soluciones = encontrar_caminos(tablero)

    if soluciones:
        print(f"Se encontraron {len(soluciones)} caminos válidos.")
    else:
        print("No se encontró ningún camino.")

    # Mostrar visualmente cada camino
    for i, camino in enumerate(soluciones, 1):
        print(f"Camino {i}:")
        copia = [fila.copy() for fila in tablero]
        paso = 1
        for (x, y) in camino:
            copia[x][y] = paso
            paso += 1

        for fila in copia:
            print(" ".join(f"{c:2}" for c in fila))
        print()

    # Guardar en archivo
    guardar_en_txt(soluciones)
    print("Soluciones guardadas en 'soluciones.txt'.")

# Ejecutar programa
if __name__ == "__main__":
    main()
