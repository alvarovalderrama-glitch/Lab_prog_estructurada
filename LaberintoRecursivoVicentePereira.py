MAX = 3

# movimientos: derecha, abajo, izquierda, arriba
posx = [0, 1, 0, -1]
posy = [1, 0, -1, 0]
#verificar que no se salga del tablero, o los movimientos no sean validos
def valida(tablero, candidato, x, y):
    nx = x + posx[candidato-1]
    ny = y + posy[candidato-1]
    if nx < 0 or nx >= MAX: return False
    if ny < 0 or ny >= MAX: return False
    return tablero[nx][ny] == 0
#Avanzar normalmente, de una posicion en una
def siguiente_posicion(candidato, x, y):
    nx = x + posx[candidato-1]
    ny = y + posy[candidato-1]
    return nx, ny
#el final del tablero, el extremo inferior derecho
def final(nx, ny):
    return nx == MAX - 1 and ny == MAX - 1
#recorre cada fila y cada columna de la matriz, cada valor de cada posicion
def mostrar_tablero(tablero):
    for i in range(MAX):
        for j in range(MAX):
            print(tablero[i][j], end=" ")
        print("")
    print("")

def resolver_recursivo(tablero, x, y, contador):
    # si llegamos al final, que solucion encontrada
    if final(x, y):
        return True

    # probar con los candidatos del 1 al 4
    for candidato in range(1, 5):

        # si el candidato es valido, avanzar normal
        if valida(tablero, candidato, x, y):

            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1  # avanzar

            # recursion desde la nueva casilla
            if resolver_recursivo(tablero, nx, ny, contador + 1):
                return True  # propaga la solución

            # en caso de no funcionar retrocede 
            tablero[nx][ny] = 0

    # si es que ningun candaidato funciono 
    return False

def encontrar_una_solucion():
    tablero = [[0 for _ in range(MAX)] for _ in range(MAX)]
    tablero[0][0] = 1  # empezamos en (0,0)
#en caso de ser verdadero el if, imprimira solucion encontrada, de lo contrario no hay solucion.
    if resolver_recursivo(tablero, 0, 0, 1):
        print("Solución encontrada:")
        mostrar_tablero(tablero)
    else:
        print("No se encontró solución.")

# Probar
encontrar_una_solucion()