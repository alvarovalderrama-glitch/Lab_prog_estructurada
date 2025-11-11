
# -----------------------------------------------
# LABERINTO (BACKTRACKING) TODAS LAS SOLUCIONES
# -----------------------------------------------


import random

MAX = int(input("ingrese las dimensiones del tablero: "))

# ---- Movimientos posibles (derecha, abajo, izquierda, arriba) ----
mov_x = [0, 1, 0, -1]
mov_y = [1, 0, -1, 0]

# ---- Muestra el tablero ----
def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(f"{c:2}" for c in fila)) #une las celdas con un espacio
    print("") #vacío                            #y las muestra como una fila

# ---- Verifica si una posición es válida ----
def es_valida(tablero, x, y, visitado):
    return (0 <= x < MAX) and (0 <= y < MAX) and tablero[x][y] != -1 and not visitado[x][y]

# ---- Backtracking para encontrar todos los caminos ----
def encontrar_caminos(tablero, x, y, camino, visitado, soluciones):
    # Si llegamos al final, guardamos el camino
    if x == MAX - 1 and y == MAX - 1:
        soluciones.append(camino.copy()) #copia los caminos encontrados en el archivo
        return

    # Marcamos la posición como visitada
    visitado[x][y] = True

    # Probamos las 4 direcciones
    for i in range(4):
        nx = x + mov_x[i]
        ny = y + mov_y[i]

        if es_valida(tablero, nx, ny, visitado):
            camino.append((nx, ny)) #añade la posición al camino actual
            encontrar_caminos(tablero, nx, ny, camino, visitado, soluciones)
            camino.pop()  # retroceder (backtracking)

    # Desmarcamos al retroceder
    visitado[x][y] = False


def colocar_obstaculos(tablero, porcentaje=0.2):
    cantidad = int(MAX * MAX * porcentaje)  # 20% del tablero serán obstáculos
    for _ in range(cantidad):
        x = random.randint(0, MAX - 1)
        y = random.randint(0, MAX - 1)
        if (x, y) not in [(0,0), (MAX-1,MAX-1)]:  # no bloquees inicio y fin
            tablero[x][y] = -1


# ---- Guarda los caminos en un archivo txt ----
def guardar_en_txt(soluciones, tablero_original):
    with open("soluciones.txt", "w", encoding="utf-8") as f:
        if not soluciones:
            f.write("No hay caminos válidos.\n")
            return

        for i, camino in enumerate(soluciones, 1): #Recorre cada camino encontrado y los enumera
            f.write(f"Camino {i}:\n")

            # Crear una copia del tablero para dibujar el camino
            tablero = [fila.copy() for fila in tablero_original]

            # Dibujar el camino en el tablero
            for (x, y) in camino:
                tablero[x][y] = "*"

            # Marcar inicio y fin
            sx, sy = camino[0]
            fx, fy = camino[-1]
            tablero[sx][sy] = "S"
            tablero[fx][fy] = "E"

            # Escribir el tablero
            for fila in tablero: #todas las celdas de la fila están separadas con un espacio
                f.write(" ".join(f"{str(c):2}" for c in fila) + "\n")

            f.write("\n-----------------------------------------\n\n")

        f.write(f"Total de caminos encontrados: {len(soluciones)}\n")


# ---- Programa principal ----
def main():
    tablero = [[0]*MAX for _ in range(MAX)]
    colocar_obstaculos(tablero)

    print("Tablero con obstáculos:")
    mostrar_tablero(tablero)

    visitado = [[False]*MAX for _ in range(MAX)]
    soluciones = []

    # Comienza desde (0,0)
    if tablero[0][0] == -1 or tablero[MAX-1][MAX-1] == -1:
        print("Inicio o fin bloqueado. No hay solución.")
        return

    encontrar_caminos(tablero, 0, 0, [(0,0)], visitado, soluciones)

    if soluciones:
        print(f"Se encontraron {len(soluciones)} caminos válidos.")
    else:
        print("No se encontró ningún camino.")

    guardar_en_txt(soluciones, tablero)
    print("Soluciones guardadas en 'soluciones.txt'.")


# ---- Ejecutar ----
if __name__ == "__main__":
    main()