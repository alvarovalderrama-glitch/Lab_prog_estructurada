import copy

def crear_laberinto():
    return [[0 for i in range(10)] for j in range(10)]

def mostrar_laberinto(laberinto):
    for linea in laberinto:
        suma = ''
        for componente in linea:
            suma += str(componente) + '  '
        print(suma)
    print()

def buscar_xy(laberinto, marca):
    for i, linea in enumerate(laberinto):
        for j, elemento in enumerate(linea):
            if elemento == marca:
                return (i, j)
    return None

def colocar_obstaculos(laberinto, lista_con_x_y_de_los_obstaculos):
    for x, y in lista_con_x_y_de_los_obstaculos:
        laberinto[x][y] = 'x'

def movimiento_coordenada(laberinto, coordenada, indice):
    x, y = coordenada
    delta_x = [0, 1, 0, -1]
    delta_y = [1, 0, -1, 0]
    n_x, n_y = x + delta_x[indice], y + delta_y[indice]
    if not (0 <= n_x < 10 and 0 <= n_y < 10):
        return []
    elif laberinto[n_x][n_y] != 0:
        return []
    else:
        return (n_x, n_y)

def soluciones(laberinto, inicio, final):
    posicion_actual = inicio
    p_x, p_y = posicion_actual
    indice = 0
    marca = 1
    laberinto[p_x][p_y] = marca
    camino_solucion = [inicio]
    all_soluciones = []
    laberinto_aux = [[0 for _ in range(10)] for _ in range(10)]

    while indice != 4:
        nueva_posicion = movimiento_coordenada(laberinto, posicion_actual, indice)
        if nueva_posicion == []:
            indice += 1
            while indice == 4 and posicion_actual != inicio:
                camino_solucion.remove(posicion_actual)
                laberinto[p_x][p_y] = 0
                marca -= 1
                posicion_actual = buscar_xy(laberinto, marca)
                p_x, p_y = posicion_actual
                indice = laberinto_aux[p_x][p_y]
        elif nueva_posicion == final:
            copia_solucion = copy.deepcopy(camino_solucion)
            copia_solucion.append(final)
            all_soluciones.append(copia_solucion)
            indice += 1
        else:
            marca += 1
            n_x, n_y = nueva_posicion
            laberinto[n_x][n_y] = marca
            laberinto_aux[p_x][p_y] = indice + 1
            posicion_actual = nueva_posicion
            p_x, p_y = posicion_actual
            camino_solucion.append(posicion_actual)
            indice = 0
    laberinto[p_x][p_y] = 0

    return all_soluciones

def mostrar_camino(laberinto, lista_caminos):
    indice = 1
    for lista in lista_caminos:
        laberinto_aux = copy.deepcopy(laberinto)
        for x, y in lista:
            if (x,y) == inicio:
                laberinto_aux[x][y] = 'I'
            elif (x,y) == final:
                laberinto_aux[x][y] = 'F'
            else:
                laberinto_aux[x][y] = '◼'
        print(f'{indice})')
        mostrar_laberinto(laberinto_aux)
        indice += 1

# Programa principal
laberinto = crear_laberinto()
lista_obstaculos = [(0, 5), (0, 6), (1, 1), (1, 2), (1, 3), (1, 5), (1, 6), (1, 8),
                    (2, 1), (2, 3), (2, 8), (3, 1), (3, 3), (3, 4), (3, 5), (3, 6),
                    (3, 8), (4, 1), (4, 6), (4, 8), (5, 3), (5, 4), (5, 6), (5, 8),
                    (6, 1), (6, 2), (6, 3), (6, 4), (6, 6), (6, 8), (7, 1), (7, 8),
                    (8, 1), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8), (9, 3), (9, 4)]
colocar_obstaculos(laberinto, lista_obstaculos)

inicio = (0, 0)
final = (9, 9)

lista_movimientos_ganadores = soluciones(laberinto, inicio, final)

if lista_movimientos_ganadores == []:
    print('No es posible llegar a la meta.')
else:
    for fila in laberinto:
        for i, elemento in enumerate(fila):
            if elemento == 0:
                fila[i] = '◻'

    print(f'Laberinto original (inicio en {inicio}; Final en {final}):')
    mostrar_laberinto(laberinto)
    
    print('\nSoluciones:')
    mostrar_camino(laberinto, lista_movimientos_ganadores)