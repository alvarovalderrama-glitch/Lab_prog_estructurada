# Función que crea el laberinto de 10x10
def crear_laberinto():
    return [['◻' for i in range(10)] for j in range(10)]

# Función que muestra el laberinto
def mostrar_laberinto(laberinto):
    for linea in laberinto:
        suma = ''
        for componente in linea:
            suma += str(componente) + '  '
        print(suma)
    print()

# Función que busca las coordenadas donde se aloja una determinada marca en el laberinto
def buscar_xy(laberinto, marca):
    for i, linea in enumerate(laberinto):
        for j, elemento in enumerate(linea):
            if elemento == marca:
                return (i, j)
    return None

# Función que coloca los obstaculos según las coordenadas que se le entregue dentro de una lista
def colocar_obstaculos(laberinto, lista_con_x_y_de_los_obstaculos):
    for x, y in lista_con_x_y_de_los_obstaculos:
        laberinto[x][y] = 'x'

# Función que calcula el movimiento que se hara en una determinada posición del laberinto según el indice correspondiente
def movimiento_coordenada(laberinto, coordenada, indice):
    x, y = coordenada
    delta_x = [0, 1, 0, -1]
    delta_y = [1, 0, -1, 0]
    n_x, n_y = x + delta_x[indice], y + delta_y[indice]
    if not (0 <= n_x < 10 and 0 <= n_y < 10):
        return []
    elif laberinto[n_x][n_y] != '◻':
        return []
    else:
        return (n_x, n_y)

# Función que encuentra los caminos desde el inicio hasta el final o determina que no hay caminos.
def solucion(laberinto, inicio, final):
    posicion_actual = inicio
    p_x, p_y = posicion_actual
    indice = 0
    marca = 1
    laberinto[p_x][p_y] = marca
    camino_solucion = [inicio]
    all_soluciones = []
    laberinto_aux = [[0 for _ in range(10)] for _ in range(10)]
    # El ciclo continua hasta que el indice sea igual a 4, lo que significa que se probaron todas las posibilidades.
    while indice != 4:
        # Se calcula la nueva posición para la posición actual (que puede no ser valida)
        nueva_posicion = movimiento_coordenada(laberinto, posicion_actual, indice)
        # Si la nueva posición no es valida, tomara el valor de una lista vacia y se sumara una unidad al indice
        if nueva_posicion == []:
            indice += 1
            while indice == 4 and posicion_actual != inicio:
                camino_solucion.remove(posicion_actual)
                laberinto[p_x][p_y] = '◻'
                marca -= 1
                posicion_actual = buscar_xy(laberinto, marca)
                p_x, p_y = posicion_actual
                indice = laberinto_aux[p_x][p_y]
        # Si la nueva posición es igual al final, hemos encontrado un camino, por lo que se guarda en la lista que almacena los caminos.
        elif nueva_posicion == final:
            copia_solucion = camino_solucion + [final]
            all_soluciones.append(copia_solucion)
            indice = 4
        # En caso de no estar en ninguno de los dos casos anteriores, la nueva posición se vuelve la posición actual.
        else:
            marca += 1
            n_x, n_y = nueva_posicion
            laberinto[n_x][n_y] = marca
            laberinto_aux[p_x][p_y] = indice + 1
            posicion_actual = nueva_posicion
            p_x, p_y = posicion_actual
            camino_solucion.append(posicion_actual)
            indice = 0
    laberinto[p_x][p_y] = '◻'

    return all_soluciones
# Esta función muestra en la terminal todos los caminos diferentes que se pueden recorrer de inicio a final
def mostrar_camino(laberinto, lista_caminos):
    indice = 1
    for lista in lista_caminos:
        laberinto_aux = [[0 for i in range(len(laberinto))] for j in range(len(laberinto))]
        for i in range(len(laberinto_aux)):
            for j in range(len(laberinto_aux)):
                laberinto_aux[i][j] = laberinto[i][j]
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

print(f'Laberinto original (inicio en {inicio}; Final en {final}):')
mostrar_laberinto(laberinto)
    
lista_movimientos_ganadores = solucion(laberinto, inicio, final)
# Si la lista que almacena los caminos ganadores esta vacia, significa que no hay camino en el laberinto para llegar al final.
if lista_movimientos_ganadores == []:
    print('No es posible llegar a la meta.')
# De no ser asi, se remplazan los 0 en laberinto por cuadrados vacios y se muestran las soluciones.
else:
    for fila in laberinto:
        for i, elemento in enumerate(fila):
            if elemento == 0:
                fila[i] = '◻'
                
    print('\nSolución:')

    mostrar_camino(laberinto, lista_movimientos_ganadores)