tamano_tablero = 5

obstaculos = [(3, 2), (2, 4)]

# movimientos: arriba, derecha, abajo, izquierda
mov_x = [-1, 0, 1, 0]
mov_y = [0, 1, 0, -1]


def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(c) for c in fila))
    print()


def es_valido(x, y, tablero):
    # valida el siguiente moviento, revisa si se sale del tablero, si ya esta ocupado y si hay un obstaculo
    if not (0 <= x < tamano_tablero and 0 <= y < tamano_tablero):
        return False
    if tablero[x][y] != 0:
        return False
    if (x, y) in obstaculos:
        return False
    return True


def laberinto():
    tablero = [[0 for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]
    for (x, y) in obstaculos:
        tablero[x][y] = "X"

    tablero_aux = [[0 for _ in range(tamano_tablero)] for _ in range(tamano_tablero)]

    x, y = 0, 0
    paso = 1
    tablero[x][y] = paso
    candidato = 0  # movimiento inical (arriba)

    while True:
        # si llega al final, se termina e imprime tablero
        if (x, y) == (tamano_tablero - 1, tamano_tablero - 1):
            print("Camino encontrado:\n")
            mostrar_tablero(tablero)
            return

        # Busca movimientos validos
        while candidato < 4:
            nx = x + mov_x[candidato]
            ny = y + mov_y[candidato]
            if es_valido(nx, ny, tablero):
                break
            candidato += 1

        if candidato < 4:  # si hay un movimiento valida, avanza
            tablero_aux[x][y] = candidato
            x = nx
            y = ny
            paso += 1
            tablero[x][y] = paso
            candidato = 0  # reinicia movimientos
        else:
            # retrocede
            tablero[x][y] = 0
            paso -= 1
            if paso == 0:
                print("No hay camino encontrado.")
                return
            # busca coordenadas del paso anterior
            for i in range(tamano_tablero):
                for j in range(tamano_tablero):
                    if tablero[i][j] == paso:
                        x, y = i, j
                        break
            candidato = tablero_aux[x][y] + 1
            tablero_aux[x][y] = 0


laberinto()