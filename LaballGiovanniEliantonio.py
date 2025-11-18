
def valida(tablero, candidato, x, y):
    """ Verifica si una posible posición es válida (dentro de los límites
    del tablero y sin obstáculos) """
    nx = x + pos_x[candidato - 1]
    ny = y + pos_y[candidato - 1]

    #Verifica límites del tablero
    if not (0 <= nx < tamaño_tablero and 0 <= ny < tamaño_tablero):
        return False
    
    # Solo se puede avanzar si la celda es 0 (libre)
    return tablero[nx][ny] == 0

def siguiente_posicion(candidato, x, y):
    """ Devuelve las coordenadas (nx, ny) de la siguiente
    posición según el movimiento candidato """
    nx = x + pos_x[candidato - 1]
    ny = y + pos_y[candidato - 1]
    
    return nx, ny


def final(nx, ny):
    """ Determina si se ha llegado al final del laberinto """
    if (nx == tamaño_tablero - 1) and (ny == tamaño_tablero - 1):
        return True
    
    return False

def buscar_xy(tablero, contador):
    """ Busca las coordenadas (x, y) donde se encuentra
    "contador" dentro del tablero """
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            if tablero[i][j] == contador:
                return i, j

def solucion(tablero):
    """ Algoritmo principal, busca una
    ruta válida desde (0,0) hasta (tamaño_tablero-1,tamaño_tablero-1)"""
    
    total_soluciones = 0        # contador total de soluciones
    x = 0 ; y = 0               # Posición inicial          
    contador = 1                # Contador de pasos
    candidato = 1               # Número del paso dentro del camino
    tablero[x][y] = contador    # Marca la celda inicial con el paso 1
    
    # Matriz auxiliar para recordar qué movimientos ya probó cada celda
    tablero_aux = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]

    # Si el inicio o el final están bloqueados, no hay solución
    if (tablero[0][0] == -1) or (tablero[tamaño_tablero - 1][tamaño_tablero - 1] == -1):
        return 0

    #Se ejecuta mientras queden movimientos posibles
    while not (x == 0 and y == 0 and candidato > 4):

        # Si el movimiento es válido, avanzar
        if candidato <= 4 and valida(tablero, candidato, x, y):
            nx, ny = siguiente_posicion(candidato, x, y)
            tablero[nx][ny] = contador + 1      # Marca el siguiente paso

            if final(nx, ny):
                total_soluciones += 1           #cuenta la solución encontrada
                tablero[nx][ny] = 0             #limpiar para seguir buscando
            else:
                tablero_aux[x][y] = candidato   # Guardar movimiento usado
                x, y = nx, ny                   # Avanzar
                contador += 1
                candidato = 1                   # Reiniciar movimientos
                continue

        # Probar siguiente movimiento
        candidato += 1

        # Retroceso 
        while candidato == 5 and not (x == 0 and y == 0):
           
            tablero[x][y] = 0                   # Limpia el paso actual
            contador -= 1                       # Retrocede un paso
            x, y = buscar_xy(tablero, contador) # Ubica la celda anterior
            candidato = tablero_aux[x][y] + 1   # Reanudar movimientos
            tablero_aux[x][y] = 0               # Limpia el registro

    # devolvemos el total encontrado
    return total_soluciones


def mostrar_tablero(tablero):
    """Imprime el tablero en pantalla"""
    for i in range(tamaño_tablero):
        for j in range(tamaño_tablero):
            print(f'{tablero[i][j]:2}', end = " ")
        print("")
    print("")

def colocar_obstaculo(tablero):
    """Coloca obstáculos fijos en posiciones definidas"""
    #tablero[0][2] = -1
    tablero[1][1] = -1
    tablero[2][1] = -1
    tablero[2][2] = -1
    #tablero[2][3] = -1
    tablero[3][2] = -1

# Programa principal

tamaño_tablero = 4          # Dimensión del tablero

pos_x = [0,1,0,-1]          # Desplazamientos posibles en X
pos_y = [1,0,-1,0]          # Desplazamientos posibles en Y 

# Crear tablero vacío
tablero = [[0 for i in range(tamaño_tablero)] for j in range(tamaño_tablero)]
colocar_obstaculo(tablero)  # Agregar obstáculos

print("Laberinto inicial:")
mostrar_tablero(tablero)

# llamamos a la función y se guarda el resultado
total = solucion(tablero)

if total > 0:
    print(f"Total de soluciones posibles: {total}")
else:
    print("No hay solución")


