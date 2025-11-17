MAX = 5

def valida(tablero, candidato, x, y):
    # Movimientos posibles del caballo
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    nx = x + mov_x[candidato - 1]
    ny = y + mov_y[candidato - 1]
    
    if nx < 0 or nx >= MAX or ny < 0 or ny >= MAX:
        return False
    if tablero[nx][ny] != 0:
        return False
    return True

def siguiente_posicion(tablero, candidato, x, y):
    mov_x = [2, 1, -1, -2, -2, -1, 1, 2]
    mov_y = [1, 2, 2, 1, -1, -2, -2, -1]
    
    nx = x + mov_x[candidato - 1]
    ny = y + mov_y[candidato - 1]
    return nx, ny

def final(tablero):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == 0:
                return False
    return True

def buscar_xy(tablero, contador):
    for i in range(MAX):
        for j in range(MAX):
            if tablero[i][j] == contador:
                return i, j
    return None, None

def copiar_tablero(tab):
    return [fila[:] for fila in tab]

def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(f"{tablero[i][j]:2}", end=" ")
        print()
    print()

def mostrar_todas(soluciones):
    if not soluciones:
        print("No hay solucion")
        return
    print(f"Total soluciones: {len(soluciones)}\n")
    for idx, sol in enumerate(soluciones, start=1):
        print(f"Solucion #{idx}:")
        mostrar_tablero(sol)

def solucion(tablero):
    soluciones = []
    candidato = 1
    x, y = 0, 0
    contador = 1

    tablero_aux = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[x][y] = contador

    while True:
        if candidato <= 8:
            if valida(tablero, candidato, x, y):
                nx, ny = siguiente_posicion(tablero, candidato, x, y)
                contador += 1
                tablero[nx][ny] = contador
                tablero_aux[x][y] = candidato

                if final(tablero):
                    soluciones.append(copiar_tablero(tablero))
                    tablero[nx][ny] = 0
                    contador -= 1
                    candidato += 1

                    while candidato == 9 and not (x == 0 and y == 0):
                        tablero[x][y] = 0
                        contador -= 1
                        px, py = buscar_xy(tablero, contador)
                        if px is None:
                            break
                        candidato = tablero_aux[px][py] + 1
                        tablero_aux[px][py] = 0
                        x, y = px, py
                else:
                    x, y = nx, ny
                    candidato = 1
            else:
                candidato += 1
                while candidato == 9 and not (x == 0 and y == 0):
                    tablero[x][y] = 0
                    contador -= 1
                    px, py = buscar_xy(tablero, contador)
                    if px is None:
                        break
                    candidato = tablero_aux[px][py] + 1
                    tablero_aux[px][py] = 0
                    x, y = px, py
        else:
            if x == 0 and y == 0:
                break
            tablero[x][y] = 0
            contador -= 1
            px, py = buscar_xy(tablero, contador)
            if px is None:
                break
            candidato = tablero_aux[px][py] + 1
            tablero_aux[px][py] = 0
            x, y = px, py

    return soluciones
#progrma principal
if __name__ == "__main__":
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    print("Tablero inicial:")
    mostrar_tablero(tablero)

    sols = solucion(tablero)
    mostrar_todas(sols)
