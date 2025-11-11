
# -----------------------------------------------
# LABERINTO (BACKTRACKING) ÚNICA SOLUCIÓN
# -----------------------------------------------


MAX = int(input("ingrese las dimensiones del tablero: "))

# ---- Movimientos posibles (derecha, abajo, izquierda, arriba) ----
mov_x = [0, 1, 0, -1]
mov_y = [1, 0, -1, 0]

# ---- Muestra el tablero ----
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{c:2}" for c in fila)) #une cada celda de la fila con un espacio
    print("") #vacío

# ---- Verifica si una posición es válida ----
def es_valida(tablero, x, y, visitado):
    return (0 <= x < MAX) and (0 <= y < MAX) and tablero[x][y] != -1 and not visitado[x][y]

# ---- Backtracking para encontrar el mejor camino (mínimos pasos) ----
def encontrar_mejor_camino(tablero, x, y, camino, visitado, mejor_camino):
    if x == MAX - 1 and y == MAX - 1:
        # Si no hay mejor camino o el actual es más corto, lo reemplazamos
        if not mejor_camino or len(camino) < len(mejor_camino[0]):
            mejor_camino.clear() #elimina el mejor camino antiguo
            mejor_camino.append(camino.copy()) #copia el mejor camino nuevo
        return

    visitado[x][y] = True #casilla visitada

    for i in range(4):
        nx = x + mov_x[i]
        ny = y + mov_y[i]
        if es_valida(tablero, nx, ny, visitado):
            camino.append((nx, ny))
            encontrar_mejor_camino(tablero, nx, ny, camino, visitado, mejor_camino)
            camino.pop() #permite retroceder al eliminar el último movimiento

    visitado[x][y] = False #Se desmarca la celda al retroceder

# ---- Coloca obstáculos ----
def colocar_obstaculos(tablero):
    tablero[0][3] = -1
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[2][2] = -1
    tablero[2][3] = -1

# ---- Guarda el mejor camino en un archivo txt ----
def guardar_en_txt(mejor_camino, tablero_original, nombre_archivo="mejor_camino.txt"):
    with open(nombre_archivo, "w", encoding="utf-8") as f: #permite ocupar caracteres especiales
        if not mejor_camino:
            f.write("No hay caminos válidos.\n")
            return

        camino = mejor_camino[0]
        f.write("Mejor camino (menos pasos):\n")
        f.write(" → ".join(str(p) for p in camino) + "\n\n")#convierte todo a string y los une con flechas

        # Crear tablero visual con obstáculos
        tablero_vista = [[" . " for _ in range(MAX)] for _ in range(MAX)]
        for i in range(MAX):
            for j in range(MAX):
                if tablero_original[i][j] == -1:
                    tablero_vista[i][j] = " X "

        # Marcar el camino con el número de paso
        for paso, (x, y) in enumerate(camino, start=1): #enumera el camino en orden
            tablero_vista[x][y] = f"{paso:3d}" #3 espacios (alineado)

        # Escribir el tablero al archivo
        for fila in tablero_vista:
            f.write(" ".join(fila) + "\n")

# ---- Programa principal ----
def main():
    tablero = [[0]*MAX for _ in range(MAX)]
    colocar_obstaculos(tablero)
    visitado = [[False]*MAX for _ in range(MAX)] #las casillas están desocupadas
    mejor_camino = []

    # Si inicio o fin están bloqueados
    if tablero[0][0] == -1 or tablero[MAX-1][MAX-1] == -1:
        with open("mejor_camino.txt", "w", encoding="utf-8") as f:
            f.write("Inicio o fin bloqueado. No hay caminos.\n")
        return

    encontrar_mejor_camino(tablero, 0, 0, [(0,0)], visitado, mejor_camino)
    if mejor_camino:
        print(f"Se encontró el mejor camino con {len(mejor_camino[0])} pasos. Se ha guardado en 'mejor_camino.txt'.")
    else:
        print("No se encontró ningún camino válido.")
    
    guardar_en_txt(mejor_camino, tablero)

# ---- Ejecutar ----
if __name__ == "__main__":
    main()